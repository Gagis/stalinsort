# -*- coding: utf-8 -*-

"""Python implementation of the StalinSort algorithm.

References
----------
-   :cite:`mathew` : @mathew@mastodon.social (2018/10/26 04:20:16)
    ''I came up with a single pass O(n) sort algorithm I call StalinSort. You
    iterate down the list of elements checking if they're in order. Any element
    which is out of order is eliminated. At the end you have a sorted list.''
"""

def stalinsort(iterable, key=None, ascending=False):
    """Sorts iterable according to the single pass O(n) StalinSort algorithm.

    Parameters
    ----------
    iterable: iterable object

    key: function
        A function of one argument that is used to extract a comparison key
        from each element. Default is None.

    Returns
    -------
    survivors: list
        List of surviving elements of iterable.
    
    Example
    -------
    >>>from stalinsort import stalinsort
    >>>a = [3, 2, 5, 7, 1, 3]
    >>>stalinsort(a)
    [3, 2, 1]
    """

    ascending = False # There is only descent under communism.

    if key is not None:
        keys = iterable.apply(key)
    else:
        keys = list(iterable)

    survivors = iterable[:1] # I prefer to think in terms of survivors.
    for victim in keys[1:]:
        if  survivors[-1] >= victim:
            survivors.append(victim)
            
    return survivors
