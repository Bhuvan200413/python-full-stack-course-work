'''type(d)
<class 'dict'>
d =  dict()
d
{}
s = set()
data = {'name': 'John', 'age': 30, 'course': 'Python' , 'skills': 'python'}
data
{'name': 'John', 'age': 30, 'course': 'Python', 'skills': 'python'}
data['name']        
'John'
data['age']
30
data['course']
'Python'
data['skills']
'python'
data['name'] = 'Jane'
data
{'name': 'Jane', 'age': 30, 'course': 'Python', 'skills': 'python'}
data['skills'] = 'python, java'
data
{'name': 'Jane', 'age': 30, 'course': 'Python', 'skills': 'python, java'}
data['country'] = 'USA'
data
{'name': 'Jane', 'age': 30, 'course': 'Python', 'skills': 'python, java', 'country': 'USA'}
data['skills'] = data['skills'].split(', ')
data
{'name': 'Jane', 'age': 30, 'course': 'Python', 'skills': ['python', 'java'], 'country': 'USA'}
data['skills'].append('C++')
data
{'name': 'Jane', 'age': 30, 'course': 'Python', 'skills': ['python', 'java', 'C++'], 'country': 'USA'}  
d
{1: 'int'}
d[1.1] = 'float'
d
{1: 'int', 1.1: 'float'}    
d['ygdkw'] = 'string'
d[True] = 'bool'
d
{1: 'int', 1.1: 'float', 'ygdkw': 'string', True: 'bool'}
d[2+2j] = 'complex'
d   
{1: 'int', 1.1: 'float', 'ygdkw': 'string', True: 'bool', 2+2j: 'complex'}
id(d)
140432878896448
d[1] = 'integer'
d
{1: 'integer', 1.1: 'float', 'ygdkw': 'string', True: 'bool', 2+2j: 'complex'}          
d[1.1] = 'floating point'
d['age'] = 31
d['Name']= 'Jane Doe'
d['Name'] = 'kushal'
d
{1: 'integer', 1.1: 'floating point', 'ygdkw': 'string', True: 'bool', 2+2j: 'complex', 'age': 31, 'Name': 'kushal'}
d.items()
dict_items([(1, 'integer'), (1.1, 'floating point'), ('ygdkw', 'string'), (True, 'bool'), (2+2j, 'complex'), ('age', 31), ('Name', 'kushal')])
d.keys()    
dict_keys([1, 1.1, 'ygdkw', True, 2+2j, 'age', 'Name'])
d.values()
dict_values(['integer', 'floating point', 'string', 'bool', 'complex', 31, 'kushal'])
len(d)
7
sorted(d)
[1, 1.1, 2+2j, 'Name', 'age', 'ygdkw', True]
max(d)
True
min(d)
1
del d[1.1]
d   
{1: 'integer', 'ygdkw': 'string', True: 'bool', 2+2j: 'complex', 'age': 31, 'Name': 'kushal'}
d.clear()
d
{}  
data.pop('name')
'Jane'
data    
{'age': 31, 'course': 'Python', 'skills': ['python', 'java', 'C++'], 'country': 'USA', 'Name': 'kushal'}
data.popitem()
('Name', 'kushal')
data
{'age': 31, 'course': 'Python', 'skills': ['python', 'java', 'C++'], 'country': 'USA'}
data.popitem()
('country', 'USA')
data
{'age': 31, 'course': 'Python', 'skills': ['python', 'java', 'C++']}
data.clear()
data
{}'''

