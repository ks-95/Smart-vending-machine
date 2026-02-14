class InventoryManager:
    def __init__(self):
        self.inventory = {"Coke": 10, "Chips": 5, "Water": 8}
        self.prices = {"Coke": 25, "Chips": 20, "Water": 15}

    def check_stock(self, item):
        return self.inventory.get(item, 0) > 0

    def get_price(self, item):
        return self.prices.get(item, 0)

    def reduce_stock(self, item):
        self.inventory[item] -= 1

class PaymentProcessor:
    def __init__(self):
        self.balance = 0

    def insert_money(self, amount):
        self.balance += amount
        print(f"Current Balance: ₹{self.balance}")

    def process_payment(self, cost):
        if self.balance >= cost:
            self.balance -= cost
            return True
        return False

class VendingMachine:
    def __init__(self):
        self.inventory = InventoryManager()
        self.payment = PaymentProcessor()

    def select_product(self, item):
        if not self.inventory.check_stock(item):
            print(f"Sorry, {item} is out of stock.")
            return

        price = self.inventory.get_price(item)
        print(f"{item} costs ₹{price}.")
        
        if self.payment.process_payment(price):
            self.inventory.reduce_stock(item)
            print(f"Dispensing {item}. Enjoy!")
        else:
            print("Insufficient balance. Please insert more money.")

# Example Usage:
# vm = VendingMachine()
# vm.payment.insert_money(50)
# vm.select_product("Coke")