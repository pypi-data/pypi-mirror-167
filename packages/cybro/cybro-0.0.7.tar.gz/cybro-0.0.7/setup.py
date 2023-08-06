# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cybro']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.0', 'backoff>=1.11.0', 'cachetools>=5.0.0', 'yarl>=1.7.2']

setup_kwargs = {
    'name': 'cybro',
    'version': '0.0.7',
    'description': 'Asynchronous Python client for Cybro scgi server.',
    'long_description': '# python-cybro\n\n[![GitHub Release][releases-shield]][releases]\n[![GitHub Activity][commits-shield]][commits]\n[![License][license-shield]](LICENSE)\n\n[![pre-commit][pre-commit-shield]][pre-commit]\n[![Black][black-shield]][black]\n\n[![Project Maintenance][maintenance-shield]][user_profile]\n\n## Functionality\n\nPython library to communicate with a cybro scgi server\nTo use this library you need to have a running scgi server (it could be a docker container or native installed).\nFurther information of the docker container can be found here: [![dockerhub][scgi-docker-shield]][scgi-docker]\n\n## Tested scgi server\n\n- Cybrotech scgi server v3.1.3\n\n## Contributions are welcome!\n\nIf you want to contribute to this please read the [Contribution guidelines](https://github.com/killer0071234/python-cybro/blob/master/CONTRIBUTING.md)\n\n---\n\n[black]: https://github.com/psf/black\n[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge\n[commits-shield]: https://img.shields.io/github/commit-activity/y/killer0071234/python-cybro.svg?style=for-the-badge\n[commits]: https://github.com/killer0071234/python-cybro/commits/main\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge\n[license-shield]: https://img.shields.io/github/license/killer0071234/python-cybro.svg?style=for-the-badge\n[maintenance-shield]: https://img.shields.io/badge/maintainer-@killer0071234-blue.svg?style=for-the-badge\n[releases-shield]: https://img.shields.io/github/release/killer0071234/python-cybro.svg?style=for-the-badge\n[releases]: https://github.com/killer0071234/python-cybro/releases\n[user_profile]: https://github.com/killer0071234\n[scgi-docker-shield]: https://img.shields.io/badge/dockerhub-cybroscgiserver-brightgreen.svg?style=for-the-badge\n[scgi-docker]: https://hub.docker.com/r/killer007/cybroscgiserver\n',
    'author': 'Daniel Gangl',
    'author_email': 'killer007@gmx.at',
    'maintainer': 'Daniel Gangl',
    'maintainer_email': 'killer007@gmx.at',
    'url': 'https://github.com/killer0071234/python-cybro',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
