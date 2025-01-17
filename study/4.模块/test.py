# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/models.py','w'))
# map(lambda f:f.close() ,l)

# 可以导入glance这个包
# import glance   # 在导入一个包的时候. 默认执行的是这个包下的__init__.py
# import master  # master.py
# glance.api.policy.get()  # 不可以这样直接使用


# import glance.api.policy
#
# glance.api.policy.get()


# 这种方案是我们使用包使用最多的
# from urllib.request import Request
# from glance.api import policy
# policy.get()


# # 错误示范       在使用from这种形式的导包. import后面不允许出现.
# from glance import api.policy
# api.policy.get()


from glance.api import policy
policy.get()



