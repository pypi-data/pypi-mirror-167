# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rutracker_api']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'rutracker-api',
    'version': '0.22.9',
    'description': 'Rutracker API provider',
    'long_description': '# rutracker-api\nFork of https://github.com/raitonoberu/rutracker-api\n\n# Requirements\n    - python3-lxml\n    - beautifulsoup4\n    - requests\n\n## Usage\n```python\n>>> from rutracker_api import RutrackerApi\n>>> api = RutrackerApi()\n>>> api.login("username", "password")\n>>> search = api.search("ubuntu mate")\n>>> search\n{\'count\': 16, \'page\': 1, \'total_pages\': 1, \'result\': [<Torrent 5956108>, <Torrent 5942849>, <Torrent 5710800>, <Torrent 5560789>, <Torrent 5533679>, <Torrent 5345515>, <Torrent 5336791>, <Torrent 5257800>, <Torrent 5099277>, <Torrent 4358219>, <Torrent 4857137>, <Torrent 4791999>, <Torrent 4692014>, <Torrent 4565546>, <Torrent 4348745>, <Torrent 4144976>]}\n>>> result = search[\'result\'][0]\n>>> result.title\n\'[amd64] Ubuntu*Pack 20.04 MATE (сентябрь 2020)\'\n>>> result.get_magnet()\n\'magnet:?xt=urn%3Abtih%3AB2EDD8F9A0BEB1368A5EDEBBAB4907B53A69DCCA&tr=http%3A%2F%2Fbt2.t-ru.org%2Fann%3Fmagnet&dn=%5Bamd64%5D+Ubuntu%2APack+20.04+MATE+%28%D1%81%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8C+2020%29&as=http%3A%2F%2Frutracker.org%2Fforum%2Fviewtopic.php%3Ft%3D5956108\'\n```\n\n## Documentation\nComing soon!\n',
    'author': 'Vladislav Boyko',
    'author_email': 'v1aght@ya.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
