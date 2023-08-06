# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['humblepy', 'humblepy.transform', 'humblepy.validate']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.4,<2.0.0', 'pyupgrade>=2.37.3,<3.0.0']

extras_require = \
{'pyspark': ['pyspark[pandas_on_spark,sql]>=3.3.0,<4.0.0']}

setup_kwargs = {
    'name': 'humblepy',
    'version': '0.6.0',
    'description': 'Tasty recipes for analytics engineering.',
    'long_description': '<div align="center">\n![logo](https://firebasestorage.googleapis.com/v0/b/oktiv-1a64a.appspot.com/o/images%2Fhumblepy-logo.png?alt=media)\n\n[![Build status](https://github.com/OKTIVAnalytics/humblepy/workflows/build/badge.svg?branch=master&event=push)](https://github.com/OKTIVAnalytics/humblepy/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/humblepy.svg)](https://pypi.org/project/humblepy/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/OKTIVAnalytics/humblepy/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/OKTIVAnalytics/humblepy/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/OKTIVAnalytics/humblepy/releases)\n[![License](https://img.shields.io/github/license/OKTIVAnalytics/humblepy)](https://github.com/OKTIVAnalytics/humblepy/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nTasty recipes for analytics engineering.\n\n</div>\n\n## Installation\n\n```bash\npip install -U humblepy\n```\n\nor install with `Poetry`\n\n```bash\npoetry add humblepy\n```\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/OKTIVAnalytics/humblepy)](https://github.com/OKTIVAnalytics/humblepy/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `Apache Software License 2.0` license. See [LICENSE](https://github.com/OKTIVAnalytics/humblepy/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```bibtex\n@misc{humblepy,\n  author = {OKTIV Analytics},\n  title = {Tasty recipes for analytics engineering.},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/OKTIVAnalytics/humblepy}}\n}\n```\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'OKTIV Analytics',
    'author_email': 'humblepy@oktivanalytics.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/OKTIVAnalytics/humblepy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
