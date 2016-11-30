import random
import fractions


class OneEqn:
    def __init__(self):
        # setup
        bank = set(range(2, 10) + range(-9, -1)) # bank of coefficients

        # Generate problem statement
        ptype = random.randint(1, 3)
        (a, b, c, d) = random.sample(bank, 4)

        self.prefix = '$x=$'
        self.suffix = ''

        if ptype == 4:  # x/a+b=c
            if a > 0:
                self.problem = 'Solve for $x$ in the equation $x/%d+%d=%d$.' % (a, b, c)
            else:
                self.problem = 'Solve for $x$ in the equation $-x/%d+%d=%d$.' % (-a, b, c)
            self.ans = str((c - b) * a)
            self.anstex = "The answer is $%s$." % self.ans

            if b > 0:
                self.hint = 'Subtract $%d$ from both sides then multiply both sides by $%d$.' % (b, a)
            else:
                self.hint = 'Add $%d$ to both sides then multiply both sides by $%d$.' % (-b, a)

        if ptype == 1:  # ax+b=c
            self.problem = 'Solve for $x$ in the equation $%dx+%d=%d$.' % (a, b, c)
            if b > 0:
                self.hint = 'Subtract $%d$ from both sides then divide both sides by $%d$.' % (b, a)
            else:
                self.hint = 'Add $%d$ to both sides then divide both sides by $%d$.' % (-b, a)

        if ptype == 3:  # ax+b=dx+c
            self.problem = 'Solve for $x$ in the equation $%dx+%d=%dx+%d$.' % (a, b, d, c)
            a -= d
            if b > 0 and d > 0:
                s = ['Subtract', 'from', 'subtract', 'from']
            elif b > 0 and d < 0:
                s = ['Subtract', 'from', 'add', 'to']
            elif b < 0 and d > 0:
                s = ['Add', 'to', 'subtract', 'from']
            else:
                s = ['Add', 'to', 'add', 'to']

            self.hint = '%s $%d$ %s both sides, %s $%dx$ %s both sides, then divide both sides by $%d$.' % (
            s[0], abs(b), s[1], s[2], abs(d), s[3], a)

        elif ptype == 2:  # ax+b-c=0
            self.problem = 'Solve for $x$ in the equation $%dx+%d=0$' % (a, b - c)
            if b - c > 0:
                self.hint = 'Subtract $%d$ from both sides then divide both sides by $%d$.' % (b - c, a)
            else:
                self.hint = 'Add $%d$ to both sides then divide both sides by $%d$.' % (c - b, a)

        if ptype == 1 or ptype == 2 or ptype == 3:
            top = c - b
            bot = a

            f = fractions.gcd(top, bot)
            if top > 0 and bot < 0 and f > 0: f *= -1
            topf = top / f
            botf = bot / f

            self.ans = '%d/%d' % (topf, botf)
            if botf == 1:
                self.anstex = 'The answer is $x=%d$.' % (topf)
            else:
                self.anstex = 'The answer is $x=\frac{%d}{%d}$.' % (topf, botf)

        # Clean up the tex
        self.problem = self.problem.replace('+-', '-')
        self.problem = self.problem.replace('1y', 'y')
        self.problem = self.problem.replace('1x', 'x')


class SysEqn:
    def __init__(self, numvar, sub=False):
        # setup
        numcoeff = numvar * numvar
        bank = set(range(2, 10) + range(-9, -1))

        # pick values
        coeffs = random.sample(bank, numcoeff)
        if sub:
            a = random.randrange(numcoeff)
            coeffs[a] = 1 * -1 ** (random.randrange(2))
        xy = random.sample(bank, numvar)

        # Generate problem statement
        if numvar == 2:
            # Check for infinitely many solutions (2D only)
            if coeffs[0] * coeffs[3] == coeffs[1] * coeffs[2] and numvar == 2:  # if discriminate 0
                if coeffs[0] == 1:  # don't change the value that's 1 in case it's substitution
                    coeffs[1] *= 2
                else:
                    coeffs[1] *= 2

            rhs = [xy[0] * coeffs[0] + xy[1] * coeffs[1], xy[0] * coeffs[2] + xy[1] * coeffs[3]]
            self.problem = 'Solve the system of equations $%dx+%dy=%d$ and $%dx+%dy=%d$.  Separate your answer with a comma (e.g. "3,-1").' \
                           % tuple(coeffs[:2] + [rhs[0]] + coeffs[2:] + [rhs[1]])
            self.ans = '<%d,%d>' % tuple(xy)
            self.prefix = '$(x,y)=$'

            # Generate hint (2D)
            if sub:
                if a == 0:
                    self.hint = 'Try using substitution. Solve for x in the first equation and substitute that into the second equation.'
                elif a == 1:
                    self.hint = 'Try using substitution. Solve for y in the first equation and substitute that into the second equation.'
                elif a == 2:
                    self.hint = 'Try using substitution. Solve for x in the second equation and substitute that into the first equation.'
                elif a == 3:
                    self.hint = 'Try using substitution. Solve for y in the second equation and substitute that into the first equation.'
            else:  # elimination
                f = fractions.gcd(coeffs[0], coeffs[2])
                if coeffs[0] < 0 and coeffs[2] > 0 and f < 0:
                    f *= -1
                strstuf = (coeffs[2] / f, -coeffs[0] / f)
                if coeffs[0] == -coeffs[2]:
                    self.hint = 'Try using elimination. Add the two equations together and the $x$s will cancel.'
                elif coeffs[1] == -coeffs[3]:
                    self.hint = 'Try using elimination. Add the two equations together and the $y$s will cancel.'
                else:
                    self.hint = 'Try using elimination.  Multiply the first equation by $%d$ and' \
                                ' the second by $%d$, then add them together.' % strstuf

        else:  # numvar==3
            rhs = [xy[0] * coeffs[0] + xy[1] * coeffs[1] + xy[2] * coeffs[2],
                   xy[0] * coeffs[3] + xy[1] * coeffs[4] + xy[2] * coeffs[5],
                   xy[0] * coeffs[6] + xy[1] * coeffs[7] + xy[2] * coeffs[8]]
            self.problem = 'Solve the system of equations $%dx+%dy+%dz=%d$, $%dx+%dy+%dz=%d$, and $%dx+%dy+%dz=%d$.  ' \
                           'Separate your answer with a comma (e.g. "3,-1,2").' \
                           % tuple(coeffs[:3] + [rhs[0]] + coeffs[3:6] + [rhs[1]] + coeffs[6:] + [rhs[2]])
            self.ans = '<%d,%d,%d>' % tuple(xy)
            self.prefix = '$(x,y,z)=$'
            self.hint = ''

        self.anstex = 'The answer is %s%s$.' % (self.prefix[:-1], self.ans)
        self.suffix = ''

        # Clean up the tex
        self.problem = self.problem.replace('+-', '-')
        self.problem = self.problem.replace('1y', 'y')
        self.problem = self.problem.replace('1x', 'x')
        self.anstex = self.anstex.replace('<', '(')
        self.anstex = self.anstex.replace('>', ')')
