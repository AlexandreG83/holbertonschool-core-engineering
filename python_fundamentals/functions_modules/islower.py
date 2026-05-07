def islower(c):
    """
    Return True if all cased characters
    in the string are lowercase and there
    is at least one cased character,
    False otherwise.

    >>> islower('abc')
    True
    >>> islower('Abc')
    False
    >>> islower('123')
    False
    >>> islower('')
    False
    """

    return 97 <= ord(c) <= 122
