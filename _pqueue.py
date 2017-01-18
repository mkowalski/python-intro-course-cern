class EmptyQueue(Exception):
    'Extracting element from empty queue.'


# This is the model solution. It uses separate subqueues, one for each
# priority.
class priority_queue:

    def __init__(self):
        self._queues = [ [] for x in range(5) ] # = [[],[],[],[],[]]

    def pop(self):
        for queue in self._queues:
            if queue:
                return queue.pop()
        raise EmptyQueue("pop from empty queue")

    def add(self, item, priority=2):
        if not 0 <= priority < 5:
            raise ValueError("priority must be in range 0-4")
        self._queues[priority].insert(0, item)

    def __len__(self):
        return sum(map(len, self._queues))


# Same as original, but adding to the end, and removing from the front
class priority_queue_backwards:

    def __init__(self):
        self._queues = [ [] for x in range(5) ]

    def pop(self):
        for queue in self._queues:
            if queue:
                return queue.pop(0)
        raise EmptyQueue("pop from empty queue")

    def add(self, item, priority=2):
        if not 0 <= priority < 5:
            raise ValueError("priority must be in range 0-4")
        self._queues[priority].append(item)

    def __len__(self):
        return sum(map(len, self._queues))


# Same as the original, but uses deque instead of list to represent a
# subqueue. Deques are designed for cheap addition and removal at both
# ends, so this should be even more efficient.
from collections import deque

class priority_queue_deque:

    def __init__(self):
        self._queues = [ deque() for x in range(5) ] # = [[],[],[],[],[]]

    def pop(self):
        for queue in self._queues:
            if queue:
                return queue.popleft()
        raise EmptyQueue("pop from empty queue")

    def add(self, item, priority=2):
        if not 0 <= priority < 5:
            raise ValueError("priority must be in range 0-4")
        self._queues[priority].append(item)

    def __len__(self):
        return sum(map(len, self._queues))

# Same again, reversing the direction of motion through the queue
class priority_queue_deque_backwards:

    def __init__(self):
        self._queues = [ deque() for x in range(5) ] # = [[],[],[],[],[]]

    def pop(self):
        for queue in self._queues:
            if queue:
                return queue.pop()
        raise EmptyQueue("pop from empty queue")

    def add(self, item, priority=2):
        if not 0 <= priority < 5:
            raise ValueError("priority must be in range 0-4")
        self._queues[priority].appendleft(item)

    def __len__(self):
        return sum(map(len, self._queues))


# This is a small modification of the original which generalizes
# it. The number of priorities is no longer hard-wired, but may be
# specified at construction time. This implementation still passes all
# the tests in the test suite, becaues the number of priorities
# defaults to 5.
class priority_queue_g1:

    def __init__(self, priorities=5):
        self._queues = [ [] for x in range(priorities) ]
        self._priorities = priorities

    def pop(self):
        for queue in self._queues:
            if queue:
                return queue.pop()
        raise EmptyQueue("pop from empty queue")

    def add(self, item, priority=2):
        if not 0 <= priority < self._priorities:
            raise ValueError("priority must be in range 0-%s" % (self._priorities-1))
        self._queues[priority].insert(0, item)

    def __len__(self):
        return sum(map(len, self._queues))


# A further generalization: the default priority can now also be
# specified at construction time.
class priority_queue_g2:

    def __init__(self, priorities=5, default=2):
        self._queues = [ [] for x in range(priorities) ]
        self._priorities = priorities
        self._default_priority = default

    def pop(self):
        for queue in self._queues:
            if queue:
                return queue.pop()
        raise EmptyQueue("pop from empty queue")

    def add(self, item, priority=None):
        if priority is None:
            priority = self._default_priority
        if not 0 <= priority < self._priorities:
            raise ValueError("priority must be in range 0-%s" % (self._priorities-1))
        self._queues[priority].insert(0, item)

    def __len__(self):
        return sum(map(len, self._queues))

