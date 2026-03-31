import random

random.seed(7)

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l = ['java','python','c++']

print(random.choice(l))
print(random.choices(l,k=2))
