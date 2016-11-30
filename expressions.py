import random


class SimplifyRadicals:
    def __init__(self):
        bank = set([])

        bank.add((343, (7, 7)))
        bank.add((245, (7, 5)))
        bank.add((325, (5, 13)))
        bank.add((275, (5, 11)))
        bank.add((175, (5, 7)))
        bank.add((125, (5, 5)))
        bank.add((363, (11, 3)))
        bank.add((147, (7, 3)))
        bank.add((75, (5, 3)))
        bank.add((375, (5, 15)))
        bank.add((117, (3, 13)))
        bank.add((99, (3, 11)))
        bank.add((63, (3, 7)))
        bank.add((45, (3, 5)))
        bank.add((315, (3, 35)))
        bank.add((27, (3, 3)))
        bank.add((351, (3, 39)))
        bank.add((297, (3, 33)))
        bank.add((189, (3, 21)))
        bank.add((135, (3, 15)))
        bank.add((243, (9, 3)))
        bank.add((338, (13, 2)))
        bank.add((242, (11, 2)))
        bank.add((98, (7, 2)))
        bank.add((50, (5, 2)))
        bank.add((350, (5, 14)))
        bank.add((250, (5, 10)))
        bank.add((294, (7, 6)))
        bank.add((150, (5, 6)))
        bank.add((18, (3, 2)))
        bank.add((306, (3, 34)))
        bank.add((342, (3, 38)))
        bank.add((234, (3, 26)))
        bank.add((198, (3, 22)))
        bank.add((126, (3, 14)))
        bank.add((90, (3, 10)))
        bank.add((54, (3, 6)))
        bank.add((378, (3, 42)))
        bank.add((270, (3, 30)))
        bank.add((162, (9, 2)))
        bank.add((52, (2, 13)))
        bank.add((44, (2, 11)))
        bank.add((28, (2, 7)))
        bank.add((364, (2, 91)))
        bank.add((308, (2, 77)))
        bank.add((20, (2, 5)))
        bank.add((340, (2, 85)))
        bank.add((380, (2, 95)))
        bank.add((260, (2, 65)))
        bank.add((220, (2, 55)))
        bank.add((140, (2, 35)))
        bank.add((12, (2, 3)))
        bank.add((204, (2, 51)))
        bank.add((228, (2, 57)))
        bank.add((276, (2, 69)))
        bank.add((348, (2, 87)))
        bank.add((372, (2, 93)))
        bank.add((156, (2, 39)))
        bank.add((132, (2, 33)))
        bank.add((84, (2, 21)))
        bank.add((60, (2, 15)))
        bank.add((300, (10, 3)))
        bank.add((396, (6, 11)))
        bank.add((252, (6, 7)))
        bank.add((180, (6, 5)))
        bank.add((108, (6, 3)))
        bank.add((8, (2, 2)))
        bank.add((136, (2, 34)))
        bank.add((152, (2, 38)))
        bank.add((184, (2, 46)))
        bank.add((232, (2, 58)))
        bank.add((248, (2, 62)))
        bank.add((296, (2, 74)))
        bank.add((328, (2, 82)))
        bank.add((344, (2, 86)))
        bank.add((376, (2, 94)))
        bank.add((104, (2, 26)))
        bank.add((88, (2, 22)))
        bank.add((56, (2, 14)))
        bank.add((392, (14, 2)))
        bank.add((40, (2, 10)))
        bank.add((280, (2, 70)))
        bank.add((200, (10, 2)))
        bank.add((24, (2, 6)))
        bank.add((312, (2, 78)))
        bank.add((264, (2, 66)))
        bank.add((168, (2, 42)))
        bank.add((120, (2, 30)))
        bank.add((72, (6, 2)))
        bank.add((360, (6, 10)))
        bank.add((216, (6, 6)))
        bank.add((208, (4, 13)))
        bank.add((176, (4, 11)))
        bank.add((112, (4, 7)))
        bank.add((80, (4, 5)))
        bank.add((48, (4, 3)))
        bank.add((336, (4, 21)))
        bank.add((240, (4, 15)))
        bank.add((32, (4, 2)))
        bank.add((352, (4, 22)))
        bank.add((224, (4, 14)))
        bank.add((160, (4, 10)))
        bank.add((96, (4, 6)))
        bank.add((288, (12, 2)))
        bank.add((320, (8, 5)))
        bank.add((192, (8, 3)))
        bank.add((128, (8, 2)))
        bank.add((384, (8, 6)))

        i = random.randrange(len(bank))
        pick = random.sample(bank, 1)[0]
        number = pick[0]
        outside = pick[1][0]
        inside = pick[1][1]
        self.problem = "When simplified, $\\sqrt{" + str(
            number) + "}=a\\sqrt{b}$. What are $a$ and $b$ (separate answer with a comma)?"
        self.ans = "<" + str(pick[1])[1:-1] + ">"
        self.prefix = "$a,b=$"
        self.suffix = ''
        self.hint = '$\\sqrt{%d}=\\sqrt{%d \\cdot %d}$' % (number, inside, outside ** 2)
        self.anstex = self.prefix[:-1] + '(%d, %d)$ because $\\sqrt{%d}$ simplifies to $%d\\sqrt{%d}$.' % (
        outside, inside, number, outside, inside)