# A version built around heapq. I have left out the generalization of
# g1 and g2, to highlight the use of the heapq.
from heapq import heappush, heappop
class priority_queue_heap:

    def __init__(self):
        self._q = []
        self._order = 0

    def pop(self):
        try:
            return heappop(self._q)[2]
        except IndexError:
            raise EmptyQueue

    def add(self, item, priority=2):
        if not (0 <= priority <= 4):
            raise ValueError
        if not isinstance(priority, int):
            raise TypeError
        self._order += 1
        heappush(self._q, (priority, self._order, item))

    def __len__(self):
        return len(self._q)

# A variation on the above which takes advantage of itertools (which
# we will meet later in the course)
from heapq import heappush, heappop
import itertools
class priority_queue_heap_itertools:

    def __init__(self):
        self._q = []
        self._order = itertools.count().next

    def pop(self):
        try:
            return heappop(self._q)[2]
        except IndexError:
            raise EmptyQueue

    def add(self, item, priority=2):
        if not (0 <= priority <= 4):
            raise ValueError
        if not isinstance(priority, int):
            raise TypeError
        heappush(self._q, (priority, self._order(), item))

    def __len__(self):
        return len(self._q)

class priority_queue_parallel_heap:

    def __init__(self):
        self._qs = [ [] for _ in range(5) ]
        self._order = 0

    def pop(self):
        for q in self._qs:
            if q:
                return heappop(q)[1]
        raise EmptyQueue

    def add(self, item, priority=2):
        if not (0 <= priority <= 4):
            raise ValueError
        self._order += 1
        heappush(self._qs[priority], (self._order, item))

    def __len__(self):
        return sum(map(len, self._qs))


# This is a slower version which implements an insertion sort. It
# takes advantage of the knowledge that the list into which it inserts
# a new item is already sorted.
class priority_queue_slow:

    def __init__(self):
        self._q = []

    def add(self, obj, pri=2):
        if type(pri) is not int:
            raise TypeError
        if not (0 <= pri < 5):
            raise ValueError
        for index, (o, p) in enumerate (self._q):
            if p>pri:
                self._q.insert(index, (obj, pri))
                break
        else:
            self._q.append((obj, pri))

    def pop(self):
        try:
            return self._q.pop(0)[0]
        except IndexError:
            raise EmptyQueue

    def __len__(self):
        return len(self._q)

# This version improves on the insertion sort by avoiding the need for
# a linear search through the queue. It does this by remembering the
# location of boundaries between the priorities.
class priority_queue_not_so_slow:

    def __init__(self):
        self._q = []
        self._where_to_insert = [0] * 5

    def add(self, obj, pri=2):
        if type(pri) is not int:
            raise TypeError
        if not (0 <= pri < 5):
            raise ValueError
        self._q.insert(self._where_to_insert[pri], obj)
        for i in range(pri, 5):
            self._where_to_insert[i] += 1

    def pop(self):
        try:
            obj = self._q.pop(0)
        except IndexError:
            raise EmptyQueue
        else:
            self._where_to_insert = [max(0, n-1) # 0 if n == 0 else n-1
                                     for n in self._where_to_insert]
            return obj

    def __len__(self):
        return len(self._q)

# This version uses Python's built-in sort, which is unaware that the
# list into which it is inserting the new item is already sorted,
# which means that it ends up doing lots of unnecessary work.
class priority_queue_very_slow:

    def __init__(self):
        self._q = []

    def add(self, item, priority=2):
        if type(priority) is not int:
            raise TypeError
        if not (0 <= priority < 5):
            raise ValueError
        self._q.append((item, priority))

    def pop(self):
        if not self._q:
            raise EmptyQueue
        #self._q.sort(key=lambda e:e[1]) # This only works in Python 2.4 or newer.
        self._q.sort(lambda a,b:cmp(a[1],b[1]))
        return self._q.pop(0)[0]

    def __len__(self):
        return len(self._q)


import sys
if sys.version_info < (2,3):
    # Emulate function which only became available in Python 2.3

    def sum(sequence, start=0):
        return reduce(lambda a,b: a+b, sequence, start)

    def enumerate(iterable):
        result = []
        counter = 0
        for item in iterable:
            result.append((counter, item))
            counter = counter + 1
        return result
