import random
import fractions


class OneEqn:
    def __init__(self, **kwargs):
        # setup
        bank = set(range(2, 10) + range(-9, -1)) # bank of coefficients

        # Generate problem statement
        if 'ptype' in kwargs:
            ptype = kwargs['ptype']
        else:
            ptype = random.randint(1, 3)

        (a, b, c, d) = random.sample(bank, 4)
        self.coefficients = (a, b, c, d)
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
            d = 0
            self.problem = 'Solve for $x$ in the equation $%dx+%d=%d$.' % (a, b, c)
            if b > 0:
                self.hint = 'Subtract $%d$ from both sides then divide both sides by $%d$.' % (b, a)
            else:
                self.hint = 'Add $%d$ to both sides then divide both sides by $%d$.' % (-b, a)

        if ptype == 3:  # ax+b=dx+c
            self.problem = 'Solve for $x$ in the equation $%dx+%d=%dx+%d$.' % (a, b, d, c)
            #a -= d  #LOOK HERE: this is why d works...not the best way to write tho
            if b > 0 and d > 0:
                s = ['Subtract', 'from', 'subtract', 'from']
            elif b > 0 and d < 0:
                s = ['Subtract', 'from', 'add', 'to']
            elif b < 0 and d > 0:
                s = ['Add', 'to', 'subtract', 'from']
            else:
                s = ['Add', 'to', 'add', 'to']

            self.hint = '%s $%d$ %s both sides, %s $%dx$ %s both sides, then divide both sides by $%d$.' % (
            s[0], abs(b), s[1], s[2], abs(d), s[3], a-d)

        elif ptype == 2:  # ax+b-c=0
            d = 0
            self.problem = 'Solve for $x$ in the equation $%dx+%d=0$' % (a, b - c)
            if b - c > 0:
                self.hint = 'Subtract $%d$ from both sides then divide both sides by $%d$.' % (b - c, a)
            else:
                self.hint = 'Add $%d$ to both sides then divide both sides by $%d$.' % (c - b, a)

        if ptype == 1 or ptype == 2 or ptype == 3:
            top = c - b
            bot = a - d

            f = fractions.gcd(top, bot)
            if top > 0 and bot < 0 and f > 0:
                f *= -1
            topf = top / f
            botf = bot / f

            self.ans = '%d/%d' % (topf, botf)
            if botf == 1:
                self.anstex = 'The answer is $x=%d$.' % (topf)
            else:
                self.anstex = 'The answer is $x=\\frac{%d}{%d}$.' % (topf, botf)

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

class IntersectingLine:
    def __init__(self):
        # ax+b=dx+c
        one_eqn = OneEqn(ptype=3)
        (a,b,c,d) = one_eqn.coefficients
        self.problem = 'Find the $x$-coordinate of the point intersection of the lines ' \
                       '$y=%dx+%d$ and $y=%dx+%d$.' % (a, b, d, c)
        self.ans = one_eqn.ans
        self.anstex = one_eqn.anstex
        self.hint = "Start by setting the right hand sides of each equation equal to each other.  Then, "+one_eqn.hint.lower()
        self.prefix = "$x=$"
        self.suffix = ""


class ArithmeticSeries:
    def __init__(self):
        first_term = random.sample((1, 10)+(-8, -3),1)[0]
        number_of_terms = random.randint(10,20)
        difference = random.sample((1, 5)+(-5, -2),1)[0]
        last_term = first_term + difference*(number_of_terms-1)
        series_sum = (number_of_terms * (first_term + last_term)) // 2
        #print first_term, last_term, difference, number_of_terms, sum

        if first_term + 3 * difference < 0:
            plus_or_minus = "-"
        else:
            plus_or_minus = "+"

        self.problem = "Find the sum $%d+%d+%d%s...%d+%d$." % (first_term, first_term+difference,
                                                               first_term+2*difference, plus_or_minus,
                                                               last_term-difference, last_term)
        self.problem = self.problem.replace("+-","-")

        self.hint = "There are $\displaystyle\\frac{%d-%d}{%d}+1=%d$ terms, the formula for the sum is " \
                    "$%d\cdot \displaystyle\\frac{%d+%d}{2}."\
                    %(last_term, first_term, difference, number_of_terms, number_of_terms, first_term, last_term)
        self.prefix=""
        self.suffix=""
        self.ans=series_sum
        self.anstex = "The sum is %d"%series_sum


