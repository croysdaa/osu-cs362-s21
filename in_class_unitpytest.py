#import difflib

userInput = input("Enter a string to check if it's a palindrome: ")
i = len(userInput)
backwardsString = ""
while i > 0: 
    backwardsString += userInput[i - 1] 
    i = i - 1 
print(userInput, "is ")
if (str(userInput.strip('\n')) != str(backwardsString.strip())):
    print("not a palindrome")
elif (str(userInput.strip('\n')) == str(backwardsString.strip())):
    print("a palindrome.")
#diff = list(difflib.ndiff([userInput], [backwardsString]))
#print ("\n".join(list(diff)))
