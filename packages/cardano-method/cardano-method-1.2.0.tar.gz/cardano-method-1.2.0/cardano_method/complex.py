
from math import *
from typing import Union

class _Complex:

    def __init__(self, real, imaginary = None):
        # assigning the real part of this complex number to a relevant parameter
        self.real = real

        if imaginary is None:
            # if the parameter for an imaginary number is not provided, then a default value is set
            self.imaginary = 0
        else:
            # if the parameter is given, however, it is to be set accordingly
            self.imaginary = imaginary

        # finding the magnitude of this complex number
        self.absValue = sqrt((self.real ** 2) + (self.imaginary ** 2))

    # supporting the addition operation

    def __add__(self, other):
        # determining the real part of the new complex number
        realPart = self.real + other.real

        # determining the imaginary part of the new complex number
        imaginaryPart = self.imaginary + other.imaginary

        return _Complex(realPart, imaginaryPart)

    # supporting the subtraction operation

    def __sub__(self, other):
        # determining the real part of the new complex number
        realPart = self.real - other.real

        # determining the imaginary part of the new complex number
        imaginaryPart = self.imaginary - other.imaginary

        return _Complex(realPart, imaginaryPart)

    # supporting the multiplication operation (Complex * something)

    def __mul__(self, other: Union[int, float]):
        if isinstance(other, (int, float)):
            # multiplying a complex number with a numerical number (integer or float)

            return _Complex(self.real*other, self.imaginary*other)
        else:
            # multiplying a complex number with another complex number

            # determining the real part of the new complex number
            realPart = self.real*other.real - self.imaginary*other.imaginary

            # determining the imaginary part of the new complex number
            imaginaryPart = self.real*other.imaginary + self.imaginary*other.real

            return _Complex(realPart, imaginaryPart)

    # cont. supporting multiplication operation (something * Complex)

    def __rmul__(self, other: Union[int, float]):
        # calling the other multiplication method to allow multiplication
        return self.__mul__(other)

    # supporting the division operation

    def __truediv__(self, other):
        # determining the numerator of the new complex number
        numerator = self*_Complex(other.real, -1*other.imaginary)

        # determining the denominator of the new complex number
        denominator = (other.real ** 2) + (other.imaginary ** 2)

        return _Complex(numerator.real/denominator, numerator.imaginary/denominator)

    # supporting exponentation

    def __pow__(self, number): # pre-condition number >= 0 
        if number < 0:
            # returning none if the pre-condition is not met
            return None

        if (number == 0):
            # if the exponent is zero, then return the integer 1
            return _Complex(1, 0)
        else:
            # if the exponent is non-zero and > 0, perform exponentiation
            currentNumber = self

            # looping number of times necessary for multiplication
            for _ in range(number-1):
                currentNumber *= self

            return currentNumber

    # math behavior methods

    def __round__(self, numDigits=6):
        # determining the rounded real part of the complex number
        revReal = round(self.real, numDigits)

        # determining the rounded imaginary pary of the complex number
        revImaginary = round(self.imaginary, numDigits)

        return _Complex(revReal, revImaginary)

    def root(self, value=2.0):
        # using DeMoivre's Theorem to compute the 'value-th' root of the Complex number

        # determining a 'k' value as sin x = a/k, cos x = b/k
        k = self.absValue

        if k == 0:
            return _Complex(0, 0)

        # determining the angle associated with the complex number
        x = degrees(acos(self.real/k))

        # since square rots is basically having the angle
        x /= value

        # to get the cube root of the magnitude of the Complex number
        r = k**(1/float(value))

        # determining the real and imaginary parts of the root
        revReal = r*cos(radians(x))
        revImaginary = r*sin(radians(x))

        return _Complex(revReal, revImaginary)

    # class behavior methods

    # supporting the less than operator

    def __lt__(self, other):
        return self.absValue < other.absValue

    # supporting the less than or equal to operator

    def __le__(self, other):
        return self.absValue <= other.absValue

    # supporting the greater than operator

    def __gt__(self, other):
        return self.absValue > other.absValue

    # supporting the greater than or equal to operator

    def __ge__(self, other):
        return self.absValue >= other.absValue

    # supporting the equal to operator

    def __eq__(self, other):
        if self.real != other.real:
            # if the real parts are not equal, then both of the numbers cannot be equal
            return False 

        if self.imaginary != other.imaginary:
            # if the imaginary parts are not equal, then both of the numbers cannot be equal
            return False

        return True

    def __repr__(self):
        # if the imaginary part is zero, then return just the real part of the number
        if self.imaginary == 0:
            return str(self.real)

        # declaring a variable to keep track of the sign to be placed between the real and imaginary
        sign = '+'

        # if the number is negative, then this sign has to be a minus instead of a plus
        if (self.imaginary < 0):
            sign = '-'

        return ("{}" + sign + "{}i").format(self.real, abs(self.imaginary))
