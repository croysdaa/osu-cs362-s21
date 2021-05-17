import pytest

userInput = input("Enter a string to check its word count: ")
wordCount = len(userInput.split())
print ("Your sentence has: " +  str(wordCount) + " words.")

#def test_capital_case():
#    assert capital_case('semaphore') == 'Semaphore'
