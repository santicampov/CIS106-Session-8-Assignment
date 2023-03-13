#input
f = open("names.txt","r")
accbonus = 0
name = str(f.readline().rstrip('\n'))

#process
while name!="":
  salary = int(f.readline())
  if salary >= 100000:
    rate = 0.2
  elif salary >= 50000:
    rate = 0.15
  else:
    rate = 0.1
  bonus = rate * salary
  print(f"Last name: {name}")
  print(f"Salary: ${salary:.2f}")
  print(f"Bonus: ${bonus:.2f}\n")
  accbonus = accbonus + bonus
  name = str(f.readline())
f.close()

#output
print(f"The sum of all bonuses paid out is: ${accbonus:.2f}")