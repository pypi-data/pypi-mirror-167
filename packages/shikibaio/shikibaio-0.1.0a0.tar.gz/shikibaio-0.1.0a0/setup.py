# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['shikibaio',
 'shikibaio.enums',
 'shikibaio.filters',
 'shikibaio.testing',
 'shikibaio.types']

package_data = \
{'': ['*']}

install_requires = \
['aiocometd>=0.4.5,<0.5.0', 'shiki4py>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'shikibaio',
    'version': '0.1.0a0',
    'description': 'Asynchronous bot development framework for shikimori.',
    'long_description': '<p align="center">\n  <a href="https://github.com/ren3104/shikibaio/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ren3104/shikibaio"></a>\n  <a href="https://pypi.org/project/shikibaio"><img src="https://img.shields.io/pypi/v/shikibaio?color=blue" alt="PyPi package version"></a>\n  <a href="https://pypi.org/project/shikibaio"><img src="https://img.shields.io/pypi/pyversions/shikibaio.svg" alt="Supported python versions"></a>\n  <img src="https://img.shields.io/github/repo-size/ren3104/shikibaio" alt="GitHub repo size">\n  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>\n</p>\n\n> Данный пакет находится в стадии разработки, потому может содержать баги и недоработки!\n\n~~Shikimori bot asyncio~~ Shikibaio - это асинхронный python фреймворк разработки ботов для [shikimori](https://shikimori.one).\n\n- [Особенности](#особенности)\n- [Установка](#установка)\n- [Пример эхо бота](#пример-эхо-бота)\n- [Тестирование](#тестирование)\n- [Зависимости](#зависимости)\n\n## Особенности\n- Асинхронность\n- Типизированность\n\n## Установка\n```bash\npip install -U shikibaio\n```\n\n## Пример эхо бота\n```python\nfrom shikibaio import Dispatcher\nfrom shikibaio.types import Event\nfrom shiki4py import Shikimori\n\n\napi = Shikimori("Api Test")\ndp = Dispatcher(api)\n\ndp.subscribe_topic(topic_id=555400, is_user_topic=True)\n\n\n@dp.topic_handler()\nasync def echo(event: Event):\n    await api.comments.create(event.text, event.chat_id, "User")\n\n\ndp.run()\n```\n\n## Тестирование\nВ shikibaio предусмотрены специальные классы для тестирования ваших проектов, чтобы не спамить в топиках шикимори.\n\nДля этого изменим код в примере эхо бота:\n```python\nfrom shikibaio import Dispatcher\nfrom shikibaio.types import Event\nfrom shikibaio.testing import Topic\nimport asyncio\n\n\ndp = Dispatcher()\n\n\n@dp.topic_handler()\nasync def echo(event: Event):\n    print(event.text)\n\n\nasync def main():\n    topic = Topic(dp)\n    await topic.create_comment("test")\n\n\nasyncio.run(main())\n```\n\n## Зависимости\n- [aiocometd](https://github.com/robertmrk/aiocometd) - для взаимодействия с faye сервером по веб сокету.\n- [shiki4py]() - для взаимодействия c api shikimori.\n',
    'author': 'ren3104',
    'author_email': '2ren3104@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ren3104/shikibaio',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
