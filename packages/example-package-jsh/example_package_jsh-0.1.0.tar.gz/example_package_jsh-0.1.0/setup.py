# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['example_package_jsh', 'example_package_jsh.simple']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'example-package-jsh',
    'version': '0.1.0',
    'description': 'A small example package',
    'long_description': '# Example Package\n\nThis is a simple example package. You can use\n[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)\nto write your content.\n',
    'author': 'Jeffrey S. Haemer',
    'author_email': 'jeffrey.haemer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
