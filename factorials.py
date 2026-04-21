def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
num = int(input("Enter a number: "))
if num < 0:
    print("Sorry negative numbers don't have factorials")
elif num == 0:
    print("Factorial of 0 is always 1")
else:
    print("The factorial of ",num, "is", recur_factorial(num))