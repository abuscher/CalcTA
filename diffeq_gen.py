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
import math
from math import *
import re
import latex
from latex import *
import fractions


class SOV:
    def __init__(self):
        bank = {}
        # dy/dx=f(x)
        bank['\ln(x)/x$, $y(1)=1$'] = ['$y(x)=$', '(ln(x)^2)/(2)+1', '']
        bank['\sin(x)$, $y(0)=1$'] = ['$y(x)=$', '2-cos(x)', '']
        bank['\\tan(x)$, $y(0)=1$'] = ['$y(x)=$', '1-ln(cos(x))', 'Use a $u$-substitution with $u=\cos(x)$']
        # bank['\ln(x)$, $y(0)=1$']=['$y(x)=$','','Use integration by parts with $u=\ln(x)$ and $v=1$.']
        bank['x^2+1$, $y(0)=2$'] = ['$y(x)=$', 'x^3/3+x+2', '']
        # dy/dx=f(y), careful....
        bank['y$, $y(0)=1$'] = ['$y(x)=$', 'e^(-x)', '']
        bank['y^2$, $y(2)=1$'] = ['$y(x)=$', '(-1)/(x-3)', '']
        bank['1/y$, $y(0)=1$'] = ['$y(x)=$', '(2*x+1)^(1/2)', '']
        bank['y^2+4$, $y(0)=0$'] = ['$y(x)=$', '2*tan(2*x)', '']

        # dy/dx=f(x) */ f(y)
        bank['\displaystyle\\frac{2x}{y^2+2*y+1}$, $y(0)=1$'] = ['$y(x)=$', '(3*x^2+8)^(1/3)-1', '']
        bank['xy^2+x$, $y(0)=0$'] = ['$y(x)=$', 'tan(x^2/2)', '']
        bank['x/e^y$, $y(1)=0$'] = ['$y(x)=$', 'ln(x^2/2+1/2)', '']
        bank['\sec(x)^2\cdot y^2$, $y(0)=1$'] = ['$y(x)=$', '1/(1-tan(x))', '']
        bank['y^2\cdot e^x$, $y(0)=0$'] = ['$y(x)=$', '(1)/(2-e^x)', '']

        # dy/dx=f(x)/y
        bank['x/y$, $y(1)=2$'] = ['$y(x)=$', '(x^2 + 8 )^(1/2)', '']
        bank['\sin(x)/y$, $y(0)=1$'] = ['$y(x)=$', '(3-2*cos(x))^(1/2)', '']
        # bank['x$, $y(0)=0$']=['$y(x)=$','','']
        # bank['x$, $y(0)=0$']=['$y(x)=$','','']

        # dy/dx=y*f(x)
        bank['xy$, $y(0)=2$'] = ['$y(x)=$', '2*e^(x^2/2)', '']
        bank['xy^2$, $y(0)=1$'] = ['$y(x)=$', '(1)/(1-x^2/2)', '']
        bank['x^2y$, $y(0)=1$'] = ['$y(x)=$', 'e^(x^3/3)', '']
        bank['y/x$, $y(1)=3$'] = ['$y(x)=$', '3*x', '']
        # bank['x$, $y(0)=0$']=['$y(x)=$','','']
        self.problem = random.choice(bank.keys())
        # self.problem='y^2$, $y(2)=1$'
        [self.prefix, self.ans, self.suffix] = bank[self.problem]
        self.problem = 'Solve for $y(x)$ in the equation $\displaystyle\\frac{dy}{dx}=' + self.problem
        self.problem = self.problem.replace('$, $y(', '$, with the boundary condition $y(')
        self.problem += '.'
        # print self.problem,self.ans
        self.anstex = 'The answer is %s $%s$.' % (self.prefix, frac(toTEX(self.ans)))
        # print self.ans
        # print frac(self.ans)
        self.hint = ''


