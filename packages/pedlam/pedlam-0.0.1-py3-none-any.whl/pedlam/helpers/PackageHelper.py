import os
import re
import pkg_resources

class PackageHelper:

    __name = "a"

    __description = "Python memory allocation helper"

    __long_description = "Python memory allocation helper"

    __alias = "pedlam"

    __version = "0.0.1"

    @staticmethod
    def get_name():
        return PackageHelper.__name

    @staticmethod
    def get_description():
        return PackageHelper.__description

    @staticmethod
    def get_long_description():
        return PackageHelper.__long_description

    @staticmethod
    def get_alias():
        return PackageHelper.__alias

    @staticmethod
    def get_version():
        return PackageHelper.__version