print("Would you like to add, subtract, multiply or divide?")
answer = 'a'
while answer != 'quit':
    answer = input("Enter 'a', 's', 'm', 'd' or 'quit': ")
    if answer != 'quit':
        first = input("Enter first number: ")
        sec = input("Enter second number: ")
    if answer == 'quit':
        print("Goodbye")
    elif answer == 'a':
        sum1 = float(first) + float(sec)
        print(sum1)
    elif answer == 's':
        difference = float(first) - float(sec)
        print(difference)
    elif answer == 'm':
        product = float(first) * float(sec)
        print(product)
    elif answer == 'd':
        quotient = float(first) / float(sec)
        print(quotient)
    else:
        print("Try again")
