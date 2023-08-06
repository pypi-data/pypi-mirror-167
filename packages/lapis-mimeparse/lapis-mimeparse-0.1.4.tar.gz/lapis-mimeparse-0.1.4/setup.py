# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['mimeparse']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'lapis-mimeparse',
    'version': '0.1.4',
    'description': 'A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.',
    'long_description': 'This module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.\n\nSee section 14.1 of RFC 2616 (the HTTP specification) for a complete explanation.\n\nTesting\n=======\nThe format of the JSON test data file is as follows:\nA top-level JSON object which has a key for each of the functions to be tested. The value corresponding to that key is a list of tests. Each test contains: the argument or arguments to the function being tested, the expected results and an optional description.\n\n\nPython\n======\nThe Python tests require either Python 2.6 or the installation of the SimpleJSON library.\n\nInstalling SimpleJson can be done by:\nsudo easy_install simplejson\n\nRun the tests by typing:\nPYTHONPATH=. python tests/mimeparse_test.py\n',
    'author': 'Joe Gregorio',
    'author_email': 'joe@bitworking.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
