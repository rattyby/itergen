import FlatIterator as FI
from flatter import flatgen


if __name__ == '__main__':
    nested_list = [
        'A', 34, True,
        ['a', 'b', 'c', ['F', 'True', 11, [False, 'egg'], 'rat', []]],
        ['d', 'e', 'f', ['k', 'l', ['m', 'n'], 'p', 'o'], 'h', False],
        [1, 2, None]
    ]

    for item in FI.FlatIterator(nested_list):
        print(item)

    for item in flatgen(nested_list):
        print(item)
