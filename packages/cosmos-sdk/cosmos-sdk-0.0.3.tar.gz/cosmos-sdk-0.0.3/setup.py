# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cosmos_sdk',
 'cosmos_sdk.client',
 'cosmos_sdk.client.lcd',
 'cosmos_sdk.client.lcd.api',
 'cosmos_sdk.core',
 'cosmos_sdk.core.auth',
 'cosmos_sdk.core.auth.data',
 'cosmos_sdk.core.auth.msgs',
 'cosmos_sdk.core.authz',
 'cosmos_sdk.core.bank',
 'cosmos_sdk.core.crisis',
 'cosmos_sdk.core.distribution',
 'cosmos_sdk.core.feegrant',
 'cosmos_sdk.core.gov',
 'cosmos_sdk.core.ibc',
 'cosmos_sdk.core.ibc.data',
 'cosmos_sdk.core.ibc.msgs',
 'cosmos_sdk.core.ibc.proposals',
 'cosmos_sdk.core.ibc_transfer',
 'cosmos_sdk.core.osmosis_gamm',
 'cosmos_sdk.core.params',
 'cosmos_sdk.core.slashing',
 'cosmos_sdk.core.staking',
 'cosmos_sdk.core.staking.data',
 'cosmos_sdk.core.upgrade',
 'cosmos_sdk.core.upgrade.data',
 'cosmos_sdk.core.wasm',
 'cosmos_sdk.key',
 'cosmos_sdk.util']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'attrs>=21.4.0,<22.0.0',
 'bech32>=1.2.0,<2.0.0',
 'betterproto==2.0.0b4',
 'bip32utils>=0.3.post4,<0.4',
 'boltons>=21.0.0,<22.0.0',
 'ecdsa>=0.17.0,<0.18.0',
 'furl>=2.1.3,<3.0.0',
 'mnemonic>=0.19,<0.20',
 'nest-asyncio>=1.5.4,<2.0.0',
 'osmosis-protobuf>=0.0.1,<0.0.2',
 'protobuf>=3.19.1,<4.0.0',
 'terra-proto==2.1.0',
 'wheel>=0.37.1,<0.38.0',
 'wrapt>=1.13.3,<2.0.0']

setup_kwargs = {
    'name': 'cosmos-sdk',
    'version': '0.0.3',
    'description': 'The Python SDK for supported Cosmos SDK chains.',
    'long_description': '# Python SDK for the Cosmos Ecosystem\n\n<p><sub>(Unfamiliar with Cosmos?  <a href="https://docs.terra.money/">Check out the Cosmos Network Docs</a>)</sub></p>\n\nThis (SDK) in Python is a simple library toolkit for building software that can interact with the supported Cosmos blockchains and provides simple abstractions over core data structures, serialization, key management, and API request generation.\n\nNote - This is currently a W.I.P.\n\n## Features\n\n- This SDK follows a module specific approach, and new Cosmos Modules will be added to the SDK on a priority basis.\n- Written in Python with extensive support libraries\n- Versatile support for key management solutions\n\n❗ This SDK currently does not support Terra Classic. If you want to communicate with Terra Classic, use terra-sdk==2.x\n\n<br/>\n\n## Requirements\n\nCosmos.py SDK requires <a href="https://www.python.org/downloads/">Python v3.7+</a>.\n\n## Installation\n\n<sub>**NOTE:** _All code starting with a `$` is meant to run on your terminal (a bash prompt). All code starting with a `>>>` is meant to run in a python interpreter, like <a href="https://pypi.org/project/ipython/">ipython</a>._</sub>\n\nCosmos SDK can be installed (preferably in a `virtual environment` from PyPI using `pip`) as follows:\n  \n```\n$ pip install -U cosmos_SDK\n```\n\n<sub>_You might have `pip3` installed instead of `pip`; proceed according to your own setup._<sub>\n\n## Usage Examples\n\n```\nfrom cosmos_sdk.client.lcd import LCDClient\nfrom cosmos_sdk.key.mnemonic import MnemonicKey\n\nmnemonic = <MNEMONIC_PHRASE>\n\n# Terra client\nterra_client = LCDClient(chain_id="phoenix-1", url="https://phoenix-lcd.terra.dev")\nmk = MnemonicKey(mnemonic,"terra")\nterra_wallet = terra_client.wallet(mk)\n\n# Persistence client\npersistence_client = LCDClient(chain_id="core-1", url="http://rest.core.persistence.one")\nmk = MnemonicKey(mnemonic,"persistence")\npersistence_wallet = persistence_client.wallet(mk)\n```\n\n\n## Dependencies\n\nCosmos SDK uses <a href="https://python-poetry.org/">Poetry</a> to manage dependencies. To get set up with all the required dependencies, run:\n\n```\n$ pip install poetry\n$ poetry install\n```\n\nIf you encounter "version solving failed." error, try `poetry add <package_name>`, followed by `poetry lock` and then `poetry install`\n\n\n<br/>\n\n# Contributing\n\nCommunity contribution, whether it\'s a new feature, correction, bug report, additional documentation, or any other feedback is always welcome. Please read through this section to ensure that your contribution is in the most suitable format for us to effectively process.\n\n<br/>\n\n# License\n\nThis reporitory was forked from  <a href="https://github.com/terra-money/terra.py">Terra SDK</a> and is being repurposed from there on. \n\n',
    'author': 'Terraform Labs, PTE.',
    'author_email': 'engineering@terra.money',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/terra-money/terra.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
