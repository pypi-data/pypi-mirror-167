import signal
import colorlog

from pedlam.helpers.PackageHelper import PackageHelper

class Driver:

    def __init__(self, args):

        self.__args = args

    def start(self):
        colorlog.getLogger().info("Hello World!")