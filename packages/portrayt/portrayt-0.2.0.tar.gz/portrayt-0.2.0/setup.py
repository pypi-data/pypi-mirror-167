# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['portrayt',
 'portrayt.configuration',
 'portrayt.generators',
 'portrayt.interface',
 'portrayt.renderers']

package_data = \
{'': ['*']}

install_requires = \
['gradio>=3.3,<4.0',
 'opencv-python>=4.6.0.66,<5.0.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'replicate>=0.0.1a16,<0.0.1',
 'types-requests>=2.28.10,<3.0.0']

entry_points = \
{'console_scripts': ['run-portrayt = portrayt.main:main']}

setup_kwargs = {
    'name': 'portrayt',
    'version': '0.2.0',
    'description': "This project combines e-paper, raspberry pi's, and StableDiffusion to make a picture frame that portrays anything you ask of it.",
    'long_description': "# portrayt\nThis project combines e-paper, raspberry pi's, and StableDiffusion to make a picture frame that portrays anything you ask of it.\n_________________\n\n[![PyPI version](https://badge.fury.io/py/portrayt.svg)](http://badge.fury.io/py/portrayt)\n[![Test Status](https://github.com/apockill/portrayt/workflows/Test/badge.svg?branch=main)](https://github.com/apockill/portrayt/actions?query=workflow%3ATest)\n[![Lint Status](https://github.com/apockill/portrayt/workflows/Lint/badge.svg?branch=main)](https://github.com/apockill/portrayt/actions?query=workflow%3ALint)\n[![codecov](https://codecov.io/gh/apockill/portrayt/branch/main/graph/badge.svg)](https://codecov.io/gh/apockill/portrayt)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)\n_________________\n\n[Read Latest Documentation](https://apockill.github.io/portrayt/) - [Browse GitHub Code Repository](https://github.com/apockill/portrayt/)\n_________________\n\n## Development\n\n### Installing python dependencies\n```shell\npoetry install\n```\n\n### Running Tests\n```shell\npytest .\n```\n\n### Formatting Code\n```shell\nbash .github/format.sh\n```\n\n### Linting\n```shell\nbash .github/check_lint.sh\n```\n\n## Running the Program\nOn your terminal, run:\n```\npoetry shell\nrun-portrayt\n```",
    'author': 'Alex Thiele',
    'author_email': 'apocthiel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
