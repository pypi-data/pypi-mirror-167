# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hashdb_cli']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['hashdb = hashdb_cli:app']}

setup_kwargs = {
    'name': 'hashdb-cli',
    'version': '0.1.0',
    'description': 'Access the open analysis hashdb via cli',
    'long_description': '# HashDB CLI\nFor information about hashdb take a look at https://hashdb.openanalysis.net. This is a small python CLI which allows querying for hashes/algorithms from the commandline.\n\n```\nUsage: hashdb [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n\nCommands:\n  algorithms  Load and dump available algorithms.\n  get         Get original strings for a given algorithm and a hash.\n  hunt        Check if given hashes are available via different hash...\n  resolve     Try to hunt for a single hash and grab the string afterwards.\n```\n',
    'author': '3c7',
    'author_email': '3c7@posteo.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/3c7/hashdb-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
