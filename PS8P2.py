#input
n1 = 0
n2 = 1

#process and output
for count in range (1,21,1):
  nextn = n1 + n2
  print(f"#{count} - {nextn}")
  n1 = n2
  n2 = nextn