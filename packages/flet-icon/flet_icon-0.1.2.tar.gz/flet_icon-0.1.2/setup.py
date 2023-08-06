# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flet_icon']

package_data = \
{'': ['*']}

install_requires = \
['flet>=0.1.58,<0.2.0', 'pyperclip>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'flet-icon',
    'version': '0.1.2',
    'description': 'a collection of icons for flutter as flet',
    'long_description': '## a flet icons application\n\n![](images/img.png)\n\n⚡ It is a flet-based icon application that categorizes the icons available for flet for easy finding and use.\n\n## Installation\n    \n    pip install flet_icon\n\n## Usage\n```python\nimport flet\nfrom flet_icon import Application\n\nflet.app(target=Application())\n\n```\n',
    'author': 'Tai',
    'author_email': '1174501146@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
