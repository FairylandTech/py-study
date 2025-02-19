# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-14 19:24:42 UTC+08:00
"""

import base64

from fairylandfuture.enums.enconding import EncodingEnum


class Base64CryptionToolkits:

    @classmethod
    def encode(cls, data: str) -> str:
        """
        Encode the data using Base64.

        :param data: Required. The data to be encoded.
        :type data: str
        :return: Encoded data.
        :rtype: str
        """
        data = data.encode(EncodingEnum.utf8.value)
        encoded_data = base64.b64encode(data)
        return encoded_data.decode(EncodingEnum.utf8.value)

    @classmethod
    def decode(cls, encoded_data: str) -> str:
        """
        Decode the encoded data using Base64.

        :param encoded_data: Required. The encoded data to be decoded.
        :type encoded_data: str
        :return: Decoded data.
        :rtype: str
        """
        encoded_data = encoded_data.encode(EncodingEnum.utf8.value)
        decoded_data = base64.b64decode(encoded_data)
        return decoded_data.decode(EncodingEnum.utf8.value)
