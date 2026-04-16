try:
    balance =  1000
    amount = -10
    if amount<0:
        raise Exception('amount need to be positive')
    balance+= amount

except Exception as e:
    print("Error occured:" ,e)

else:
    print("current Balance: ",balance)
finally:
    print("End of the program2 ")