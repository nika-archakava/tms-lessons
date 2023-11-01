class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __mul__(self, other) -> 'Rational':
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other) -> 'Rational':
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __add__(self, other) -> 'Rational':
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other) -> 'Rational':
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def normalise(self):
        dels = []
        for i in range(2, min(self.numerator, self.denominator) + 1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                dels.append(i)
        nod = max(dels)
        return Rational(int(self.numerator / nod), int(self.denominator / nod))
