#grading system

data={
    'anju':{'status':True,'python':70,'mysql':60,'django':77},
    'manoj':{'status':True,'python':99,'mysql':99,'django':97},
    'bhuvan':{'status':True,'python':80,'mysql':89,'django':77},
    'kushal':{'status':False,'python':None,'mysql':None,'django':None},
    'manideep':{'status':True,'python':50,'mysql':55,'django':57},
    'himaja':{'status':True,'python':35,'mysql':39,'django':37},
    'vijay':{'status':True,'python':22,'mysql':33,'django':27},
}

name=input("Enter the student name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+ data[name]['mysql']+ data[name]['django']
        avg = sum/3
        if avg>=90:
            print(f'Congrats {name}, You got first class')
        elif avg>=75:
            print(f'Good {name}, wish you all the best for next time')
        elif avg>=50:
            print(f'{name}, need improvement')
        elif avg>=35:
            print(f'bad {name}, word hard next time')
        elif avg<35:
            print(f'{name}, you failed in the exam, bring your parents')
    else:
        print(f'{name}, you have not written the exams.please bring your parents')
else:
    print(f'{name} data is not found')