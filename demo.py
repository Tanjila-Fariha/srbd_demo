
class User:
    """Base class for all users"""
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def login(self):
        print(f"LOG: {self.username} has logged in.")

class Cart:
    """A standalone class to hold items"""
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str):
        self.items.append(item_name)
        print(f"CART: Added {item_name} to the cart.")

class Customer(User):
    """A Customer IS-A User (Inheritance) and HAS-A Cart (Composition)"""
    def __init__(self, username: str, email: str):
        super().__init__(username, email)
        self.shopping_cart = Cart()  # Linking Customer to Cart

    def place_order(self):
        if self.shopping_cart.items:
            print(f"ORDER: {self.username} placed an order for: {self.shopping_cart.items}")
        else:
            print("ORDER: Cart is empty!")

class Admin(User):
    """An Admin IS-A User (Inheritance)"""
    def __init__(self, username: str, email: str, access_level: int):
        super().__init__(username, email)
        self.access_level = access_level

    def delete_user(self, user: User):
        print(f"ADMIN: User {user.username} has been removed from the system.")

# --- THE DRIVER CODE (Execution) ---

if __name__ == "__main__":
    print("--- Starting Corporate System Test ---")

    # 1. Create a Customer and use the Cart
    buyer = Customer("Alice_Dev", "alice@corp.com")
    buyer.login()
    buyer.shopping_cart.add_item("ThinkPad Laptop")
    buyer.place_order()

    print("-" * 30)

    # 2. Create an Admin to manage the Customer
    boss = Admin("SuperUser", "admin@corp.com", access_level=10)
    boss.login()
    boss.delete_user(buyer)

    print("--- Test Complete ---")