'''wish = lambda name: f'hello {name}, welcome to python'

print(wish("bhuvan"))
print(wish("manideep"))
'''
'''
def add(a,b,c):
    return (a+b+c)/3

addl = lambda a,b,c: (a+b+c)/3

print(add(1,2,3))
print(addl(6,7,8))
'''
#even or odd using lambda function
'''
def iseven(n):
    if n%2==0:
        return "Even"
    else:
        return 'Odd'
    
isevenl = lambda n: 'even' if n%2==0 else 'odd'

print(iseven(18))
print(isevenl(13))'''

#greater number 
'''

def greater(a,b):
    if a>b:
        return a
    else:
        return b
    


greaterl = lambda a,b: a if a>b else b

print(greater(7,17))
print(greaterl(13,19))

'''


#map filter reduce
#first letter captial
'''
def fun(l):
    for i in range(len(l)):
        l[i]=l[i].title()
    return l


l =["bhuvan",'manideep','rahul','manoj','kushal']


res = list(map(lambda i:i.title(),l))

print(fun(l))
print(res)'''

# filtering in listt using lambda 
'''
def fun(l):
    res = []
    for i in range(len(l)):
        if l[i] % 3 == 0:
            res.append(l[i])
    return res


l = [20, 30, 40, 50, 60, 70, 80, 90, 100]

res = list(filter(lambda i: i % 3 == 0, l))

print(fun(l))
print(res)
 '''

'''
l = {
    'laptop': True,
    'iphone': False,
    'mouse': True,
    'tablet': False,
    'charger': True
}

res = list(filter(lambda i: l[i], l))

print(res)'''
#using reduce 
'''
from functools import reduce

l = [1, 2, 3, 1, 3, 4, 5, 5, 6, 2, 3, 5, 6, 7, 8, 2]

res = reduce(lambda a, b: a * b, l)

print(res)'''

'''
from functools import reduce

l = ['python', 'java', 'c++', 'c', 'html', 'reactjs']

res = reduce(lambda a, b: a + ' ' + b, l)

print(res)'''

d ={
    'apple' : 30,
    'orange': 35,
    'pineaple': 83,
    'mango' : 52,
    'graps':120,
    'banana':40
}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))