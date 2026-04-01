import collections

s='python programming'

res = collections.defaultdict(int)
for i in s:
    res[i] = res[i]+1
print(res)