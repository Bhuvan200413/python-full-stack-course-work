# loops
#for varable in seq:
#satement
#seq : list, tuple, string, range,set,dictionary

# for loop
'''
products = ['bread', 'butter', 'milk', 'eggs', 'cheese']
for item in products:
    print(item)'''
#for dictionary
'''
products = {'bread:50','butter:79','milk:90','eggs:23','cheese:82'}
for items in products:
    print("products: ",items)
   # print("price:",products[items])
    print("Buy now | Add to cart")
    print("Add to fav")
    print('-------------------------')'''
'''
#for loop with string - iterates through each character
s = 'python programimg'
for ch in s:
    print(ch)'''
#range(start,stop+1,step) =(0,stop+1,1)
'''
n= int(input("Enter a number: "))
for i in range(1,21):
    print(f"{n}*{i}={n*i}")
    '''
#break statement
'''
for i in range(10):
    if i == 15:
        break
    print(i)
else:
    print("End of number range")'''

pin = 1234
for i in range(5):
    user_pin = int(input("Enter the pin: "))
    if user_pin == pin:
        print("login sucessful")
        break
    else:
        print("Incorrect pin. Please try again.")
else:
    print("You have reached the max attemots,try after 5 time.")