# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scripts', 'xklb']

package_data = \
{'': ['*']}

install_requires = \
['catt',
 'ffmpeg-python',
 'humanize',
 'ipython',
 'joblib',
 'mutagen',
 'natsort',
 'protobuf<4',
 'pysubs2>=1.4.3,<2.0.0',
 'python-mpv-jsonipc>=1.1.13,<2.0.0',
 'rich',
 'sqlite-utils',
 'subliminal',
 'tabulate',
 'tinytag']

entry_points = \
{'console_scripts': ['lb = xklb.lb:main', 'library = xklb.lb:main']}

setup_kwargs = {
    'name': 'xklb',
    'version': '1.16.10',
    'description': 'xk library',
    'long_description': '',
    'author': 'Jacob Chapman',
    'author_email': '7908073+chapmanjacobd@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chapmanjacobd/lb/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
