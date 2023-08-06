# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyup']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3',
 'paramiko>=2.10.2',
 'pymongo[srv]>=4.0.2',
 'pyperclip>=1.8.2',
 'python-dotenv>=0.20.0',
 'rich>=10.11.0',
 'tqdm>=4.62.3']

entry_points = \
{'console_scripts': ['pyup = pyup:cli.main']}

setup_kwargs = {
    'name': 'pyup',
    'version': '0.1.4',
    'description': 'Caddy file server in Python with many additional features!',
    'long_description': '# pyup\n\n# Getting Started\n\n- On the server host machine:\n\n1. Clone the repo:\n\n```shell\ngit clone https://github.com/Alyetama/pyup.git\n```\n\n2. Rename and update `.env`:\n\n```shell\nmv .env.example .env\nnano .env  # or any other text editor\n```\n\n3. Create a docker volume, then run the container:\n\n```shell\ndocker volume create fileserver_mongodb_volume\ndocker-compose up -d\n```\n\n- Copy the `.env` file from the server host to the client machine (where you will upload from), then, run:\n\n```shell\nmv .env ~/.pyup\n```\n\n## Install\n\n```shell\npip install pyup\n```\n\n## Basic Usage\n\n```\nusage: pyup [-h] [-d DOMAIN_NAME] [-k] [--overwrite] [-l] [--no-notifications] [-v {0,1,2,3,4,5}] [-p]\n            [--save-logs]\n            [files ...]\n\npositional arguments:\n  files                 Files to upload\n\noptions:\n  -h, --help            show this help message and exit\n  -d DOMAIN_NAME, --domain-name DOMAIN_NAME\n                        The domain name to use for the URL\n  -k, --keep-name       Keep the original file name\n  --overwrite           Overwrite if name is kept and the file name already exists on the server\n  -l, --local-only      Allow uploads from local IP addresses only\n  --no-notifications    Suppress notifications (notifications are supported on macOS only)\n  -v {0,1,2,3,4,5}, --verbosity-level {0,1,2,3,4,5}\n                        Set the logging verbosity level\n  -p, --parallel        Upload files in parallel\n  --save-logs           Save logs to a file\n```\n',
    'author': 'Alyetama',
    'author_email': 'malyetama@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
