print("Welcome to my restaurant")
print("Here is a list of food items available")
food_menu = {
"Fufu" : 15,
"Banku" : 10,
"Omotuo" : 10,
"Konkonte" : 10
}
for food, price in food_menu.items():
    print(f"{food} : GH₵{price}")
order_menu = input("Please enter what you like to order ")
if order_menu in food_menu:
    print(f"You have ordered: {order_menu}")
    print(f"Price GH₵{food_menu[order_menu]}")
else:
    print("We don't have what you ordered")      
print("Thank-you for ordering from us")