class IntFact:
    def __init__(self):
        bank = {}
        bank['5\, t + 2\, t\, y\!\left(t\right)'] = ['(9*exp(t^2))/2 - 5/2',
                                                     ' $\frac{9\, \mathrm{e}^{t^2}}{2} - \frac{5}{2}$.', '', '', '',
                                                     '2']
        bank['t\, \left(y\!\left(t\right) + 1\right)'] = ['- 3*exp(t^2/2) - 1',
                                                          ' $ - 3\, \mathrm{e}^{\frac{t^2}{2}} - 1$.', '', '', '', '-4']
        bank['2\, t - 32\, t\, y\!\left(t\right)'] = ['1/16 - 49/(16*exp(16*t^2))',
                                                      ' $\frac{1}{16} - \frac{49}{16\, \mathrm{e}^{16\, t^2}}$.', '',
                                                      '', '', '-3']
        bank['- t\, \left(y\!\left(t\right) - 1\right)'] = ['1', ' $1$.', '', '', '', '1']

        bank['- 2\, t\, \left(y\!\left(t\right) - 2\right)'] = ['1/exp(t^2) + 2', ' $\mathrm{e}^{- t^2} + 2$.', '', '',
                                                                '', '3']
        bank['5\, t - 7\, t\, y\!\left(t\right)'] = ['23/(7*exp((7*t^2)/2)) + 5/7',
                                                     ' $\frac{23}{7\, \mathrm{e}^{\frac{7\, t^2}{2}}} + \frac{5}{7}$.',
                                                     '', '', '', '4']
        bank['2\, t - 32\, t\, y\!\left(t\right)'] = ['1/16 - 65/(16*exp(16*t^2))',
                                                      ' $\frac{1}{16} - \frac{65}{16\, \mathrm{e}^{16\, t^2}}$.', '',
                                                      '', '', '-4']
        bank[' - 3\, t - 7\, t\, y\!\left(t\right)'] = ['31/(7*exp((7*t^2)/2)) - 3/7',
                                                        ' $\frac{31}{7\, \mathrm{e}^{\frac{7\, t^2}{2}}} - \frac{3}{7}$.',
                                                        '', '', '', '4']

        bank['t - 4\, t\, y\!\left(t\right)'] = ['1/4 - 9/(4*exp(2*t^2))',
                                                 ' $\frac{1}{4} - \frac{9}{4\, \mathrm{e}^{2\, t^2}}$.', '', '', '',
                                                 '-2']
        bank[' - t - 32\, t\, y\!\left(t\right)'] = ['97/(32*exp(16*t^2)) - 1/32',
                                                     ' $\frac{97}{32\, \mathrm{e}^{16\, t^2}} - \frac{1}{32}$.', '', '',
                                                     '', '3']
        bank['t - 7\, t\, y\!\left(t\right)'] = ['1/7 - 22/(7*exp((7*t^2)/2))',
                                                 ' $\frac{1}{7} - \frac{22}{7\, \mathrm{e}^{\frac{7\, t^2}{2}}}$.', '',
                                                 '', '', '-3']
        bank['- t\, \left(y\!\left(t\right) - 1\right)'] = ['2/exp(t^2/2) + 1',
                                                            ' $\frac{2}{\mathrm{e}^{\frac{t^2}{2}}} + 1$.', '', '', '',
                                                            '3']

        bank['t - 6\, t\, y\!\left(t\right)'] = ['1/6 - 1/(6*exp(3*t^2))',
                                                 ' $\frac{1}{6} - \frac{1}{6\, \mathrm{e}^{3\, t^2}}$.', '', '', '',
                                                 '0']
        bank['t - 7\, t\, y\!\left(t\right)'] = ['27/(7*exp((7*t^2)/2)) + 1/7',
                                                 ' $\frac{27}{7\, \mathrm{e}^{\frac{7\, t^2}{2}}} + \frac{1}{7}$.', '',
                                                 '', '', '4']
        bank['- 4\, t\, \left(y\!\left(t\right) - 1\right)'] = ['1 - 1/exp(2*t^2)', ' $1 - \mathrm{e}^{- 2\, t^2}$.',
                                                                '', '', '', '0']
        bank[' - t - 7\, t\, y\!\left(t\right)'] = ['- 27/(7*exp((7*t^2)/2)) - 1/7',
                                                    ' $ - \frac{27}{7\, \mathrm{e}^{\frac{7\, t^2}{2}}} - \frac{1}{7}$.',
                                                    '', '', '', '-4']

        bank['t^2\, \left(y\!\left(t\right) + 1\right)'] = ['-1', ' $-1$.', '', '', '', '-1']
        bank['t^2 - 32\, t^2\, y\!\left(t\right)'] = ['1/32 - 1/(32*exp((32*t^3)/3))',
                                                      ' $\frac{1}{32} - \frac{1}{32\, \mathrm{e}^{\frac{32\, t^3}{3}}}$.',
                                                      '', '', '', '0']
        bank['- 2\, t^2\, \left(y\!\left(t\right) - 1\right)'] = ['1 - 2/exp((2*t^3)/3)',
                                                                  ' $1 - \frac{2}{\mathrm{e}^{\frac{2\, t^3}{3}}}$.',
                                                                  '', '', '', '-1']
        bank['- t^2\, \left(y\!\left(t\right) + 1\right)'] = ['1/exp(t^3/3) - 1', ' $\mathrm{e}^{-\frac{t^3}{3}} - 1$.',
                                                              '', '', '', '0']

        bank['4\, t^3 - 7\, t^3\, y\!\left(t\right)'] = ['17/(7*exp((7*t^4)/4)) + 4/7',
                                                         ' $\frac{17}{7\, \mathrm{e}^{\frac{7\, t^4}{4}}} + \frac{4}{7}$.',
                                                         '', '', '', '3']
        bank['- t^3\, \left(y\!\left(t\right) - 2\right)'] = ['2 - 1/exp(t^4/4)', ' $2 - \mathrm{e}^{-\frac{t^4}{4}}$.',
                                                              '', '', '', '1']
        bank['5\, t^3 - 4\, t^3\, y\!\left(t\right)'] = ['5/4 - 13/(4*exp(t^4))',
                                                         ' $\frac{5}{4} - \frac{13}{4\, \mathrm{e}^{t^4}}$.', '', '',
                                                         '', '-2']
        bank['2\, t^3\, y\!\left(t\right) + t^3'] = ['- exp(t^4/2)/2 - 1/2',
                                                     ' $ - \frac{\mathrm{e}^{\frac{t^4}{2}}}{2} - \frac{1}{2}$.', '',
                                                     '', '', '-1']

        bank['-\frac{6\, t^{\frac{1}{5}}\, \left(y\!\left(t\right) + 1\right)}{5}'] = ['- 1/exp(t^(6/5)) - 1',
                                                                                       ' $ - \mathrm{e}^{- t^{\frac{6}{5}}} - 1$.',
                                                                                       '', '', '', '-2']
        bank['-\frac{6\, t^{\frac{1}{5}}\, \left(2\, y\!\left(t\right) - 1\right)}{5}'] = ['5/(2*exp(2*t^(6/5))) + 1/2',
                                                                                           ' $\frac{5}{2\, \mathrm{e}^{2\, t^{\frac{6}{5}}}} + \frac{1}{2}$.',
                                                                                           '', '', '', '3']
        bank['\frac{6\, t^{\frac{1}{5}}\, \left(3\, y\!\left(t\right) + 1\right)}{5}'] = [
            '- (5*exp(3*t^(6/5)))/3 - 1/3', ' $ - \frac{5\, \mathrm{e}^{3\, t^{\frac{6}{5}}}}{3} - \frac{1}{3}$.', '',
            '', '', '-2']
        bank['-\frac{6\, t^{\frac{1}{5}}\, \left(4\, y\!\left(t\right) - 1\right)}{5}'] = ['1/4 - 9/(4*exp(4*t^(6/5)))',
                                                                                           ' $\frac{1}{4} - \frac{9}{4\, \mathrm{e}^{4\, t^{\frac{6}{5}}}}$.',
                                                                                           '', '', '', '-2']

        bank['- \sin\!\left(t\right)\, \left(32\, y\!\left(t\right) - 3\right)'] = [
            '(125*exp(32*cos(t)))/(32*exp(32)) + 3/32',
            ' $\frac{125\, \mathrm{e}^{32\, \cos\!\left(t\right)}}{32\, \mathrm{e}^{32}} + \frac{3}{32}$.', '', '', '',
            '4']
        bank['- \sin\!\left(t\right)\, \left(2\, y\!\left(t\right) + 1\right)'] = ['(3*exp(2*cos(t)))/(2*exp(2)) - 1/2',
                                                                                   ' $\frac{3\, \mathrm{e}^{2\, \cos\!\left(t\right)}}{2\, \mathrm{e}^{2}} - \frac{1}{2}$.',
                                                                                   '', '', '', '1']
        bank['- \sin\!\left(t\right)\, \left(4\, y\!\left(t\right) + 3\right)'] = [
            '- (13*exp(4*cos(t)))/(4*exp(4)) - 3/4',
            ' $ - \frac{13\, \mathrm{e}^{4\, \cos\!\left(t\right)}}{4\, \mathrm{e}^{4}} - \frac{3}{4}$.', '', '', '',
            '-4']
        bank['\sin\!\left(t\right)\, \left(3\, y\!\left(t\right) + 1\right)'] = ['- (8*exp(3))/(3*exp(3*cos(t))) - 1/3',
                                                                                 ' $ - \frac{8\, \mathrm{e}^{3}}{3\, \mathrm{e}^{3\, \cos\!\left(t\right)}} - \frac{1}{3}$.',
                                                                                 '', '', '', '-3']

        bank['\cos\!\left(t\right)\, \left(2\, y\!\left(t\right) + 5\right)'] = ['(3*exp(2*sin(t)))/2 - 5/2',
                                                                                 ' $\frac{3\, \mathrm{e}^{2\, \sin\!\left(t\right)}}{2} - \frac{5}{2}$.',
                                                                                 '', '', '', '-1']
        bank['- \cos\!\left(t\right)\, \left(9\, y\!\left(t\right) + 1\right)'] = ['- 26/(9*exp(9*sin(t))) - 1/9',
                                                                                   ' $ - \frac{26}{9\, \mathrm{e}^{9\, \sin\!\left(t\right)}} - \frac{1}{9}$.',
                                                                                   '', '', '', '-3']
        bank['- \cos\!\left(t\right)\, \left(y\!\left(t\right) + 1\right)'] = ['-1', ' $-1$.', '', '', '', '-1']
        bank['- \cos\!\left(t\right)\, \left(y\!\left(t\right) - 1\right)'] = ['1 - 4/exp(sin(t))',
                                                                               ' $1 - \frac{4}{\mathrm{e}^{\sin\!\left(t\right)}}$.',
                                                                               '', '', '', '-3']

        bank['-\frac{32\, y\!\left(t\right) - 1}{{\cos\!\left(t\right)}^2}'] = ['1/32 - 33/(32*exp(32*tan(t)))',
                                                                                ' $\frac{1}{32} - \frac{33}{32\, \mathrm{e}^{32\, \tan\!\left(t\right)}}$.',
                                                                                '', '', '', '-1']
        bank['-\frac{9\, y\!\left(t\right) - 4}{{\cos\!\left(t\right)}^2}'] = ['4/9 - 31/(9*exp(9*tan(t)))',
                                                                               ' $\frac{4}{9} - \frac{31}{9\, \mathrm{e}^{9\, \tan\!\left(t\right)}}$.',
                                                                               '', '', '', '-3']
        bank['\frac{y\!\left(t\right) + 1}{{\cos\!\left(t\right)}^2}'] = ['- 2*exp(tan(t)) - 1',
                                                                          ' $ - 2\, \mathrm{e}^{\tan\!\left(t\right)} - 1$.',
                                                                          '', '', '', '-3']
        bank['-\frac{2\, y\!\left(t\right) + 1}{{\cos\!\left(t\right)}^2}'] = ['- 5/(2*exp(2*tan(t))) - 1/2',
                                                                               ' $ - \frac{5}{2\, \mathrm{e}^{2\, \tan\!\left(t\right)}} - \frac{1}{2}$.',
                                                                               '', '', '', '-3']

        bank['- \mathrm{e}^{t}\, \left(9\, y\!\left(t\right) - 2\right)'] = ['2/9 - (2*exp(9))/(9*exp(9*exp(t)))',
                                                                             ' $\frac{2}{9} - \frac{2\, \mathrm{e}^{9}}{9\, \mathrm{e}^{9\, \mathrm{e}^{t}}}$.',
                                                                             '', '', '', '0']
        bank['- \mathrm{e}^{t}\, \left(4\, y\!\left(t\right) + 1\right)'] = ['(13*exp(4))/(4*exp(4*exp(t))) - 1/4',
                                                                             ' $\frac{13\, \mathrm{e}^{4}}{4\, \mathrm{e}^{4\, \mathrm{e}^{t}}} - \frac{1}{4}$.',
                                                                             '', '', '', '3']
        bank['- \mathrm{e}^{t}\, \left(4\, y\!\left(t\right) - 3\right)'] = ['exp(4)/(4*exp(4*exp(t))) + 3/4',
                                                                             ' $\frac{\mathrm{e}^{4}}{4\, \mathrm{e}^{4\, \mathrm{e}^{t}}} + \frac{3}{4}$.',
                                                                             '', '', '', '1']
        bank['- \mathrm{e}^{t}\, \left(2\, y\!\left(t\right) + 3\right)'] = ['(7*exp(2))/(2*exp(2*exp(t))) - 3/2',
                                                                             ' $\frac{7\, \mathrm{e}^{2}}{2\, \mathrm{e}^{2\, \mathrm{e}^{t}}} - \frac{3}{2}$.',
                                                                             '', '', '', '2']

        i = random.randrange(len(bank))
        p = bank.keys()[i]
        self.problem = "Solve for $y(t)$ given the equation $y'(t) = %s$ with $y(0)=%s$." % (p, bank[p][-1])
        self.ans = bank[p][0]

        if len(bank[p][2]) == 0:
            self.prefix = "$y(t)=$"
        else:
            self.prefix = bank[p][2]
        if len(bank[p][4]) == 0:
            self.hint = "Use integrating factor."
        else:
            self.hint = bank[p][4]
        self.suffix = ""
        self.anstex = "The answer is %s %s" % (self.prefix, bank[p][1])  # p[1] includes $ and .

        self.problem = self.problem.replace('\r', '\\r')
        self.problem = self.problem.replace('\f', '\\f')
        self.problem = self.problem.replace('\frac', '\displaystyle\frac')
        self.anstex = self.anstex.replace('\frac', '\displaystyle\frac')
        self.anstex = self.anstex.replace('\r', '\\r')
        self.anstex = self.anstex.replace('\f', '\\f')


class Exact2:
    def __init__(self):
        bank = {}

        # innocent y
        bank['3\, y + 2\, x\, y + y\'\, x\, \left(x + 3\right)=0$, with $y(1)=1'] = ['4/(x^2 + 3*x)',
                                                                                     ' $\frac{4}{x^2 + 3\, x}$.', '',
                                                                                     '', '']
        bank['y\' + 2\, x=0$, with $y(1)=0'] = ['1 - x^2', ' $1 - x^2$.', '', '', '']
        bank['y\, \cos\!\left(x\right) + y\'\, \sin\!\left(x\right)$, with $ y(\pi)=1'] = ['1/sin(x)',
                                                                                           ' $\frac{1}{\sin\!\left(x\right)}$.',
                                                                                           '', '', '']
        bank['y\'\, \left(x^2 + 4\right) + 2\, x\, y$, with $ y(3)=3'] = ['39/(x^2 + 4)', ' $\frac{39}{x^2 + 4}$.', '',
                                                                          '', '']
        bank['\frac{y}{x} + y\'\, \ln\!\left(x\right)$, with $ y(\mathrm{e})=2'] = ['2/log(x)',
                                                                                    ' $\frac{2}{\ln\!\left(x\right)}$.',
                                                                                    '', '', '']
        bank['y\' + 2\, x\, \mathrm{e}^{x^2}$, with $ y(0)=4'] = ['5 - exp(x^2)', ' $5 - \mathrm{e}^{x^2}$.', '', '',
                                                                  '']

        # sqrt or cube root

        # trig in y

        # exponent/log in y

        i = random.randrange(len(bank))
        p = bank.keys()[i]
        self.problem = "Solve for $y(x)$ given $%s$." % p
        self.ans = bank[p][0]

        if len(bank[p][2]) == 0:
            self.prefix = "$y(x)=$"
        else:
            self.prefix = bank[p][2]
        if len(bank[p][4]) == 0:
            self.hint = "This is an <a target='_blank' href='http://tutorial.math.lamar.edu/Classes/DE/Exact.aspx' >exact</a> equation.  Try to put it in the form $\Psi_x+\Psi_yy'=0$ for unknown function $\Phi(x,y)$."  # add reference
        else:
            self.hint = bank[p][4]
        self.suffix = ""
        self.anstex = "The answer is %s %s" % (self.prefix, bank[p][1])  # p[1] includes $ and .

        self.problem = self.problem.replace('\r', '\\r')
        self.problem = self.problem.replace('\f', '\\f')
        self.anstex = self.anstex.replace('\r', '\\r')
        self.anstex = self.anstex.replace('\f', '\\f')


