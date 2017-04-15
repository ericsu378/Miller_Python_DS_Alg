__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures Release 3.0
# Brad Miller, David Ranum
# September 22, 2013

# 1.4.3 Control Structure Self Check

# Original Code
# word_list = ['cat','dog','rabbit']
# letter_list = []
# for a_word in word_list:
#     for a_letter in a_word:
#         letter_list.append(a_letter)
# print(letter_list)

# 1. Modify the given code so that the final list only contains a single copy of each letter.
#  the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
# word_list = ['cat','dog','rabbit']
# letter_list = []
# for a_word in word_list:
#     for a_letter in a_word:
#         if a_letter not in letter_list:
#             letter_list.append(a_letter)
# print(letter_list)


#2. Redo the given code using list comprehensions.
# For an extra challenge, see if you can figure out how to remove the duplicates.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
# word_list = ['cat','dog','rabbit']
# letter_list = [a_letter for a_word in word_list for a_letter in a_word]
# print(letter_list)

# Approach 1
# unique = []
# [unique.append(a_letter) for a_word in word_list for a_letter in a_word if a_letter not in unique]
# print(unique)

# Approach 2, using sets
# unique2 = {a_letter for a_word in word_list for a_letter in a_word}
# print unique2
# print list(unique2)

string = "abcdefg"
print string[2]
string_list = list(string)
string_list[2] = "z"
print "".join(string_list)