# stalinsort
Sorts iterable according to the single pass O(n) StalinSort algorithm.

# Example
    from stalinsort import stalinsort
    a = [3, 2, 5, 7, 1, 3]
    stalinsort(a)
    [3, 2, 1]

# References
@mathew@mastodon.social (2018/10/26 04:20:16)
> I came up with a single pass O(n) sort algorithm I call StalinSort. You iterate down the list of elements checking if they're in order. Any element which is out of order is eliminated. At the end you have a sorted list.
