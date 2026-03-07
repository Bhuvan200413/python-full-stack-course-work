#condition statements
#if statement
'''data = ('user@gmail.com','user@123')
mail = input('Enter the mail: ')
password = input('Enter the password: ')

if data == (mail,password) :
    print('Login successful')
else: 
    print('Invalid login')'''
'''
#if else statement
fruits = ['mango','papaya','pine apple']
search_item = input("search item: ")
if search_item in fruits :
    print('found item buy now')
else:
    print("item notfound: ")'''
# elif statement
'''

time = int(input("Eenter the hour: "))

print("Avalialble buses are: ")
if 0 <= time <=6 :
    print("Bus2\nBus7\nBus13\nBus17")
elif 7 <= time <=12 :
    print("Bus3\nBus8\nBus14\nBus18")
elif 13 <= time <=18 :
    print("Bus4\nBus9\nBus15\nBus19")  
elif 19 <= time <=24 :
    print("Bus5\nBus10\nBus16\nBus20")  
else:
    print("Enter the valid time range: ")
    '''
#elif statement condition
'''
print("Welcome to uber, Book your ride now: ")
print("1.Bike")
print("2.Auto")
print("3.Cab")

choice = int(input("Enter your choice: "))
if choice == 1 :
    print("You have booked Bike\n Driver is on the way\n Wear the healmet :")
elif choice == 2 :
    print("You have booked Auto\n Driver is on the way :")
elif choice == 3 :
    print("You have booked Cab\n Driver is on the way\n Put on seatbealt :")'''
#nested if statement
login_status = True
premium_account = True

if login_status:
    print("Welcome to the Hotstar")
    if premium_account:
        print("Play the video with high quality and without ads")
    else:
        print("Play the video with normal quality and with ads")
else:
    print("Invalid Login") 
    