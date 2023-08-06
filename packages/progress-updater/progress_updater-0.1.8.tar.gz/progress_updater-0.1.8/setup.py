# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['progress_updater', 'progress_updater.backends']

package_data = \
{'': ['*']}

install_requires = \
['psycopg2-binary>=2.9.3,<3.0.0',
 'psycopg2>=2.9.3,<3.0.0',
 'pydantic>=1.10.1,<2.0.0',
 'pymongo>=4.2.0,<5.0.0',
 'redis>=4.3.4,<5.0.0',
 'sqlmodel>=0.0.8,<0.0.9']

setup_kwargs = {
    'name': 'progress-updater',
    'version': '0.1.8',
    'description': 'Progress Updater',
    'long_description': 'progress-updater\n=================\n\n[![Documentation Status](https://readthedocs.org/projects/progress-updater/badge/?version=latest)](https://progress-updater.readthedocs.io/en/latest/?badge=latest)\n[![License-MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pyprogrammerblog/progress-updater/blob/master/LICENSE)\n[![GitHub Actions](https://github.com/pyprogrammerblog/progress-updater/workflows/CI/badge.svg/)](https://github.com/pyprogrammerblog/progress-updater/workflows/CI/badge.svg/)\n[![PyPI version](https://badge.fury.io/py/progress-updater.svg)](https://badge.fury.io/py/progress-updater)\n\nWriting the progress of a task to a backend!\n\nInstallation\n-------------\n\nInstall it using ``pip``\n\n```shell\npip install progress-updater\n```\n\nBasic usage\n-------------\n\n```python\nfrom progress_updater import ProgressUpdater\nfrom progress_updater.backends.mongo import MongoSettings\n\nsettings = MongoSettings(\n    mongo_connection="mongodb://user:pass@mongo:27017",\n    mongo_db="db",\n    mongo_collection="logs",\n)\n\nupdater = ProgressUpdater(task_name="My Task", settings=settings)\n\nwith updater(block_name="First part"):\n    # doing things\n    updater.notify("doing first block...")\n    # doing more things\n\nwith updater(block_name="Second part"):\n    # doing things\n    updater.notify("doing second block...")\n    # doing more things\n\nupdater.raise_latest_exception()  # if exists\n```\n\nThe output is:\n```shell\n- Task: My task\n\n- Entering First part\n  doing first block...\n\tTime spent: 0h0m\n\tSuccessfully completed\n\n- Entering Second part\n  doing second block...\n\tTime spent: 0h0m\n\tSuccessfully completed\n```\n\nBackends\n-------------------\nThe available backends to store logs are **Mongo**, **Redis** and **SQL**.\nPlease read the [docs](https://progress-updater.readthedocs.io/en/latest/) \nfor further information.\n\nEnvironment variables\n-----------------------\nYou can set your backend by defining env vars.\nThe `PU__` prefix indicates that it belongs to `ProgressUpdater`.\n```shell\n# SQL\nPU__SQL_DSN=\'postgresql+psycopg2://user:pass@postgres:5432/db\'\nPU__SQL_TABLE=\'logs\'\n\n# Redis\nPU__REDIS_HOST=\'redis\'\nPU__REDIS_DB=\'1\'\nPU__REDIS_PASSWORD=\'pass\'\n\n# Mongo\nPU__MONGO_CONNECTION=\'mongodb://user:pass@mongo:27017\'\nPU__MONGO_DB=\'db\'\nPU__MONGO_COLLECTION=\'logs\'\n```\n\nAnd then when creating a `ProgressUpdater` object, the backend will be \nautomatically configured.\n```python\nfrom progress_updater import ProgressUpdater\n\nwith ProgressUpdater(task_name="My Task") as updater:\n    pass\n```\n\nDocumentation\n--------------\n\nPlease visit this [link](https://progress-updater.readthedocs.io/en/latest/) for documentation.\n',
    'author': 'Jose Vazquez',
    'author_email': 'josevazjim88@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pyprogrammerblog/progress-updater',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
