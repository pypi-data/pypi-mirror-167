# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyail']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'pyail',
    'version': '0.0.3',
    'description': '',
    'long_description': "PyAIL\n======\n\n[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)\n\n# PyAIL - Python library using the AIL Rest API\n\nPyAIL is a Python library to access [AIL](https://github.com/ail-project/ail-framework) platforms via their REST API.\n\n## Install from pip\n\n**It is strongly recommended to use a virtual environment**\n\nIf you want to know more about virtual environments, [python has you covered](https://docs.python.org/3/tutorial/venv.html)\n\nInstall pyail:\n```bash\npip3 install pyail\n```\n\n## Usage\n\n### Feeding items to AIL\n\n```python\nfrom pyail import PyAIL\n\nail_url = 'https://localhost:7000'\nail_key = '<AIL API KEY>'\ntry:\n    pyail = PyAIL(ail_url, ail_key, ssl=False)\nexcept Exception as e:\n    print(e)\n    sys.exit(0)\n\ndata = 'my item content'\nmetadata = {}\nsource = '<FEEDER NAME>'\nsource_uuid = '<feeder UUID v4>'\n\npyail.feed_json_item(data, metadata, source, source_uuid)\n```\n",
    'author': 'Aurelien Thirion (terrtia)',
    'author_email': 'aurelien.thirion@circl.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ail-project/PyAIL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
