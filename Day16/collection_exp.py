import collections

s = 'python programming'
l = [1, 2, 3, 12, 34, 1, 1, 2, 3, 4, 2, 3]
r = 'this is that that is this'.split()

res = collections.Counter(s)
res1 = collections.Counter(l)
res2 = collections.Counter(r)

print(res)
print(res1)
print(res2)