# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-26 00:29:04 UTC+08:00
"""

import os
import platform
import sys


class OSPlatform:
    """
    OS Platform
    """

    @staticmethod
    def platform():
        """
        Get OS Platform
        :return: OS Platform
        """
        return platform.system()

    @staticmethod
    def uid():
        """
        Get OS UID
        :return: OS UID
        """
        return os.getuid()

    @staticmethod
    def gid():
        """
        Get OS PID
        :return: OS PID
        """
        return os.getgid()

    @staticmethod
    def username():
        """
        Get OS Username
        :return: OS Username
        """
        return os.getlogin()

    @staticmethod
    def version():
        """
        Get OS Version
        :return: OS Version
        """
        return platform.version()

    @staticmethod
    def architecture():
        """
        Get OS Architecture
        :return: OS Architecture
        """
        return platform.machine()

    @staticmethod
    def python_version():
        """
        Get Python Version
        :return: Python Version
        """
        return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
