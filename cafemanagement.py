menu={
  'pizza':40,
  'pasta':38,
  'burger':58,
  'salad':67,
}
print("welcome to SAMAR Restaurant")
print("pizza: Rs40\npasta: Rs38\nburger: Rs58\nsalad: Rs67\n")

order_total=0
item_1= input("enter the name of your item you want to order= ")
if item_1 in menu:
  order_total+= menu[item_1]
  print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")
another_order= input ("do you want to add another item?(yes/no)")
if another_order=="yes":
      item_2=input("enter the name of your second item=")
      if item_2 in menu:
       order_total+=menu[item_2]
      print(f"item {item_2} has been added to order")
else:
    print(f"ordered item {item_2}is not available yet!")
    print(f"the total amount of item to pay is {order_total}")