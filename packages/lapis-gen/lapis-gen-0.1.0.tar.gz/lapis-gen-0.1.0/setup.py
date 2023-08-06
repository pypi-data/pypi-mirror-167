# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lapis', 'lapis.openapi', 'lapis.render', 'lapis.render.elems']

package_data = \
{'': ['*'], 'lapis.render': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'black>=22.8.0,<23.0.0',
 'inflection>=0.5.1,<0.6.0',
 'lapis-client-base>=0.1.0,<0.2.0',
 'pydantic[email]>=1.9.2,<2.0.0',
 'tomlkit>=0.11.4,<0.12.0',
 'typer>=0.6.1,<0.7.0']

setup_kwargs = {
    'name': 'lapis-gen',
    'version': '0.1.0',
    'description': 'Python API client generator',
    'long_description': 'None',
    'author': 'Raphael Krupinski',
    'author_email': 'rafalkrupinski@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