class Linear2h:
    def __init__(self, ptype):
        bank = {}
        if ptype == 'real':
            bank['y\'\' = 5\, y\''] = ['(3*exp(5*t))/5 - 18/5', ' $\frac{3\, \mathrm{e}^{5\, t}}{5} - \frac{18}{5}$.',
                                       '', '', '', '-3', '3']
            bank['y\'\' = 4\, y\' + 5\, y'] = ['- 19/(6*exp(t)) - (11*exp(5*t))/6',
                                               ' $ - \frac{19}{6\, \mathrm{e}^{t}} - \frac{11\, \mathrm{e}^{5\, t}}{6}$.',
                                               '', '', '', '-5', '-6']
            bank['y\'\' = 3\, y\' + 10\, y'] = ['44/(7*exp(2*t)) + (12*exp(5*t))/7',
                                                ' $\frac{44}{7\, \mathrm{e}^{2\, t}} + \frac{12\, \mathrm{e}^{5\, t}}{7}$.',
                                                '', '', '', '8', '-4']
            bank['y\'\' = 2\, y\' + 15\, y'] = ['1/exp(3*t) + exp(5*t)',
                                                ' $\mathrm{e}^{- 3\, t} + \mathrm{e}^{5\, t}$.', '', '', '', '2', '2']
            bank['y\'\' + 2\, y\' = 35\, y'] = ['(7*exp(5*t))/6 + 11/(6*exp(7*t))',
                                                ' $\frac{7\, \mathrm{e}^{5\, t}}{6} + \frac{11}{6\, \mathrm{e}^{7\, t}}$.',
                                                '', '', '', '3', '-7']
            bank['y\'\' + 12\, y = 7\, y\''] = ['3*exp(3*t) - exp(4*t)',
                                                ' $3\, \mathrm{e}^{3\, t} - \mathrm{e}^{4\, t}$.', '', '', '', '2', '5']
            bank['y\'\' + 4\, y = 5\, y\''] = ['exp(4*t) - 7*exp(t)', ' $\mathrm{e}^{4\, t} - 7\, \mathrm{e}^{t}$.', '',
                                               '', '', '-6', '-3']
            bank['y\'\' = 4\, y\''] = ['6 - exp(4*t)', ' $6 - \mathrm{e}^{4\, t}$.', '', '', '', '5', '-4']
            bank['y\'\' + y\' = 20\, y'] = ['(16*exp(4*t))/3 + 11/(3*exp(5*t))',
                                            ' $\frac{16\, \mathrm{e}^{4\, t}}{3} + \frac{11}{3\, \mathrm{e}^{5\, t}}$.',
                                            '', '', '', '9', '3']
            bank['y\'\' + 18\, y = 9\, y\''] = ['(52*exp(3*t))/3 - (28*exp(6*t))/3',
                                                ' $\frac{52\, \mathrm{e}^{3\, t}}{3} - \frac{28\, \mathrm{e}^{6\, t}}{3}$.',
                                                '', '', '', '8', '-4']
            bank['y\'\' + 6\, y = 5\, y\''] = ['6*exp(2*t) - 6*exp(3*t)',
                                               ' $6\, \mathrm{e}^{2\, t} - 6\, \mathrm{e}^{3\, t}$.', '', '', '', '0',
                                               '-6']
            bank['y\'\' + 3\, y = 4\, y\''] = ['3*exp(3*t) - 12*exp(t)',
                                               ' $3\, \mathrm{e}^{3\, t} - 12\, \mathrm{e}^{t}$.', '', '', '', '-9',
                                               '-3']
            bank['y\'\' = 3\, y\''] = ['(2*exp(3*t))/3 + 13/3', ' $\frac{2\, \mathrm{e}^{3\, t}}{3} + \frac{13}{3}$.',
                                       '', '', '', '5', '2']
            bank['y\'\' = 2\, y\' + 3\, y'] = ['- 15/(4*exp(t)) - (13*exp(3*t))/4',
                                               ' $ - \frac{15}{4\, \mathrm{e}^{t}} - \frac{13\, \mathrm{e}^{3\, t}}{4}$.',
                                               '', '', '', '-7', '-6']
            bank['y\'\' = 9\, y'] = ['- 7/(3*exp(3*t)) - (11*exp(3*t))/3',
                                     ' $ - \frac{7}{3\, \mathrm{e}^{3\, t}} - \frac{11\, \mathrm{e}^{3\, t}}{3}$.', '',
                                     '', '', '-6', '-4']
            bank['y\'\' + 2\, y\' = 15\, y'] = ['(17*exp(3*t))/4 + 11/(4*exp(5*t))',
                                                ' $\frac{17\, \mathrm{e}^{3\, t}}{4} + \frac{11}{4\, \mathrm{e}^{5\, t}}$.',
                                                '', '', '', '7', '-1']
            bank['y\'\' + 4\, y\' = 21\, y'] = ['(23*exp(3*t))/10 + 17/(10*exp(7*t))',
                                                ' $\frac{23\, \mathrm{e}^{3\, t}}{10} + \frac{17}{10\, \mathrm{e}^{7\, t}}$.',
                                                '', '', '', '4', '-5']
            bank['y\'\' + 10\, y = 7\, y\''] = ['(4*exp(5*t))/3 - (13*exp(2*t))/3',
                                                ' $\frac{4\, \mathrm{e}^{5\, t}}{3} - \frac{13\, \mathrm{e}^{2\, t}}{3}$.',
                                                '', '', '', '-3', '-2']
            bank['y\'\' = 2\, y\''] = ['(7*exp(2*t))/2 - 13/2', ' $\frac{7\, \mathrm{e}^{2\, t}}{2} - \frac{13}{2}$.',
                                       '', '', '', '-3', '7']
            bank['y\'\' + y\' = 6\, y'] = ['(7*exp(2*t))/5 + 8/(5*exp(3*t))',
                                           ' $\frac{7\, \mathrm{e}^{2\, t}}{5} + \frac{8}{5\, \mathrm{e}^{3\, t}}$.',
                                           '', '', '', '3', '-2']
            bank['y\'\' + 4\, y\' = 12\, y'] = ['(17*exp(2*t))/8 + 7/(8*exp(6*t))',
                                                ' $\frac{17\, \mathrm{e}^{2\, t}}{8} + \frac{7}{8\, \mathrm{e}^{6\, t}}$.',
                                                '', '', '', '3', '-1']
            bank['y\'\' + 5\, y = 6\, y\''] = ['exp(5*t)/4 - (33*exp(t))/4',
                                               ' $\frac{\mathrm{e}^{5\, t}}{4} - \frac{33\, \mathrm{e}^{t}}{4}$.', '',
                                               '', '', '-8', '-7']
            bank['y\'\' + 3\, y\' = 4\, y'] = ['7/(5*exp(4*t)) + (13*exp(t))/5',
                                               ' $\frac{7}{5\, \mathrm{e}^{4\, t}} + \frac{13\, \mathrm{e}^{t}}{5}$.',
                                               '', '', '', '4', '-3']
            bank['y\'\' + 4\, y\' = 5\, y'] = ['(8*exp(t))/3 - 2/(3*exp(5*t))',
                                               ' $\frac{8\, \mathrm{e}^{t}}{3} - \frac{2}{3\, \mathrm{e}^{5\, t}}$.',
                                               '', '', '', '2', '6']
            bank['y\'\' + 6\, y\' = 7\, y'] = ['(9*exp(t))/8 - 1/(8*exp(7*t))',
                                               ' $\frac{9\, \mathrm{e}^{t}}{8} - \frac{1}{8\, \mathrm{e}^{7\, t}}$.',
                                               '', '', '', '1', '2']
            bank['y\'\' = 4\, y\''] = ['(3*exp(4*t))/2 - 15/2', ' $\frac{3\, \mathrm{e}^{4\, t}}{2} - \frac{15}{2}$.',
                                       '', '', '', '-6', '6']
            bank['y\'\' = 3\, y\''] = ['- (5*exp(3*t))/3 - 22/3',
                                       ' $ - \frac{5\, \mathrm{e}^{3\, t}}{3} - \frac{22}{3}$.', '', '', '', '-9', '-5']
            bank['y\'\' = 2\, y\''] = ['19/2 - (7*exp(2*t))/2', ' $\frac{19}{2} - \frac{7\, \mathrm{e}^{2\, t}}{2}$.',
                                       '', '', '', '6', '-7']
            bank['y\'\' = y\''] = ['4 - 4*exp(t)', ' $4 - 4\, \mathrm{e}^{t}$.', '', '', '', '0', '-4']
            bank['y\'\' + 2\, y\' = 0'] = ['-10', ' $-10$.', '', '', '', '-10', '0']
            bank['y\'\' + 6\, y\' = 0'] = ['2/(3*exp(6*t)) + 1/3', ' $\frac{2}{3\, \mathrm{e}^{6\, t}} + \frac{1}{3}$.',
                                           '', '', '', '1', '-4']
            bank['y\'\' = 5\, y\' + 6\, y'] = ['31/(7*exp(t)) + (4*exp(6*t))/7',
                                               ' $\frac{31}{7\, \mathrm{e}^{t}} + \frac{4\, \mathrm{e}^{6\, t}}{7}$.',
                                               '', '', '', '5', '-1']
            bank['y\'\' = y\' + 2\, y'] = ['- 14/(3*exp(t)) - (7*exp(2*t))/3',
                                           ' $ - \frac{14}{3\, \mathrm{e}^{t}} - \frac{7\, \mathrm{e}^{2\, t}}{3}$.',
                                           '', '', '', '-7', '0']
            bank['y\'\' = y'] = ['3/(2*exp(t)) + exp(t)/2',
                                 ' $\frac{3}{2\, \mathrm{e}^{t}} + \frac{\mathrm{e}^{t}}{2}$.', '', '', '', '2', '-1']
            bank['y\'\' + 4\, y\' + 3\, y = 0'] = ['5/exp(t) - 4/exp(3*t)',
                                                   ' $\frac{5}{\mathrm{e}^{t}} - \frac{4}{\mathrm{e}^{3\, t}}$.', '',
                                                   '', '', '1', '7']
            bank['y\'\' + 6\, y\' + 5\, y = 0'] = ['5/(4*exp(5*t)) - 33/(4*exp(t))',
                                                   ' $\frac{5}{4\, \mathrm{e}^{5\, t}} - \frac{33}{4\, \mathrm{e}^{t}}$.',
                                                   '', '', '', '-7', '2']
            bank['y\'\' = y\' + 6\, y'] = ['- 17/(5*exp(2*t)) - (23*exp(3*t))/5',
                                           ' $ - \frac{17}{5\, \mathrm{e}^{2\, t}} - \frac{23\, \mathrm{e}^{3\, t}}{5}$.',
                                           '', '', '', '-8', '-7']
            bank['y\'\' = 4\, y'] = ['- 19/(4*exp(2*t)) - (5*exp(2*t))/4',
                                     ' $ - \frac{19}{4\, \mathrm{e}^{2\, t}} - \frac{5\, \mathrm{e}^{2\, t}}{4}$.', '',
                                     '', '', '-6', '7']
            bank['y\'\' + 5\, y\' + 6\, y = 0'] = ['17/exp(2*t) - 12/exp(3*t)',
                                                   ' $\frac{17}{\mathrm{e}^{2\, t}} - \frac{12}{\mathrm{e}^{3\, t}}$.',
                                                   '', '', '', '5', '2']
            bank['y\'\' + 7\, y\' + 10\, y = 0'] = ['1/exp(5*t) - 5/exp(2*t)',
                                                    ' $\mathrm{e}^{- 5\, t} - \frac{5}{\mathrm{e}^{2\, t}}$.', '', '',
                                                    '', '-4', '5']
            bank['y\'\' + 9\, y\' + 14\, y = 0'] = ['13/(5*exp(2*t)) - 8/(5*exp(7*t))',
                                                    ' $\frac{13}{5\, \mathrm{e}^{2\, t}} - \frac{8}{5\, \mathrm{e}^{7\, t}}$.',
                                                    '', '', '', '1', '6']
            bank['y\'\' = 2\, y\' + 15\, y'] = ['9/(2*exp(3*t)) + (3*exp(5*t))/2',
                                                ' $\frac{9}{2\, \mathrm{e}^{3\, t}} + \frac{3\, \mathrm{e}^{5\, t}}{2}$.',
                                                '', '', '', '6', '-6']
            bank['y\'\' + 2\, y\' = 3\, y'] = ['- 1/(4*exp(3*t)) - (11*exp(t))/4',
                                               ' $ - \frac{1}{4\, \mathrm{e}^{3\, t}} - \frac{11\, \mathrm{e}^{t}}{4}$.',
                                               '', '', '', '-3', '-2']
            bank['y\'\' + 3\, y\' = 0'] = ['- 1/exp(3*t) - 3', ' $ - \mathrm{e}^{- 3\, t} - 3$.', '', '', '', '-4', '3']
            bank['y\'\' + 4\, y\' + 3\, y = 0'] = ['1/exp(3*t) - 4/exp(t)',
                                                   ' $\mathrm{e}^{- 3\, t} - \frac{4}{\mathrm{e}^{t}}$.', '', '', '',
                                                   '-3', '1']
            bank['y\'\' + 8\, y\' + 15\, y = 0'] = ['17/(2*exp(5*t)) - 27/(2*exp(3*t))',
                                                    ' $\frac{17}{2\, \mathrm{e}^{5\, t}} - \frac{27}{2\, \mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-5', '-2']
            bank['y\'\' + 10\, y\' + 21\, y = 0'] = ['61/(4*exp(3*t)) - 29/(4*exp(7*t))',
                                                     ' $\frac{61}{4\, \mathrm{e}^{3\, t}} - \frac{29}{4\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '8', '5']
            bank['y\'\' + 2\, y\' = 8\, y'] = ['4/(3*exp(4*t)) - exp(2*t)/3',
                                               ' $\frac{4}{3\, \mathrm{e}^{4\, t}} - \frac{\mathrm{e}^{2\, t}}{3}$.',
                                               '', '', '', '1', '-6']
            bank['y\'\' + 7\, y\' + 12\, y = 0'] = ['25/exp(3*t) - 17/exp(4*t)',
                                                    ' $\frac{25}{\mathrm{e}^{3\, t}} - \frac{17}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '8', '-7']
            bank['y\'\' + 11\, y\' + 28\, y = 0'] = ['15/exp(4*t) - 8/exp(7*t)',
                                                     ' $\frac{15}{\mathrm{e}^{4\, t}} - \frac{8}{\mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '7', '-4']
            bank['y\'\' + 4\, y\' = 5\, y'] = ['1/(6*exp(5*t)) - (37*exp(t))/6',
                                               ' $\frac{1}{6\, \mathrm{e}^{5\, t}} - \frac{37\, \mathrm{e}^{t}}{6}$.',
                                               '', '', '', '-6', '-7']
            bank['y\'\' + 6\, y\' + 5\, y = 0'] = ['13/(2*exp(t)) - 5/(2*exp(5*t))',
                                                   ' $\frac{13}{2\, \mathrm{e}^{t}} - \frac{5}{2\, \mathrm{e}^{5\, t}}$.',
                                                   '', '', '', '4', '6']
            bank['y\'\' + 7\, y\' + 10\, y = 0'] = ['23/(3*exp(2*t)) - 5/(3*exp(5*t))',
                                                    ' $\frac{23}{3\, \mathrm{e}^{2\, t}} - \frac{5}{3\, \mathrm{e}^{5\, t}}$.',
                                                    '', '', '', '6', '-7']
            bank['y\'\' + 11\, y\' + 30\, y = 0'] = ['50/exp(6*t) - 59/exp(5*t)',
                                                     ' $\frac{50}{\mathrm{e}^{6\, t}} - \frac{59}{\mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '-9', '-5']
            bank['y\'\' + 12\, y\' + 35\, y = 0'] = ['59/(2*exp(5*t)) - 41/(2*exp(7*t))',
                                                     ' $\frac{59}{2\, \mathrm{e}^{5\, t}} - \frac{41}{2\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '9', '-4']
            bank['y\'\' = 36\, y'] = ['41/(12*exp(6*t)) + (55*exp(6*t))/12',
                                      ' $\frac{41}{12\, \mathrm{e}^{6\, t}} + \frac{55\, \mathrm{e}^{6\, t}}{12}$.', '',
                                      '', '', '8', '7']
            bank['y\'\' + 3\, y\' = 18\, y'] = ['2*exp(3*t) + 1/exp(6*t)',
                                                ' $2\, \mathrm{e}^{3\, t} + \mathrm{e}^{- 6\, t}$.', '', '', '', '3',
                                                '0']
            bank['y\'\' + 4\, y\' = 12\, y'] = ['- (57*exp(2*t))/8 - 23/(8*exp(6*t))',
                                                ' $ - \frac{57\, \mathrm{e}^{2\, t}}{8} - \frac{23}{8\, \mathrm{e}^{6\, t}}$.',
                                                '', '', '', '-10', '3']
            bank['y\'\' + 5\, y\' = 6\, y'] = ['- 1/exp(6*t) - 4*exp(t)',
                                               ' $ - \mathrm{e}^{- 6\, t} - 4\, \mathrm{e}^{t}$.', '', '', '', '-5',
                                               '2']
            bank['y\'\' + 6\, y\' = 0'] = ['- 2/(3*exp(6*t)) - 7/3',
                                           ' $ - \frac{2}{3\, \mathrm{e}^{6\, t}} - \frac{7}{3}$.', '', '', '', '-3',
                                           '4']
            bank['y\'\' + 7\, y\' + 6\, y = 0'] = ['57/(5*exp(t)) - 12/(5*exp(6*t))',
                                                   ' $\frac{57}{5\, \mathrm{e}^{t}} - \frac{12}{5\, \mathrm{e}^{6\, t}}$.',
                                                   '', '', '', '9', '3']
            bank['y\'\' + 3\, y\' = 28\, y'] = ['- (49*exp(4*t))/11 - 39/(11*exp(7*t))',
                                                ' $ - \frac{49\, \mathrm{e}^{4\, t}}{11} - \frac{39}{11\, \mathrm{e}^{7\, t}}$.',
                                                '', '', '', '-8', '7']
            bank['y\'\' + 5\, y\' = 14\, y'] = ['- (40*exp(2*t))/9 - 5/(9*exp(7*t))',
                                                ' $ - \frac{40\, \mathrm{e}^{2\, t}}{9} - \frac{5}{9\, \mathrm{e}^{7\, t}}$.',
                                                '', '', '', '-5', '-5']
            bank['y\'\' + 6\, y\' = 7\, y'] = ['- 5/(4*exp(7*t)) - (31*exp(t))/4',
                                               ' $ - \frac{5}{4\, \mathrm{e}^{7\, t}} - \frac{31\, \mathrm{e}^{t}}{4}$.',
                                               '', '', '', '-9', '1']
            bank['y\'\' + 7\, y\' = 0'] = ['4/(7*exp(7*t)) + 10/7',
                                           ' $\frac{4}{7\, \mathrm{e}^{7\, t}} + \frac{10}{7}$.', '', '', '', '2', '-4']
            bank['y\'\' + 8\, y\' + 7\, y = 0'] = ['8/(3*exp(7*t)) - 38/(3*exp(t))',
                                                   ' $\frac{8}{3\, \mathrm{e}^{7\, t}} - \frac{38}{3\, \mathrm{e}^{t}}$.',
                                                   '', '', '', '-10', '-6']
            bank['y\'\' + 9\, y\' + 14\, y = 0'] = ['52/(5*exp(2*t)) - 17/(5*exp(7*t))',
                                                    ' $\frac{52}{5\, \mathrm{e}^{2\, t}} - \frac{17}{5\, \mathrm{e}^{7\, t}}$.',
                                                    '', '', '', '7', '3']
            bank['y\'\' + 11\, y\' + 28\, y = 0'] = ['12/exp(7*t) - 22/exp(4*t)',
                                                     ' $\frac{12}{\mathrm{e}^{7\, t}} - \frac{22}{\mathrm{e}^{4\, t}}$.',
                                                     '', '', '', '-10', '4']
            bank['y\'\' + 12\, y\' + 35\, y = 0'] = ['31/(2*exp(5*t)) - 23/(2*exp(7*t))',
                                                     ' $\frac{31}{2\, \mathrm{e}^{5\, t}} - \frac{23}{2\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '4', '3']
            bank['y\'\' + 13\, y\' + 42\, y = 0'] = ['56/exp(7*t) - 65/exp(6*t)',
                                                     ' $\frac{56}{\mathrm{e}^{7\, t}} - \frac{65}{\mathrm{e}^{6\, t}}$.',
                                                     '', '', '', '-9', '-2']
            bank['y\'\' + 4\, y\' = 32\, y'] = ['(55*exp(4*t))/12 + 29/(12*exp(8*t))',
                                                ' $\frac{55\, \mathrm{e}^{4\, t}}{12} + \frac{29}{12\, \mathrm{e}^{8\, t}}$.',
                                                '', '', '', '7', '-1']
            bank['y\'\' + 8\, y\' = 0'] = ['7/(8*exp(8*t)) - 15/8',
                                           ' $\frac{7}{8\, \mathrm{e}^{8\, t}} - \frac{15}{8}$.', '', '', '', '-1',
                                           '-7']
            bank['y\'\' + 9\, y\' + 8\, y = 0'] = ['4/(7*exp(8*t)) - 18/(7*exp(t))',
                                                   ' $\frac{4}{7\, \mathrm{e}^{8\, t}} - \frac{18}{7\, \mathrm{e}^{t}}$.',
                                                   '', '', '', '-2', '-2']
            bank['y\'\' + 12\, y\' + 32\, y = 0'] = ['39/(2*exp(4*t)) - 21/(2*exp(8*t))',
                                                     ' $\frac{39}{2\, \mathrm{e}^{4\, t}} - \frac{21}{2\, \mathrm{e}^{8\, t}}$.',
                                                     '', '', '', '9', '6']
            bank['y\'\' + 13\, y\' + 40\, y = 0'] = ['13/(3*exp(8*t)) - 25/(3*exp(5*t))',
                                                     ' $\frac{13}{3\, \mathrm{e}^{8\, t}} - \frac{25}{3\, \mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '-4', '7']
            bank['y\'\' + 14\, y\' + 48\, y = 0'] = ['45/(2*exp(6*t)) - 35/(2*exp(8*t))',
                                                     ' $\frac{45}{2\, \mathrm{e}^{6\, t}} - \frac{35}{2\, \mathrm{e}^{8\, t}}$.',
                                                     '', '', '', '5', '5']
            bank['y\'\' + 3\, y\' = 54\, y'] = ['(43*exp(6*t))/15 + 17/(15*exp(9*t))',
                                                ' $\frac{43\, \mathrm{e}^{6\, t}}{15} + \frac{17}{15\, \mathrm{e}^{9\, t}}$.',
                                                '', '', '', '4', '7']
            bank['y\'\' + 7\, y\' = 18\, y'] = ['- (20*exp(2*t))/11 - 2/(11*exp(9*t))',
                                                ' $ - \frac{20\, \mathrm{e}^{2\, t}}{11} - \frac{2}{11\, \mathrm{e}^{9\, t}}$.',
                                                '', '', '', '-2', '-2']
            bank['y\'\' + 9\, y\' = 0'] = ['2/(3*exp(9*t)) + 22/3',
                                           ' $\frac{2}{3\, \mathrm{e}^{9\, t}} + \frac{22}{3}$.', '', '', '', '8', '-6']
            bank['y\'\' + 10\, y\' + 9\, y = 0'] = ['33/(4*exp(t)) - 5/(4*exp(9*t))',
                                                    ' $\frac{33}{4\, \mathrm{e}^{t}} - \frac{5}{4\, \mathrm{e}^{9\, t}}$.',
                                                    '', '', '', '7', '3']
            bank['y\'\' + 13\, y\' + 36\, y = 0'] = ['19/(5*exp(9*t)) - 49/(5*exp(4*t))',
                                                     ' $\frac{19}{5\, \mathrm{e}^{9\, t}} - \frac{49}{5\, \mathrm{e}^{4\, t}}$.',
                                                     '', '', '', '-6', '5']
            bank['y\'\' + 15\, y\' + 54\, y = 0'] = ['6/exp(6*t) - 4/exp(9*t)',
                                                     ' $\frac{6}{\mathrm{e}^{6\, t}} - \frac{4}{\mathrm{e}^{9\, t}}$.',
                                                     '', '', '', '2', '0']
            bank['y\'\' + 4\, y\' = 60\, y'] = ['- (29*exp(6*t))/16 - 19/(16*exp(10*t))',
                                                ' $ - \frac{29\, \mathrm{e}^{6\, t}}{16} - \frac{19}{16\, \mathrm{e}^{10\, t}}$.',
                                                '', '', '', '-3', '1']
            bank['y\'\' + 17\, y\' + 70\, y = 0'] = ['13/exp(10*t) - 19/exp(7*t)',
                                                     ' $\frac{13}{\mathrm{e}^{10\, t}} - \frac{19}{\mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-6', '3']

        elif ptype == 'repeated':
            bank['y\'\' + 169\, y = 26\, y\''] = ['72*t*exp(13*t) - 5*exp(13*t)',
                                                  ' $72\, t\, \mathrm{e}^{13\, t} - 5\, \mathrm{e}^{13\, t}$.', '', '',
                                                  '', '-5', '7']
            bank['y\'\' + 144\, y = 24\, y\''] = ['113*t*exp(12*t) - 10*exp(12*t)',
                                                  ' $113\, t\, \mathrm{e}^{12\, t} - 10\, \mathrm{e}^{12\, t}$.', '',
                                                  '', '', '-10', '-7']
            bank['y\'\' + 121\, y = 22\, y\''] = ['95*t*exp(11*t) - 9*exp(11*t)',
                                                  ' $95\, t\, \mathrm{e}^{11\, t} - 9\, \mathrm{e}^{11\, t}$.', '', '',
                                                  '', '-9', '-4']
            bank['y\'\' + 100\, y = 20\, y\''] = ['27*t*exp(10*t) - 2*exp(10*t)',
                                                  ' $27\, t\, \mathrm{e}^{10\, t} - 2\, \mathrm{e}^{10\, t}$.', '', '',
                                                  '', '-2', '7']
            bank['y\'\' + 81\, y = 18\, y\''] = ['79*t*exp(9*t) - 9*exp(9*t)',
                                                 ' $79\, t\, \mathrm{e}^{9\, t} - 9\, \mathrm{e}^{9\, t}$.', '', '', '',
                                                 '-9', '-2']
            bank['y\'\' + 64\, y = 16\, y\''] = ['6*exp(8*t) - 41*t*exp(8*t)',
                                                 ' $6\, \mathrm{e}^{8\, t} - 41\, t\, \mathrm{e}^{8\, t}$.', '', '', '',
                                                 '6', '7']
            bank['y\'\' + 49\, y = 14\, y\''] = ['3*exp(7*t) - 19*t*exp(7*t)',
                                                 ' $3\, \mathrm{e}^{7\, t} - 19\, t\, \mathrm{e}^{7\, t}$.', '', '', '',
                                                 '3', '2']
            bank['y\'\' + 36\, y = 12\, y\''] = ['11*t*exp(6*t) - 3*exp(6*t)',
                                                 ' $11\, t\, \mathrm{e}^{6\, t} - 3\, \mathrm{e}^{6\, t}$.', '', '', '',
                                                 '-3', '-7']
            bank['y\'\' + 25\, y = 10\, y\''] = ['3*exp(5*t) - 11*t*exp(5*t)',
                                                 ' $3\, \mathrm{e}^{5\, t} - 11\, t\, \mathrm{e}^{5\, t}$.', '', '', '',
                                                 '3', '4']
            bank['y\'\' + 16\, y = 8\, y\''] = ['31*t*exp(4*t) - 7*exp(4*t)',
                                                ' $31\, t\, \mathrm{e}^{4\, t} - 7\, \mathrm{e}^{4\, t}$.', '', '', '',
                                                '-7', '3']
            bank['y\'\' + 9\, y = 6\, y\''] = ['2*exp(3*t) - 2*t*exp(3*t)',
                                               ' $2\, \mathrm{e}^{3\, t} - 2\, t\, \mathrm{e}^{3\, t}$.', '', '', '',
                                               '2', '4']
            bank['y\'\' + 4\, y = 4\, y\''] = ['6*t*exp(2*t) - 2*exp(2*t)',
                                               ' $6\, t\, \mathrm{e}^{2\, t} - 2\, \mathrm{e}^{2\, t}$.', '', '', '',
                                               '-2', '2']
            bank['y\'\' + y = 2\, y\''] = ['3*t*exp(t) - 7*exp(t)', ' $3\, t\, \mathrm{e}^{t} - 7\, \mathrm{e}^{t}$.',
                                           '', '', '', '-7', '-4']
            bank['y\'\' + 2\, y\' + y = 0'] = ['8/exp(t) + (15*t)/exp(t)',
                                               ' $\frac{8}{\mathrm{e}^{t}} + \frac{15\, t}{\mathrm{e}^{t}}$.', '', '',
                                               '', '8', '7']
            bank['y\'\' + 4\, y\' + 4\, y = 0'] = ['- 7/exp(2*t) - (12*t)/exp(2*t)',
                                                   ' $ - \frac{7}{\mathrm{e}^{2\, t}} - \frac{12\, t}{\mathrm{e}^{2\, t}}$.',
                                                   '', '', '', '-7', '2']
            bank['y\'\' + 6\, y\' + 9\, y = 0'] = ['- 9/exp(3*t) - (34*t)/exp(3*t)',
                                                   ' $ - \frac{9}{\mathrm{e}^{3\, t}} - \frac{34\, t}{\mathrm{e}^{3\, t}}$.',
                                                   '', '', '', '-9', '-7']
            bank['y\'\' + 8\, y\' + 16\, y = 0'] = ['- 5/exp(4*t) - (22*t)/exp(4*t)',
                                                    ' $ - \frac{5}{\mathrm{e}^{4\, t}} - \frac{22\, t}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '-5', '-2']
            bank['y\'\' + 10\, y\' + 25\, y = 0'] = ['3/exp(5*t) + (9*t)/exp(5*t)',
                                                     ' $\frac{3}{\mathrm{e}^{5\, t}} + \frac{9\, t}{\mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '3', '-6']
            bank['y\'\' + 12\, y\' + 36\, y = 0'] = ['- 3/exp(6*t) - (19*t)/exp(6*t)',
                                                     ' $ - \frac{3}{\mathrm{e}^{6\, t}} - \frac{19\, t}{\mathrm{e}^{6\, t}}$.',
                                                     '', '', '', '-3', '-1']
            bank['y\'\' + 14\, y\' + 49\, y = 0'] = ['- 1/exp(7*t) - (7*t)/exp(7*t)',
                                                     ' $ - \mathrm{e}^{- 7\, t} - \frac{7\, t}{\mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-1', '0']
            bank['y\'\' + 16\, y\' + 64\, y = 0'] = ['6/exp(8*t) + (49*t)/exp(8*t)',
                                                     ' $\frac{6}{\mathrm{e}^{8\, t}} + \frac{49\, t}{\mathrm{e}^{8\, t}}$.',
                                                     '', '', '', '6', '1']
            bank['y\'\' + 18\, y\' + 81\, y = 0'] = ['- 6/exp(9*t) - (58*t)/exp(9*t)',
                                                     ' $ - \frac{6}{\mathrm{e}^{9\, t}} - \frac{58\, t}{\mathrm{e}^{9\, t}}$.',
                                                     '', '', '', '-6', '-4']
            bank['y\'\' + 20\, y\' + 100\, y = 0'] = ['- 9/exp(10*t) - (94*t)/exp(10*t)',
                                                      ' $ - \frac{9}{\mathrm{e}^{10\, t}} - \frac{94\, t}{\mathrm{e}^{10\, t}}$.',
                                                      '', '', '', '-9', '-4']
            bank['y\'\' + 22\, y\' + 121\, y = 0'] = ['- 3/exp(11*t) - (29*t)/exp(11*t)',
                                                      ' $ - \frac{3}{\mathrm{e}^{11\, t}} - \frac{29\, t}{\mathrm{e}^{11\, t}}$.',
                                                      '', '', '', '-3', '4']
            bank['y\'\' + 24\, y\' + 144\, y = 0'] = ['- 8/exp(12*t) - (100*t)/exp(12*t)',
                                                      ' $ - \frac{8}{\mathrm{e}^{12\, t}} - \frac{100\, t}{\mathrm{e}^{12\, t}}$.',
                                                      '', '', '', '-8', '-4']
            bank['y\'\' + 26\, y\' + 169\, y = 0'] = ['- 10/exp(13*t) - (132*t)/exp(13*t)',
                                                      ' $ - \frac{10}{\mathrm{e}^{13\, t}} - \frac{132\, t}{\mathrm{e}^{13\, t}}$.',
                                                      '', '', '', '-10', '-2']

        elif ptype == 'complex':
            bank['y\'\' + 41\, y = 10\, y\''] = ['2*sin(4*t)*exp(5*t) - cos(4*t)*exp(5*t)',
                                                 ' $2\, \sin\!\left(4\, t\right)\, \mathrm{e}^{5\, t} - \cos\!\left(4\, t\right)\, \mathrm{e}^{5\, t}$.',
                                                 '', '', '', '-1', '3']
            bank['y\'\' + 41\, y = 10\, y\''] = ['5*cos(4*t)*exp(5*t) - 8*sin(4*t)*exp(5*t)',
                                                 ' $5\, \cos\!\left(4\, t\right)\, \mathrm{e}^{5\, t} - 8\, \sin\!\left(4\, t\right)\, \mathrm{e}^{5\, t}$.',
                                                 '', '', '', '5', '-7']
            bank['y\'\' + 50\, y = 10\, y\''] = ['7*cos(5*t)*exp(5*t) - (29*sin(5*t)*exp(5*t))/5',
                                                 ' $7\, \cos\!\left(5\, t\right)\, \mathrm{e}^{5\, t} - \frac{29\, \sin\!\left(5\, t\right)\, \mathrm{e}^{5\, t}}{5}$.',
                                                 '', '', '', '7', '6']
            bank['y\'\' + 20\, y = 8\, y\''] = ['3*cos(2*t)*exp(4*t) - (17*sin(2*t)*exp(4*t))/2',
                                                ' $3\, \cos\!\left(2\, t\right)\, \mathrm{e}^{4\, t} - \frac{17\, \sin\!\left(2\, t\right)\, \mathrm{e}^{4\, t}}{2}$.',
                                                '', '', '', '3', '-5']
            bank['y\'\' + 17\, y = 8\, y\''] = ['4*exp(4*t)*cos(t) - 16*exp(4*t)*sin(t)',
                                                ' $4\, \mathrm{e}^{4\, t}\, \cos\!\left(t\right) - 16\, \mathrm{e}^{4\, t}\, \sin\!\left(t\right)$.',
                                                '', '', '', '4', '0']
            bank['y\'\' + 34\, y = 6\, y\''] = ['(12*sin(5*t)*exp(3*t))/5 - 3*cos(5*t)*exp(3*t)',
                                                ' $\frac{12\, \sin\!\left(5\, t\right)\, \mathrm{e}^{3\, t}}{5} - 3\, \cos\!\left(5\, t\right)\, \mathrm{e}^{3\, t}$.',
                                                '', '', '', '-3', '3']
            bank['y\'\' + 10\, y = 6\, y\''] = ['6*exp(3*t)*sin(t) - 2*exp(3*t)*cos(t)',
                                                ' $6\, \mathrm{e}^{3\, t}\, \sin\!\left(t\right) - 2\, \mathrm{e}^{3\, t}\, \cos\!\left(t\right)$.',
                                                '', '', '', '-2', '0']
            bank['y\'\' + 25\, y = 6\, y\''] = ['8*cos(4*t)*exp(3*t) - (19*sin(4*t)*exp(3*t))/4',
                                                ' $8\, \cos\!\left(4\, t\right)\, \mathrm{e}^{3\, t} - \frac{19\, \sin\!\left(4\, t\right)\, \mathrm{e}^{3\, t}}{4}$.',
                                                '', '', '', '8', '5']
            bank['y\'\' + 29\, y = 4\, y\''] = ['4*sin(5*t)*exp(2*t) - 8*cos(5*t)*exp(2*t)',
                                                ' $4\, \sin\!\left(5\, t\right)\, \mathrm{e}^{2\, t} - 8\, \cos\!\left(5\, t\right)\, \mathrm{e}^{2\, t}$.',
                                                '', '', '', '-8', '4']
            bank['y\'\' + 53\, y = 4\, y\''] = ['-(3*sin(7*t)*exp(2*t))/7',
                                                ' $-\frac{3\, \sin\!\left(7\, t\right)\, \mathrm{e}^{2\, t}}{7}$.', '',
                                                '', '', '0', '-3']
            bank['y\'\' + 5\, y = 2\, y\''] = ['(11*sin(2*t)*exp(t))/2 - 10*cos(2*t)*exp(t)',
                                               ' $\frac{11\, \sin\!\left(2\, t\right)\, \mathrm{e}^{t}}{2} - 10\, \cos\!\left(2\, t\right)\, \mathrm{e}^{t}$.',
                                               '', '', '', '-10', '1']
            bank['y\'\' + 10\, y = 2\, y\''] = ['(5*sin(3*t)*exp(t))/3 - 3*cos(3*t)*exp(t)',
                                                ' $\frac{5\, \sin\!\left(3\, t\right)\, \mathrm{e}^{t}}{3} - 3\, \cos\!\left(3\, t\right)\, \mathrm{e}^{t}$.',
                                                '', '', '', '-3', '2']
            bank['y\'\' + 26\, y = 2\, y\''] = ['(3*sin(5*t)*exp(t))/5 - 10*cos(5*t)*exp(t)',
                                                ' $\frac{3\, \sin\!\left(5\, t\right)\, \mathrm{e}^{t}}{5} - 10\, \cos\!\left(5\, t\right)\, \mathrm{e}^{t}$.',
                                                '', '', '', '-10', '-7']
            bank['y\'\' + 37\, y = 2\, y\''] = ['cos(6*t)*exp(t) + sin(6*t)*exp(t)',
                                                ' $\cos\!\left(6\, t\right)\, \mathrm{e}^{t} + \sin\!\left(6\, t\right)\, \mathrm{e}^{t}$.',
                                                '', '', '', '1', '7']
            bank['y\'\' + 50\, y = 2\, y\''] = ['sin(7*t)*exp(t) - 4*cos(7*t)*exp(t)',
                                                ' $\sin\!\left(7\, t\right)\, \mathrm{e}^{t} - 4\, \cos\!\left(7\, t\right)\, \mathrm{e}^{t}$.',
                                                '', '', '', '-4', '3']
            bank['y\'\' + 9\, y = 0'] = ['-2*sin(3*t)', ' $- 2\, \sin\!\left(3\, t\right)$.', '', '', '', '0', '-6']
            bank['y\'\' + 49\, y = 0'] = ['5*cos(7*t) + (5*sin(7*t))/7',
                                          ' $5\, \cos\!\left(7\, t\right) + \frac{5\, \sin\!\left(7\, t\right)}{7}$.',
                                          '', '', '', '5', '5']
            bank['y\'\' + 2\, y\' + 37\, y = 0'] = ['(7*cos(6*t))/exp(t) + (2*sin(6*t))/(3*exp(t))',
                                                    ' $\frac{7\, \cos\!\left(6\, t\right)}{\mathrm{e}^{t}} + \frac{2\, \sin\!\left(6\, t\right)}{3\, \mathrm{e}^{t}}$.',
                                                    '', '', '', '7', '-3']
            bank['y\'\' + 2\, y\' + 10\, y = 0'] = ['- (5*cos(3*t))/exp(t) - (10*sin(3*t))/(3*exp(t))',
                                                    ' $ - \frac{5\, \cos\!\left(3\, t\right)}{\mathrm{e}^{t}} - \frac{10\, \sin\!\left(3\, t\right)}{3\, \mathrm{e}^{t}}$.',
                                                    '', '', '', '-5', '-5']
            bank['y\'\' + 2\, y\' + 50\, y = 0'] = ['(3*cos(7*t))/exp(t) - (4*sin(7*t))/(7*exp(t))',
                                                    ' $\frac{3\, \cos\!\left(7\, t\right)}{\mathrm{e}^{t}} - \frac{4\, \sin\!\left(7\, t\right)}{7\, \mathrm{e}^{t}}$.',
                                                    '', '', '', '3', '-7']
            bank['y\'\' + 4\, y\' + 13\, y = 0'] = ['(5*cos(3*t))/exp(2*t) + (10*sin(3*t))/(3*exp(2*t))',
                                                    ' $\frac{5\, \cos\!\left(3\, t\right)}{\mathrm{e}^{2\, t}} + \frac{10\, \sin\!\left(3\, t\right)}{3\, \mathrm{e}^{2\, t}}$.',
                                                    '', '', '', '5', '0']
            bank['y\'\' + 4\, y\' + 8\, y = 0'] = ['(8*cos(2*t))/exp(2*t) + (19*sin(2*t))/(2*exp(2*t))',
                                                   ' $\frac{8\, \cos\!\left(2\, t\right)}{\mathrm{e}^{2\, t}} + \frac{19\, \sin\!\left(2\, t\right)}{2\, \mathrm{e}^{2\, t}}$.',
                                                   '', '', '', '8', '3']
            bank['y\'\' + 4\, y\' + 4\, y = 0'] = ['1/exp(2*t) + (9*t)/exp(2*t)',
                                                   ' $\mathrm{e}^{- 2\, t} + \frac{9\, t}{\mathrm{e}^{2\, t}}$.', '',
                                                   '', '', '1', '7']
            bank['y\'\' + 4\, y\' + 5\, y = 0'] = ['-(7*sin(t))/exp(2*t)',
                                                   ' $-\frac{7\, \sin\!\left(t\right)}{\mathrm{e}^{2\, t}}$.', '', '',
                                                   '', '0', '-7']
            bank['y\'\' + 4\, y\' + 13\, y = 0'] = ['(2*cos(3*t))/exp(2*t) + (4*sin(3*t))/(3*exp(2*t))',
                                                    ' $\frac{2\, \cos\!\left(3\, t\right)}{\mathrm{e}^{2\, t}} + \frac{4\, \sin\!\left(3\, t\right)}{3\, \mathrm{e}^{2\, t}}$.',
                                                    '', '', '', '2', '0']
            bank['y\'\' + 4\, y\' + 53\, y = 0'] = ['(5*cos(7*t))/exp(2*t) + (15*sin(7*t))/(7*exp(2*t))',
                                                    ' $\frac{5\, \cos\!\left(7\, t\right)}{\mathrm{e}^{2\, t}} + \frac{15\, \sin\!\left(7\, t\right)}{7\, \mathrm{e}^{2\, t}}$.',
                                                    '', '', '', '5', '5']
            bank['y\'\' + 6\, y\' + 25\, y = 0'] = ['- (4*cos(4*t))/exp(3*t) - (9*sin(4*t))/(4*exp(3*t))',
                                                    ' $ - \frac{4\, \cos\!\left(4\, t\right)}{\mathrm{e}^{3\, t}} - \frac{9\, \sin\!\left(4\, t\right)}{4\, \mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-4', '3']
            bank['y\'\' + 6\, y\' + 9\, y = 0'] = ['3/exp(3*t) + (5*t)/exp(3*t)',
                                                   ' $\frac{3}{\mathrm{e}^{3\, t}} + \frac{5\, t}{\mathrm{e}^{3\, t}}$.',
                                                   '', '', '', '3', '-4']
            bank['y\'\' + 6\, y\' + 10\, y = 0'] = ['- (8*cos(t))/exp(3*t) - (24*sin(t))/exp(3*t)',
                                                    ' $ - \frac{8\, \cos\!\left(t\right)}{\mathrm{e}^{3\, t}} - \frac{24\, \sin\!\left(t\right)}{\mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-8', '0']
            bank['y\'\' + 6\, y\' + 13\, y = 0'] = ['- (7*cos(2*t))/exp(3*t) - (19*sin(2*t))/(2*exp(3*t))',
                                                    ' $ - \frac{7\, \cos\!\left(2\, t\right)}{\mathrm{e}^{3\, t}} - \frac{19\, \sin\!\left(2\, t\right)}{2\, \mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-7', '2']
            bank['y\'\' + 6\, y\' + 34\, y = 0'] = ['(2*sin(5*t))/(5*exp(3*t)) - cos(5*t)/exp(3*t)',
                                                    ' $\frac{2\, \sin\!\left(5\, t\right)}{5\, \mathrm{e}^{3\, t}} - \frac{\cos\!\left(5\, t\right)}{\mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-1', '5']
            bank['y\'\' + 6\, y\' + 45\, y = 0'] = ['- (5*cos(6*t))/exp(3*t) - (10*sin(6*t))/(3*exp(3*t))',
                                                    ' $ - \frac{5\, \cos\!\left(6\, t\right)}{\mathrm{e}^{3\, t}} - \frac{10\, \sin\!\left(6\, t\right)}{3\, \mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-5', '-5']
            bank['y\'\' + 6\, y\' + 58\, y = 0'] = ['- (8*cos(7*t))/exp(3*t) - (22*sin(7*t))/(7*exp(3*t))',
                                                    ' $ - \frac{8\, \cos\!\left(7\, t\right)}{\mathrm{e}^{3\, t}} - \frac{22\, \sin\!\left(7\, t\right)}{7\, \mathrm{e}^{3\, t}}$.',
                                                    '', '', '', '-8', '2']
            bank['y\'\' + 8\, y\' + 25\, y = 0'] = ['(10*cos(3*t))/exp(4*t) + (11*sin(3*t))/exp(4*t)',
                                                    ' $\frac{10\, \cos\!\left(3\, t\right)}{\mathrm{e}^{4\, t}} + \frac{11\, \sin\!\left(3\, t\right)}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '10', '-7']
            bank['y\'\' + 8\, y\' + 20\, y = 0'] = ['(5*cos(2*t))/exp(4*t) + (17*sin(2*t))/(2*exp(4*t))',
                                                    ' $\frac{5\, \cos\!\left(2\, t\right)}{\mathrm{e}^{4\, t}} + \frac{17\, \sin\!\left(2\, t\right)}{2\, \mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '5', '-3']
            bank['y\'\' + 8\, y\' + 17\, y = 0'] = ['(3*sin(t))/exp(4*t) - cos(t)/exp(4*t)',
                                                    ' $\frac{3\, \sin\!\left(t\right)}{\mathrm{e}^{4\, t}} - \frac{\cos\!\left(t\right)}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '-1', '7']
            bank['y\'\' + 8\, y\' + 16\, y = 0'] = ['- 6/exp(4*t) - (29*t)/exp(4*t)',
                                                    ' $ - \frac{6}{\mathrm{e}^{4\, t}} - \frac{29\, t}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '-6', '-5']
            bank['y\'\' + 8\, y\' + 17\, y = 0'] = ['(3*cos(t))/exp(4*t) + (14*sin(t))/exp(4*t)',
                                                    ' $\frac{3\, \cos\!\left(t\right)}{\mathrm{e}^{4\, t}} + \frac{14\, \sin\!\left(t\right)}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '3', '2']
            bank['y\'\' + 8\, y\' + 20\, y = 0'] = ['- (8*cos(2*t))/exp(4*t) - (17*sin(2*t))/exp(4*t)',
                                                    ' $ - \frac{8\, \cos\!\left(2\, t\right)}{\mathrm{e}^{4\, t}} - \frac{17\, \sin\!\left(2\, t\right)}{\mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '-8', '-2']
            bank['y\'\' + 8\, y\' + 41\, y = 0'] = ['(6*cos(5*t))/exp(4*t) + (19*sin(5*t))/(5*exp(4*t))',
                                                    ' $\frac{6\, \cos\!\left(5\, t\right)}{\mathrm{e}^{4\, t}} + \frac{19\, \sin\!\left(5\, t\right)}{5\, \mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '6', '-5']
            bank['y\'\' + 8\, y\' + 52\, y = 0'] = ['(6*cos(6*t))/exp(4*t) + (19*sin(6*t))/(6*exp(4*t))',
                                                    ' $\frac{6\, \cos\!\left(6\, t\right)}{\mathrm{e}^{4\, t}} + \frac{19\, \sin\!\left(6\, t\right)}{6\, \mathrm{e}^{4\, t}}$.',
                                                    '', '', '', '6', '-5']
            bank['y\'\' + 10\, y\' + 50\, y = 0'] = ['- (7*cos(5*t))/exp(5*t) - (6*sin(5*t))/exp(5*t)',
                                                     ' $ - \frac{7\, \cos\!\left(5\, t\right)}{\mathrm{e}^{5\, t}} - \frac{6\, \sin\!\left(5\, t\right)}{\mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '-7', '5']
            bank['y\'\' + 10\, y\' + 34\, y = 0'] = ['cos(3*t)/exp(5*t) + (8*sin(3*t))/(3*exp(5*t))',
                                                     ' $\frac{\cos\!\left(3\, t\right)}{\mathrm{e}^{5\, t}} + \frac{8\, \sin\!\left(3\, t\right)}{3\, \mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '1', '3']
            bank['y\'\' + 10\, y\' + 26\, y = 0'] = ['(3*cos(t))/exp(5*t) + (17*sin(t))/exp(5*t)',
                                                     ' $\frac{3\, \cos\!\left(t\right)}{\mathrm{e}^{5\, t}} + \frac{17\, \sin\!\left(t\right)}{\mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '3', '2']
            bank['y\'\' + 10\, y\' + 41\, y = 0'] = ['(7*cos(4*t))/exp(5*t) + (19*sin(4*t))/(2*exp(5*t))',
                                                     ' $\frac{7\, \cos\!\left(4\, t\right)}{\mathrm{e}^{5\, t}} + \frac{19\, \sin\!\left(4\, t\right)}{2\, \mathrm{e}^{5\, t}}$.',
                                                     '', '', '', '7', '3']
            bank['y\'\' + 12\, y\' + 61\, y = 0'] = ['- (5*cos(5*t))/exp(6*t) - (29*sin(5*t))/(5*exp(6*t))',
                                                     ' $ - \frac{5\, \cos\!\left(5\, t\right)}{\mathrm{e}^{6\, t}} - \frac{29\, \sin\!\left(5\, t\right)}{5\, \mathrm{e}^{6\, t}}$.',
                                                     '', '', '', '-5', '1']
            bank['y\'\' + 12\, y\' + 45\, y = 0'] = ['(10*cos(3*t))/exp(6*t) + (21*sin(3*t))/exp(6*t)',
                                                     ' $\frac{10\, \cos\!\left(3\, t\right)}{\mathrm{e}^{6\, t}} + \frac{21\, \sin\!\left(3\, t\right)}{\mathrm{e}^{6\, t}}$.',
                                                     '', '', '', '10', '3']
            bank['y\'\' + 12\, y\' + 37\, y = 0'] = ['- (3*cos(t))/exp(6*t) - (17*sin(t))/exp(6*t)',
                                                     ' $ - \frac{3\, \cos\!\left(t\right)}{\mathrm{e}^{6\, t}} - \frac{17\, \sin\!\left(t\right)}{\mathrm{e}^{6\, t}}$.',
                                                     '', '', '', '-3', '1']
            bank['y\'\' + 12\, y\' + 45\, y = 0'] = ['- (9*cos(3*t))/exp(6*t) - (47*sin(3*t))/(3*exp(6*t))',
                                                     ' $ - \frac{9\, \cos\!\left(3\, t\right)}{\mathrm{e}^{6\, t}} - \frac{47\, \sin\!\left(3\, t\right)}{3\, \mathrm{e}^{6\, t}}$.',
                                                     '', '', '', '-9', '7']
            bank['y\'\' + 14\, y\' + 85\, y = 0'] = ['- (3*cos(6*t))/exp(7*t) - (5*sin(6*t))/(2*exp(7*t))',
                                                     ' $ - \frac{3\, \cos\!\left(6\, t\right)}{\mathrm{e}^{7\, t}} - \frac{5\, \sin\!\left(6\, t\right)}{2\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-3', '6']
            bank['y\'\' + 14\, y\' + 65\, y = 0'] = ['- cos(4*t)/exp(7*t) - (3*sin(4*t))/(2*exp(7*t))',
                                                     ' $ - \frac{\cos\!\left(4\, t\right)}{\mathrm{e}^{7\, t}} - \frac{3\, \sin\!\left(4\, t\right)}{2\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-1', '1']
            bank['y\'\' + 14\, y\' + 50\, y = 0'] = ['- (8*cos(t))/exp(7*t) - (58*sin(t))/exp(7*t)',
                                                     ' $ - \frac{8\, \cos\!\left(t\right)}{\mathrm{e}^{7\, t}} - \frac{58\, \sin\!\left(t\right)}{\mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-8', '-2']
            bank['y\'\' + 14\, y\' + 53\, y = 0'] = ['- (5*cos(2*t))/exp(7*t) - (39*sin(2*t))/(2*exp(7*t))',
                                                     ' $ - \frac{5\, \cos\!\left(2\, t\right)}{\mathrm{e}^{7\, t}} - \frac{39\, \sin\!\left(2\, t\right)}{2\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-5', '-4']
            bank['y\'\' + 14\, y\' + 58\, y = 0'] = ['- (8*cos(3*t))/exp(7*t) - (18*sin(3*t))/exp(7*t)',
                                                     ' $ - \frac{8\, \cos\!\left(3\, t\right)}{\mathrm{e}^{7\, t}} - \frac{18\, \sin\!\left(3\, t\right)}{\mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '-8', '2']
            bank['y\'\' + 14\, y\' + 85\, y = 0'] = ['(4*cos(6*t))/exp(7*t) + (31*sin(6*t))/(6*exp(7*t))',
                                                     ' $\frac{4\, \cos\!\left(6\, t\right)}{\mathrm{e}^{7\, t}} + \frac{31\, \sin\!\left(6\, t\right)}{6\, \mathrm{e}^{7\, t}}$.',
                                                     '', '', '', '4', '3']
            bank['y\'\' + 16\, y\' + 100\, y = 0'] = ['- (2*cos(6*t))/exp(8*t) - (11*sin(6*t))/(3*exp(8*t))',
                                                      ' $ - \frac{2\, \cos\!\left(6\, t\right)}{\mathrm{e}^{8\, t}} - \frac{11\, \sin\!\left(6\, t\right)}{3\, \mathrm{e}^{8\, t}}$.',
                                                      '', '', '', '-2', '-6']
            bank['y\'\' + 16\, y\' + 68\, y = 0'] = ['- (4*cos(2*t))/exp(8*t) - (27*sin(2*t))/(2*exp(8*t))',
                                                     ' $ - \frac{4\, \cos\!\left(2\, t\right)}{\mathrm{e}^{8\, t}} - \frac{27\, \sin\!\left(2\, t\right)}{2\, \mathrm{e}^{8\, t}}$.',
                                                     '', '', '', '-4', '5']
            bank['y\'\' + 16\, y\' + 89\, y = 0'] = ['- cos(5*t)/exp(8*t) - (4*sin(5*t))/(5*exp(8*t))',
                                                     ' $ - \frac{\cos\!\left(5\, t\right)}{\mathrm{e}^{8\, t}} - \frac{4\, \sin\!\left(5\, t\right)}{5\, \mathrm{e}^{8\, t}}$.',
                                                     '', '', '', '-1', '4']
            bank['y\'\' + 18\, y\' + 117\, y = 0'] = ['(3*cos(6*t))/exp(9*t) + (11*sin(6*t))/(3*exp(9*t))',
                                                      ' $\frac{3\, \cos\!\left(6\, t\right)}{\mathrm{e}^{9\, t}} + \frac{11\, \sin\!\left(6\, t\right)}{3\, \mathrm{e}^{9\, t}}$.',
                                                      '', '', '', '3', '-5']
            bank['y\'\' + 18\, y\' + 97\, y = 0'] = ['(3*cos(4*t))/exp(9*t) + (5*sin(4*t))/exp(9*t)',
                                                     ' $\frac{3\, \cos\!\left(4\, t\right)}{\mathrm{e}^{9\, t}} + \frac{5\, \sin\!\left(4\, t\right)}{\mathrm{e}^{9\, t}}$.',
                                                     '', '', '', '3', '-7']
            bank['y\'\' + 18\, y\' + 90\, y = 0'] = ['- (5*cos(3*t))/exp(9*t) - (52*sin(3*t))/(3*exp(9*t))',
                                                     ' $ - \frac{5\, \cos\!\left(3\, t\right)}{\mathrm{e}^{9\, t}} - \frac{52\, \sin\!\left(3\, t\right)}{3\, \mathrm{e}^{9\, t}}$.',
                                                     '', '', '', '-5', '-7']
            bank['y\'\' + 18\, y\' + 85\, y = 0'] = ['- (6*cos(2*t))/exp(9*t) - (57*sin(2*t))/(2*exp(9*t))',
                                                     ' $ - \frac{6\, \cos\!\left(2\, t\right)}{\mathrm{e}^{9\, t}} - \frac{57\, \sin\!\left(2\, t\right)}{2\, \mathrm{e}^{9\, t}}$.',
                                                     '', '', '', '-6', '-3']
            bank['y\'\' + 20\, y\' + 125\, y = 0'] = ['(4*cos(5*t))/exp(10*t) + (46*sin(5*t))/(5*exp(10*t))',
                                                      ' $\frac{4\, \cos\!\left(5\, t\right)}{\mathrm{e}^{10\, t}} + \frac{46\, \sin\!\left(5\, t\right)}{5\, \mathrm{e}^{10\, t}}$.',
                                                      '', '', '', '4', '6']
            bank['y\'\' + 20\, y\' + 116\, y = 0'] = ['- (4*cos(4*t))/exp(10*t) - (17*sin(4*t))/(2*exp(10*t))',
                                                      ' $ - \frac{4\, \cos\!\left(4\, t\right)}{\mathrm{e}^{10\, t}} - \frac{17\, \sin\!\left(4\, t\right)}{2\, \mathrm{e}^{10\, t}}$.',
                                                      '', '', '', '-4', '6']
            bank['y\'\' + 20\, y\' + 109\, y = 0'] = ['sin(3*t)/exp(10*t)',
                                                      ' $\frac{\sin\!\left(3\, t\right)}{\mathrm{e}^{10\, t}}$.', '',
                                                      '', '', '0', '3']
            bank['y\'\' + 20\, y\' + 116\, y = 0'] = ['- cos(4*t)/exp(10*t) - (5*sin(4*t))/(2*exp(10*t))',
                                                      ' $ - \frac{\cos\!\left(4\, t\right)}{\mathrm{e}^{10\, t}} - \frac{5\, \sin\!\left(4\, t\right)}{2\, \mathrm{e}^{10\, t}}$.',
                                                      '', '', '', '-1', '0']
            bank['y\'\' + 20\, y\' + 125\, y = 0'] = ['- (8*cos(5*t))/exp(10*t) - (76*sin(5*t))/(5*exp(10*t))',
                                                      ' $ - \frac{8\, \cos\!\left(5\, t\right)}{\mathrm{e}^{10\, t}} - \frac{76\, \sin\!\left(5\, t\right)}{5\, \mathrm{e}^{10\, t}}$.',
                                                      '', '', '', '-8', '4']

        i = random.randrange(len(bank))
        p = bank.keys()[i]
        y0 = bank[p][-2]
        Dy0 = bank[p][-1]
        self.problem = "Solve for $y(x)$ given $%s$ with initial conditions $y(0)=%s$ and $y'(0)=%s$." % (p, y0, Dy0)
        self.ans = bank[p][0]

        if len(bank[p][2]) == 0:
            self.prefix = "$y(x)=$"
        else:
            self.prefix = bank[p][2]
        if len(bank[p][4]) == 0:
            self.hint = ''  # "This is an \"exact\" equation." #add reference
        else:
            self.hint = bank[p][4]
        self.suffix = ""
        self.anstex = "The answer is %s %s" % (self.prefix, bank[p][1])  # p[1] includes $ and .

        self.problem = self.problem.replace('\r', '\\r')
        self.problem = self.problem.replace('\f', '\\f')
        self.anstex = self.anstex.replace('\frac', '\displaystyle\frac')
        self.anstex = self.anstex.replace('\r', '\\r')
        self.anstex = self.anstex.replace('\f', '\\f')


def main():
    options = sys.argv[1]
    # options='100000'
    if int(options) == 0: options = '1' + options[1:]

    pick = []
    for i in range(len(options)):
        if options[i] == '1': pick.append(i)
    type1 = pick[random.randrange(0, len(pick))]

    if type1 == 0:
        a = SOV()
    if type1 == 1:
        a = IntFact()
    if type1 == 2:
        a = Exact2()

    if type1 == 3:
        a = Linear2h('real')
    if type1 == 4:
        a = Linear2h('repeated')
    if type1 == 5:
        a = Linear2h('complex')

    print a.problem
    print a.ans
    print a.anstex
    print a.prefix
    print a.suffix
    print a.hint


if __name__ == '__main__':
    main()


    ##class Particular:
    ##  def __init__(self):
    ##    pass
    ##
    ##class System2:
    ##  def __init__(self):
    ##    pass
