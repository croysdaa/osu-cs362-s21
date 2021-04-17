import random
usernum = input("Enter a number: ")
i = 1
password = random.randint(1,10)
while i < int(usernum):
    password = str(password) + str(random.randint(1,10))
    i = i + 1
print(password)
