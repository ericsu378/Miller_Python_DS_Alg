__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 1.7 Programming Exercises

# 1. Implement the simple methods get_num and get_den that will return the numerator
# and denominator of a fraction.

# 2. In many ways it would be better if all fractions were maintained in lowest terms right
# from the start. Modify the constructor for the Fraction class so that GCD is used to
# reduce fractions immediately. Notice that this means the __add__ function no longer
# needs to reduce. Make the necessary modifications.

# 3. Implement the remaining simple arithmetic operators (__sub__, __mul__, and
# __truediv__).

# 4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and
# __ne__)

# 5. Modify the constructor for the fraction class so that it checks to make sure that the numerator
# and denominator are both integers. If either is not an integer the constructor
# should raise an exception.

# 6. In the definition of fractions we assumed that negative fractions have a negative numerator
# and a positive denominator. Using a negative denominator would cause some of the
# relational operators to give incorrect results. In general, this is an unnecessary constraint.
# Modify the constructor to allow the user to pass a negative denominator so that all of the
# operators continue to work properly.

# 7. Research the __radd__ method. How does it differ from __add__? When is it used?
# Implement __radd__.
# __add__ | myobj + 4 | my.obj.__add__(4)
# __radd__ | 4 + myobj | (4)._add__(myobj) or myobj.__radd__(4)

# 8. Repeat the last question but this time consider the __iadd__ method.
# __iadd__ | x += 1 --> x = x + 1

# 9. Research the __repr__ method. How does it differ from __str__? When is it used?
# Implement __repr__.
# When printing an object, __str__ will be used if defined, otherwise, __repr__ will be used.
# __repr__ is typically what is echoed in your python shell when it evaluates an expression that returns an object
# example: <__main__.Foo object at 0x7f80665abdd0>
# ( module the object is from, class name, and hexadecimal representation of its location in memory)
# example2:
# __repr__
# >>> datetime.datetime.now()
# datetime.datetime(2015, 1, 24, 20, 5, 36, 491180)
# __str__
# >>> print(datetime.datetime.now())
# 2015-01-24 20:05:44.977951
# Define __repr__ for objects you write so you and other developers have a reproducible example when
# using it as you develop. Define __str__ when you need a human readable string representation of it.

class Fraction:

    # constructor
    def __init__(self,top,bottom):

        # Ensures Numerator and Denominator are integers
        if not isinstance(top, int):
            raise RuntimeError("Numerator is not an int")
        if not isinstance(bottom, int):
            raise RuntimeError("Denominator is not an int")
        # Ensure negative denominators are handled correctly
        if bottom < 0:
            top = -top
            bottom = -bottom

        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    # override __str__ function (used for print)
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(
      self.__module__, type(self).__name__, hex(id(self)))

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __radd__(self, other_fraction):
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __iadd__(self, other_fraction):
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    # Self check: implement *
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    # Self check: implement /
    def __div__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    # Self check: implement -
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num != second_num

    # Self check: implement <
    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num <= second_num

    # Self check: implement >
    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num

    def show(self):
        print(self.num, "/", self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

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


def main():
    # Fraction Stuff
    # Instance of Fraction class (instance invokes constructor)
    x = Fraction(1,2)
    y = Fraction(2,3)
    z = Fraction(2, -3)
    print (z)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x == y)
    print(x < y)
    print(x > y)

    x += Fraction(1,2)
    print(x)

    print x.__repr__()


if __name__ == '__main__': main()