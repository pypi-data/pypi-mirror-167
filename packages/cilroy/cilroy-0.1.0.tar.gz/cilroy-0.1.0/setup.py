# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cilroy', 'cilroy.resources']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.4,<0.5']

extras_require = \
{'dev': ['pytest>=7.0,<8.0'], 'test': ['pytest>=7.0,<8.0']}

entry_points = \
{'console_scripts': ['cilroy = cilroy.__main__:cli']}

setup_kwargs = {
    'name': 'cilroy',
    'version': '0.1.0',
    'description': 'kilroy controller 🎛️',
    'long_description': '<h1 align="center">cilroy</h1>\n\n<div align="center">\n\nkilroy controller 🎛️\n\n[![Multiplatform tests](https://github.com/kilroybot/cilroy/actions/workflows/test-multiplatform.yml/badge.svg)](https://github.com/kilroybot/cilroy/actions/workflows/test-multiplatform.yml)\n[![Docker tests](https://github.com/kilroybot/cilroy/actions/workflows/test-docker.yml/badge.svg)](https://github.com/kilroybot/cilroy/actions/workflows/test-docker.yml)\n[![Docs](https://github.com/kilroybot/cilroy/actions/workflows/docs.yml/badge.svg)](https://github.com/kilroybot/cilroy/actions/workflows/docs.yml)\n\n</div>\n\n---\n\nTODO\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kilroybot/cilroy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
