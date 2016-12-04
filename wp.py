import random

class Algebra:
    def __init__(self):
        bank = set([])

        # Pigs and Chickens/Nickels and Dimes/Bake sale
        bank.add(('John has a farm with pigs and chickens. If he looks out and counts 34 heads and 72 tails, '
                  'how many pigs does he have?',
                 2, '', 'pigs', ''))
        bank.add(('John has a farm with pigs and chickens. If he looks out and counts 16 heads and 40 tails, '
                  'how many chickens does he have?',
                 12, '', 'chickens', ''))
        bank.add(('John has a farm with pigs and chickens. If he looks out and counts 87 heads and 252 tails, '
                 'how many pigs does he have?',
                 39, '', 'pigs', ''))
        bank.add(('John has a farm with pigs and chickens. If he looks out and counts 54 heads and 150 tails, '
                  'how many chickens does he have?',
                 33, '', 'chickens', ''))

        bank.add(('Alicia has 23 coins, all nickels or dimes, totaling to $\$1.75$.  How many dimes does she have? 12 '
                  'dimes', 12, '', 'dimes', ''))
        bank.add(('Alicia has 14 coins, all nickels or quarters totaling to $\$2.70$.  How many nickels does she have?',
                  4, '', 'dimes', ''))

        bank.add(('Super Taxi charges $2.40 plus $1.05 per mile and Awesome Cab charges $3.65 plus $1.00 per mile.  '
                  'How many miles do you have to drive for Super Taxi to be 50 cents cheaper than Awesome Cab?',
                  15, '', 'miles', ''))

        # mixing/percentage
        bank.add(('13% of a number is 45, what is 39% of that same number?', 135, '', '', ''))
        bank.add(('I have a $20$ oz jar containing a solution of $30\%$ acid and a 12 oz jar containing a solution of '
                  '$10\%$ acid.  I pour them both into a 40 oz jar, then top it off with acid.  What percentage of '
                  'the $40$ oz jar is filled with acid?', 38, '', '$\%$', ''))

        # age
        bank.add(('The sum of the ages of Billy\'s seven children is 34.  '
                  'What will the sum of their ages be in 10 years?',
                  104, '', 'years', ''))
        bank.add(('Ken is two years older than Eric.  Half of Eric\'s age minus 3 is equal to one third Ken\'s age.  '
                  'How old is Ken?',
                  24, '', 'years old', ''))

        # rate and time
        # paint a fence
        bank.add(('John can paint a fence alone in 3 hours.  Alex can paint a fence alone in 2 hours.  '
                  'How many minutes will it take working together?', 72, '', 'minutes', ''))
        bank.add(('Paul can paint a fence alone in 12 hours.  If he works with Jed, they can complete it in 3 hours.  '
                  'How long will it take Jed working alone?', 4, '', 'hours', ''))
        bank.add(('Three workers of equal skill can complete a fence in 2 hours.  After an hour of work, one of the '
                  'workers leaves.  How much additional time (in minutes) is required to finish the fence? ',
                  90, '', 'minutes', ''))

        # faucets
        bank.add(('A bathtub has three faucets - A, B and C - which can fill the tub alone in 1,3, and 6 hours '
                  'respectively.  If all 3 faucets are on, how many minutes will it take to fill the tub?',
                  40, '', 'minutes', ''))

        # driving
        bank.add(('John drives 252 miles to LA in 5 hours and 298 miles back in 6.  What is his average speed '
                  'for the entire trip?', 50, '', 'mph', ''))
        bank.add(('John drives to LA at a speed of 56 mph and back at a speed of 42 mph, what is his average speed?',
                  48, '', 'mph', ''))

        # Add them together
        bank.add(('Given the system $x+y=6$, $y+z=5$, and $x+z=79$, find $x+y+z$.', 24, '$x+y+z=$',
                  '', 'Add all three equations together.'))
        bank.add(('Given the system $a+b=-4$, $b+c=2$, and $a+c=-34$, find $a+b+c$.', -8, '$a+b+c=$',
                  '', 'Add all three equations together.'))
        bank.add(('Given the system $2x+5y=6$, $-2y+z=5$, $-w+2z=2$, and $x+4w=2$, find $x+y+z+w$.', 5, '$x+y+z+w=$',
                  '', 'Add all four equations together.'))

        bank.add(('Given the system $7x+2y=2$, $4y+7z=15$, and $x+y+z=3$, find $y$.', 24, '$y=$',
                  '', 'Add the first two equations together.'))
        # bank.add(('Given the system $x+y=6$, $y+z=5$, and $x+z=79$, find $x+y+z$.',24,'$x+y+z=$','Add all three equations together.'))

        # square it
        bank.add(('Given the system $x+\frac{1}{x}=3$, find $x^2+\frac{1}{x^2}$.', 7, '$x^2+\frac{1}{x^2}=$',
                  '', 'Square the equation and simplify.'))
        bank.add(('Given $x+1/x=5$, find $x^2+1/x^2$.', 23, '$x^2+1/x^2=$', '', 'Square both sides of the given equation.'))
        bank.add(('Given $x-6/x=0$, find $x^2$.', 6, '$x^2=$', '', 'Multiply both sides by $x$.'))

        bank.add(('Given $x+y=6$ and $xy=3$, find $x^2+y^2$.', 30, '$x^2+y^2=$', '', 'Square the first equation.'))
        bank.add(('Given $x+y=-3$ and $xy=2$, find $x^2+y^2$.', 5, '$x^2+y^2=$', '', 'Square the first equation.'))

        i = random.randrange(len(bank))
        pick = random.sample(bank, 1)[0]
        self.problem = pick[0]
        self.ans = pick[1]
        self.prefix = pick[2]

        self.suffix = pick[3]
        if len(pick) > 4:
            self.hint = pick[4]
        else:
            self.hint = ""

        self.anstex = "The answer is %s$%s$ %s." % (self.prefix, pick[1], self.suffix)  # p[1] includes $ and .

        self.anstex = self.anstex.replace('$$', '')
        self.anstex = self.anstex.replace('$ $', '')
        self.anstex = self.anstex.replace(' .', '.')

