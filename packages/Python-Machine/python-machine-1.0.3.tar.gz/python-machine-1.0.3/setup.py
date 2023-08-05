# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['Python_Machine', 'Python_Machine.tests']

package_data = \
{'': ['*'], 'Python_Machine': ['textures/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0']

setup_kwargs = {
    'name': 'python-machine',
    'version': '1.0.3',
    'description': 'A python package that allows you to run cell machine',
    'long_description': '# Python Machine\n\nSimulate Cell Machine inside python\n\n## Instalation\n\n```bash\n$ pip install \n```\n\n## Usage\n\n```python\nfrom Python_Machine import CellMachine\n\ncellmachine = CellMachine()\ncellmachine.parse_code("...")\n\n...Doing actions on the level...\n\ncellmachine.view().show()\n```\n\n## License\n\nthe Cell Machine license is currently owned by Sam Hogan, Mystic and Snazz and is under the Apache license',
    'author': 'youtissoum',
    'author_email': 'youtissoum@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
