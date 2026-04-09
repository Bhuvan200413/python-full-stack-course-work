class Flipkart:
    #Class attribute
    discount = 10

    @classmethod
    def myDiscount(cls,new_discount):
        cls.discount = new_discount

   
    @staticmethod
    def welcome():
        print('Welcome to the flipkart')


    def myorder(self,order_id):
        #instance attribute
        self.order_id = order_id
        print(f"You have order these product with id: {self.order_id}")




bhuvan = Flipkart()
manoj = Flipkart()

print(bhuvan.discount)
print(Flipkart.discount)

bhuvan.myorder(1)

print(bhuvan.order_id)

bhuvan.myDiscount(20)
bhuvan.myorder(2)
bhuvan.welcome()

Flipkart.myDiscount(20)
Flipkart.welcome()

bhuvan.myorder(1)
bhuvan.myorder(2)
bhuvan.myorder(3)