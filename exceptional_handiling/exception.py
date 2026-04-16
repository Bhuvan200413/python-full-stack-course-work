#single Exception
# try:
#     a=int(input("Enter a integer: "))
# except ValueError:
#     print("Please enter a valid integer")
# else:
#     print("a=",a)

# finally:
#     print("End of the program")

#multiple exceptions

# try: 
#     l=[2,33]
#     #print(l[7])
#     d = {1:2,3:2,2:4}
#     #print(d[9])
#     #a = int(input("enter a interger"))
#     #print(10/0)
#     print('a'+10)

# except TypeError:
#     print("give the same data type")

# except ZeroDivisionError:
#     print("Cant divide by 0")

# except KeyError:
#     print("key is not present")

# except IndexError:
#     print("error")

# else:
#     print("a=",a)

# finally:
#     print("End of program")



try: 
     #print(b)
     l=[2,33]
     #print(l[7])
     d = {1:2,3:2,2:4}
     #print(d[9])
     #a = int(input("enter a interger"))
     print(10/0)
     print('a'+10)
except (TypeError,ZeroDivisionError,KeyError,IndexError,ValueError) as e:
    print("Erroe occured: ",e)

else:
     print("a=",a)

finally:
     print("End of the program")

