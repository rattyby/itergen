def flatgen(some_list):
    # Рекурсивный генератор элементов из списка списков
    for el in some_list:
        if isinstance(el, list):
            yield from flatgen(el)
        else:
            yield el