class Counting:
    def __init__(self):
        bank = set([])

        # coins
        bank.add(('If I flip 2 coins, how many different ways can they land?', 4, '',
                  'If I flip $n$ coins, they can land $2^n$ different ways.'))
        bank.add(('If I flip 3 coins, how many different ways can they land?', 8, '',
                  'If I flip $n$ coins, they can land $2^n$ different ways.'))
        bank.add(('If I flip 4 coins, how many different ways can they land?', 16, '',
                  'If I flip $n$ coins, they can land $2^n$ different ways.'))
        bank.add(('If I flip 5 coins, how many different ways can they land?', 32, '',
                  'If I flip $n$ coins, they can land $2^n$ different ways.'))
        bank.add(('If I flip 6 coins, how many different ways can they land?', 64, '',
                  'If I flip $n$ coins, they can land $2^n$ different ways.'))
        bank.add(('If I flip 8 coins, how many different ways can they land?', 256, '',
                  'If I flip $n$ coins, they can land $2^n$ different ways.'))

        bank.add(('If I flip 3 coins, how many ways can exactly 1 land heads?', 3, '',
                  'This is equivalent to the letter arrangement problem HTT which has answer $\\frac{3!}{2!}$.'))
        bank.add(('If I flip 3 coins, how many ways can exactly 2 land heads?', 3, '',
                  'This is equivalent to the letter arrangement problem HHT which has answer $\\frac{3!}{2!}$.'))
        bank.add(('If I flip 4 coins, how many ways can exactly 1 land heads?', 4, '',
                  'This is equivalent to the letter arrangement problem HTTT which has answer $\\frac{4!}{3!}$.'))
        bank.add(('If I flip 5 coins, how many ways can exactly 2 land heads?', 10, '',
                  'This is equivalent to the letter arrangement problem HHTTT which has answer $\\frac{5!}{3!2!}$.'))

        bank.add(('If I flip 3 coins, what is the probability they all land heads?', '1/8', '', ''))
        bank.add(('If I flip 3 coins, what is the probability exactly 1 land heads?', '3/8', '', ''))
        bank.add(('If I flip 3 coins, what is the probability exactly 2 land heads?', '3/8', '', ''))
        bank.add(('If I flip 4 coins, what is the probability exactly 1 land heads?', '1/4', '', ''))
        bank.add(('If I flip 4 coins, what is the probability exactly 2 land heads?', '3/8', '', ''))

        bank.add(('There are 4 people in a room.  If everyone shakes hands with every other person in the room once, '
                  'how any handshakes occur? ',
                 6, '', 'Order does not matter, so there are $\\binom{4}{2}$ ways.'))
        bank.add(('There are 6 people in a room.  If everyone shakes hands with every other person in the room once, '
                  'how any handshakes occur? ',
                 15, '', 'Order does not matter, so there are $\\binom{6}{2}$ ways.'))
        bank.add(('There are 7 people in a room.  If everyone shakes hands with every other person in the room once, '
                  'how any handshakes occur? ',
                 21, '', 'Order does not matter, so there are $\\binom{7}{2}$ ways.'))
        bank.add(('In a six team round robin tournament each team plays each other team twice. '
                  'How many games are played?',
                  30, '', 'Order does not matter, so there are $2\cdot \\binom{6}{2}$ ways.'))
        bank.add(('In a 10-team league each team plays each other team exactly once. '
                  'How many games are played?',
                  45, '', 'Order does not matter, so there are $\\binom{10}{2}$ ways.'))

        bank.add(('How many diagonals can be drawn in a convex pentagon?', 5, '',
                  'There are $\\binom{5}{2}-5$ diagonals.'))
        bank.add(('How many diagonals can be drawn in a convex hexagon?', 9, '',
                  'There are $\\binom{6}{2}-6$ diagonals.'))
        bank.add(('How many diagonals can be drawn in a convex octagon?', 20, '',
                  'There are $\\binom{8}{2}-8$ diagonals.'))


        # license plate, sandwich
        bank.add(('How many 4 digit security codes can be made with the digits 0-9 if digits cannot be repeated.',
                  5040, '', ''))
        bank.add(('How many 4 digit security codes can be made with the digits 0-9 if digits can be repeated.',
                  10000, '', ''))
        bank.add(('Jimmy has $4$ hats, $3$ shirts, $4$ pairs of pants, and $10$ pairs of shoes.  How many different '
                  'outfits can he make', 480,
                  '', 'This is like a license plate problem, there are $4\cdot 3\cdot 4\cdot 10$ ways.'))
        bank.add(('Jill has $4$ hats, $3$ shirts, and $7$ pairs of pants.  How many different '
                  'outfits can she make', 84,
                  '', 'This is like a license plate problem, there are $4\cdot 3\cdot 7$ ways.'))

        bank.add(('How many ways can first, second, and third be awarded to seven competitors?', 210,'',
                  'There are $7$ choices for 1st, $6$ for 2nd, and $5$ for 3rd so there are $7\cdot 6\cdot 5$ ways '
                  '(order matters).'))
        bank.add(('How many ways can first, second, and third be awarded to $10$ competitors?', 720,'',
                  'There are $10$ choices for 1st, $9$ for 2nd, and $8$ for 3rd so there are $10\cdot 9\cdot 8$ ways'
                  '(order matters).'))

        bank.add(('How many ways can I pick five starters from a basketball team with $8$ players?', 56,
                  '', 'Order does not matter so use the choose function $\\binom{8}{5}$'))
        bank.add(('How many ways can I pick three out of my $10$ friends to go to Diisney Land with me?', 120,
                  '', 'Order does not matter so use the choose function $\\binom{10}{3}$'))

        # Letter arrangment
        bank.add(('How many ways can you arrange the letters in the word ARRANGE if the R\'s must stay together?', 360,
                  '', 'Treat RR as a single letter.  Then there are $6$ letters with two As repeated.'))  # 720/2

        bank.add(('How many ways can I arrange the letter in the word PHONIES?', 5040, '',
                  'There are seven unique letters so the answer is $7!$.'))
        bank.add(('How many ways can I arrange the letter in the word ZEBRA?', 120, '',
                  'There are five unique letters so the answer is $5!$.'))
        bank.add(('How many ways can I arrange the letter in the word BASEBALL?', 5040, '',
                  'There are 8 letters; B, A, and L are each repeated twice so the answer is $\\frac{8!}{2!2!2!}$'))
        bank.add(('How many ways can I arrange the letter in the word LOLLIPOP?', 1680, '',
                  'There are 8 letters; L, O, and P are repeated 3, 2, and 2 times so the answer is $\\frac{8!}{3!2!2!}$'))

        bank.add(('John is walking directly from home to school.  He needs to go 4 blocks North and 4 blocks West.  '
                  'How many different ways can he do this?',70, '',
                  'This is equivalent to the letter arrangement problem NNNNWWWW which has answer $\\frac{8!}{4!4!}$.'))
        bank.add(('Jane is walking directly home from the gym.  She needs to go 4 blocks North and 2 blocks West.  '
                 'How many different ways can she do this?',
                 15, '',
                  'This is equivalent to the letter arrangement problem NNNNWW which has answer $\\frac{6!}{4!2!}$.'))

        bank.add(('I have 4 unique books, how many ways can I give 2 each to 2 of my friends?', 6, '',
                  'Order does not matter so use the choose function: $\\binom{4}{2}$.'))

        bank.add(('I have 3 red checkers and 5 black checkers.  How many different ways can I stack them?', 56, '',
                  'This is equivalent to the letter arrangement problem RRRBBBBB which has answer $\\frac{8!}{5!3!}$ '
                  '(this is the same as $\\binom{8}{3}$).'))
        bank.add(('How many six-digit numbers contain one 1, two 2\'s, and three 3\'s?', 60, '',
                  'This is a letter arrangement problem for the word 122333 which has answer $\\frac{6!}{3!2!}$'))

        i = random.randrange(len(bank))
        pick = random.sample(bank, 1)[0]
        self.problem = pick[0]
        self.ans = pick[1]
        self.prefix = pick[2]
        if pick[2] == "":
            self.anstex = "The answer is $%s$." % pick[1]
        else:
            self.anstex = "The answer is %s%s$." % (self.prefix[:-1], pick[1])
        self.suffix = ''
        self.hint = pick[3]

"""
class Probability:
    def __init__(self):
        bank = set([])

        # coins
        bank.add(('If I flip 3 coins, what is the probability they all land heads?', '1/8', '', ''))
        bank.add(('If I flip 3 coins, what is the probability exactly 1 land heads?', '3/8', '', ''))
        bank.add(('If I flip 3 coins, what is the probability exactly 2 land heads?', '3/8', '', ''))
        bank.add(('If I flip 4 coins, what is the probability exactly 1 land heads?', '1/4', '', ''))
        bank.add(('If I flip 4 coins, what is the probability exactly 2 land heads?', '3/8', '', ''))

        # dice

        # other?

        i = random.randrange(len(bank))
        pick = random.sample(bank, 1)[0]
        self.problem = pick[0]
        self.ans = pick[1]
        self.prefix = pick[2]
        self.anstex = "The answer is %s%s." % (self.prefix[:-1], pick[1])  # p[1] includes $ and .
        self.suffix = ''
        self.hint = pick[3]
"""

