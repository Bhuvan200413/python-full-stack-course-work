data = {}
n = int(input('enter the number of students:'))
for i in range(n):
    name =input('enter the names of students:')
    data[name] = False

for name in data:
    status = int(input(f"Enter the {name} status(0-absent,1-present): "))
    data[name]= bool(status)
print(data)