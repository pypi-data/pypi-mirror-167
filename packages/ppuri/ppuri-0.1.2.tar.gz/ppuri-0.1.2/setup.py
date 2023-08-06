# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ppuri', 'ppuri.component', 'ppuri.scheme']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['click>=8.1.3,<9.0.0', 'pyparsing>=3.0.9,<4.0.0']

setup_kwargs = {
    'name': 'ppuri',
    'version': '0.1.2',
    'description': 'A pyparsing based URI parser/scanner',
    'long_description': '# ppURI\n\nA [pyparsing](https://pyparsing-docs.readthedocs.io/en/latest/) based URI parser/scanner.\n\nInstall using pipx, pip or your tool of choice e.g.\n\n```\npipx install ppuri\n```\n\n## Usage\n\n### Parsing\n\nEither import `Uri` from `ppuri.uri` and use the pyparsing `parse_string` method to match and parse against all URI schemes e.g.\n\n```python\nfrom ppuri.uri import Uri\ninfo = Uri.parse_string("https://www.example.com:443/a.path?q=aparam#afragment")\nprint(inf["scheme"])\nprint(info["authority"]["address"])\n```\n\nprints\n\n```\nhttps\nwww.example.com\n```\n\nOr import a specific scheme\n\n```python\nfrom ppuri.scheme.http import Http\ninfo = Http.parse_string()\n```\n\nand use that to parse\n\n### Scanning\n\nTo scan text for URIs use the `scan_string` method\n\n## Supported schemes\n\nCurrently supports the following schemes\n\n- http(s)\n- urn\n- aaa\n- about\n- coap\n- crid\n- data\n- file\n- mailto\n\n### Http(s)\n\n`parse_string` returns a dictionary of the form\n\n```python\n{\n    "scheme": "http" or "https",\n    "authority": {\n        "address": "hostname" or "ipv4 address" or "ipv6 address",\n        "port": "port number",\n        "username": "user name if provided",\n        "password": "pasword if provided"\n    },\n    "path": "path if provided",\n    "parameters": [\n        "list of parameters if provided",\n        {\n            "name": "parameter name",\n            "value": "parameter value or None if not provided"\n        }\n    ],\n    "fragment": "fragment if provided"\n}\n```\n\n### Urn\n\n`parse_string` returns a dictionary of the form\n\n```python\n{\n    "scheme": "urn",\n    "nid": "Namespace Identifier",\n    "nss": "Namespace Specific String"\n}\n```\n\n### MailTo\n\n`parse_string` returns a dictionary of the form\n\n```python\n{\n    "scheme": "mailto",\n    "addresses": [\n        "List of email addresses",\n    ]\n    "parameters": [\n        "list of parameters if provided",\n        {\n            "name": "bcc",\n            "value": "dave@example.com"\n        }\n}\n```\n\n### Data\n\n`parse_string` returns a dictionary of the form\n\n```python\n{\n    "scheme": "data",\n    "type": "Mime type",\n    "subtype": "Mime Subtype",\n    "encoding": "base64 if specified",\n    "data": "The actual data"\n}\n```\n\n### File\n\n`parse_string` returns a dictionary of the form\n\n```python\n{\n    "scheme": "file",\n    "path": "The /file/path",\n}\n```\n\n## Package Status\n\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/sffjunkie/ppuri/ppuri-test) ![PyPI - Downloads](https://img.shields.io/pypi/dm/ppuri)\n',
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
