class FlatIterator:
    def extending(self, lst):
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
        res, nest_flag = self.extending(some_list)
        while nest_flag:
            res, nest_flag = self.extending(res)
        return res


    def __init__(self, some_list) -> None:
        self.lst = self.flatter(some_list)
        if len(self.lst):
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
    