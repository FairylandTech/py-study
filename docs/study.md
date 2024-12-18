解释性语言, 在win中可以被编译为pyd, 在unix中可以被编译为so/pyo, pyc文件是py的二进制文件, 在执行py脚本时, 会以脚本的当前路径为根路径生产``__pycache__`的文件夹, 里面就是pyc二进制文件



python 各个版本有出入

python2.7, python3.6.3, python3.8, python3.9, python3.11



开发IDEA: pycharm, IDEA, vscode, vs



脚本/项目, 都有两类方式, 面向对象(复用性高), 函数式(简单, 逻辑通透)



python的运行方式, 只有一个主入口, 而且一定要注意导包(建议 `from ... import ...`)



python包: 文件夹形式, 但是这个文件夹中又`__init__.py`的文件叫python的包, 没有py文件的叫`目录`

python模块: 一个py文件就是一个模块



python的解释器和虚拟环境

pip: python的包管理工具(第三方包管理) `https://pypi.com`

pipenv, venv, pipreq, toml

科学计算: Anaconda, MiniAnaconda



基础模块:

```python
import os
import sys
import shutil
import subprocess
import math
import time
import datetime
import json

import yaml

import requests

import pandas as pd
import numpy as np
```