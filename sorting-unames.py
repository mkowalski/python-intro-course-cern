passwds = []

with open("/etc/passwd") as my_file:
    for line in my_file:
        if not line.startswith("#"):
            uname, _, uid, _ = line.split(":", 3)
            passwds.append((uname, int(uid)))


print sorted(passwds, cmp=lambda x, y: cmp(x[1], y[1]))

###

def key(x):
    def key(y):
        return y[x]
    return key
    # return lambda y: y[x]

print sorted(passwds, key=key(1))

###

from functools import partial
def key(n, pair):
    return pair[n]

print sorted(passwds, key=partial(key, 1))

###

print sorted(passwds, key=lambda x: x[1])

###

def my_partial(callable, *args):
    def proxy(*args2):
        return callable(*(args+args2))
    return proxy

print sorted(passwds, key=my_partial(key, 1))

###

from operator import itemgetter
print sorted(passwds, key=itemgetter(1))
