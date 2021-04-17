import math

usernum = input("Enter a number: ")
i = 1
num = int(usernum)
while i < math.sqrt(num):
    if num % i == 0:
        if num / i == i:
            print(float(i))
        else:
            print(float(i))
            print(num/i)
    i = i + 1
