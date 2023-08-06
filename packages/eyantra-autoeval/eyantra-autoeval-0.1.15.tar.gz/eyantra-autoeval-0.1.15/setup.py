# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eyantra_autoeval',
 'eyantra_autoeval.utils',
 'eyantra_autoeval.year.y2022.SD.task0']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'distro>=1.7.0,<2.0.0',
 'python-keycloak>=2.5.0,<3.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['eyantra-autoeval = eyantra_autoeval.console:cli']}

setup_kwargs = {
    'name': 'eyantra-autoeval',
    'version': '0.1.15',
    'description': 'A python module to aid auto evaluation',
    'long_description': '\n\n# e-Yantra Autoeval\n\n## Usage\n\n- For `Sentinel Drone` theme\n\n```sh\neyantra-autoeval evaluate --year 2022 --theme SD --task 0  # used internally\neyantra-autoeval dryrun --year 2022 --theme SD --task 0  # dryrun for them to evaluate themselves\neyantra-autoeval submit --year 2022 --theme SD --task 0  # submit to push file to server\n```\n\n',
    'author': 'Ameya Shenoy',
    'author_email': 'shenoy.ameya@gmail.com',
    'maintainer': 'Ameya Shenoy',
    'maintainer_email': 'shenoy.ameya@gmail.com',
    'url': 'https://github.com/erts-rnd/eyantra-autoeval',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
