# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpvs',
 'dpvs.callbacks',
 'dpvs.configs',
 'dpvs.datasets',
 'dpvs.engines',
 'dpvs.logging',
 'dpvs.metrics',
 'dpvs.model',
 'dpvs.model.hpnet',
 'dpvs.utils']

package_data = \
{'': ['*'], 'dpvs.configs': ['model/*']}

install_requires = \
['hydra-core>=1.2.0,<2.0.0',
 'ipython>=8.5.0,<9.0.0',
 'tables>=3.7.0,<4.0.0',
 'xgboost>=1.6.2,<2.0.0']

setup_kwargs = {
    'name': 'dpvs',
    'version': '0.1.3',
    'description': '',
    'long_description': '# Installation\n```bash\n# using `-e` you can change anything in dpvs folder and it will take effect immediately\npip install -e .\n```\n\n\n# How to run\n\nfirst you should define `PROJECT_ROOT` environmental variable in a `.env` file that is located in the same directory with your script or your jupyter notebook\n\n```sh\npython main.py\n```\n\n\n# ChangeLog\n\n~~__pre_init__ ==> pre_initialize~~\n',
    'author': 'dennislblog',
    'author_email': 'dennisl@udel.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
