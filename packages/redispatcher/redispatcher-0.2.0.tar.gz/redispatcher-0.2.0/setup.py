# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redispatcher']

package_data = \
{'': ['*']}

install_requires = \
['aioredis>=1.3.1,<2.0.0', 'pydantic>=1.8.1,<2.0.0']

entry_points = \
{'console_scripts': ['monitor = redispatcher.monitor:monitor_cli']}

setup_kwargs = {
    'name': 'redispatcher',
    'version': '0.2.0',
    'description': 'Dispatch and run distributed work asynchronously, brokered by Redis',
    'long_description': '# redispatcher\n\n<a href="https://rafalstapinski.github.io/redispatcher">\n  <img src="https://rafalstapinski.github.io/redispatcher/img/logo.svg" alt="redispatcher logo" />\n</a>\n\n<p align="center">\n  <strong>\n    <em>\n        Dispatch and run distributed work asynchronously, brokered by Redis\n    </em>\n  </strong>\n</p>\n\n---\n\n**Documentation**: <a href="https://rafalstapinski.github.io/redispatcher">https://rafalstapinski.github.io/redispatcher</a>\n\n**Source Code**: <a href="https://github.com/rafalstapinski/redispatcher">https://github.com/rafalstapinski/redispatcher</a>\n\n---\n\n<p align="center">\n  <a href="https://github.com/rafalstapinski/redispatcher/actions/workflows/test.yml" target="_blank">\n    <img src="https://github.com/rafalstapinski/redispatcher/actions/workflows/test.yml/badge.svg" alt="Test Status" />\n  </a>\n  <a href="https://pypi.org/project/redispatcher" target="_blank">\n    <img src="https://img.shields.io/pypi/v/redispatcher?color=%2334D058" alt="pypi" />\n  </a>\n  <a href="https://pypi.org/project/redispatcher" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/redispatcher?color=%23334D058" alt="Supported Python Versions: 3.8, 3.9, 3.10" />\n  </a>\n  <a href="https://github.com/rafalstapinski/redispatcher/blob/master/LICENSE" target="_blank">\n    <img src="https://img.shields.io/pypi/l/redispatcher?color=%23334D058" alt="MIT License" />\n  </a>\n</p>\n\n## What is redispatcher\n\nredispatcher allows you to dispatch work that needs to be done in a process separate from your main program loop. This is useful in cases when you need to process some long running work that doesn\'t necessarily need to be done synchronously within your code. A classic example of this is sending a welcome email to a user as they sign up for your service. It\'s not necessary to wait for the results of sending an email, and it may take a few seconds to do so. redispatcher lets you fire-and-forget this work (as a message put into a Redis server) and have it be executed in the background, asynchronously, in a separate process (or machine) entirely.\n\nredispatcher comes in two parts:\n1. A library that lets you define workers, define strongly typed messages sent to workers, and provides helper functions to facilitate dispatching that work\n2. A daemon that runs your workers in a pool, consistently listening for any incoming messages to be processed\n\n\n## Why use it\n\nThere are certainly other solutions for orchestrating distributed workers. redispatcher aims to be super lightweight, very fast and simple to set up (there are many free cloud-hosted Redis solutions available), and has robust type validation and intellisense support.\n## Features\n* Full intellisense support across your code, despite a distributed workload\n* Strongly typed message contract between your publishing code and consumer\n* Minimal boilerplate required to setup and start publishing compared than most alternatives\n* Minimal performance overhead and completely non-blocking, thanks to `asyncio` (and works with alternatives like `uvloop`)\n\n### Dependencies\n* `aioredis` is used under the hood to publish message to and read messages from Redis\n* `pydantic` is used to to validate messages conform to your strongly typed contracts\n\n\n## Installation\nInstall with `poetry`\n```bash\n$ poetry add redispatcher\n```\nor with `pip`\n```bash\n$ pip install redispatcher\n```\n## Basic Usage\n### Defining your worker\n```python\nfrom redispatcher import BaseConsumer\n\nclass SendWelcomeEmail(BaseConsumer):\n\n    QUEUE = "send-welcome-email"\n\n    class Message(BaseConsumer.Message):\n        email: str\n        name: str\n    \n    async def process_message(self, message: Message):\n        # construct an email and send it to the `message.email` address\n```\n\n### Dispatching work\n```python\nfrom clients import my_aioredis_client\n\n@app.post("/register")\nasync def register(...)\n    ...\n    message = SendWelcomeEmail.Message(email=..., name=..., registered=True)\n    await SendWelcomeEmail.dispatch(message, my_aioredis_client)\n    ...\n```\n\n### Running redispatcher\n```python\nfrom redispatcher import Redispatcher, RedispatcherConfig, ConsumerConfig\n\nconfig = RedispatcherConfig(\n    redis_dsn="redis://localhost:6379/0",\n    consumers=[\n        ConsumerConfig(\n            consumer_class=SendWelcomeEmail,\n            count=2\n        )\n    ]\n)\n\nif __name__ == "__main__":\n    dispatcher = Redispatcher(config)\n    dispatcher.start() \n```\n\n\n### Contributing\n\n`redispatcher` is already used in production, but is still in its infancy.\n\nIf you find a bug, <a href="https://github.com/rafalstapinski/redispatcher/issues/new">open an issue</a> with a detailed description and steps to reproduce.\n\nIf you\'re looking for a feature, <a href="https://github.com/rafalstapinski/redispatcher/issues/new">open an issue</a> with a detailed description and use case. Feel free <a href="https://github.com/rafalstapinski/redispatcher/pulls">open a pull request</a> if you want to contribure directly!\n',
    'author': 'Rafal Stapinski',
    'author_email': 'stapinskirafal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://rafalstapinski.github.io/redispatcher',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
