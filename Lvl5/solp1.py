# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd),
# or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter 
# (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters
# used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

# vowelCounter = 0
# threeVowels = False
# doubleLetter = False
# noBadStrings = False

def checkString(string):
    vowelList = ['a','e','i','o','u']
    badStrings = ['ab','cd','pq','xy']
    vowelCounter = 0
    threeVowels = False
    doubleLetter = False
    noBadStrings = True
    i = len(string) - 1
    if string[i] in vowelList:
        vowelCounter += 1
    while i > 0:
        char1 = string[i]
        char2 = string[i-1]
        
        if char1 == char2:
            doubleLetter = True
        if char2 in vowelList:
            vowelCounter += 1
        if char2 + char1 in badStrings:
            noBadStrings = False
        i -= 1
    if vowelCounter >= 3:
        threeVowels = True
    
    if threeVowels and doubleLetter and noBadStrings:
        return 1
    else:
        return 0

print(checkString("jchzalrnumimnmhp"))
print(checkString("haegwjzuvuyypxyu"))
print(checkString("dvszwmarrgswjxmb"))


with open('data5p1.txt') as f:
    numNice = 0
    for line in f:
        numNice += checkString(line)
    print(numNice)
        
        
