# Simple Billing System
# acording to items user input items and their price



# user input item
item = input("enter your items here:  ")
price1 = int(input("enter items price here:-- ")) 
item = input("enter your items here:  ")
price2 = int(input("enter items price here:-- ")) 


total = price1 + price2 
gst = total *18 / 100
final_price = float(total + gst)
print(f"your final price is {final_price} ")
