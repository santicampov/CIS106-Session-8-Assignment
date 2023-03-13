#input 
p = float(input("Enter the principle ammount."))
r = float(input("Enter interest rate in decimal form."))

accint = 0

#process and output
for count in range(1,6,1):
  i = p * r
  eb = p + i 
  print(f"Year: {count}   Principle: ${p:.2f}   Ending Balance: ${eb:.2f}")
  p = eb
  accint = accint + i

print(f"The accumulated interest for the 5 years is: ${accint:.2f}")