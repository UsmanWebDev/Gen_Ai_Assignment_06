# Initialize an empty shopping cart
cart = []

# Function to display the cart
def display_cart():
    print("Shopping Cart:")
    for item in cart:
        print(item)

# Function to add an item to the cart
def add_item():
    item = input("Enter an item: ")
    cart.append(item)
    print(f"Added {item} to the cart.")

# Function to remove an item from the cart
def remove_item():
    display_cart()
    item = input("Enter an item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"Removed {item} from the cart.")
    else:
        print("Item not found in cart.")

# Main function
def shopping_cart_program():
    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Exit")
        
        choice = input("Choose an operation: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_cart()
        elif choice == "4":
            print("Exiting the shopping cart program.")
            break
        else:
            print("Invalid choice, please select again.")

# Run the shopping cart program
shopping_cart_program()