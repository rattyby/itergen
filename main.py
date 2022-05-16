
class FlatIterator:
    def __init__(self, some_list) -> None:
        pass

graph = {
    'a': {'b': {'c'}},
    'd': {},
    'e': {'f': {'g': {}, 'h': {'i': {'j'}}}}
}

def nested_dict_keys(some_dict):
    for key, value in some_dict.items():
        yield key
        if isinstance(value, dict):
            for nested_key in nested_dict_keys(value):
                yield nested_key


for item in nested_dict_keys(graph):
    print(item)