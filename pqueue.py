class EmptyQueue(Exception):
    pass


class priority_queue:

    def __init__(self):
        self._content = [[] for _ in range(5)]

    def __len__(self):
        return sum(map(len, self._content))

    def add(self, elem, prio=2):
        if 5 > prio > -1:
            self._content[prio].append(elem)
        else:
            raise ValueError

    def pop(self):
        try:
            return filter(len, self._content)[0].pop(0)
        except IndexError:
            raise EmptyQueue

    # def pop(self):
    #     for q in self._content:
    #         if q:
    #             return q.pop(0)
    #     raise EmptyQueue
