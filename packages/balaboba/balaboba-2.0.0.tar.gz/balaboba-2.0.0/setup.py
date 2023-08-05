# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balaboba']

package_data = \
{'': ['*']}

install_requires = \
['cloudscraper>=1.2.64,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=3.7.4.3,<5']}

setup_kwargs = {
    'name': 'balaboba',
    'version': '2.0.0',
    'description': 'Wrapper for Yandex Balaboba',
    'long_description': '# balaboba\n\n[![CI](https://github.com/monosans/balaboba/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/balaboba/actions/workflows/ci.yml)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/balaboba/main.svg)](https://results.pre-commit.ci/latest/github/monosans/balaboba/main)\n[![codecov](https://codecov.io/gh/monosans/balaboba/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/balaboba)\n\nWrapper for [Yandex Balaboba](https://yandex.com/lab/yalm-en) ([Яндекс Балабоба](https://yandex.ru/lab/yalm)).\n\nAsynchronous version [here](https://github.com/monosans/aiobalaboba).\n\n## Disclaimer\n\nThe neural network doesn’t really know what it’s saying, so it can say absolutely anything. Don’t get offended if it says something that hurts your feelings. When sharing the texts, make sure they’re not offensive or violate the law.\n\n## Installation\n\n```bash\npython -m pip install balaboba\n```\n\n## Usage example\n\n```python\nfrom balaboba import Balaboba\n\nbb = Balaboba()\n\n# Get text types\nintros = bb.intros(language="en")\n\n# Get the first text type\nintro = next(intros)\n\n# Print Balaboba\'s response to the "Hello" query\nresponse = bb.balaboba("Hello", intro=intro.number)\nprint(response)\n```\n\n## License\n\n[MIT](https://github.com/monosans/balaboba/blob/main/LICENSE)\n',
    'author': 'monosans',
    'author_email': 'hsyqixco@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/monosans/balaboba',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
