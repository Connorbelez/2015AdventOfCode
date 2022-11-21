# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model 
# of determining whether a string is naughty or nice. None of the old
# rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in
# the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), 
# but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter
# between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) 
# and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter 
# that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat 
# with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with 
# one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?

def checkString(string):
    pairSet = set()
    i = len(string)-1
    pattern1 = False
    pattern2 = False
    overlapThreat = False
    blackList = []
    while i >= 1:
        print("============= Iteration {i} =============".format(i=i))

        if i >= 2:
            window1 = string[i-2:i+1]
            print("WINDOW1: ", window1)
            if window1[0] == window1[2]:
                pattern1 = True
            if window1[0] == window1[1] == window1[2]:
                overlapThreat = True
        
        window2 = string[i-1:i+1]
        print("WINDOW2: ", window2)
        pair = window2[0] + window2[1]
        if pair not in pairSet:
            pairSet.add(pair)
            print("Added Pair: ", pair," to set")
        elif i not in blackList:
            pattern2 = True
            print("Pattern2 True, pair: ", pair)
            print("Index: ", i)

        if overlapThreat:
            blackList.append(i-1)
            print("BlackList: ", blackList)
            overlapThreat = False
        i -= 1
    print(pairSet)
    if pattern1 and pattern2:
        return True
    else:
        return False
    
    
#generate test cases for checkString:


if __name__ == "__main__":
    print(checkString("rthkunfaakmwmushzzz"))
    
    
    with open('data5p2.txt') as f:
        niceStrings = 0
        for line in f:
            if checkString(line):
                niceStrings += 1
    print(niceStrings)