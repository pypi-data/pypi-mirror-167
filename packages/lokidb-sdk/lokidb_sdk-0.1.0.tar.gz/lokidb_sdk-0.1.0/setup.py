# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lokidb_sdk', 'lokidb_sdk.gen_grpc']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.48.1,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'lokidb-sdk',
    'version': '0.1.0',
    'description': 'LokiDB python client SDK',
    'long_description': '# py-client\n LokiDB python client SDK\n\n---\n\n## Example\n```python\nfrom random import randrange\n\nfrom lokidb_sdk import Client\n\nc = Client(\n    [\n        ("localhost", 50051),\n        ("localhost", 50052),\n        ("localhost", 50053),\n        ("localhost", 50054),\n        ("localhost", 50055),\n    ]\n)\n\nfor _ in range(1000):\n    key = f\'{randrange(-99999999, 99999999)}\'\n    value = f\'{randrange(-99999999, 99999999)}\'*10\n\n    c.set(key, value)\n    print(c.get(key))\n\n# Get all keys from all nodes\nprint(c.keys())\n\n# Close connection to all nodes\nc.close()\n\n```\n\n## API\n| Method | Input                  | Output                   |\n|--------|------------------------|--------------------------|\n| Get    | key (str)              | value (str)              |\n| Set    | key (str), value (str) |                          |\n| Del    | key(str)               |                          |\n| Keys   |                        | list of keys (list[str]) |\n| Flush  |                        |                          |',
    'author': 'yehoyada',
    'author_email': 'hvuhsg5@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
