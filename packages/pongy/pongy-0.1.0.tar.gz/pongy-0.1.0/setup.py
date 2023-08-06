# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pongy', 'pongy.server', 'pongy.ui', 'server', 'ui']

package_data = \
{'': ['*']}

modules = \
['run']
install_requires = \
['aiohttp[speedups]==3.8.1',
 'click==8.1.3',
 'pydantic==1.10.2',
 'pygame==2.1.2',
 'python-json-logger==2.0.4',
 'single-source==0.3.0',
 'uvloop==0.17.0']

entry_points = \
{'console_scripts': ['pongy = run:main']}

setup_kwargs = {
    'name': 'pongy',
    'version': '0.1.0',
    'description': 'Ping-pong multiplayer client-server game up to 4 players over network in early development stage.',
    'long_description': '# Pongy\n\nPing-pong multiplayer client-server game up to 4 players over network in early development stage.\n\n## Requires\n\nPython 3.10\n\n## Install\n\n```\n$ pip install pongy\n```\n\nor\n\n```\n$ poetry shell\n$ poetry add pongy\n```\n\n## Run Server\n\n```\n$ pongy -d -h 0.0.0.0 -p 8888\n```\n\n## Run Client\n\n```\n$ pongy -h 192.168.1.1 -p 8888\n```\n\n![UI screenshot](https://github.com/vyalovvldmr/pongy/blob/main/screen.png?raw=true)\n\n## TODO\n\n- [ ] Racket bouncing\n- [ ] Score counting\n- [ ] Test coverage\n- [ ] Think about UDP vs websockets (it should be better for realtime)\n- [ ] Think about p2p vs client-server\n',
    'author': 'Vladimir Vyalov',
    'author_email': 'vyalov.v@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vyalovvldmr/pongy',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
