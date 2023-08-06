# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['kivymd_icon_viewer']
entry_points = \
{'console_scripts': ['iconviewer = kivymd_icon_viewer:launch']}

setup_kwargs = {
    'name': 'kivymd-icon-viewer',
    'version': '0.1.1',
    'description': 'KivyMD Icon Viewer',
    'long_description': '# KivyMD Icon Viewer\n\n![](screenshot/0001.png)\n![](screenshot/0002.png)\n\n[Youtube](https://youtu.be/h_ARi0fqnLw)\n\n## Installation\n\n```\npip install kivymd-icon-viewer kivy kivymd\n```\n\n## How to launch\n\nOnce you installed the `kivymd-icon-viewer`, you can launch it using `iconviewer` command.',
    'author': 'Nattōsai Mitō',
    'author_email': 'flow4re2c@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
