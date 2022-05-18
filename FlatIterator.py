class FlatIterator:
    '''
        Итератор по списку списков любой вложенности. Сначала получает простой список, затем по нему итерируется.
        Вход - список.
        Выход - итератор простых элементов.
    '''
    def extending(self, lst):
        # Расширение списка подсписками первой вложенности с проверкой, что остались вложенные списки
        res = []
        nest_flg = 0
        for el in lst:
            if isinstance(el, list):
                res.extend(el)
                nest_flg = 1
            else:
                res.append(el)
        return res, nest_flg


    def flatter(self, some_list):
        # Последовательное уплощение списка, пока не исчезнут вложенные списки
        res, nest_flag = self.extending(some_list)
        while nest_flag:
            res, nest_flag = self.extending(res)
        return res


    def __init__(self, some_list):
        self.lst = self.flatter(some_list)
        self.start = -1
        self.end = len(self.lst)


    def __iter__(self):
        return self


    def __next__(self):
        self.start += 1
        if 0 <= self.start < self.end:
            return self.lst[self.start]
        else:
            raise StopIteration
