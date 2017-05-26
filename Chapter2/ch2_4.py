__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 3.4. An Anagram Detection Example


# 3.4.1. Solution 1: Checking Off
# Premise: If it is possible to “checkoff” each character, then the two strings must be anagrams.
# Algorithm:
#   1) Check length
#   2) Go through string1, if it exists in string2, replace that letter in string2 with 'None'
# Problem: Does not check for length or duplicate letters
# Big-O- n^2. for each element in s1, algorithm will cycle through s2 until found...
def anagramSolution1(s1,s2):
    aList = list(s2)
    pos1 = 0
    stillOK = True
    # Continue until end of s1 string or a mismatch is found (stillOK = False)
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(aList) and not found: # Only finds one occurance... flawed....
            if s1[pos1] == aList[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            aList[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1
    return stillOK


# 3.4.2. Solution 2: Sort and Compare
# Premise: Even though s1 and s2 are different, they are anagrams only if they consist exactly of the same characters
# Algorithm:
#   1) Sort both strings
#   2) If equal, anagrams, if not, false
# Problem: More accurate than approach 1, but still gets hit with the sort cost
# Big-O: n^2 or similar since sort is expensives
def anagramSolution2(s1,s2):
    aList1 = list(s1)
    aList2 = list(s2)

    aList1.sort()
    aList2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if aList1[pos]==aList2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


# 3.4.4. Solution 4: Count and Compare
# Premise: Anagrams will not only have the same length, but the same number of character occurrences
# Algorithm:
#   1) Count the number of times each character occurs for each string
#   2) If two list of counters are equal, they are anagrams
# Problem: We take a hit on memory. Since this is a trivial example, its not that important but still something to consider
# Big-O: n, each list count is n, and the comparison will always be 26 letters if we are dealing with the US Alphabet
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    # Count first string
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a') # ord returns an integer representing the Unicode code point of that character
        c1[pos] = c1[pos] + 1
    # Count second string
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK


def main():
    print(anagramSolution1('abcd','dcba'))
    print(anagramSolution2('abcde','edcba'))
    print(anagramSolution4('apple', 'pleap'))


# def anagramSolution1(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     s1_list = list(s1)
#     s2_list = list(s2)
#     print(s1_list)
#     print(s2_list)
#     for letter in s1_list:
#         print(letter)
#         if s2_list.index(letter):
#             s2_list[s2.list.index(letter)] = None
#             print(s2_list)
#         else:
#             return False
#
# def main():
#     s1 = "it works"
#     s2 = "it works"
#     print(anagramSolution1(s1, s2))



if __name__ == '__main__':
    main()







# If all characters within the first string occurs within the second string and len(string1) == len(string2), then
# string 1 and string 2 should be anagrams.