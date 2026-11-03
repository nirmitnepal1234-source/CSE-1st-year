print("***Tip Calculator***")
items=int(input("Enter the number of items:"))
item_name=[]
item_price=[]
item_quantity=[]
item_total=[]
for i in range (1,items+1):
    name=input(f"Enter the name of you item {i}:")
    price=float(input(f"Enter the price of {name} (in Rs.):"))
    quantity=int(input(f"Enter the quantity of {name}:"))
    total=price*quantity
    item_quantity.append(quantity)
    item_name.append(name)
    item_price.append(price)
    item_total.append(total)
subtotal=sum(p*q for p,q in zip(item_price,item_quantity))
tip=float(input("Enter the amound you want to tip (in Rs.):"))

print("\n"+"="*40)
print("               Detailed Bill")
print("="*40)
print("Item     Quantity     Price    Total")
print("-"*40)
for name,quantity,price,total in zip(item_name,item_quantity,item_price,item_total):
    print(f"{name:<15}{quantity:>5}{price:>8.2f}{total:>8.2f}")
print("-"*40)
print(f"Subtotal                   :Rs {subtotal}")
print(f"Tip Amount                 :Rs {tip}")
print("-"*40)
print(f"Total                      :Rs {subtotal+tip}")
print("Thank you for visiting!")


