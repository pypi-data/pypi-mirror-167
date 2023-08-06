from collections import defaultdict
from functools import partial
from operator import getitem
from typing import Callable, Iterable, Literal, TypeVar

T = TypeVar("T")
K = TypeVar("K")
R = TypeVar("R")

_apply_methods = {"count": len}


def _identity(x: T) -> T:
    return x


def _groupby(it: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    d = defaultdict(list)
    for i in it:
        d[key(i)].append(i)
    return d


def groupapply(
    it: Iterable[T],
    key: str | Callable[[T], K] = None,
    apply: Literal["count"] | Callable[[list[T]], R] = None,
) -> dict[K, R]:
    """Group values in an iterable by a key function then apply a function to the
    resultant list of values in each group.

    Parameters
    ----------
    it : Iterable[T]
        Iterable of values to be operated on.
    key : str | Callable[[T], K], optional
        Function to generate a key to group on. Should take an argument of the same type
        as elements of `it` and return a hashable value. A value of `None` is the
        identity function `lambda x: x`. A `str` corresponds to `getitem(T, key)`, by
        default `None`
    apply : &quot;count&quot; | Callable[[list[T]], R], optional
        Function to operator on each group. Should take an argument of a list of the
        same type as elements of `it` and return a hashable value. A value of `None` is
        the identity function `lambda x: x`, by default `None`

    Returns
    -------
    dict[K, R]
        A dictionary with keys matching the return of the key function and values
        matching the return of the apply function.

    Raises
    ------
    ValueError
        If etiher a non-callable or valid apply option is provided.

    Examples
    --------
    >>> import satchel import groupapply

    >>> string = "AAABBAAAACCB"
    >>> groupapply(string, apply="count")
    {'A': 7, 'B': 3, 'C': 2}

    >>> data = [1, 1, 2, 2, 2, 1, 4]
    >>> groupapply(data, key=lambda x: "lower" if x < 3 else "higher", apply="count")
    {'lower': 6, 'higher': 1}

    >>> data = [
        {"label": "a", "val": 1},
        {"label": "a", "val": 10},
        {"label": "a", "val": 4},
        {"label": "b", "val": 6},
        {"label": "b", "val": 3},
    ]

    >>> groupapply(data, lambda d: d["label"], lambda l: sum([d["val"] for d in l]))
    {'a': 15, 'b': 9}

    >>> data = [
        {"label": "a", "val": 1},
        {"label": "a", "val": 1},
        {"label": "a", "val": 1},
        {"label": "b", "val": 2},
        {"label": "b", "val": 2},
    ]
    >>> groupapply(data, "label", "count")
    {'a': 3, 'b': 2}
    """

    if key is None:
        key = _identity
    elif isinstance(key, str):
        key = partial(lambda x, k: getitem(x, k), k=key)

    if apply is None:
        apply = _identity

    if isinstance(apply, str):
        apply = _apply_methods.get(apply, None)
        if apply is None:
            raise ValueError(
                f"Argument `apply` must be a callable or {list(_apply_methods.keys())}"
            )
    return {k: apply(g) for k, g in _groupby(it, key).items()}
