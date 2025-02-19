# coding: UTF-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-30 14:20:28 UTC+08:00
"""

from fairylandfuture.core.superclass.modules.file import BaseFile, BaseTextFile, BaseYamlFile, BaseJsonFile


class File(BaseFile):
    """Base File class."""


class TextFile(BaseTextFile):
    """Base Text File class."""


class YamlFile(BaseYamlFile):
    """Base YAML File class."""


class JsonFile(BaseJsonFile):
    """Base JSON File class."""


class OtherTextFile(BaseTextFile):
    """Other File class."""
