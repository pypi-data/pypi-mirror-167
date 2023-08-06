# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['notify', 'notify.channels']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ml-simple-notify',
    'version': '0.1.1',
    'description': '一个简单可扩展的消息通知库',
    'long_description': '### 一个简单可扩展的消息通知库\n\n#### 安装\n> pip install ml-simple-notify\n\n#### 使用\n```python\nfrom notify.notification import Notify\n# import settings\n\nnotify = Notify.from_settings()\nnotify.send_message(content="content", title="title")\n```\n\nsettings模板文件可参考default_settings.py\n\n```python\n# 消息通知渠道的配置项\nCHANNELS = {\n    \'DING\': {\n        \'ACCESS_TOKEN\': "ee45bea8e9b5029a9c71*********6f0d98cff232a6b35e52df2",\n        \'AT_ALL\': True\n    }\n}\n# 消息通知启用项目\nTRIGGERS = {\n    # 开启库中钉钉消息通知，对应的CHANNELS中需要配置钉钉的token\n    \'notify.channels.ding.Ding\': 100,\n}\n```\n\n#### 自己开发消息通知\n```python\nfrom notify.notification import Notification\n\n\nclass Custom(Notification):\n    """自定义消息"""\n    def __init__(self, settings):\n        self.settings = settings\n\n    def send_message(self, content, title=None):\n        print(f"来自自定义的消息{content}")\n\n    @classmethod\n    def from_settings(cls, settings):\n        return cls(settings)\n```\n随后在settings.py文件中的TRIGGERS开启此通知\n```python\nTRIGGERS = {\n    \'channels.custom.Custom\': 100,\n}\n```\n触发器的值为字典类型，键名为包路径，键值为优先级，值越小优先级越高',
    'author': 'miclon',
    'author_email': 'jcnd@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
