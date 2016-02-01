__author__ = 'ESU_2'

# Problem Solving with Algorithms and Data Structures Release 3.0
# Brad Miller, David Ranum
# September 22, 2013

# 1.4.6 Object-Oriented Programming in Python: Defining Classes

# Self Check (modify existing code)
# To make sure you understand how operators are implemented in Python classes, and how to
# properly write methods, write some methods to implement *, /, and -. Also implement comparison
# operators > and <.

class Fraction:

    # constructor
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    # override __str__ function (used for print)
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    # Self check: implement *
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    # Self check: implement /
    def __div__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    # Self check: implement -
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    # Self check: implement <
    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num < second_num

    # Self check: implement >
    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num > second_num


# Helper Functions

# Euclid's Algorithm states that the greatest common divisor of two integers m and n is n if
# n divides m evenly. However, if n does not divide m evenly, then the answer is the greatest
# common divisor of n and the remainder of m divided by n.
def gcd(m,n):
    while m%n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

# Instance of Fraction class (instance invokes constructor)
x = Fraction(1,2)
y = Fraction(2,3)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x == y)
print(x < y)
print(x > y)