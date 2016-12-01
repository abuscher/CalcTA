# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Austin
#
# Created:     13/01/2014
# Copyright:   (c) Austin 2014
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import sys
import random
from equations import OneEqn, SysEqn
from expressions import Exponents, SimplifyRadicals
from number_theory import LeastCommonMultiple, GreatestCommonFactor, NumberBase

import wp


class Proportion:
    def __init__(self,problem_type):
        self.prefix = ''
        self.suffix = ''
        self.hint = ''

        bank={
            2:[3, 5, 7, 9, 11, 15],
            3:[4, 5, 7, 8, 10],
            4:[3, 5, 7, 9, 11],
            5:[2, 3, 6, 7, 8, 9, 11],
            6:[5, 7, 11, 13],
            7:[2, 3, 5, 8, 9, 10, 11],
            8:[3, 5, 9, 11, 13]
        }

        ratio = sorted(random.sample(xrange(1,10),2))

#        if ratio[1]==1:
#            ratio = [ratio[1],ratio[0]] #smaller proportion first

        if problem_type == 1:
            ratio[0] = 1

        A = random.sample(bank,1)[0]
        B = random.sample(bank[A],1)[0]
        C = A*ratio[1]
        D = B*ratio[1]
        A *= ratio[0]
        B *= ratio[0]
        print problem_type, ratio

        if problem_type == 0:
            ABCorD = random.randrange(4)
            if ABCorD==0:
                self.problem="Find $A$ if $\displaystyle\\frac{A}{%d}\displaystyle\\frac{%d}{%d}$."%(B,C,D)
                self.ans = A
                self.prefix = "$A=$"
                self.suffix = ""
                self.anstex = "The answer is $A=%d$"%A
                self.hint="$A=\displaystyle\\frac{B\cdot C}{D}$."

            elif ABCorD == 1:
                self.problem = "Find $B$ if $\displaystyle\\frac{%d}{B}\displaystyle\\frac{%d}{%d}$." % (A, C, D)
                self.ans = B
                self.prefix = "$B=$"
                self.suffix = ""
                self.anstex = "The answer is $B=%d$" % B
                self.hint = "$B=\displaystyle\\frac{A\cdot D}{C}$."
            elif ABCorD == 2:
                self.problem = "Find $C$ if $\displaystyle\\frac{%d}{%d}\displaystyle\\frac{C}{%d}$." % (A, B, D)
                self.ans = C
                self.prefix = "$C=$"
                self.suffix = ""
                self.anstex = "The answer is $C=%d$" % C
                self.hint = "$C=\displaystyle\\frac{A\cdot D}{B}$."
            else:
                self.problem = "Find $D$ if $\displaystyle\\frac{%d}{%d}\displaystyle\\frac{%d}{D}$." % (A, B, C)
                self.ans = D
                self.prefix = "$D=$"
                self.suffix = ""
                self.anstex = "The answer is $D=%d$" % D
                self.hint = "$D=\displaystyle\\frac{B\cdot C}{A}$."

        elif problem_type == 1:
            type2 = random.randrange(3)
            if type2 == 0:
                self.problem = "The ratio of boys to girls in a class is $%d:%d$.  If there are %d boys, how many girls are in the class?" %(A,B,C)
                self.ans = D
                self.prefix = ""
                self.suffix = "girls"
                self.anstex = "The answer is $%d$ girls." % D
                self.hint = ""
            elif type2 == 1:
                self.problem = "The ratio of boys to girls in a class is $%d:%d$.  If there are %d girls, how many boys are in the class?"%(A,B,D)
                self.ans = C
                self.prefix = ""
                self.suffix = "boys"
                self.anstex = "The answer is $%d$ boys." % C
                self.hint = ""
            else:
                self.problem = "The ratio of boys to girls in a class is $%d:%d$.  If there are %d girls, how many students are in the class?"%(A,B,C)
                self.ans = C+D
                self.prefix = ""
                self.suffix = "students"
                self.anstex = "The answer is $%d$ students." % (C+D)
                self.hint = ""


