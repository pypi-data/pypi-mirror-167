import os
import logging
import eons as e
import shutil
import jsonpickle
from pathlib import Path

######## START CONTENT ########
# All APIer errors
class APIError(Exception): pass


# Exception used for miscellaneous API errors.
class OtherAPIError(APIError): pass

class EBBS(e.Executor):

    def __init__(this):
        super().__init__(name="Application Program Interface with eons", descriptionStr="A readily extensible take on APIs.")

        # this.RegisterDirectory("ebbs")


    #Configure class defaults.
    #Override of eons.Executor method. See that class for details
    def Configure(this):
        super().Configure()

        this.defualtConfigFile = "apie.json"


    #Override of eons.Executor method. See that class for details
    def RegisterAllClasses(this):
        super().RegisterAllClasses()
        # this.RegisterAllClassesInDirectory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build"))


    #Override of eons.Executor method. See that class for details
    def AddArgs(this):
        super().AddArgs()
        this.argparser.add_argument('-h','--host', type = str, metavar = '127.0.0.1', default = '0.0.0.0', help = 'host ip to accept connections through', dest = 'host')
        this.argparser.add_argument('-p','--port', type = str, metavar = '80', help = 'port to run on', dest = 'port')


    #Override of eons.Executor method. See that class for details
    def UserFunction(this):
        super().UserFunction()
        


class Endpoint(e.UserFunctor):
    def __init__(this, name=e.INVALID_NAME()):
        super().__init__(name)

        this.enableRollback = False


    # Call things!
    # Override this or die.
    # Empty Callers can be used with call.json to start call trees.
    def Call(this):
        pass


    # Deprecated!
    # Override this to perform whatever success checks are necessary.
    # This will be called before running the next call step.
    def DidCallSucceed(this):
        return True


    # API compatibility shim
    def DidUserFunctionSucceed(this):
        return this.DidCallSucceed()


    # Hook for any pre-call configuration
    def PreCall(this):
        pass


    # Hook for any post-call configuration
    def PostCall(this):
        pass


    # Override of eons.Functor method. See that class for details
    def UserFunction(this):

        this.PreCall()

        logging.debug(f"<---- Calling {this.name} ---->")
        this.Call()
        logging.debug(f">---- Done Calling {this.name} ----<")

        this.PostCall()



