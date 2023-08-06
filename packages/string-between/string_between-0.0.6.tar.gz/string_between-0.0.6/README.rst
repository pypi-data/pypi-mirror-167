string_between

Using string_between
====================

.. code-block:: python

    from string_between import string_between
    
    # syntax
    string_between(left, right, subject, [,start [,end]] [,greedy=False] [,inclusive=False] [,repl=None] [,retn_all_on_fail=False] [,retn_class=False] [,rightmost=False]) -> str

    Return the substring delineated by `left` and `right` within the search
    space subject[start:end].  Optional default_arguments `start` and `end` 
    are interpreted as per slice notation.
    
    Return the string between `left` and `right` or empty string on failure

    @param left str|re|list: left anchor, or '' for start of subject; regex must be compiled
    @param right str|re|list: right anchor, or '' for end of subject; regex must be compiled
    @param subject: string to be searched
    @param start: start index for search
    @param end: start and end are interpreted as in slice notation.
    @param greedy: match biggest substring possible
    @param inclusive: include anchors in result
    @param repl [str|callable]: replace matched substring with repl in result
    @param retn_all_on_fail: return original string if match not made
    @param retn_class: return result as StringBetweenResult object
    @param rightmost: match rightmost substring, possible by greedily searching for `left`; implies `greedy`
    @return matched substring | original string | empty | StringBetweenResult object
    
    Note: regular expressions must be compiled

    If left and right are lists, then string_between() takes a value from
    each list and uses them as left and right on subject. If right has
    fewer values than left, then an empty string is used for the rest of
    replacement values. The converse applies. If left is a list and right 
    is a string, then this replacement string is used for every value of left. 
    The converse also applies.

    Examples:
    ---------

    >>> s = 'The *quick* brown [fox] jumps _over_ the **lazy** [dog]'
    >>> string_between('[', ']', s)
    'fox'

    >>> string_between('[', ']', s, inclusive=True)
    '[fox]'

    >>> string_between('[', ']', s, rightmost=True)
    'dog'

    >>> string_between('[', ']', s, inclusive=True, greedy=True)
    '[fox] jumps _over_ the **lazy** [dog]'
    
    > b'result'

Changelog
=========

0.0.1: initial release (2021-09-07)

0.0.6: many things since then (2020-09-16)

