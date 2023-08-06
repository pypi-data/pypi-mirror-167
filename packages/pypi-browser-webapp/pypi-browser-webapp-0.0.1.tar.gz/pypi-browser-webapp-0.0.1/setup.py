# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypi_browser']

package_data = \
{'': ['*'],
 'pypi_browser': ['static/*',
                  'templates/_base.html',
                  'templates/_base.html',
                  'templates/_base.html',
                  'templates/_base.html',
                  'templates/_base.html',
                  'templates/_base.html',
                  'templates/_macros.html',
                  'templates/_macros.html',
                  'templates/_macros.html',
                  'templates/_macros.html',
                  'templates/_macros.html',
                  'templates/_macros.html',
                  'templates/home.html',
                  'templates/home.html',
                  'templates/home.html',
                  'templates/home.html',
                  'templates/home.html',
                  'templates/home.html',
                  'templates/package.html',
                  'templates/package.html',
                  'templates/package.html',
                  'templates/package.html',
                  'templates/package.html',
                  'templates/package.html',
                  'templates/package_file.html',
                  'templates/package_file.html',
                  'templates/package_file.html',
                  'templates/package_file.html',
                  'templates/package_file.html',
                  'templates/package_file.html',
                  'templates/package_file_archive_path.html',
                  'templates/package_file_archive_path.html',
                  'templates/package_file_archive_path.html',
                  'templates/package_file_archive_path.html',
                  'templates/package_file_archive_path.html',
                  'templates/package_file_archive_path.html']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'MarkupSafe>=2.1.1,<3.0.0',
 'Pygments>=2.13.0,<3.0.0',
 'aiofiles>=22.1.0,<23.0.0',
 'fluffy-code>=0.0.2,<0.0.3',
 'httpx>=0.23.0,<0.24.0',
 'identify>=2.5.5,<3.0.0',
 'starlette']

setup_kwargs = {
    'name': 'pypi-browser-webapp',
    'version': '0.0.1',
    'description': 'PyPI package browsing web application',
    'long_description': 'pypi-browser\n============\n',
    'author': 'Chris Kuehl',
    'author_email': 'ckuehl@ckuehl.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
