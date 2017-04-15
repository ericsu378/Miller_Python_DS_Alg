__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 1.13.1. A Fraction Class
# Self Check
# To make sure you understand how operators are implemented in Python classes, and how to properly write methods,
# write some methods to implement *, /, and - . Also implement comparison operators > and <

# Additional Programming Exercises [1.17]
# 1) Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
# 2) In many ways it would be better if all fractions were maintained in lowest terms right from the start.
#    Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately.
#    Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
# 3) Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).
# 4) Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)
# 5) Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator
#    are both integers. If either is not an integer the constructor should raise an exception.
# 6) In the definition of fractions we assumed that negative fractions have a negative numerator and a positive
#    denominator. Using a negative denominator would cause some of the relational operators to give incorrect results.
#    In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative
#    denominator so that all of the operators continue to work properly.
# 7) Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.
# 8) Repeat the last question but this time consider the __iadd__ method.
# 9) Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):

        # Check input type
        if isinstance(top, int):
            self.num = top
        else:
            raise ValueError("ERROR: Top isn't an int!")
        if isinstance(bottom, int):
            self.den = bottom
        else:
            raise ValueError("Error: Bottom isn't an int!")

        # Ensures negative fractions have a negative numerator and positive denominator
        if self.den < 0:
            self.den *= (-1)
            self.num *= (-1)

        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        """
        __repr__ returns the canonical string representation
        With the return value of repr(), it should be possible to recreate our object using eval()
        Provides backup behaviour if __str__ is missing
        In short, str() has a readable output designed for the end user while
                  repr() returns the python code needed to rebuild the object designed for the developer
        Ex.
                import datetime
                now = datetime.datetime.now()
                str(now)
                ‘2015-04-04 20:51:31.766862’
                repr(now)
                ‘datetime.datetime(2015, 4, 4, 20, 51, 31, 766862)’
        """
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return (self.num)

    def getDen(self):
        return (self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        # common = gcd(newnum,newden)
        # return Fraction(newnum//common,newden//common)
        return Fraction(newnum, newden)

    def __radd__(self, otherfraction):
        """
        Reverse Add. Used for times when A+B doesn't work since A doesn't know how to add to B's type,
        By default, when __add__ doesn't work, try __radd__
        """
        return self.__add__(otherfraction)

    def __iadd__(self, otherfraction):
        """
        In-place Add. Function used when you do the following operation: "+="
        Typically used for optimization, but will default to __add__ when __iadd__ isn't available.
        """
        return self.__add__(otherfraction)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum


def run_FractionClass():
    x = Fraction(1, -2) # -3/6
    y = Fraction(2, 3)  # 4/6
    print(x)
    print(y)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x == y)
    print(x < y)
    print(x > y)


def main():
    run_FractionClass()


if __name__ == '__main__':
    main()
