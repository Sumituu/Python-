# Develop a Python program that uses a dictionary to store the prices of items in a shopping cart. Calculate the total cost of the items and display it to the user.

item_prices = {
    "apple": 0.5,
    "banana": 0.25,
    "orange": 0.75,
    "milk": 2.0,
    "bread": 1.5
}


shopping_cart = []

def calculate_total_cost(cart, prices):
    total_cost = 0
    for item in cart:
        if item in prices:
            total_cost += prices[item]
        else:
            print(f"Warning: Item '{item}' is not in the price list and was ignored.")
    return total_cost

while True:
    item = input("Enter an item to add to your cart (or 'done' to finish): ").lower()
    if item == 'done':
        break
    shopping_cart.append(item)

total_cost = calculate_total_cost(shopping_cart, item_prices)
print(f"Total cost of your shopping cart: ${total_cost:.2f}")

