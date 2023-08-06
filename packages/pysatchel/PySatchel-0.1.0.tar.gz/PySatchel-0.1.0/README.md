# Satchel

Satchel is a compendium of pure python functions to carry with you and get things done.

## Installation

```
pip install PySatchel
```

## Usage

Sometimes it is useful to split a list into smaller lists to work with.

```python
>>> import satchel import chunk

>>> some_list = [1, 2, 3, 4, 5]
>>> chunk(some_list, 2, "length", True)
# [[1, 2], [3, 4], [5]]

>>> chunk(some_list, 2, "count", True)
# [[1, 2, 3], [3, 5]]
```

You can also group values and apply a function to the groups.

```python
>>> import satchel import groupapply

>>> string = "AAABBAAAACCB"
>>> groupapply(string, apply="count")
# {'A': 7, 'B': 3, 'C': 2}

>>> data = [1, 1, 2, 2, 2, 1, 4]
>>> groupapply(data, key=lambda x: "lower" if x < 3 else "higher", apply="count")
# {'lower': 6, 'higher': 1}

>>> data = [
    {"label": "a", "val": 1},
    {"label": "a", "val": 10},
    {"label": "a", "val": 4},
    {"label": "b", "val": 6},
    {"label": "b", "val": 3},
]
>>> groupapply(data, lambda d: d["label"], lambda l: sum([d["val"] for d in l]))
# {'a': 15, 'b': 9}

>>> data = [
    {"label": "a", "val": 1},
    {"label": "a", "val": 1},
    {"label": "a", "val": 1},
    {"label": "b", "val": 2},
    {"label": "b", "val": 2},
]
>>> groupapply(data, "label", "count")
# {'a': 3, 'b': 2}
```
