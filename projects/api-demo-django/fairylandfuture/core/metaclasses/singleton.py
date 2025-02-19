# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-03 22:53:43 UTC+08:00
"""

import threading
from typing import Dict


class SingletonMeta(type):
    """
    Singleton pattern metaclass
    """

    _instance: Dict = {}
    _lock: threading.Lock = threading.Lock()

    # @functools.lru_cache(maxsize=0)
    def __call__(cls, *args, **kwargs):
        """
        Singleton pattern metaclass

        :param args: ...
        :type args: tuple
        :param kwargs: ...
        :type kwargs: dict
        :return: get instance
        :rtype: object
        """
        # if not hasattr(cls, "_instance"):
        #     setattr(cls, "_instance", super().__call__(*args, **kwargs))
        #     return getattr(cls, "_instance")
        # else:
        #     return getattr(cls, "_instance")

        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kwargs)
                cls._instance.update({cls: instance})
        return cls._instance.get(cls)
