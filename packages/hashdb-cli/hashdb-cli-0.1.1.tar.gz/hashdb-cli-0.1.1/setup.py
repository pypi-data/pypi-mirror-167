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
    'version': '0.1.1',
    'description': 'Access the open analysis hashdb via cli',
    'long_description': '# HashDB CLI\nFor information about hashdb take a look at https://hashdb.openanalysis.net. This is a small python CLI which allows querying for hashes/algorithms from the commandline.\n\n## Installation\n\n```\npip install hashdb-cli\n```\n\n## Usage\n\n```\nUsage: hashdb [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n\nCommands:\n  add         Add a new string to hashdb\n  algorithms  Load and dump available algorithms.\n  get         Get original strings for a given algorithm and a hash.\n  hunt        Check if given hashes are available via different hash...\n  resolve     Try to hunt for a single hash and grab the string afterwards.\n  string      Get information about a string which is already available...\n```\n\n### List algorithms\n\n```\nhashdb algorithms (--description)\n```\n\n### Get string\nHashdb requires the hash to be an unsigned integer, however, hex strings can be used in combination with `-h/--hex` parameter.\n\n```\nhashdb get (--hex) <algo_name> <hash>\n```\n\n### Hunt\nPass multiple hashes to the API in order to find a fitting algorithm.\n\n```\nhashdb hunt <h1> <h2> <h3> ... <hn> (--hex)\n```\n\n### Resolve\nCombination of hunt and get.\n\n```\nhashdb resolve <h1> ... <hn>\n```\n\n### String\nGet information about a string in the database\n\n```\nhashdb string <string>\n```\n',
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
