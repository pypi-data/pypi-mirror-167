# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['solpyb']

package_data = \
{'': ['*']}

install_requires = \
['solana>=0.25.1,<0.26.0']

setup_kwargs = {
    'name': 'solpyb',
    'version': '0.0.2',
    'description': 'Pythonic Bridge to Solana Programs',
    'long_description': '[![Upload Python Package](https://github.com/amor71/solpyb/actions/workflows/python-publish.yml/badge.svg)](https://github.com/amor71/solpyb/actions/workflows/python-publish.yml)\n[![codecov](https://codecov.io/gh/amor71/solpyb/branch/master/graph/badge.svg?token=gUJ78Gdh6q)](https://codecov.io/gh/amor71/solpyb)\n\n# solpyb\n\nPythonic Bridge to Solana Programs.\n\n## Overview\n\nThe project simplifies executing and getting responses from Solana Programs (a.k.a *Smart Contracts*), that are running on the Solana [Blockchain](https://solana.com/).\n\n## Setup\n\n`pip install solpyb`\n\n## A Simple Example\n\n```python\n    import asyncio\n    from solpyb import SolBase, load_wallet\n\n\n    class MyProgram(SolBase):\n        slope: float\n        intercept: float\n\n\n    contract = MyProgram(\n        program_id="64ZdvpvU73ig1NVd36xNGqpy5JyAN2kCnVoF7M4wJ53e", payer=load_wallet()\n    )\n    if asyncio.run(contract([10.5, 20.7, 30.8, 40.12, 50.20, 60.0])):\n        print(f"slope: {contract.slope} intercept {contract.intercept}")\n```\n\n*(This script is complete, it should run "as is")*\n\nWhat\'s going on here:\n\n* "64ZdvpvU73ig1NVd36xNGqpy5JyAN2kCnVoF7M4wJ53e" is a Solana Program (a.k.a *Smart Contract*) that performs a [Linear regression](https://en.wikipedia.org/wiki/Linear_regression) on set of points and returns the slope and intercept as floats.\n* load_wallet() loads the default wallet keys (`.config/solana/id.json`), as the payer for the transaction.\n* *MyProgram* class implement a Pythonic wrapper class. Calling the call creates a transaction on chain and result is returned,\n* *SolBase* populates `slope` and `intercept` with the values returned from the Blockchain.\n',
    'author': 'amor71',
    'author_email': 'amor71@sgeltd.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
