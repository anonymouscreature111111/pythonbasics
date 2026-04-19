days_present = int(input("Enter the number of days you were present: "))
total_days = 100

days_presentpercentage = (days_present/total_days)*100

if days_presentpercentage >= 75:
    print("You will be able to take the test")
elif days_presentpercentage < 75:
    print("You wont be able to take the test")

