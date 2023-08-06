# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioclamd']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioclamd',
    'version': '1.0.0',
    'description': 'Asynchronous client for virus scanning with ClamAV',
    'long_description': '# aioclamd\n\n[![aioclamd](https://img.shields.io/pypi/v/aioclamd.svg)](https://pypi.python.org/pypi/aioclamd)\n[![Build and Test](https://github.com/swedwise/aioclamd/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/swedwise/aioclamd/actions/workflows/build_and_test.yml)\n[![Format and Lint](https://github.com/swedwise/aioclamd/actions/workflows/format_and_lint.yml/badge.svg)](https://github.com/swedwise/aioclamd/actions/workflows/format_and_lint.yml)\n[![Publish to pypi.org](https://github.com/swedwise/aioclamd/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/swedwise/aioclamd/actions/workflows/pypi-publish.yml)\n[![Publish to test.pypi.org](https://github.com/swedwise/aioclamd/actions/workflows/test-pypi-publish.yml/badge.svg)](https://github.com/swedwise/aioclamd/actions/workflows/test-pypi-publish.yml)\n\n\nThis package is an asynchronous version of the pleasant package \n[`python-clamd`](https://github.com/graingert/python-clamd). It has the same external\nAPI, only all methods are coroutines and all communication is handled \nasynchronously using the ``asyncio`` framework.\n\nThe `ClamdAsyncClient` connects to a [ClamAV](https://www.clamav.net/) antivirus instance and scans\nfiles and data for malicious threats. This package does not bundle ClamAV in any way,\nso a running instance of the `clamd` deamon is required.\n\n## Installation\n\n```\npip install aioclamd\n```\n\n## Usage\n\nTo scan a file (on the system where ClamAV is installed):\n\n```python\nimport asyncio\n\nfrom aioclamd import ClamdAsyncClient\n\nasync def main(host, port):\n    clamd = ClamdAsyncClient(host, port)\n    print(await clamd.scan(\'/etc/clamav/clamd.conf\'))\n\nasyncio.run(main("127.0.0.1", 3310))\n\n# Output:\n# {\'/etc/clamav/clamd.conf\': (\'OK\', None)}\n```\n\nTo scan a data stream:\n\n```python\nimport asyncio\nimport base64\nfrom io import BytesIO\n\nfrom aioclamd import ClamdAsyncClient\n\nEICAR = BytesIO(\n    base64.b64decode(\n        b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNU"\n        b"QU5EQVJELUFOVElWSVJVUy1URVNU\\nLUZJTEUhJEgrSCo=\\n"\n    )\n)\n\nasync def main(host, port):\n    clamd = ClamdAsyncClient(host, port)\n    print(await clamd.instream(EICAR))\n\nasyncio.run(main("127.0.0.1", 3310))\n\n# Output:\n# {\'stream\': (\'FOUND\', \'Win.Test.EICAR_HDB-1\')}\n```\n\n## Development\n\nA local instance of  [ClamAV](https://www.clamav.net/) can be had with Docker:\n\n```powershell\ndocker run -p 3310:3310 --rm clamav/clamav\n```\n',
    'author': 'Henrik Blidh',
    'author_email': 'henrik.blidh@swedwise.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/swedwise/aioclamd',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
