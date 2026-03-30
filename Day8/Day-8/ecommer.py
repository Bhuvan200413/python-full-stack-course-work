#ecommerce
products = [['laptop',56000],
            ['mobile',15000],
            ['headphones',2000],
            ['keyboard',1500],
            ['mouse',800]
            ]
def view_products():
    print('product name'.ljust(15), 'price')
    for i in products:
        print(f"{i[0]}: Rs.{i[1]}")
def add_product():
    product_name = input("Enter the product name: ")
    price = int(input("Enter the price: "))
    products.append([product_name, price])
    print(f"{product_name} is added.")
def del_product():
    product_id = int(input("Enter the product ID to delete: "))
    print(f"Products [product_id] is deleted.")
    products.pop(product_id)

while True:
    print("------- Welcome to the flipkart admin site --------")
    print("1. View products")
    print("2. Add product")     
    print("3. Delete product")
    print("4. Exit")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        view_products()
    elif ch == 2:
        add_product()
    elif ch == 3:
        del_product()
    elif ch == 4:
        print("Thankyou...")
        break
    else:
        print("Invalid choice. Please try again.")