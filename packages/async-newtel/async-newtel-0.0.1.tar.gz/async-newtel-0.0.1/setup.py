# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_newtel']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.21,<0.22']

setup_kwargs = {
    'name': 'async-newtel',
    'version': '0.0.1',
    'description': 'New-Tel simple async client based on httpx.',
    'long_description': "# Async-NewTel\n\nNew-Tel simple async client based on httpx.\n\n# Installation\n\n```bash\npip install async-newtel\n```\n\n# Usage\n\n```python\nimport async_newtel\nimport os\n\nAPI_KEY = os.environ.get('API_KEY')\nSIGNING_KEY = os.environ.get('SIGNING_KEY')\n\nnumber = '+1234567890'\ncode = '1234'\n# Send email with context manager\n\nasync with async_newtel.AsyncClient(\n    api_key=API_KEY,\n    signing_key=SIGNING_KEY\n) as client:\n    response = await client.call(number, code)\n\n# Send email without context manager\n\nclient = simple_sendgrid.AsyncClient(api_key=API_KEY, signing_key=SIGNING_KEY)\nawait client.open()\nresponse = await client.call(number, code)\nawait client.close()\n\n```\n",
    'author': 'Saltymakov Timofey',
    'author_email': 'saltytimofey@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sensodevices/async-newtel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
