a = range(10)
a[3]
a[-3]
a[3:6]
a[3:-3]
a[6:3]
a[:6]
a[0:6:2]

a[2:4] = ['x']
print a

a[-1:] = 'abc'
print a

a = range(4)
print a + [9,8,7]
print a * 4

b = [[0]*4]*4
print b
b[0][0] = 1
print b

a += [9]
a.append(7)
