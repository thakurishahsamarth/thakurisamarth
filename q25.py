number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz\n")
elif number % 3 == 0:
    print("Fizz\n")
elif number % 5 == 0:
    print("Buzz\n")
else:
    print(number)