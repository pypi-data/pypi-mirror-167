# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['todocom']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['todo = todocom.cli:main']}

setup_kwargs = {
    'name': 'todocom',
    'version': '0.2.6',
    'description': 'CLI to retrieve a list of all TODO comments in the code',
    'long_description': '# todocom (Todo Comments)\nCLI program that retrieves all TODO comments from file(s) and prints them in terminal/shell. It was created in order to automatically update a list of TODO tasks by simply adding "TODO:" comments in the code. It also enables prioritization of tasks by using "TODO soon:" or "TODO urgent". \nTo create the TODO list, simply open terminal and run the following command:\n```\ntodo [folder/file]\n```\n\nThis command will print out all TODO comments that were found in the code, sorted by their prioritization: urgent, soon and regular. \n_Urgent_ tasks will be printed in RED, _soon_ in CYAN and _regular_ comments in WHITE to make it easier to read. There is also an option to filter comments by their priotization:\n```\n# Prints urgent TODOs\ntodo -u [folder/file]\n```\nOr:\n```\n# Prints soon TODOs\ntodo -s [folder/file]\n```\n\nFinally, there is an option to save the list in a text file (stores as regular text without colors):\n```\n# Store results in a txt file\ntodo -o [path/to/sample.txt] [folder/file]\n```\n\n\n## Setup\n```\npip install todocom\n```',
    'author': 'avivfaraj',
    'author_email': 'avivfaraj4@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/avivfaraj/todocom',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
