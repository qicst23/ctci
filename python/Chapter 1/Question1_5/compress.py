def compress(string):
    previous_character = string[0]
    counter = 1
    result = ''
    for c in string[1:]:
        if c == previous_character:
            counter += 1
        else:
            result += previous_character + str(counter)
            previous_character = c
            counter = 1
    return result + c + str(counter)

import itertools

def compress(str_):
    """ Using itertools.groupby().

    There is a function in the standard library, itertools.groupby() (new in
    Python 2.4), that does exactly what we need here: it makes an iterator that
    returns consecutive keys and groups from the input iterable, defaulting to
    an identity function to compute the key value for each element. Example:

    >>> [list(g) for k, g in itertools.groupby('AAAABBBCCD')]
    [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]

    """

    groups = itertools.groupby(str_)
    compressed = ''.join('{0}{1}'.format(k, len(list(g))) for k, g in groups)
    if len(compressed) < len(str_):
        return compressed
    else:
        return str_

if __name__ == '__main__':
    words = ('aabcccccaaa', 'aaabbbbcccccdee', 'abc', 'a', '', ' ', 'aabccdde', 'aab', 'aaabb')
    for w in words:
        print('compress({}): {}'.format(w, compress(w)))
