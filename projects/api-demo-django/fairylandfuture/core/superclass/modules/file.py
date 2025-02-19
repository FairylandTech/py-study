# coding: UTF-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-30 15:02:13 UTC+08:00
"""

import hashlib
import json
import os
from pathlib import Path
from typing import Union, AnyStr, Sequence, Optional, Any, Self

import yaml

from fairylandfuture.enums.enconding import EncodingEnum
from fairylandfuture.enums.file import FileModeEnum


class BaseFile:
    """
    Base file class.

    :param path: file path.
    :type path: Union[Path, str]
    :param create: create file if not exists.
    :type create: bool

    Usage:
        >>> from fairylandfuture.core.superclass.files import BaseFile
        >>> from fairylandfuture.enums.enconding import EncodingEnum, FileModeEnum
        >>> file = BaseFile("path/to/file.txt")
        >>> file.name
        "file"
        >>> file.ext
        ".txt"
        >>> file.size_byte
        123456
        >>> file.size_kilobyte
        123.46
        >>> file.size_megabytes
        0.12
        >>> file.size_gigabyte
        0.00012
        >>> file.size_trillionbyte
        0.0000000012
        >>> file.size_petabyte
        0.0000000000012
        >>> file.size_exabyte
        0.0000000000000012
        >>> file.size_zettabyte
        0.0000000000000000012
        >>> file.size_yottabyte
        0.0000000000000000000012
        >>> file.size_brontobyte
        0.000000000012
        >>> file.dir_path
        "path/to"
        >>> file.read(FileModeEnum.r)
        "Hello, world!"
        >>> file.md5
        "1b2cf535f27732324c34a76544b79991"
        >>> file.sha256
        "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
        >>> file.write("Hello, world!", mode=FileModeEnum.w)
        "path/to/file.txt"
    """

    def __init__(self, path: Union[Path, str], /, *, create: bool = False):
        if os.path.isdir(path):
            raise ValueError("Path is a directory.")
        if not os.path.exists(path):
            if create:
                open(path, "w").close()
            else:
                raise FileNotFoundError("File not found.")

        self._path: Union[Path, str] = path
        self.max_size: Union[int, float] = 10 * (1024**2)
        self._dir_path: str = os.sep.join(self._path.split(os.sep)[:-1])
        self._file_name, self._file_ext = os.path.splitext(self._path.split(os.sep)[-1])
        self._file_size: float = os.path.getsize(self._path)

    @property
    def name(self) -> str:
        return self._file_name

    @property
    def ext(self) -> str:
        return self._file_ext

    @property
    def path(self):
        return self._path

    @property
    def dir_path(self) -> str:
        return self._dir_path

    @property
    def size_byte(self) -> float:
        return self._file_size

    @property
    def size_kilobyte(self) -> float:
        return self._file_size / 1024

    @property
    def size_megabytes(self) -> float:
        return self._file_size / (1024**2)

    @property
    def size_gigabyte(self) -> float:
        return self._file_size / (1024**3)

    @property
    def size_trillionbyte(self) -> float:
        return self._file_size / (1024**4)

    @property
    def size_petabyte(self) -> float:
        return self._file_size / (1024**5)

    @property
    def size_exabyte(self) -> float:
        return self._file_size / (1024**6)

    @property
    def size_zettabyte(self) -> float:
        return self._file_size / (1024**7)

    @property
    def size_yottabyte(self) -> float:
        return self._file_size / (1024**8)

    @property
    def size_brontobyte(self) -> float:
        return self._file_size / (1024**9)

    @property
    def md5(self) -> str:
        data = self.read(FileModeEnum.rb)

        return hashlib.md5(data).hexdigest()

    @property
    def sha256(self) -> str:
        data = self.read(FileModeEnum.rb)

        return hashlib.sha256(data).hexdigest()

    def vaildate_ext(self, exts: Sequence[str], /) -> None:
        if self.ext not in exts:
            raise TypeError("File extension is not valid.")

    def read(self, mode: FileModeEnum = None, /, *, encoding: Optional[EncodingEnum] = None) -> AnyStr:
        """
        Read data from file.

        :param mode: File mode.
        :type mode: str
        :param encoding: File encoding.
        :type encoding: str
        :return: Read data.
        :rtype: str
        """
        if not mode:
            mode = FileModeEnum.r
        if not encoding:
            encoding = EncodingEnum.default

        if self.size_byte > self.max_size:
            raise ValueError("Out of file size max.")

        if "b" in mode.value:
            with open(self.path, mode.value) as stream:
                data = stream.read()
            return data
        else:
            with open(self.path, mode.value, encoding=encoding.value) as stream:
                data = stream.read()
            return data

    def write(self, data: AnyStr, /, *, mode: FileModeEnum, encoding: Optional[EncodingEnum] = None) -> str:
        """
        Write data to file.

        :param mode: File mode.
        :type mode: str
        :param data: File data.
        :type data: ...
        :param encoding: File encoding.
        :type encoding: str
        :return: File path.
        :rtype: str
        """
        if not mode:
            mode = FileModeEnum.w
        if not encoding:
            encoding = EncodingEnum.default

        if self.size_byte > self.max_size:
            raise ValueError(f"Out of file size max: {self.max_size}.")

        if "b" in mode.value:
            with open(self.path, mode.value) as stream:
                stream.write(data)
        else:
            with open(self.path, mode.value, encoding=encoding.value) as stream:
                stream.write(data)

        return str(self.path)


class BaseTextFile(BaseFile):
    """
    Text file.

    :param path: file path.
    :type path: Union[Path, str]
    :param create: create file if not exists.
    :type create: bool

    Usage:
        >>> file = BaseTextFile("path/to/file.txt")
        >>> file.load_text()
        "Hello, world!"
        >>> file.save_text("Hello, world!")
        "path/to/file.txt"
    """

    def __init__(self, path: Union[Path, str], create: bool = False):
        super().__init__(path, create=create)

    def load_text(self) -> str:
        """
        Load text data from file.

        :return: Text data.
        :rtype: str
        """
        return super().read(FileModeEnum.r)

    def save_text(self, data: AnyStr, /) -> str:
        """
        Save text data to file.

        :param data: Text file data.
        :type data: ...
        :return: Text file path.
        :rtype: str
        """
        return super().write(data, mode=FileModeEnum.w)


class BaseYamlFile(BaseFile):
    """
    Yaml file.

    :param path: file path.
    :type path: Union[Path, str]
    :param create: create file if not exists.
    :type create: bool

    Usage:
        >>> file = BaseYamlFile("path/to/file.yaml")
        >>> file.load_yaml()
        {'key': 'value'}
        >>> file.save_yaml({'key': 'value'})
        "path/to/file.yaml"
    """

    def __init__(self, path: Union[Path, str], create: bool = False):
        super().__init__(path, create=create)

        self.vaildate_ext((".yaml", ".yml"))

    def load_yaml(self) -> Any:
        """
        Load yaml data from file.

        :return: Python YAML object.
        :rtype: ...
        """
        data = super().read(FileModeEnum.r)

        return yaml.load(data, Loader=yaml.FullLoader)

    def save_yaml(self, data: Any, /) -> str:
        """
        Save yaml data to file.

        :param data: Yaml file data.
        :type data: ...
        :return: Yaml file path.
        :rtype: str
        """
        yaml_data = yaml.dump(data, indent=2)

        return super().write(yaml_data, mode=FileModeEnum.w)


class BaseJsonFile(BaseFile):
    """
    Json file.

    :param path: file path.
    :type path: Union[Path, str]
    :param create: create file if not exists.
    :type create: bool

    Usage:
        >>> file = BaseJsonFile("path/to/file.json")
        >>> file.load_json()
        {'key': 'value'}
        >>> file.save_json({'key': 'value'})
        "path/to/file.json"
    """

    def __init__(self, path: Union[Path, str], create: bool = False):
        super().__init__(path, create=create)

        self.vaildate_ext((".json",))

    def load_json(self) -> Any:
        """
        Load json data from file.

        :return: Python JSON object.
        :rtype: ...
        """
        data = super().read(FileModeEnum.r)

        return json.loads(data)

    def save_json(self, data: Any) -> str:
        """
        Save json data to file.

        :param data: Json file data.
        :type data: ...
        :return: Json file path.
        :rtype: str
        """
        data = json.dumps(data, indent=2, ensure_ascii=False)

        return super().write(data, mode=FileModeEnum.w)
