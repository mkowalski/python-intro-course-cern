passwds = []

with open("/etc/passwd") as my_file:
    for line in my_file:
        if not line.startswith("#"):
            uname, _, uid, _ = line.split(":", 3)
            passwds.append((uname, int(uid)))


def key(x):
    def key(y):
        return y[x]
    return key
    # return lambda y: y[x]


# print sorted(passwds, cmp=lambda x, y: cmp(x[1], y[1]))
# print sorted(passwds, key=lambda x: x[1])
print sorted(passwds, key=key(1))
