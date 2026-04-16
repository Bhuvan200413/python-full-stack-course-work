import re

text = 'Python programming'
pattern - r'[0-9]'


result = re.match(pattern,text)

print(result.group() if result else "No match found")