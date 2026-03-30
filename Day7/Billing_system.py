#billing products
products =['Rice','Sugar','wheat','Bread','Salt','Tea','Cooking Oil','Eggs','Milk','soap']

prices =[60,30,40,45,90,10,50,10,15,20]

print("-----------------------Billing System------------------")
print("Here is the list of products available:\n")

print('Index'.ljust(6,' '),'Product'.ljust(15,' '),'Price'.ljust(6, ' '))


for i in range(10):
    print(str(i+1)ljust(6,' '),products[i].ljust(15,' '),str(prices[i]).ljust(6,' '))

    items = list(map(int,input("Enter the index of the products you want to buy (separated by space): ").split()))