#inputs
c = open("item.txt","r")
count = 0
extendedsum = 0
item = str(c.readline().rstrip('\n'))
print("Order : \n")

#process 
while item!="":
  qty=int(c.readline())
  price=int(c.readline())
  extprice = qty * price
  extendedsum = extendedsum + extprice
  count = count + 1
  print(f"Item: {item}")
  print(f"Qty: {qty}")
  print(f"Price : ${price:.2f}")
  print(f"Total: ${extprice:.2f}\n")
  item=str(c.readline())

c.close
average = extendedsum/count

#output
print(f"The sum of the order is: ${extendedsum:.2f}")
print(f"Total number of orders: {count}")
print(f"The average value is ${average:.2f}")