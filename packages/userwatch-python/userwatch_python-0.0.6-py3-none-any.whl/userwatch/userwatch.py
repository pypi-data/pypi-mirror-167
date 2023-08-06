import grpc
import json
from datetime import datetime
import traceback

from userwatch import userwatch_shepherd_pb2
from userwatch import userwatch_shepherd_pb2_grpc
from userwatch import userwatch_historian_pb2
from userwatch import userwatch_historian_pb2_grpc


class Userwatch:
    shepherd = None
    historian = None
    privateApiKey = None

    def __init__(self, privateApiKey, options={}):
        url = options.get("url", "api.userwat.ch:443")
        self.privateApiKey = privateApiKey
        channel = None
        if options.get("insecure", False):
            channel = grpc.insecure_channel(url)
        else:
            channel = grpc.secure_channel(
                url,
                grpc.ssl_channel_credentials()
            )
        self.shepherd = userwatch_shepherd_pb2_grpc.ShepherdStub(channel)
        self.historian = userwatch_historian_pb2_grpc.HistorianStub(channel)

    # Access the assessment of a user for whom an event was previously
    # registered with Userwatch via a track(UserInfo, EventType) call from
    # your client application.
    #
    # At this point you can also attach any additional UserInfo your server
    # has which your client might not have had available.
    def verify(self,
               eventToken,  # string
               userInfo,  # userwatch_public_pb2.UserInfo
               challengeVerification=None):  # optional userwatch_shepherd_pb2.ChallengeVerificationRequest
        def doit():
            return self.shepherd.Verify(
                userwatch_shepherd_pb2.VerifyRequest(
                    event_token=eventToken,
                    userinfo=userInfo,
                    challenge_verification=challengeVerification,
                ),
                metadata=[("x-api-key", self.privateApiKey)]
            )

        return self.__retryNonIllegalArg(doit, "verify")

    def createChallenge(self,
                        type,  # userwatch_public_pb2.ChallengeType
                        userInfo,  # userwatch_public_pb2.UserInfo
                        deviceId,  # string
                        origin=None  # Optional. Required for webauthn Should be consistent eg. login.company.com or similar
                        ):
        def doit():
            return self.shepherd.CreateChallenge(
                userwatch_shepherd_pb2.CreateChallengeRequest(
                    type=type,
                    userinfo=userInfo,
                    device_id=deviceId,
                    origin=origin
                ),
                metadata=[("x-api-key", self.privateApiKey)]
            )

        return self.__retryNonIllegalArg(doit, "createChallenge")

    def verifyChallenge(
        self,
        type,  # userwatch_public_pb2.ChallengeType
        userInfo,  # userwatch_public_pb2.UserInfo
        deviceId,  # string
        challengeId,  # string
        secretResponse  # string, eg the sms code.
    ):
        def doit():
            return self.shepherd.VerifyChallenge(
                userwatch_shepherd_pb2.ChallengeVerificationRequest(
                    type=type,
                    userinfo=userInfo,
                    device_id=deviceId,
                    challenge_id=challengeId,
                    secret_response=secretResponse
                ),
                metadata=[("x-api-key", self.privateApiKey)]
            )

        return self.__retryNonIllegalArg(doit, "verifyChallenge")

    # def reportDevice(self, userId, deviceId):
    #     return self.shepherd.reportDevice(
    #         userId=userId,
    #         deviceId=deviceId,
    #         global
    #     )

    # def approveDevice(self, userId, deviceId):
    #     return self.shepherd.approveDevice(
    #         userId=userId,
    #         deviceId=deviceId,
    #         global
    #     )

    def getDeviceList(self, userId):
        def doit():
            return self.shepherd.GetDeviceList(
                userwatch_shepherd_pb2.DeviceListRequest(user_id=userId),
                metadata=[("x-api-key", self.privateApiKey)]
            )

        return self.__retryNonIllegalArg(doit, "getDeviceList")

    # Run the function, retrying once on errors other than illegal argument.
    # Illegal argument errors, will never work a second time.
    # We primarily expect the retry to succeed when there is an intermittent
    # network error
    #
    # Consider asking customers to use the 'retry' library if they want more
    # nuanced logic. https://pypi.org/project/retry/
    # We should be cautious about what retry behaviour we apply globally.

    def __retryNonIllegalArg(self, fn, what: str):
        try:
            return fn()
        except grpc.RpcError as err:
            self.__logError(what + " failed", err)
            if err and err.code() == grpc.StatusCode.INVALID_ARGUMENT:
                raise err
            else:
                return fn()

    def __logError(self, msg, err):
        self.__log(msg, userwatch_historian_pb2.LOG_SEVERITY_ERROR, err)

    def __log(self, msg, severity, err):
        logEntry = userwatch_historian_pb2.LogEntry()
        logEntry.severity = severity

        message = msg
        if err != None and isinstance(err, Exception):
            message += " -- " + str(err)
            trace = traceback.TracebackException.from_exception(err)
            if len(trace.stack) > 0:
                filename = trace.stack[0].filename
                line = trace.stack[0].lineno
                function = trace.stack[0].name
                logEntry.source_location.file = filename
                logEntry.source_location.line = line
                logEntry.source_location.function = function
        if severity == userwatch_historian_pb2.LOG_SEVERITY_ERROR:
            message += "\n" + traceback.format_exc()

        logEntry.text_payload = json.dumps({
            "eventTime": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
            "serviceContext": {
                "service":  "pythonLibrary"
            },
            "message": message,
            "reportLocation": {
                "filePath": logEntry.source_location.file,
                "lineNumber": logEntry.source_location.line,
                "functionName": logEntry.source_location.function,
            },
        })
        logEntry.source_name =  "pythonLibrary"
        
        future = self.historian.ReportLogEntry.future(
            logEntry,
            metadata=[("x-api-key", self.privateApiKey)])
        # This callback on the future would seem to do nothing but having it seems to make all the
        # difference on if the api call is reliably made.
        future.add_done_callback(lambda f: None)
