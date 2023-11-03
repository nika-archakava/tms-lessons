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
        return f'{self.normalise.__numerator}/{self.normalise.__denominator}'

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

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    @property
    def normalise(self):
        nod = max([i for i in range(2, min(self.__numerator, self.__denominator) + 1) if
                   self.__numerator % i == 0 and self.__denominator % i == 0])
        if self.__denominator >= 0 > self.__numerator or self.__numerator >= 0 > self.__denominator:
            return Rational(int(-abs(self.__numerator / nod)), int(abs(self.__denominator / nod)))
        else:
            return Rational(int(abs(self.__numerator / nod)), int(abs(self.__denominator / nod)))


a = Rational(1, 4)
b = Rational(3, 2)
c = Rational(1, 8)
d = Rational(156, 100)
assert (a * (b + c) + d) == Rational(1573, 800)
print((a * (b + c) + d))
print(Rational(2,4))
