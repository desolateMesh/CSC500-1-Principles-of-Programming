class ItemToPurchase:
        item_name = "none"
        item_price = 0.0
        item_quantity = 0
        item_description = "none"

class ShoppingCart:
        customer_name = "none"
        current_date = "January 1, 2020"
        cart_items = []

# Create a ShoppingCart object
cart = ShoppingCart()

# Prompt for customer information
cart.customer_name = input("Enter customer's name: ")
cart.current_date = input("Enter today's date: ")

# Initialize an empty list for cart items
cart.cart_items = []

# Main menu loop
while True:
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
    choice = input("Choose an option: ")
    # Add item choice
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name: ")
        item.item_price = float(input("Enter the item price: "))
        item.item_quantity = int(input("Enter the item quantity: "))
        item.item_description = input("Enter the item description: ")
        cart.cart_items.append(item)
    # Remove item choice
    elif choice == 'r':
        name = input("Enter name of item to remove: ")
        found = False
        for item in cart.cart_items:
            if item.item_name == name:
                cart.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    # Change item quantity choice        
    elif choice == 'c':
        name = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        found = False
        for item in cart.cart_items:
            if item.item_name == name:
                item.item_quantity = quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")
    # Output items' descriptions choice       
    elif choice == 'i':
        print(f"{cart.customer_name}'s Shopping Cart - {cart.current_date}")
        print("Item Descriptions")
        for item in cart.cart_items:
            print(f"{item.item_name}: {item.item_price:.2f}")
    # Output shopping cart choice        
    elif choice == 'o':
        print(f"{cart.customer_name}'s Shopping Cart - {cart.current_date}")
        if not cart.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {sum(item.item_quantity for item in cart.cart_items)}")
            total = 0
            for item in cart.cart_items:
                item_total = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item_total:.2f}")
                total += item_total
            print(f"Total: ${total:.2f}")
    # Quit        
    elif choice == 'q':
        break
    # Invalid option message
    else:
        print("Invalid option. Please try again.")