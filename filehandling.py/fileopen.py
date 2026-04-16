# try:
#     file = open('filehandling.py/student.txt', 'r')

# except FileNotFoundError:
#     print("File is not present")

# else:
#     print(file.read())
#     file.seek(0)
#     print(file.readline())
#     file.seek(0)
#     print(file.readlines())
#     file.close()


with open('filehandling.py/student.txt', 'w+') as file:
     file.write('\nram')
     file.write('\nnagarddy')

