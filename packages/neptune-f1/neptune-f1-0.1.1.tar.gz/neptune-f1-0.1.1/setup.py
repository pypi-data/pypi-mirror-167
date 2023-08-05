# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_f1',
 'neptune_f1.domain',
 'neptune_f1.packets',
 'neptune_f1.packets.f12021',
 'neptune_f1.sources']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'neptune-f1',
    'version': '0.1.1',
    'description': 'EA F1 2021 telemetry integration with Neptune.ai',
    'long_description': '<h1 style="text-align: center">Neptune F1 Integration</h1>\n<p align="center">\n    <a href="https://github.com/Raalsky/neptune-f1/blob/master/LICENSE">\n        <img alt="GitHub" src="https://img.shields.io/github/license/Raalsky/neptune-f1.svg?color=blue">\n    </a>\n    <a href="https://codecov.io/gh/Raalsky/neptune-f1">\n        <img src="https://codecov.io/gh/Raalsky/neptune-f1/branch/master/graph/badge.svg?token=AFBHUE7GBQ"/>\n    </a>\n    <a href="https://github.com/Raalsky/neptune-f1/blob/master/.github/CODE_OF_CONDUCT.md">\n        <img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg">\n    </a>\n</p>\n',
    'author': 'Rafal Jankowski',
    'author_email': 'rafal@jankovsky.dev',
    'maintainer': 'Rafal Jankowski',
    'maintainer_email': 'rafal@jankovsky.dev',
    'url': 'https://github.com/Raalsky/neptune-f1',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
