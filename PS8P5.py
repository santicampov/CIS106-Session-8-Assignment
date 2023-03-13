#input
f = open("students.txt","r")
name = str(f.readline().rstrip('\n'))
count = 0
totaltuition = 0

#Process
while name!="":
  district = str(f.readline())
  credit = int(f.readline())
  if "I" in district:
    cprice = 250
  else:
    cprice = 500
  tuition = credit * cprice
  count = count + 1
  print(f"Student last name: {name}")
  print(f"Credits taken : {credit}")
  print(f"Tuition price: ${tuition:.2f} \n")
  totaltuition = totaltuition + tuition
  name = str(f.readline())


f.close


#output
print(f"Number of students: {count}")
print(f"Total tuition of all students is:: ${totaltuition:.2f}")