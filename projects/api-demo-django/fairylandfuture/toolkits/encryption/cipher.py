# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-14 18:12:41 UTC+08:00
"""

import hashlib
import os
import secrets
import string
from typing import Optional, Tuple

from cryptography.fernet import Fernet

from fairylandfuture.enums.enconding import EncodingEnum


class CipherToolkits:

    @classmethod
    def generate_salt(cls, length: int = 16) -> str:
        """
        Generate a random salt.

        :param length: Length of the salt.
        :type length: int
        :return: Salt.
        :rtype: str
        """
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(length))

    @classmethod
    def generate_key(cls) -> bytes:
        """
        Generate a random key.

        :return: Key.
        :rtype: bytes
        """
        return Fernet.generate_key()


class UserPasswordCryptionToolkits(CipherToolkits):

    @classmethod
    def encrypt(cls, password: str, salt: Optional[str] = None) -> Tuple[str, str]:
        """
        Use MD5 to encrypt the password.

        :param password: Required. The password to be encrypted.
        :type password: str
        :param salt: Salt to be used for encryption. If not provided, a random salt will be generated.
        :type salt: str
        :return: Tuple of encrypted password and salt.
        :rtype: Tuple[str, str]
        """
        if not salt:
            salt = os.urandom(16)
        else:
            salt = salt.encode(EncodingEnum.utf8.value)
        password = password.encode(EncodingEnum.utf8.value)
        salted_password = password + salt
        hashed_password = hashlib.md5(salted_password).hexdigest()
        return hashed_password, salt.hex() if isinstance(salt, bytes) else salt

    @classmethod
    def verify(cls, password: str, hashed_password: str, salt: str) -> bool:
        """
        Verify the password with the hashed password and salt.

        :param password: Required. The password to be verified.
        :type password: str
        :param hashed_password: Required. The hashed password to be verified.
        :type hashed_password: str
        :param salt: Required. The salt to be used for verification.
        :type salt: str
        :return: True if the password is verified, False otherwise.
        :rtype: bool
        """
        salt = bytes.fromhex(salt)
        password = password.encode(EncodingEnum.utf8.value)
        salted_password = password + salt
        hashed_password_to_verify = hashlib.md5(salted_password).hexdigest()
        return hashed_password_to_verify == hashed_password


class PasswordCryptionToolkits(CipherToolkits):

    @classmethod
    def encrypt(cls, password: str, key: bytes) -> Tuple[str, str]:
        """
        Encrypt the password using Fernet.

        :param password: Required. The password to be encrypted.
        :type password: str
        :param key: Key to be used for encryption. If not provided, a random key will be generated.
        :type key: bytes
        :return: Encrypted password and key.
        :rtype: tuple
        """
        fernet = Fernet(key)
        password = password.encode(EncodingEnum.utf8.value)
        encrypted_password = fernet.encrypt(password)
        return encrypted_password.decode(EncodingEnum.utf8.value), key.decode(EncodingEnum.utf8.value)

    @classmethod
    def decrypt(cls, encrypted_password, key):
        """
        Decrypt the encrypted password using Fernet.

        :param encrypted_password: Required. The encrypted password to be decrypted.
        :type encrypted_password: str
        :param key: Required. The key to be used for decryption.
        :type key: bytes
        :return: Decrypted password.
        :rtype: str
        """
        fernet = Fernet(key)
        encrypted_password = encrypted_password.encode(EncodingEnum.utf8.value)
        decrypted_password = fernet.decrypt(encrypted_password)
        return decrypted_password.decode(EncodingEnum.utf8.value)