class EquationOfLine:
    def __init__(self):

        m_bank = range(-4,0)+range(1,6)
        b_bank = range(-10, 10)
        t_bank = range(-4,6)
        factor_bank = [1,1,1,1,2,3,5,7] # one and primes used on purpose

        m = random.sample(m_bank, 1)[0]
        b = random.sample(b_bank, 1)[0]
        factor = random.sample(factor_bank, 1)[0]
        (x1, x2) = random.sample(t_bank, 2)
        (y1, y2) = [m * x + b for x in (x1, x2)]

        common = fractions.gcd(m,factor)
        m_top = m//common
        m_bottom = factor//common

        if abs(m_top)==1:
            m2 = str(-m_bottom/m_top)
        else:
            if m_top<0:
                m2 = "\displaystyle\\frac{%d}{%d}"%(m_bottom, -m_top)
            else:
                m2 = "\displaystyle\\frac{%d}{%d}" % (-m_bottom, m_top)
                m2 = m2.replace("--","")

        if factor==1:
            [m_tex, b_tex, y1_tex, y2_tex] = [m, b, y1, y2]
        else:
            vals = [m, b, y1, y2]
            vals_tex = [""]*4
            for i, val in enumerate(vals):
                if val % factor == 0:
                    vals[i] = str(val/factor)
                    vals_tex[i] = vals[i]
                else:
                    vals[i] = "%d/%d" % (val, factor)
                    vals_tex[i] = "\displaystyle\\frac{%d}{%d}"%(val, factor)
            [m, b, y1, y2] = vals
            [m_tex, b_tex, y1_tex, y2_tex] = vals_tex
        #print "m", m
        #print "m2", m2
        #print "b", b
        #print "x", x1, x2
        #print "y", y1, y2

        type_bank = [1, 2, 2, 2, 3, 3]
        problem_type = random.sample(type_bank,1)[0]
        #problem_type = 3
        #if problem_type == 4 and factor>1:
        #    problem_type = 2

        if problem_type == 1:
            self.problem = "Find the slope $m$ of the line that passes through the points $\left(%s, %s\\right)$ and " \
                           "$\left(%s, %s\\right)$." % (x1, y1_tex, x2, y2_tex)
            self.ans = m
            self.anstex = "The slope is $m=%s$"%m_tex
            self.prefix = "$m=$"
            self.suffix = ""
            self.hint = "Given points $(x_1, y_1)$ and $(x_2, y_2)$, the slope is " \
                        "$m=\displaystyle\\frac{y_2-y_1}{x_2-x_1}$"

        elif problem_type == 2:
            self.problem = "Find the equation of the line that passes through the points $\left(%s, %s\\right)$ and " \
                           "$\left(%s, %s\\right)$." % (x1, y1_tex, x2, y2_tex)
            self.ans = "%s*x+%s" % (m, b)
            self.anstex = "The equation is $y=%s\cdot x+%s$." % (m_tex, b_tex)
            self.prefix = "$y=$"
            self.suffix = ""
            self.hint = "The equation of a line in slope-intercept form is $y=mx+b$.  First find $m$; given points " \
                        "$(x_1, y_1)$ and $(x_2, y_2)$, the slope is $m=\displaystyle\\frac{y_2-y_1}{x_2-x_1}$. " \
                        "Now to solve for $b$, plug $x_1$, $y_1$, and $m$ into the equation and solve for $b$."

        elif problem_type == 3:
            b2 = random.randint(-10,10)
            self.problem = "Find the equation of the line perpendicular to the line y=%s*x+%s that passed through" \
                           "$\left(%s, %s\\right)$." % (m2, b2, x2, y2_tex)
            self.ans = "%s*x+%s" % (m, b)
            self.anstex = "The equation is $y=%s\cdot x+%s$." % (m_tex, b_tex)
            self.prefix = "$y=$"
            self.suffix = ""
            self.hint = "Given the slope of a line $m_1$, the slope $m_2$ of a perpendicular line is given by " \
                        "$m_2 = - \displaystyle\\frac{1}{m_1}$."
        #else:
        #    self.problem = "Find the $x$-intercept of the line that passes through the points () and ()."  # not great planning to implement unless factor is 1
        #    self.ans
        #    self.anstex
        #    self.prefix
        #    self.suffix = ""

        self.anstex = self.anstex.replace("0*x","")
        self.anstex = self.anstex.replace("=1\cdot x", "=x")
        self.anstex = self.anstex.replace("=-1\cdot x", "=-x")
        self.anstex = self.anstex.replace("+\displaystyle\\frac{-","-\displaystyle\\frac{")
        self.anstex = self.anstex.replace("+0", "")
        self.anstex = self.anstex.replace("+-", "-")
        self.anstex = self.anstex.replace("--", "")


if __name__ == "__main__":
    """
    intersecting_line = IntersectingLine()
    print intersecting_line.problem
    print intersecting_line.anstex
    print intersecting_line.hint

    a_series = ArithmeticSeries()
    print a_series.problem
    print a_series.hint

    decimal_conversion = DecimalConversion()
    print decimal_conversion.problem
    print decimal_conversion.ans
    print decimal_conversion.hint
    print decimal_conversion.anstex
#    a = OneEqn(ptype=3)
    #print a.problem
    #print a.anstex

    a = EquationOfLine()
    print a.problem
    print a.ans
    print a.anstex
    print a.prefix

    import latex
    for a in ["1/5", "5", "(-1)/(5)*x+5/6"]:
        print a, latex.frac(a).replace("*", "\cdot ")
    """