#Define the menu of the restutant

menu={
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee':80,
}
print(" Welcome to PYTHON Resturant ")
print(" Pizza: Rs 40 \n  Pasta: Rs 50 \n Burger: Rs 60 \n Salad: Rs 70 \n Coffee: Rs 80 \n")
order_total=0

item_1= input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f" your item {item_1} has been added to the menu ")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input(" Do you want to add another item ? (YES/NO)")
if another_order== "yes":
    item_2 = input ("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2} has been added to order ")

print(f"The total amount of item to pay is {order_total}")