copies = int(input("Enter the number of copies: "))

price = 0.0
if copies > 0 and copies <= 99:
  price = 0.30
  print(price*copies)
elif copies > 99 and copies <= 499:
  price = 0.28
  print(price*copies)
elif copies > 499 and copies <= 749:
  price = 0.27
  print(price*copies)
elif copies > 749 and copies <= 1000:
  price = 0.26
  print(price*copies)
elif copies >= 1000:
  price = 0.25
  print(price*copies)
else:
  print("The Number entered is invalid")