class Transaction:
    def __init__(self, amount, category, type):
        self.amount = amount
        self.category = category
        self.type = type

    def display(self):
        print(f"{self.type} | {self.category} | ₹{self.amount}")


class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, category):
        t = Transaction(amount, category, "Income")
        self.transactions.append(t)
        print("Income added successfully!")

    def add_expense(self, amount, category):
        t = Transaction(amount, category, "Expense")
        self.transactions.append(t)
        print("Expense added successfully!")

    def view_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions found")
        else:
            for t in self.transactions:
                t.display()

    def check_balance(self):
        balance = 0
        for t in self.transactions:
            if t.type == "Income":
                balance += t.amount
            else:
                balance -= t.amount
        print("Current Balance: ₹", balance)


class App:
    def __init__(self):
        self.manager = FinanceManager()

    def run(self):
        while True:
            print("\n---- Personal Finance Manager ----")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. Check Balance")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                amount = int(input("Enter income amount: "))
                category = input("Enter income source: ")
                self.manager.add_income(amount, category)

            elif choice == 2:
                amount = int(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                self.manager.add_expense(amount, category)

            elif choice == 3:
                self.manager.view_transactions()

            elif choice == 4:
                self.manager.check_balance()

            elif choice == 5:
                print("Thank you!")
                break

            else:
                print("Invalid choice")


app = App()
app.run()