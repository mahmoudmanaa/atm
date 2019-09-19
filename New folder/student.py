def apply():
    try:
        age = input("your age:" )
        age =int(age)
        if age < 18:
         print("You are too young")
        elif age > 22:
         print("You are too old")
        else :
          print("Welcome to Egypt scholarship program")
    except ValueError:
        print("Enter your age in numbers ex: 1,2,3...")
        apply()

count = 0
while count < 1000:
   apply()
   count += 1
