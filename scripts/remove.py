# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-01-17 12:44:27 UTC+08:00
"""

import os
import fnmatch

exts = (
    ".DS_Store",
)

for dirpath, dirnames, filenames in os.walk("../itcast.data"):
    for filename in fnmatch.filter(filenames, ".DS_Store"):
        filepath = os.path.join(dirpath, filename)
        print(filepath)