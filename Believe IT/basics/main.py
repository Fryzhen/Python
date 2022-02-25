# -*- coding: utf-8 -*-
import math


class SuperCalculator:

    def __init__(self):
        self.result = 0

    def add(self, *args):
        for i in args:
            self.result += i

    def add_all(self, args):
        for i in args:
            self.result += i

    def minus_all(self, args):
        for i in args:
            self.result -= i

    def minus(self, *args):
        for i in args:
            self.result -= i

    def mult(self, *args):
        for i in args:
            self.result *= i

    def divid(self, *args):
        for i in args:
            self.result /= i

    def power(self, arg):
        self.result = self.result ** arg

    def log(self, arg):
        self.result = math.log(self.result, arg)

    def expo(self):
        self.result = math.exp(self.result)

    def sqrt(self):
        self.result = math.sqrt(self.result)

    def factorial(self):
        self.result = math.factorial(int(self.result))

    def get_result(self):
        return self.result


def main():
    print("_____________/Main\____________")

    c = SuperCalculator()

    #   c.add(0)
    #   c.addAll([0])
    #   c.minus(0)
    #   c.minusAll([0])
    #   c.mult(1)
    #   c.divid(1)
    #   c.power(1)
    #   c.sqrt()
    #   c.factorial()
    #   c.expo()
    #   c.log(1)

    print("c = ", c.get_result())

    letters = {
        'a': 'A',
        'b': 'B',
    }

    letters['c'] = 'C'

    print(letters['a'])

    array = [1, 2, 3]
    array2 = [[1, 2, 3], [1, 2, 3]]


if __name__ == "__main__":
    main()
