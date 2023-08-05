# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ghgql']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1']

setup_kwargs = {
    'name': 'ghgql',
    'version': '0.0.9',
    'description': 'Thin wrapper for interacting with the Github GraphQL API',
    'long_description': '# ghgql\n\nThin wrapper for interacting with the [Github GraphQL API](https://docs.github.com/en/graphql).\n\n## Status\n\n[![Documentation Status](https://readthedocs.org/projects/ghgql/badge/?version=latest)](https://ghgql.readthedocs.io/en/latest/?badge=latest)\n[![CodeQL](https://github.com/kwk/ghgql/actions/workflows/codeql.yml/badge.svg)](https://github.com/kwk/ghgql/actions/workflows/codeql.yml)\n[![ci-cd](https://github.com/kwk/ghgql/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/kwk/ghgql/actions/workflows/ci-cd.yml)\n[![codecov](https://codecov.io/gh/kwk/ghgql/branch/main/graph/badge.svg?token=ASSPTOL3JU)](https://codecov.io/gh/kwk/ghgql)\n[![release](https://img.shields.io/github/release/kwk/ghgql.svg)](https://github.com/kwk/ghgql/releases)\n\n## Installation\n\n```bash\n$ pip install ghgql\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`ghgql` was created by Konrad Kleine. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`ghgql` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Konrad Kleine',
    'author_email': 'None',
    'maintainer': 'Konrad Kleine',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/ghgql/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
