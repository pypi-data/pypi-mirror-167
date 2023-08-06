# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['py']
install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'tomli>=2.0.1,<3.0.0',
 'typing-extensions>=4.3.0,<5.0.0',
 'xdg>=5.1.1,<6.0.0']

setup_kwargs = {
    'name': 'jelli',
    'version': '0.1.0',
    'description': 'Jelli Is For Setting(s)',
    'long_description': '# Jelli Is For Setting(s)\n',
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
