# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['satchel']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysatchel',
    'version': '0.1.0',
    'description': 'Satchel is a compendium of pure python functions to carry with you and get things done.',
    'long_description': '# Satchel\n\nSatchel is a compendium of pure python functions to carry with you and get things done.\n\n## Installation\n\n```\npip install PySatchel\n```\n\n## Usage\n\nSometimes it is useful to split a list into smaller lists to work with.\n\n```python\n>>> import satchel import chunk\n\n>>> some_list = [1, 2, 3, 4, 5]\n>>> chunk(some_list, 2, "length", True)\n# [[1, 2], [3, 4], [5]]\n\n>>> chunk(some_list, 2, "count", True)\n# [[1, 2, 3], [3, 5]]\n```\n\nYou can also group values and apply a function to the groups.\n\n```python\n>>> import satchel import groupapply\n\n>>> string = "AAABBAAAACCB"\n>>> groupapply(string, apply="count")\n# {\'A\': 7, \'B\': 3, \'C\': 2}\n\n>>> data = [1, 1, 2, 2, 2, 1, 4]\n>>> groupapply(data, key=lambda x: "lower" if x < 3 else "higher", apply="count")\n# {\'lower\': 6, \'higher\': 1}\n\n>>> data = [\n    {"label": "a", "val": 1},\n    {"label": "a", "val": 10},\n    {"label": "a", "val": 4},\n    {"label": "b", "val": 6},\n    {"label": "b", "val": 3},\n]\n>>> groupapply(data, lambda d: d["label"], lambda l: sum([d["val"] for d in l]))\n# {\'a\': 15, \'b\': 9}\n\n>>> data = [\n    {"label": "a", "val": 1},\n    {"label": "a", "val": 1},\n    {"label": "a", "val": 1},\n    {"label": "b", "val": 2},\n    {"label": "b", "val": 2},\n]\n>>> groupapply(data, "label", "count")\n# {\'a\': 3, \'b\': 2}\n```\n',
    'author': 'Taylor Beever',
    'author_email': 'taybeever@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/theelderbeever/satchel',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
