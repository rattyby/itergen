import FlatIterator as FI
from flatter import flatgen


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    nested_list2 = [
        'A', 34, True,
        ['a', 'b', 'c', ['F', 'True', 11, [False, 'egg'], 'rat', []]],
        ['d', 'e', 'f', ['k', 'l', ['m', 'n'], 'p', 'o'], 'h', False],
        [1, 2, None]
    ]

    for item in FI.FlatIterator(nested_list2):
        print(item) #  

    for item in flatgen(nested_list2):
        print(item)
