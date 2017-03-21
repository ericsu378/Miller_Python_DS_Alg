# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# Activecode 8
# The following code fragment iterates over a list of strings and for each string processes each character
# by appending it to a list. The result is a list of all the letters in all of the words.

# Self Check
# Test your understanding of what we have covered so far by trying the following exercise. Modify the code from
# Activecode 8 so that the final list only contains a single copy of each letter.
# The answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

# Self Check 2
# Test your understanding of list comprehensions by redoing Activecode 8 using list comprehensions.
# For an extra challenge, see if you can figure out how to remove the duplicates.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']


# Activecode 8
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print("Active Code 8")
print(letterlist)

# Self Check 1
# Modify the code from Activecode 8 so that the final list only contains a single copy of each letter.
# Option 1
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
            if aletter not in letterlist:
                letterlist.append(aletter)
print("Self Check 1 - Option 1")
print(letterlist)

# Option 2 (unordered)
print("Self Check 1 - Option 2(unordered)")
print(list(set(letterlist)))


# Self Check 2
# Test your understanding of list comprehensions by redoing Activecode 8 using list comprehensions.
# For an extra challenge, see if you can figure out how to remove the duplicates.

wordlist = ['cat','dog','rabbit']

print("Self Check 2 - list comprehension")
letterlist = [aletter for aword in wordlist for aletter in aword]
print(letterlist)

print("Self Check 2 - list comprehension w/ join")
letterlist = [aletter for aletter in "".join(wordlist)]
print(letterlist)

print("Self Check 2 - list comprehension w/ range")
letterlist = [word[i] for word in wordlist for i in range(len(word))]
print(letterlist)

# Filtering During Comprehension : Single Lined Version
print("Self Check 2 Challenge - remove duplicates while keeping order")
seen = set()
seen_add = seen.add
print([letter for word in wordlist for letter in word if not (letter in seen or seen_add(letter))])

print("Self Check 2 Challenge - Unordered")
unique_letterlist = list(set(letterlist))
print(unique_letterlist)


