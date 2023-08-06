# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytezos_core']

package_data = \
{'': ['*']}

install_requires = \
['base58>=2.1.1,<3.0.0',
 'fastecdsa>=2.2.3,<3.0.0',
 'mnemonic>=0.20,<0.21',
 'pyblake2>=1.1.2,<2.0.0',
 'pysodium>=0.7.10,<0.8.0',
 'secp256k1>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'pytezos-core',
    'version': '1.0.0rc1',
    'description': 'Python toolkit for Tezos',
    'long_description': '# PyTezos Core\n\n[![Python](https://img.shields.io/badge/made%20with-python-blue.svg?)](https://www.python.org)\n[![GitHub stars](https://img.shields.io/github/stars/baking-bad/pytezos-core)](https://github.com/baking-bad/pytezos-core)\n[![Latest stable release](https://img.shields.io/github/v/release/baking-bad/pytezos-core?label=stable)](https://github.com/baking-bad/pytezos-core/releases)\n[![Latest pre-release)](https://img.shields.io/github/v/release/baking-bad/pytezos-core?include_prereleases&label=latest)](https://github.com/baking-bad/pytezos-core/releases)\n[![PyPI monthly downloads](https://img.shields.io/pypi/dm/pytezos-core)](https://pypi.org/project/pytezos-core/)\n<br>\n[![GitHub tests](https://img.shields.io/github/workflow/status/baking-bad/pytezos-core/Test)](https://github.com/baking-bad/pytezos-core/actions)\n[![GitHub issues](https://img.shields.io/github/issues/baking-bad/pytezos-core)](https://github.com/baking-bad/pytezos-core/issues)\n[![GitHub pull requests](https://img.shields.io/github/issues-pr/baking-bad/pytezos-core)](https://github.com/baking-bad/pytezos-core/pulls)\n[![License: MIT](https://img.shields.io/github/license/baking-bad/pytezos-core)](https://github.com/baking-bad/pytezos-core/blob/master/LICENSE)\n\nThis repository contains utilities to work with [Tezos cryptography](https://pytezos.org/crypto.html). It is a part of the [PyTezos](https://github.com/baking-bad/pytezos) framework.\n\nTo switch from mothership library replace `pytezos.crypto` imports with `pytezos_core`.\n\n```diff\n- from pytezos.crypto.key import Key\n+ from pytezos_core.key import Key\n```\n',
    'author': 'Michael Zaikin',
    'author_email': 'mz@baking-bad.org',
    'maintainer': 'Michael Zaikin',
    'maintainer_email': 'mz@baking-bad.org',
    'url': 'https://pytezos.org',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
