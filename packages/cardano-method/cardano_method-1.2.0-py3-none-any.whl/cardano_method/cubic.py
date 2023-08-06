
from .complex import _Complex

class CubicEquation:
    """Implementation of a modularized CubicEquation class to work with
    """

    __author__ = 'isobarbaric'
    __version_info__ = (1, 2, 0)
    __version__ = '.'.join(str(k) for k in __version_info__)

    def __init__(self, coefficients: list):
        """Constructor

        :param coefficients: the coefficients of a cubic equation
        :type coefficients: list
        """
        # assigning a copy of the cofficients to an attribute
        self.equation = coefficients.copy()

        # reversing the list of coefficients, and assigning a copy of that list to an attribute variable
        coefficients.reverse()
        self.__coefficients = coefficients.copy()

        # declaring and initializing dummy variables for future use
        self.__H, self.__G, self.__shift = None, None, None
        self.answers = None

        # calling the solve() method
        self.__solve()

    @staticmethod
    def depress_cubic(coefficients: list) -> tuple:
        """Depresses a cubic equation in order to subsequently be able to use Cardano's Method

        :param coefficients: the coefficients of a cubic polynomial
        :type coefficients: list
        :return: the coefficients of the depressed polynomial, H-value, G-value, and shift value
        :rtype: tuple
        """
        # determining the shift variable
        shift = coefficients[2]/(3*coefficients[3])

        # determining H and G as per the coefficients of the polynomial
        H = (coefficients[1]-(coefficients[2]*coefficients[2])/(3*coefficients[3]))/3
        G = ((2*(coefficients[2] ** 3))/(27*(coefficients[3] ** 2))) - (coefficients[1]*coefficients[2])/(3*coefficients[3]) + coefficients[0]
        H /= coefficients[3]
        G /= coefficients[3]

        # assigning revised coefficients based on earlier results
        a_3 = 1
        a_2 = 0
        a_1 = (3*H)/coefficients[3]
        a_0 = G/coefficients[3]

        return ([a_0, a_1, a_2, a_3], H, G, shift)

    @staticmethod
    def __quadratic(a: float, b: float, c: float) -> tuple:
        """Determines the roots of a quadratic equation

        :param a: the coefficient of the x^2 term
        :type a: float
        :param b: the coefficient of the x term
        :type b: float
        :param c: the constant term
        :type c: float
        :return: the roots of the given quadratic equation
        :rtype: tuple
        """
        # determining the roots of a quadratic equation given the coefficients a, b, c
        return ((-1*b+(b*b-4*a*c).root())/(2*a), (-1*b-(b*b-4*a*c).root())/(2*a))

    @staticmethod
    def cardano_method(H: float, G: float, shift: float) -> list:
        """Applies Cardano Method to a cubic equation, based on its H, G, and shift values

        :param H: the 'H' value associated with the depressed cubic equation
        :type H: float
        :param G: the 'G' value associated with the depressed cubic equation
        :type G: float
        :param shift: the shift value associated with the depressed cubic equation
        :type shift: float
        :return: the roots of the depressed cubic equation
        :rtype: list
        """
        # finding u, v from Cardano's Method using a call to the static quadratic method
        u, v = CubicEquation.__quadratic(_Complex(1), _Complex(G), _Complex(-(H ** 3)))

        # determining the first partial root
        first = u.root(3)

        # determining the second partial root
        second = _Complex(-H)/u.root(3)

        # getting the values of the two constants omega and omegaSq
        omega, omegaSq = [round(i) for i in CubicEquation.__quadratic(_Complex(1), _Complex(1), _Complex(1))]

        # determining the roots using the constants determined
        withoutShift = [first+second, omega*first+omegaSq*second, omegaSq*first+omega*second]

        # using list-comprehension to perform the necessary shift
        answers = [round(i-_Complex(shift)) for i in withoutShift]

        # cast objects to cmath's complex type
        answers = [complex(num.real, num.imaginary) for num in answers]

        return answers

    def __solve(self) -> list:
        """Solving for the roots of a cubic equation on the current CubicEquation instance
        """
        # depressing the given cubic equation
        self.__coefficients, self.__H, self.__G, self.__shift = CubicEquation.depress_cubic(self.__coefficients)

        # using Cardano's method to get the roots of the cubic equation
        self.answers = CubicEquation.cardano_method(self.__H, self.__G, self.__shift)

    def __repr__(self):
        info = ""

        # adding the coefficient of the x^3 term to the representation
        if (self.equation[0] != 1):
            info += str(self.equation[0])
        info += "x^3 + "

        # adding the coefficient of the x^2 term to the representation
        if (self.equation[1] != 1):
            info += str(self.equation[1])
        info += "x^2 + "

        # adding the coefficient of the x term to the representation
        if (self.equation[2] != 1):
            info += str(self.equation[2])

        # adding the coefficient of the constant term to the representation
        info += "x + " + str(self.equation[3])

        return info
