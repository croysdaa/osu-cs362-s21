import re
import pytest
import unittest

userInput = input("Enter a string to check its word count: ")

def findWordCount(userInput):
    wordCount = len(re.split(';|.|,|\*|\n|\t', userInput))
    print ("Your sentence has " +  str(wordCount) + " words.")
    return(wordCount)

def test_enter():
    assert findWordCount('hi\nthere') == 2
    
def test_tab():
    assert findWordCount('hi\tthere') == 2
    
def test_astrix():
    assert findWordCount('hi\*there') == 2
    
def test_comma():
    assert findWordCount('hi,there') == 2
    
def test_semi():
    assert findWordCount('hi;there') == 2
    
def test_period():
    assert findWordCount('hi.there') == 2
