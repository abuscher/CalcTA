# -------------------------------------------------------------------------------
# Name:        poly
# Purpose:
#
# Author:      Austin
#
# Created:     16/06/2013
# Copyright:   (c) Austin 2013
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import random


class poly(object):
    def __init__(self, factors, a):
        self.coeff = [0] * 2 * factors
        bank = {}
        bank[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bank[2] = [1, 3, 5, 7, 9, 11]
        bank[3] = [3, 4, 5, 7, 8]
        bank[4] = [1, 3, 5, 7]
        bank[5] = [1, 2, 3, 4, 6, 7]
        bank[6] = [1, 5, 7]
        bank[7] = [1, 2, 3]
        bank[8] = [1, 3]

        if a == 1:
            for i in range(factors):
                self.coeff[2 * i] = 1
            picks = random.sample(range(len(bank[1])), factors)
            for i in range(factors):
                self.coeff[2 * i + 1] = (-1) ** random.randint(1, 2) * bank[1][picks[i]]
        else:
            # picks=random.sample(range(len(bank.keys())), factors)
            # add negatives
            for i in range(factors):
                if random.randint(1, 3) == 1:
                    lin = 1
                else:
                    lin = (bank.keys()[random.randrange(0, len(bank))])
                self.coeff[2 * i] = lin
                const = (random.randrange(0, len(bank[lin])))
                self.coeff[2 * i + 1] = (-1) ** random.randint(1, 2) * bank[lin][const]
        self.coeff = tuple(self.coeff)

    def make_quad(self):
        if len(self.coeff) == 2:
            (a, b) = self.coeff
            (c, d) = (a, b)
        else:
            (a, b, c, d) = self.coeff
        self.quadratic = (a * c, b * c + a * d, b * d)

    def make_cubic(self):
        if len(self.coeff) == 4:
            (a, b, c, d) = self.coeff
            self.cubic = (a * c, a * d, b * c, b * d)
        else:
            (a, b, c, d, e, f) = self.coeff
            self.cubic = (a * c * e, a * c * f + a * d * e + b * c * e, a * d * f + b * c * f + b * d * e, b * d * f)

    def make_rquad(self):
        (a, b, c, d) = self.coeff
        A = (-1) ** random.randint(1, 2) * random.randint(1, 8)
        B = (-1) ** random.randint(1, 2) * random.randint(1, 8)
        if max(A, B) < 0: A = -A
        e = B * a + A * c
        f = B * b + A * d
        self.rcoeff = (A, a, b, B, c, d, e, f)

    def make_rcubic(self):
        A = (-1) ** random.randint(1, 2) * random.randint(1, 5)
        B = (-1) ** random.randint(1, 2) * random.randint(1, 5)
        C = (-1) ** random.randint(1, 2) * random.randint(1, 4)

        if len(self.coeff) == 4:
            (a, b, c, d) = self.coeff
            e = A * c + a * B
            f = B * b + C * a
            g = A * d + C * b
            self.rcoeff = (A, a, b, B, C, c, d, e, f, g)

        else:
            (a, b, c, d, e, f) = self.coeff
            if a == c and b == d and b + d != 0:
                b = -b
            elif a == c and b == d and b + d == 0:
                b += 1
            if max(A, B, C) < 0:
                A = -A
            g = A * c * e + B * a * e + C * a * c
            h = A * (c * f + d * e) + B * (a * f + b * e) + C * (a * d + b * c)
            i = A * d * f + B * b * f + C * b * d
            self.rcoeff = (A, a, b, B, c, d, C, e, f, g, h, i)


def main():
    """a=poly(2,2)
    print a.coeff
    a.make_quad()
    print a.quadratic

    a.make_cubic()
    print a.cubic

    a=poly(3,1)
    print a.coeff
    a.make_cubic()
    print a.cubic

    #a.make_rquad()
    """
    a = poly(2, 2)
    print a.coeff

    a.make_quad()
    print a.quadratic


if __name__ == '__main__':
    main()