class Percent:
    def __init__(self,problem_type):
        self.prefix = ''
        self.suffix = ''
        self.hint = ''

        if problem_type<4:
            X = random.randint(1, 99)
            Y = random.randint(1, 99)

            if problem_type>0:
                random_index=random.randint(0,1)
                inc_dec = (-1.,1.)[random_index]
                sign_string = ("-","+")[random_index]
                m = (1.+inc_dec*Y/100.)
                Z = X*m
                if inc_dec>0:
                    up_down = 'increased'
                else:
                    up_down = 'decreased'

        if problem_type == 0:
            #What is X % of Y?
            self.ans = float(X * Y) / 100
            self.problem = "What is $%d\%%$ of $%d$."%(X,Y)
            self.anstex = "The answer is $%s$." % self.ans
            self.hint = 'To find $%d\%%$ of $%d$, multiply $\displaystyle\\frac{%d}{100}\cdot %s$.'%(X,Y,X,Y)

        elif problem_type == 1:
            # When X is decreased/increased by Y percent, the result is ans
            self.problem = "When $%d$ is %s by $%d\%%$, what is the result?"%(X,up_down,Y)
            self.ans = Z
            self.anstex = "The answer is $%s$." % self.ans
            self.hint = "To %s a number by $%d\%%$, you multiply it by $1%s\displaystyle\\frac{%d}{100}=%g$." %(up_down[:-1], Y, sign_string, Y,m)

        elif problem_type == 2:
            # When ans is decreased/increased by Y percent, the result is Z
            self.problem = "When a number $X$ is %s by $%d\%%$, the result is $%g$.  What is the number?" % (up_down, Y, Z)
            self.ans = X
            self.suffix = "$X=$"
            self.anstex = "The answer is $X=%s$." % self.ans
            self.hint = "To %s a number by $%d\%%$, you multiply it by $1%s\displaystyle\\frac{%d}{100}=%g$.\n" \
                        "You just need to solve the equation $%g\cdot X = %g$." % (up_down[:-1], Y, sign_string, Y, m, m, Z)

        """
        elif problem_type == 3:
            # When X is decreased/increased by ans percent, the result is Z
            self.problem = "When $%d$ is %s by $Y$ percent, the result is $%g$.  What was the %s, as a percent?" % (X,up_down, Z, up_down[:-1])
            self.ans = Y
            self.suffix = '$\%$'
            self.suffix = '$Y$'
            self.anstex = "The answer is $%s\%$." % self.ans
            self.hint = "To %s a number by $Y\%%$, you multiply it by $1+\\frac{Y}{100}$. \
                            Set up the equation $%d\cdot\left(1+\\frac{Y}{100}=%d\\right)$ and solve for $Y$. " % (up_down[:-1],X,Z)

        elif problem_type == 4:
            # The number Z is increase/decrease by X%, then increase/decrease by Y%.  What is the result?
            pass
        """


def main():
    options = sys.argv[1]
    if int(options) == 0: options = '1' + options[1:]

    pick = []
    for i in range(len(options)):
        if options[i] == '1':
            pick.append(i)
    type1 = pick[random.randrange(0, len(pick))]

    if type1 == 0:
        a = OneEqn()

    if type1 == 1:  # elimination
        a = SysEqn(2)

    if type1 == 2:  # substitution
        a = SysEqn(2, True)

    if type1 == 3:
        a = SysEqn(3)

    if type1 == 4:
        a = SimplifyRadicals()

    if type1 == 5:
        a = Exponents()

    if type1 == 6:
        if random.randint(0, 1) == 0:
            a = LeastCommonMultiple()
        else:
            a = GreatestCommonFactor()

    if type1 == 7:
        if random.randint(0, 1) == 0:
            a = NumberBase(True)
        else:
            a = NumberBase(False)

    if type1 == 8:
        a = Percent(random.randint(0, 2))

    if type1 == 9:
        a = Proportion(1)

    if type1 == 10:
        a = wp.Counting()

    if type1 == 11:
        a = wp.Algebra()

    print a.problem
    print a.ans
    print a.anstex
    print a.prefix
    print a.suffix
    print a.hint


if __name__ == '__main__':
    main()