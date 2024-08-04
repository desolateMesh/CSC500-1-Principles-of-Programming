# ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0.0
        self.item_quantity = 0

# New ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="August 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Add item to cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Remove item from cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    # Modify item in cart
    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0.0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Get number of items in cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Get cost of cart
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    # Print total
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_quantity * item.item_price:.2f}")
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Print descriptions
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# Main section
print("Enter customer's name:")
customer_name = input()
print("Enter today's date:")
current_date = input()
print(f"Customer name: {customer_name}")
print(f"Today's date: {current_date}")

# Create shopping cart object
cart = ShoppingCart(customer_name, current_date)

# loop for menu
while True:
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
    # Get user choice
    choice = input("Choose an option: ")
    
    # Process user choice
    if choice == 'a':
        item = ItemToPurchase()
        print("ADD ITEM TO CART")
        item.item_name = input("Enter the item name: ")
        item.item_description = input("Enter the item description: ")
        item.item_price = float(input("Enter the item price: "))
        item.item_quantity = int(input("Enter the item quantity: "))
        cart.add_item(item)

    # Remove item from cart   
    elif choice == 'r':
        print("REMOVE ITEM FROM CART")
        name = input("Enter name of item to remove: ")
        cart.remove_item(name)

    # Change item quantity       
    elif choice == 'c':
        print("CHANGE ITEM QUANTITY")
        name = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        item = ItemToPurchase()
        item.item_name = name
        item.item_quantity = quantity
        cart.modify_item(item)

    # Output items' descriptions      
    elif choice == 'i':
        cart.print_descriptions()

    # Output shopping cart        
    elif choice == 'o':
        cart.print_total()

    # Quit       
    elif choice == 'q':
        break

    # Invalid option
    else:
        print("Invalid option. Please try again.")