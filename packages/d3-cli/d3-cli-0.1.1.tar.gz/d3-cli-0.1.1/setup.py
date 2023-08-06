# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['d3_scripts']

package_data = \
{'': ['*'], 'd3_scripts': ['schemas/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'ipython>=8.4.0,<9.0.0',
 'iteration-utilities>=0.11.0,<0.12.0',
 'jsonschema>=4.4.0,<5.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'networkx>=2.8.3,<3.0.0',
 'pandas>=1.4.2,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'yamllint>=1.26.3,<2.0.0']

entry_points = \
{'console_scripts': ['d3-cli = d3_scripts.d3_cli:cli']}

setup_kwargs = {
    'name': 'd3-cli',
    'version': '0.1.1',
    'description': 'Utility scripts for ManySecured-D3 claims',
    'long_description': '# ManySecured d3-scripts\n\nUtility scripts for ManySecured-D3 claims\n\n## Installation\n\nThese utility scripts require Python to use.\n\nWhen developing these scripts, [Python Poetry](https://python-poetry.org/)\nis used to install and manage dependencies, however,\nin future, `poetry` will be used to publish these scripts in a format\nthat any Python package manager can understand (e.g. `pip`-compatable).\n\nPoetry will create a python isolated virtual environment in the `./.venv` folder and install dependencies if you run:\n\n```bash\npoetry install\n```\n\nYou cannot run scripts directly from the `./src/d3-scripts` since we are using [Python relative imports](https://realpython.com/absolute-vs-relative-python-imports/#relative-imports).\n\nInstead, you must run a script defined in the `[tool.poetry.scripts]` field of [`pyproject.toml`](./pyproject.toml):\n\n## Usage\n\nD3 Linter\n\n```console\nalois@nqm-alois-entroware:~/Documents/ManySecured-D3DB/d3-scripts$ poetry run d3lint --help\nusage: d3lint [-h] D3_FILE [D3_FILE ...]\n\nLint D3 files for YAML syntax errors\n\npositional arguments:\n  D3_FILE     Files to lint\n\noptions:\n  -h, --help  show this help message and exit\n\nExample: d3_lint.py *.d3\n```\n\n## Tests\n\nTests can be run via:\n\n```bash\npoetry run pytest\n```\n',
    'author': 'NquiringMinds',
    'author_email': 'contact@nquiringminds.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TechWorksHub/ManySecured-D3DB',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
