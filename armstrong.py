number = int(input("Enter your number here: "))
sum = 0 
temp = number
while temp > 0:
  digit = temp % 10
  sum += digit**len(str(number))
  temp//=10
if number == sum:
  print(number, " is an armstrong number")
else:
  print(number, " is not an armstrong number")  

