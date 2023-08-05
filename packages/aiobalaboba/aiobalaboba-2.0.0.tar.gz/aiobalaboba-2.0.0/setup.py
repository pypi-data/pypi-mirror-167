# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiobalaboba']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8,<4.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=3.7.4.3,<5']}

setup_kwargs = {
    'name': 'aiobalaboba',
    'version': '2.0.0',
    'description': 'Asynchronous wrapper for Yandex Balaboba',
    'long_description': '# aiobalaboba\n\n[![CI](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/aiobalaboba/main.svg)](https://results.pre-commit.ci/latest/github/monosans/aiobalaboba/main)\n[![codecov](https://codecov.io/gh/monosans/aiobalaboba/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiobalaboba)\n\nAsynchronous wrapper for [Yandex Balaboba](https://yandex.com/lab/yalm-en) ([Яндекс Балабоба](https://yandex.ru/lab/yalm)).\n\nSynchronous version [here](https://github.com/monosans/balaboba).\n\n## Disclaimer\n\nThe neural network doesn’t really know what it’s saying, so it can say absolutely anything. Don’t get offended if it says something that hurts your feelings. When sharing the texts, make sure they’re not offensive or violate the law.\n\n## Installation\n\n```bash\npython -m pip install aiobalaboba\n```\n\n## Usage example\n\n```python\nimport asyncio\n\nfrom aiobalaboba import Balaboba\n\n\nasync def main():\n    bb = Balaboba()\n\n    # Get text types\n    intros = await bb.intros(language="en")\n\n    # Get the first text type\n    intro = next(intros)\n\n    # Print Balaboba\'s response to the "Hello" query\n    response = await bb.balaboba("Hello", intro=intro.number)\n    print(response)\n\nasyncio.run(main())\n```\n\n## License\n\n[MIT](https://github.com/monosans/aiobalaboba/blob/main/LICENSE)\n',
    'author': 'monosans',
    'author_email': 'hsyqixco@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/monosans/aiobalaboba',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
