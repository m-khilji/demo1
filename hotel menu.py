# Define the menu of restaurant
menu = {
     'pizza':40,
     'pasta':50,
     'burger':40,
     'coffee':80,
     'salad':90,

}
#Greet
print("welcome to our restaurant")
print("pizza: Rs40\npasta: Rs50\nburger: Rs40\ncoffee: Rs80\nsalad: Rs90")

order_total = 0
#40 + 80 = 120

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] # 0 + 50
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not avalible yet!")

Another_order = input("Do you want to add another item? (yes/no) ")
if Another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not avalible!")

print(f"The total amount of items to pay is {order_total}")
    