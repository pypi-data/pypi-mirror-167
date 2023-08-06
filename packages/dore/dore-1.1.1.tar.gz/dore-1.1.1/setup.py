# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dore',
 'dore.attribute',
 'dore.attribute.config',
 'dore.attribute.value_generators',
 'dore.attribute.value_generators.composite',
 'dore.attribute.value_generators.composite.config',
 'dore.attribute.value_generators.faker',
 'dore.attribute.value_generators.faker.config',
 'dore.attribute.value_generators.faker.utils',
 'dore.attribute.value_generators.ref',
 'dore.attribute.value_generators.ref.config',
 'dore.attribute.value_generators.selector',
 'dore.attribute.value_generators.selector.config',
 'dore.attribute.value_generators.selector.random_selector',
 'dore.attribute.value_generators.selector.random_selector.config',
 'dore.attribute.value_generators.selector.round_robin_selector',
 'dore.attribute.value_generators.selector.round_robin_selector.config',
 'dore.cache',
 'dore.cache.pydict',
 'dore.cache.redis',
 'dore.config',
 'dore.context',
 'dore.datastore',
 'dore.datastore.config',
 'dore.engine',
 'dore.exceptions',
 'dore.manifest',
 'dore.model',
 'dore.model.config',
 'dore.protocol',
 'dore.protocol.elasticsearch',
 'dore.protocol.elasticsearch.config',
 'dore.protocol.elasticsearch.elasticsearch7',
 'dore.protocol.elasticsearch.elasticsearch8',
 'dore.protocol.mongodb',
 'dore.protocol.mongodb.config',
 'dore.protocol.mysql',
 'dore.protocol.mysql.config',
 'dore.protocol.postgresql',
 'dore.protocol.postgresql.config',
 'dore.utils',
 'dore.utils.date',
 'dore.utils.file',
 'dore.utils.graph',
 'dore.utils.rand']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=13.4.0',
 'PyPika>=0.48.9',
 'elasticsearch7>=7.17.2,<8',
 'elasticsearch8>=8.1.2,<9',
 'jsonschema>=4.6.1',
 'mysqlclient>=2.1.0',
 'progressbar2>=4.0.0',
 'psycopg>=3.0.11',
 'pymongo>=4.1.1',
 'pystache>=0.6.0',
 'redis>=4.3.3']

entry_points = \
{'console_scripts': ['dore = dore.__main__:main']}

setup_kwargs = {
    'name': 'dore',
    'version': '1.1.1',
    'description': 'Schema based fake data generator',
    'long_description': "```text\n\n8 888888888o.           ,o888888o.      8 888888888o.    8 888888888888\n8 8888    `^888.     . 8888     `88.    8 8888    `88.   8 8888\n8 8888        `88.  ,8 8888       `8b   8 8888     `88   8 8888\n8 8888         `88  88 8888        `8b  8 8888     ,88   8 8888\n8 8888          88  88 8888         88  8 8888.   ,88'   8 888888888888\n8 8888          88  88 8888         88  8 888888888P'    8 8888\n8 8888         ,88  88 8888        ,8P  8 8888`8b        8 8888\n8 8888        ,88'  `8 8888       ,8P   8 8888 `8b.      8 8888\n8 8888    ,o88P'     ` 8888     ,88'    8 8888   `8b.    8 8888\n8 888888888P'           `8888888P'      8 8888     `88.  8 888888888888\n\n\n                   SCHEMA BASED FAKE DATA GENERATOR\n```\n\n## Helpful Links\n\n* [Project Site](https://dore-datagen.github.io/)\n* [Example](https://dore-datagen.github.io/example/)\n* [GitHub](https://github.com/dore-datagen/dore-py)\n\n\n### Installation\n\nOptional, but recommended: Create a virtual env and activate it.\n\n```shell\n(venv)$ python3 -m venv venv && source venv/bin/activate\n```\n\nInstall Dore\n\n```shell\n(venv)$ python -m pip install dore\n```\n\n### Usage\nInvoke Dore with a manifest\n\n```shell\n(venv)$ dore --manifest /path/to/manifest.json --var1=val1 --var2=val2 ...\n```\n",
    'author': 'Bhargav KN',
    'author_email': 'bhargavkn.1996@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bkn-dore/dore-py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
