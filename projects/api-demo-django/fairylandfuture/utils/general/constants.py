# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-10 10:27:11 UTC+08:00
"""

from typing import Any, Dict, List, Set, Tuple


class DefaultConstantUtils:
    """
    Default constant utils.
    """

    @staticmethod
    def string() -> str:
        results = str()
        return results

    @staticmethod
    def integer() -> int:
        results = int()
        return results

    @staticmethod
    def float() -> float:
        results = float()
        return results

    @staticmethod
    def boolean() -> bool:
        results = bool()
        return results

    @staticmethod
    def list() -> List[None]:
        results = []
        return results

    @staticmethod
    def tuple() -> Tuple[None]:
        results = tuple()
        return results

    @staticmethod
    def set() -> Set[None]:
        results = set()
        return results

    @staticmethod
    def dict() -> Dict[None, None]:
        results = {}
        return results

    @staticmethod
    def none() -> None:
        return None

    @staticmethod
    def byte() -> bytes:
        results = bytes()
        return results

    @staticmethod
    def bytearray() -> bytearray:
        results = bytearray()
        return results

    @staticmethod
    def complex() -> complex:
        results = complex()
        return results


class APIConstantUtils(DefaultConstantUtils):
    """
    API constant utils.
    """

    @staticmethod
    def results() -> Dict[str, Any]:
        results = {"status": "failure", "code": 500, "data": None}
        return results


class EncodingConstantUtils(DefaultConstantUtils):
    """
    Encoding constant utils.
    """

    @staticmethod
    def encodings() -> Tuple[str, ...]:
        results = (
            "big5",
            "big5-hkscs",
            "cesu-8",
            "euc-jp",
            "euc-kr",
            "gb18030",
            "gb2312",
            "gbk",
            "ibm-thai",
            "ibm00858",
            "ibm01140",
            "ibm01141",
            "ibm01142",
            "ibm01143",
            "ibm01144",
            "ibm01145",
            "ibm01146",
            "ibm01147",
            "ibm01148",
            "ibm01149",
            "ibm037",
            "ibm1026",
            "ibm1047",
            "ibm273",
            "ibm277",
            "ibm278",
            "ibm280",
            "ibm284",
            "ibm285",
            "ibm290",
            "ibm297",
            "ibm420",
            "ibm424",
            "ibm437",
            "ibm500",
            "ibm775",
            "ibm850",
            "ibm852",
            "ibm855",
            "ibm857",
            "ibm860",
            "ibm861",
            "ibm862",
            "ibm863",
            "ibm864",
            "ibm865",
            "ibm866",
            "ibm868",
            "ibm869",
            "ibm870",
            "ibm871",
            "ibm918",
            "iso-2022-cn",
            "iso-2022-jp",
            "iso-2022-jp-2",
            "iso-2022-kr",
            "iso-8859-1",
            "iso-8859-13",
            "iso-8859-15",
            "iso-8859-2",
            "iso-8859-3",
            "iso-8859-4",
            "iso-8859-5",
            "iso-8859-6",
            "iso-8859-7",
            "iso-8859-8",
            "iso-8859-9",
            "jis_x0201",
            "jis_x0212-1990",
            "koi8-r",
            "koi8-u",
            "shift_jis",
            "tis-620",
            "us-ascii",
            "utf-16",
            "utf-16be",
            "utf-16le",
            "utf-32",
            "utf-32be",
            "utf-32le",
            "utf-8",
            "windows-1250",
            "windows-1251",
            "windows-1252",
            "windows-1253",
            "windows-1254",
            "windows-1255",
            "windows-1256",
            "windows-1257",
            "windows-1258",
            "windows-31j",
            "x-big5-hkscs-2001",
            "x-big5-solaris",
            "x-euc-jp-linux",
            "x-euc-tw",
            "x-eucjp-open",
            "x-ibm1006",
            "x-ibm1025",
            "x-ibm1046",
            "x-ibm1097",
            "x-ibm1098",
            "x-ibm1112",
            "x-ibm1122",
            "x-ibm1123",
            "x-ibm1124",
            "x-ibm1166",
            "x-ibm1364",
            "x-ibm1381",
            "x-ibm1383",
            "x-ibm300",
            "x-ibm33722",
            "x-ibm737",
            "x-ibm833",
            "x-ibm834",
            "x-ibm856",
            "x-ibm874",
            "x-ibm875",
            "x-ibm921",
            "x-ibm922",
            "x-ibm930",
            "x-ibm933",
            "x-ibm935",
            "x-ibm937",
            "x-ibm939",
            "x-ibm942",
            "x-ibm942c",
            "x-ibm943",
            "x-ibm943c",
            "x-ibm948",
            "x-ibm949",
            "x-ibm949c",
            "x-ibm950",
            "x-ibm964",
            "x-ibm970",
            "x-iscii91",
            "x-iso-2022-cn-cns",
            "x-iso-2022-cn-gb",
            "x-iso-8859-11",
            "x-jis0208",
            "x-jisautodetect",
            "x-johab",
            "x-macarabic",
            "x-maccentraleurope",
            "x-maccroatian",
            "x-maccyrillic",
            "x-macdingbat",
            "x-macgreek",
            "x-machebrew",
            "x-maciceland",
            "x-macroman",
            "x-macromania",
            "x-macsymbol",
            "x-macthai",
            "x-macturkish",
            "x-macukraine",
            "x-ms932_0213",
            "x-ms950-hkscs",
            "x-ms950-hkscs-xp",
            "x-mswin-936",
            "x-pck",
            "x-sjis_0213",
            "x-utf-16le-bom",
            "x-utf-32be-bom",
            "x-utf-32le-bom",
            "x-windows-50220",
            "x-windows-50221",
            "x-windows-874",
            "x-windows-949",
            "x-windows-950",
            "x-windows-iso2022jp",
        )
        return results
