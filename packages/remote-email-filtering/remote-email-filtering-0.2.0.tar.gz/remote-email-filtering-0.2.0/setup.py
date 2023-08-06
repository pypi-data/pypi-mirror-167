# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['remote_email_filtering']

package_data = \
{'': ['*']}

install_requires = \
['IMAPClient>=2.3.1,<3.0.0', 'exchangelib>=4.7.6,<5.0.0']

setup_kwargs = {
    'name': 'remote-email-filtering',
    'version': '0.2.0',
    'description': 'Email client library for automation',
    'long_description': '======================\nremote-email-filtering\n======================\n\nPython library to filter email remotely over IMAP/EWS\n',
    'author': 'Gaurav Juvekar',
    'author_email': 'gauravjuvekar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gauravjuvekar/remote-email-filtering',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
