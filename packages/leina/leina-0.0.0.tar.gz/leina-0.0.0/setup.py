# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['leina']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['leina = leina.__main__:main']}

setup_kwargs = {
    'name': 'leina',
    'version': '0.0.0',
    'description': 'Saffire',
    'long_description': "# Saffire\n\n[![PyPI](https://img.shields.io/pypi/v/leina.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/leina.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/leina)][pypi status]\n[![License](https://img.shields.io/pypi/l/leina)][license]\n\n[![Read the documentation at https://leina.readthedocs.io/](https://img.shields.io/readthedocs/leina/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/csala/leina/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/csala/leina/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/leina/\n[read the docs]: https://leina.readthedocs.io/\n[tests]: https://github.com/csala/leina/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/csala/leina\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Saffire_ via [pip] from [PyPI]:\n\n```console\n$ pip install leina\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Saffire_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/csala/leina/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/csala/leina/blob/main/LICENSE\n[contributor guide]: https://github.com/csala/leina/blob/main/CONTRIBUTING.md\n[command-line reference]: https://leina.readthedocs.io/en/latest/usage.html\n",
    'author': 'Carles Sala',
    'author_email': 'carles@pythiac.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/csala/leina',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