class Exponents:
    def __init__(self):
        r = [random.randint(-4, 7) for _ in range(5)]
        i = random.randint(1, 8)
        e = random.sample([-2] * 4 + [2] * 4 + [3] * 2 + [-3] * 2 + [0, 1, 4], 1)[
            0]  # exponent...small possibility of 0,1
        if i == 1:
            ptype = 1
            A = r[0] + r[1]
            problem = "x^{%d}\cdot x^{%d}" % tuple(r[:2])
            self.hint = "Use the multiplication rule $x^a\cdot x^b=x^{a+b}$."
        elif i == 2:
            ptype = 1
            A = r[0] - r[1]
            problem = '\\displaystyle\\frac{x^{%d}}{x^{%d}}' % tuple(r[:2])
            self.hint = "Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$."
        elif i == 3:
            ptype = 1
            A = r[0] * r[1]
            problem = "\left(x^{%d}\\right)^{%d}" % tuple(r[:2])
            self.hint = "Use the power rule $\left(x^a\\right)^b=x^{ab}$."
        elif i == 4:
            ptype = 1
            A = r[0] * r[1] + r[2]
            problem = "\left(x^{%d}\\right)^{%d}\cdot x^{%d}" % tuple(r[:3])
            self.hint = "Use the power rule $\left(x^a\\right)^b=x^{ab}$ and the multiplication rule $x^a\cdot x^b=x^{a+b}$."
        elif i == 5:
            ptype = 1
            A = (r[0] - r[1]) * r[2]
            problem = '\left(\\displaystyle\\frac{x^{%d}}{x^{%d}}\\right)^{%d}' % tuple(r[:3])
            self.hint = "Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$ and the power rule $\left(x^a\\right)^b=x^{ab}$."
        elif i == 6:
            ptype = 2
            A = r[0] * e + r[2]
            B = r[1] * e + r[3]
            problem = "\left(x^{%d}y^{%d}\\right)^{%d}\cdot x^{%d}y^{%d}" % tuple(r[:2] + [e] + r[2:4])
            self.hint = "Use the power rule $\left(x^a\\right)^b=x^{ab}$ and the multiplication rule $x^a\cdot x^b=x^{a+b}$."
        elif i == 7:
            ptype = 2
            A = (r[0] - r[2]) * e
            B = (r[1] - r[3]) * e
            problem = '\left(\\displaystyle\\frac{x^{%d}y^{%d}}{x^{%d}y^{%d}}\\right)^{%d}' % tuple(r[:4] + [e])
            self.hint = "Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$ and the power rule $\left(x^a\\right)^b=x^{ab}$."
        elif i == 8:
            ptype = 3
            A = r[0] - r[3]
            B = r[1] - r[4]
            C = r[2] - e
            problem = '\\displaystyle\\frac{x^{%d}y^{%d}z^{%d}}{x^{%d}y^{%d}z^{%d}}' % tuple(r + [e])
            self.hint = "Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$."

        if ptype == 1:
            self.problem = "Given $%s=x^A$, find $A$." % problem
            self.ans = str(A)
            self.prefix = "$A=$"
            self.suffix = ""
            self.anstex = self.prefix[:-1] + self.ans + "$."
        if ptype == 2:
            self.problem = "Given $%s=x^Ay^B$, find $A,B$.  Express your answer as an ordered pair $A,B$." % problem
            self.ans = str("<%d,%d>" % (A, B))
            self.prefix = "$(A,B)=$"
            self.suffix = ""
            self.anstex = self.prefix[:-1] + "(" + self.ans[1:-1] + ")$."
        if ptype == 3:
            self.problem = "Given $%s=x^Ay^Bz^C$, find $A,B,C$.  Express your answer as an ordered pair $A,B$." % problem
            self.ans = str("<%d,%d,%d>" % (A, B, C))
            self.prefix = "$(A,B,C)=$"
            self.suffix = ""
            self.anstex = self.prefix[:-1] + "(" + self.ans[1:-1] + ")$."
