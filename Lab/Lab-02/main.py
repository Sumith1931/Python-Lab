from coffee_shop.shop import CoffeeShop


shop =   CoffeeShop()                                                # How do we initialize an object here?

print("☕ Welcome to Our Coffee Shop! ☕")

shop.display_menu()                                         # Why am i not storing it in a variable here? Answer here Display does not return anything, just prints items

category = input("\nChoose a category: ").lower()

shop.display_category(category)

item = input("\nChoose an item: ").lower()
quantity = int(input("Enter quantity: "))

total = shop.order(category, item, quantity)

if total is not None:
    print("\n--------------------------")
    print(f"Item     : {item.title()}")
    print(f"Quantity : {quantity}")
    print(f"Total    : ₹{total}")                                   # How to print the total here?
    print("--------------------------")
    print("Thank you for your order! 😊")
