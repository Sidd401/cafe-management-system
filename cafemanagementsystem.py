menu={
    'Tea':10,
    'Coffee':15,
    'Pizza':100,
    'Burger':49,
    'Smoothie':75
}
print("welcom to name Restaurant")
print("Item  amt\nTea  10\nCoffee  15\nPizza  100\nBurger  49\nSmoothie  75")
order=0
item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order+=menu[item_1]
    print(f"Your item {item_1 } has been added to your order")
else:
    print(f"Order item {item_1} is not avaialable yet!")
    
another_order=input("Do you want to add another item? (Yes/No)")
if another_order =="Yes":
        order2=input("Enter your name of Second item=")
        if order2 in menu:
            order+=menu[order2]
            print(f"Item {order2} has been added to oder")
        else:
            print(f"Ordered item {order2} is not available!")
print(f"The total amount of items to pay is {order}")
            
