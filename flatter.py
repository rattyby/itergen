def flatgen(some_list):
    for el in some_list:
        if isinstance(el, list):
            yield from flatgen(el)
        else:
            yield el
