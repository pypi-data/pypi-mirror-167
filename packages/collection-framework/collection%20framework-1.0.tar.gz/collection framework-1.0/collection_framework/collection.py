from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=100)
def find_unique_elements(text: str) -> int:
    """
    Find unique elements in string and cache the results
    :param text:
    :return int:
    """

    if not isinstance(text, str):
        raise TypeError(f'Data must be a string value, not type {type(text)}')

    elements_qty = Counter(text)
    unique_elements_len = len([value for value in elements_qty.values() if value == 1])
    return unique_elements_len


if __name__ == '__main__':
    cases = [
        ('abbbccdf', 3),
        ('1', 1),
        ('', 0),
        ('AaBb', 4),
        ('aaa', 0),
        ('1 2', 3)
    ]

    for case, answer in cases:
        assert find_unique_elements(case) == answer

