# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Austin
#
# Created:     13/01/2014
# Copyright:   (c) Austin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import random
#import math
#from math import *
#import re
import fractions
import nt

class oneeqn:
  def __init__(self):
    #setup
    bank = set(range(2, 10) + range(-9, -1))

    #Generate problem statement
    ptype = random.randint(1, 3)
    (a, b, c, d) = random.sample(bank, 4)

    self.prefix = '$x=$'
    self.suffix = ''

    if ptype == 4:  #x/a+b=c
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
      
    if ptype == 1:  #ax+b=c
      self.problem = 'Solve for $x$ in the equation $%dx+%d=%d$.' % (a, b, c)
      if b > 0:
        self.hint = 'Subtract $%d$ from both sides then divide both sides by $%d$.' % (b, a)
      else:
        self.hint = 'Add $%d$ to both sides then divide both sides by $%d$.' % (-b, a)

    if ptype == 3:  #ax+b=dx+c
      self.problem = 'Solve for $x$ in the equation $%dx+%d=%dx+%d$.' % (a, b, d, c)
      a-=d
      if b>0 and d>0: s=['Subtract','from','subtract','from'] 
      elif b>0 and d<0: s=['Subtract','from','add','to']
      elif b<0 and d>0: s=['Add','to','subtract','from']
      else: s=['Add','to','add','to']

      self.hint = '%s $%d$ %s both sides, %s $%dx$ %s both sides, then divide both sides by $%d$.' % (s[0],abs(b),s[1],s[2],abs(d),s[3],a)

    elif ptype == 2:  #ax+b-c=0
      self.problem = 'Solve for $x$ in the equation $%dx+%d=0$' % (a, b - c)
      if b - c > 0:
        self.hint = 'Subtract $%d$ from both sides then divide both sides by $%d$.' % (b - c, a)
      else:
        self.hint = 'Add $%d$ to both sides then divide both sides by $%d$.' % (c - b, a)

    if ptype == 1 or ptype == 2 or ptype==3:
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

    #Clean up the tex
    self.problem = self.problem.replace('+-', '-')
    self.problem = self.problem.replace('1y', 'y')
    self.problem = self.problem.replace('1x', 'x')

	
class syseqn:
  def __init__(self, numvar, sub=False):
    #setup
    numcoeff = numvar * numvar
    bank = set(range(2, 10) + range(-9, -1))

    #pick values
    coeffs = random.sample(bank, numcoeff)
    if sub:
      a = random.randrange(numcoeff)
      coeffs[a] = 1 * -1 ** (random.randrange(2))
    xy = random.sample(bank, numvar)

    #Generate problem statement
    if numvar == 2:
      #Check for infinitely many solutions (2D only)
      if coeffs[0] * coeffs[3] == coeffs[1] * coeffs[2] and numvar == 2:  #if discriminate 0
        if coeffs[0] == 1:  #don't change the value that's 1 in case it's substitution
          coeffs[1] *= 2
        else:
          coeffs[1] *= 2

      rhs = [xy[0] * coeffs[0] + xy[1] * coeffs[1], xy[0] * coeffs[2] + xy[1] * coeffs[3]]
      self.problem = 'Solve the system of equations $%dx+%dy=%d$ and $%dx+%dy=%d$.  Separate your answer with a comma (e.g. "3,-1").' \
                     % tuple(coeffs[:2] + [rhs[0]] + coeffs[2:] + [rhs[1]])
      self.ans = '<%d,%d>' % tuple(xy)
      self.prefix = '$(x,y)=$'

      #Generate hint (2D)
      if sub:
        if a == 0:
          self.hint = 'Try using substitution. Solve for x in the first equation and substitute that into the second equation.'
        elif a == 1:
          self.hint = 'Try using substitution. Solve for y in the first equation and substitute that into the second equation.'
        elif a == 2:
          self.hint = 'Try using substitution. Solve for x in the second equation and substitute that into the first equation.'
        elif a == 3:
          self.hint = 'Try using substitution. Solve for y in the second equation and substitute that into the first equation.'
      else:  #elimination
        f = fractions.gcd(coeffs[0], coeffs[2])
        if coeffs[0] < 0 and coeffs[2] > 0 and f < 0: f *= -1
        strstuf = (coeffs[2] / f, -coeffs[0] / f)
        if coeffs[0] == -coeffs[2]:
          self.hint = 'Try using elimination. Add the two equations together and the $x$s will cancel.'
        elif coeffs[1] == -coeffs[3]:
          self.hint = 'Try using elimination. Add the two equations together and the $y$s will cancel.'
        else:
          self.hint = 'Try using elimination.  Multiply the first equation by $%d$ and' \
                      ' the second by $%d$, then add them together.' % strstuf

    else:  #numvar==3
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

    #Clean up the tex
    self.problem = self.problem.replace('+-', '-')
    self.problem = self.problem.replace('1y', 'y')
    self.problem = self.problem.replace('1x', 'x')
    self.anstex = self.anstex.replace('<', '(')
    self.anstex = self.anstex.replace('>', ')')

class exponents:
  def __init__(self):
    r=[random.randint(-4,7) for _ in range (5)]
    i = random.randint(1,8)
    e=random.sample([-2]*4+[2]*4+[3]*2+[-3]*2+[0,1,4],1)[0] #exponent...small possibility of 0,1
    if i==1:
      ptype=1
      A=r[0]+r[1]
      problem="x^{%d}\cdot x^{%d}"%tuple(r[:2])
      self.hint="Use the multiplication rule $x^a\cdot x^b=x^{a+b}$."
    elif i==2:
      ptype=1
      A=r[0]-r[1]
      problem='\\displaystyle\\frac{x^{%d}}{x^{%d}}'%tuple(r[:2])
      self.hint="Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$."
    elif i==3:
      ptype=1
      A=r[0]*r[1]
      problem="\left(x^{%d}\\right)^{%d}"%tuple(r[:2])
      self.hint="Use the power rule $\left(x^a\\right)^b=x^{ab}$."
    elif i==4:
      ptype=1
      A=r[0]*r[1]+r[2]
      problem="\left(x^{%d}\\right)^{%d}\cdot x^{%d}"%tuple(r[:3])
      self.hint="Use the power rule $\left(x^a\\right)^b=x^{ab}$ and the multiplication rule $x^a\cdot x^b=x^{a+b}$."
    elif i==5:
      ptype=1
      A=(r[0]-r[1])*r[2]
      problem='\left(\\displaystyle\\frac{x^{%d}}{x^{%d}}\\right)^{%d}'%tuple(r[:3])
      self.hint="Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$ and the power rule $\left(x^a\\right)^b=x^{ab}$."
    elif i==6:
      ptype=2
      A=r[0]*e+r[2]
      B=r[1]*e+r[3]
      problem="\left(x^{%d}y^{%d}\\right)^{%d}\cdot x^{%d}y^{%d}"%tuple(r[:2]+[e]+r[2:4])
      self.hint="Use the power rule $\left(x^a\\right)^b=x^{ab}$ and the multiplication rule $x^a\cdot x^b=x^{a+b}$."
    elif i==7:
      ptype=2
      A=(r[0]-r[2])*e
      B=(r[1]-r[3])*e
      problem='\left(\\displaystyle\\frac{x^{%d}y^{%d}}{x^{%d}y^{%d}}\\right)^{%d}'%tuple(r[:4]+[e])
      self.hint="Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$ and the power rule $\left(x^a\\right)^b=x^{ab}$."
    elif i==8:
      ptype=3
      A=r[0]-r[3]
      B=r[1]-r[4]
      C=r[2]-e
      problem='\\displaystyle\\frac{x^{%d}y^{%d}z^{%d}}{x^{%d}y^{%d}z^{%d}}'%tuple(r+[e])
      self.hint="Use the division rule $\\displaystyle\\frac{x^{a}}{x^{b}}=x^{a-b}$."

    if ptype==1:
      self.problem="Given $%s=x^A$, find $A$."%problem
      self.ans=str(A)
      self.prefix="$A=$"
      self.suffix=""
      self.anstex=self.prefix[:-1]+self.ans+"$."
    if ptype==2:
      self.problem="Given $%s=x^Ay^B$, find $A,B$.  Express your answer as an ordered pair $A,B$."%problem
      self.ans=str("<%d,%d>"%(A,B))
      self.prefix="$(A,B)=$"
      self.suffix=""
      self.anstex=self.prefix[:-1]+"("+self.ans[1:-1]+")$."
    if ptype==3:
      self.problem="Given $%s=x^Ay^Bz^C$, find $A,B,C$.  Express your answer as an ordered pair $A,B$."%problem
      self.ans=str("<%d,%d,%d>"%(A,B,C))
      self.prefix="$(A,B,C)=$"
      self.suffix=""
      self.anstex=self.prefix[:-1]+"("+self.ans[1:-1]+")$."

import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

class numberbase:
  def __init__(self,to10):
    bank = set([])
    b=random.sample([2]*4+range(3,10)+[16],1)[0]
    base_10=random.randint(1,256)
    base_xx=int2base(base_10,b)

    if to10:
      self.problem = 'Convert $%s_{%d}$ to base $10$.' % (base_xx,b)
      self.ans = base_10
      self.anstex = "The answer is $%s_{%d}=%s_{10}$." % (base_xx,b,self.ans)
      self.suffix = '$_{10}$'
    else:
      self.problem = 'Convert $%s_{10}$ to base $%d$.' % (base_10,b)
      self.ans = base_xx
      self.anstex = "The answer is $%s_{10}=%s_{%d}$." % (base_10,self.ans,b)
      self.suffix = '$_{%d}$'%b
    
    self.prefix = ''
    self.hint = ''

class template:
  def __init__(self):
    bank = set([])
    #Add them together
    bank.add(('Given the system $x+y=6$, $y+z=5$, and $x+z=79$, find $x+y+z$.', 24, '$x+y+z=$',
              'Add all three equations together.'))

    #square it
    bank.add(('Given the system $x+y=6$, find $x+y+z$.', 24, '$x+y+z=$', 'Add all three equations together.'))

    i = random.randrange(len(bank))
    pick = random.sample(bank, 1)[0]
    self.problem = pick[0]
    self.ans = pick[1]
    self.prefix = pick[2]
    self.anstex = "The answer is %s%s$." % (self.prefix[:-1], pick[1])  #p[1] includes $ and .
    self.suffix = ''
    self.hint = pick[3]


class wordprob:
  def __init__(self):
    bank = set([])

    #Pigs and Chickens/Nickels and DimesBake sale
    bank.add(('John has a farm with pigs and chickens. If he looks out and counts 34 heads and 72 tails, how many pigs does he have?',
      2, '', 'pigs', ''))
    bank.add(('John has a farm with pigs and chickens. If he looks out and counts 16 heads and 40 tails, how many chickens does he have?',
      12, '', 'chickens', ''))
    bank.add(('John has a farm with pigs and chickens. If he looks out and counts 87 heads and 252 tails, how many pigs does he have?',
      39, '', 'pigs', ''))
    bank.add(('John has a farm with pigs and chickens. If he looks out and counts 54 heads and 150 tails, how many chickens does he have?',
      33, '', 'chickens', ''))

    bank.add(('Alicia has 23 coins, all nickels or dimes, totaling to $1.75.  How many dimes does she have? 12 dimes',
             12,'', 'dimes', ''))
    bank.add(('Alicia has 14 coins, all nickels or quarters totaling to $2.70.  How many nickels does she have?',
             4, '','dimes', ''))

    bank.add(('Super Taxi charges $2.40 plus $1.05 per mile and Awesome Cab charges $3.65 plus $1.00 per mile.  '
             'How many miles do you have to drive for Super Taxi to be 50 cents cheaper than Awesome Cab?',
           15, '', 'miles',''))

    #mixing/percentage
    bank.add(('13% of a number is 45, what is 39% of that same number?', 135, '', '', ''))
    bank.add(('i have a 20 oz jar containing a solution of 30% acid and a 12 oz jar containing a solution of 10% acid.  '
             'I pour them both into a 40 oz jar, then top it off with acid.  '
             'What percentage of the 40 oz jar is filled with acid?', 38, '', '$\%$', ''))

    #age
    bank.add(('The sum of the ages of Billy\'s seven children is 34.  What will the sum of their ages be in 10 years?',104,'', 'years', ''))
    bank.add(('Ken is two years older than Eric.  Half of Eric\'s age minus 3 is equal to one third Ken\'s age.  How old is Ken?',24, '', 'years old', ''))

    #rate and time
    #paint a fence
    bank.add(('John can paint a fence alone in 3 hours.  Alex can paint a fence alone in 2 hours.  '
         'How many minutes will it take working together?', 72, '', 'minutes', ''))
    bank.add(('Paul can paint a fence alone in 12 hours.  If he works with Jed, they can complete it in 3 hours.  '
         'How long will it take Jed working alone?', 4, '', 'hours', ''))
    bank.add(('Three workers of equal skill can complete a fence in 2 hours.  '
         'After an hour of work, one of the workers leaves.  How much additional time (in minutes) is required to finish the fence? ',
         90, '', 'minutes', ''))

    #faucets
    bank.add(('A bathtub has three faucets - A, B and C - which can fill the tub alone in 1,3, and 6 hours respectively.  '
             'If all 3 faucets are on, how many minutes will it take to fill the tub?', 40, '', 'minutes', ''))

    #driving
    bank.add(('John drives 252 miles to LA in 5 hours and 298 miles back in 6.  What is his average speed for the entire trip?', 50, '', 'mph', ''))
    bank.add(('John drives to LA at a speed of 56 mph and back at a speed of 42 mph, what is his average speed?', 48, '', 'mph', ''))

	
    #Add them together
    bank.add(('Given the system $x+y=6$, $y+z=5$, and $x+z=79$, find $x+y+z$.', 24, '$x+y+z=$',
              'Add all three equations together.'))
    bank.add(('Given the system $a+b=-4$, $b+c=2$, and $a+c=-34$, find $a+b+c$.', -8, '$a+b+c=$',
              'Add all three equations together.'))
    bank.add(('Given the system $2x+5y=6$, $-2y+z=5$, $-w+2z=2$, and $x+4w=2$, find $x+y+z+w$.', 5, '$x+y+z+w=$',
              'Add all four equations together.'))

    bank.add(('Given the system $7x+2y=2$, $4y+7z=15$, and $x+y+z=3$, find $y$.', 24, '$y=$',
              'Add the first two equations together.'))
    #bank.add(('Given the system $x+y=6$, $y+z=5$, and $x+z=79$, find $x+y+z$.',24,'$x+y+z=$','Add all three equations together.'))

    #square it
    bank.add(('Given the system $x+\frac{1}{x}=3$, find $x^2+\frac{1}{x^2}$.', 7, '$x^2+\frac{1}{x^2}=$',
              'Square the equation and simplify.'))
    bank.add(('Given $x+1/x=5$, find $x^2+1/x^2$.', 23, '$x^2+1/x^2=$', 'Square both sides of the given equation.'))
    bank.add(('Given $x-6/x=0$, find $x^2$.', 6, '$x^2=$', 'Multiply both sides by $x$.'))

    bank.add(('Given $x+y=6$ and $xy=3$, find $x^2+y^2$.', 30, '$x^2+y^2=$', 'Square the first equation.'))
    bank.add(('Given $x+y=-3$ and $xy=2$, find $x^2+y^2$.', 5, '$x^2+y^2=$', 'Square the first equation.'))

	
    i = random.randrange(len(bank))
    pick = random.sample(bank, 1)[0]
    self.problem = pick[0]
    self.ans = pick[1]
    self.prefix = pick[2]

    self.suffix = pick[3]
    if len(pick)>4: 
      self.hint = pick[4]
    else:
      self.hint=""

    self.anstex = "The answer is %s$%s$ %s." % (self.prefix, pick[1],self.suffix)  #p[1] includes $ and .

    self.anstex = self.anstex.replace('$$', '')
    self.anstex = self.anstex.replace('$ $', '')
    self.anstex = self.anstex.replace(' .', '.')


class counting:
  def __init__(self):
    bank = set([])

    #coins
    bank.add(('If I flip 2 coins, how many different ways can they land?', 4, '', ''))
    bank.add(('If I flip 3 coins, how many different ways can they land?', 8, '', ''))
    bank.add(('If I flip 4 coins, how many different ways can they land?', 16, '', ''))
    bank.add(('If I flip 5 coins, how many different ways can they land?', 32, '', ''))
    bank.add(('If I flip 6 coins, how many different ways can they land?', 64, '', ''))
    bank.add(('If I flip 8 coins, how many different ways can they land?', 256, '', ''))

    bank.add(('If I flip 3 coins, how many ways can exactly 1 land heads?', 3, '', ''))
    bank.add(('If I flip 3 coins, how many ways can exactly 2 land heads?', 3, '', ''))
    bank.add(('If I flip 4 coins, how many ways can exactly 1 land heads?', 4, '', ''))
    bank.add(('If I flip 4 coins, how many ways can exactly 2 land heads?', 6, '', ''))
	
    bank.add(('There are 4 people in a room.  If everyone shakes hands with every other person in the room once, how any handshakes occur? ', 6, '', ''))
    bank.add(('There are 6 people in a room.  If everyone shakes hands with every other person in the room once, how any handshakes occur? ', 15, '', ''))
    bank.add(('There are 7 people in a room.  If everyone shakes hands with every other person in the room once, how any handshakes occur? ', 21, '', ''))

    bank.add(('How many diagonals can be drawn in a convex hexagon?', 9, '', ''))
    bank.add(('How many diagonals can be drawn in a convex octagon?', 20, '', ''))
    
    
    #license plate, sandwich
    bank.add(('In a six team round robin tournament each team plays each other team twice. How many games are played?', 30, '', ''))
    bank.add(('How many 4 digit security codes can be made with the digits 0-9 if digits cannot be repeated.', 5040, '', ''))
	#bank.add(('', -1, '', ''))
	#bank.add(('', -1, '', ''))
    bank.add(('How many ways can you arrange the letters in the word ARRANGE if the R\'s must stay together?', 360, '', '')) #720/2 
    
	#Letter arrangment
    bank.add(('How many ways can I arrange the letter in the word ZEBRA?', 120, '', ''))
    bank.add(('How many ways can I arrange the letter in the word BASEBALL?', 5040, '', ''))
    bank.add(('How many ways can I arrange the letter in the word LOLLIPOP?', 1680, '', ''))
    bank.add(('John is walking directly from home to school.  He needs to go 4 blocks North and 4 blocks West.  How many different ways can he do this?', 70, '', ''))
    bank.add(('Jane is walking directly home from the gym.  She needs to go 4 blocks North and 2 blocks West.  How many different ways can she do this?', 15, '', ''))
	
    bank.add(('I have 4 unique books, how many ways can I give 2 each to 2 of my friends?', 6, '', ''))
    bank.add(('I have 3 red checkers and 5 black checkers.  How many different ways can I stack them?', 56, '', ''))
    bank.add(('How many six-digit numbers contain one 1, two 2\'s, and three 3\'s?', 60, '', '')) #720/6/2
	
    
    i = random.randrange(len(bank))
    pick = random.sample(bank, 1)[0]
    self.problem = pick[0]
    self.ans = pick[1]
    self.prefix = pick[2]
    self.anstex = "The answer is %s%s." % (self.prefix[:-1], pick[1])  #p[1] includes $ and .
    self.suffix = ''
    self.hint = pick[3]


class probability:
  def __init__(self):
    bank = set([])

    #coins
    bank.add(('If I flip 3 coins, what is the probability they all land heads?', '1/8', '', ''))
    bank.add(('If I flip 3 coins, what is the probability exactly 1 land heads?', '3/8', '', ''))
    bank.add(('If I flip 3 coins, what is the probability exactly 2 land heads?', '3/8', '', ''))
    bank.add(('If I flip 4 coins, what is the probability exactly 1 land heads?', '1/4', '', ''))
    bank.add(('If I flip 4 coins, what is the probability exactly 2 land heads?', '3/8', '', ''))
	
	#dice
	
	#other?
	
    i = random.randrange(len(bank))
    pick = random.sample(bank, 1)[0]
    self.problem = pick[0]
    self.ans = pick[1]
    self.prefix = pick[2]
    self.anstex = "The answer is %s%s." % (self.prefix[:-1], pick[1])  #p[1] includes $ and .
    self.suffix = ''
    self.hint = pick[3]


class simplifyradicals:
  def __init__(self):
    bank = set([])
	
    bank.add((343, (7,7)))
    bank.add((245, (7,5)))
    bank.add((325, (5,13)))
    bank.add((275, (5,11)))
    bank.add((175, (5,7)))
    bank.add((125, (5,5)))
    bank.add((363, (11,3)))
    bank.add((147, (7,3)))
    bank.add((75, (5,3)))
    bank.add((375, (5,15)))
    bank.add((117, (3,13)))
    bank.add((99, (3,11)))
    bank.add((63, (3,7)))
    bank.add((45, (3,5)))
    bank.add((315, (3,35)))
    bank.add((27, (3,3)))
    bank.add((351, (3,39)))
    bank.add((297, (3,33)))
    bank.add((189, (3,21)))
    bank.add((135, (3,15)))
    bank.add((243, (9,3)))
    bank.add((338, (13,2)))
    bank.add((242, (11,2)))
    bank.add((98, (7,2)))
    bank.add((50, (5,2)))
    bank.add((350, (5,14)))
    bank.add((250, (5,10)))
    bank.add((294, (7,6)))
    bank.add((150, (5,6)))
    bank.add((18, (3,2)))
    bank.add((306, (3,34)))
    bank.add((342, (3,38)))
    bank.add((234, (3,26)))
    bank.add((198, (3,22)))
    bank.add((126, (3,14)))
    bank.add((90, (3,10)))
    bank.add((54, (3,6)))
    bank.add((378, (3,42)))
    bank.add((270, (3,30)))
    bank.add((162, (9,2)))
    bank.add((52, (2,13)))
    bank.add((44, (2,11)))
    bank.add((28, (2,7)))
    bank.add((364, (2,91)))
    bank.add((308, (2,77)))
    bank.add((20, (2,5)))
    bank.add((340, (2,85)))
    bank.add((380, (2,95)))
    bank.add((260, (2,65)))
    bank.add((220, (2,55)))
    bank.add((140, (2,35)))
    bank.add((12, (2,3)))
    bank.add((204, (2,51)))
    bank.add((228, (2,57)))
    bank.add((276, (2,69)))
    bank.add((348, (2,87)))
    bank.add((372, (2,93)))
    bank.add((156, (2,39)))
    bank.add((132, (2,33)))
    bank.add((84, (2,21)))
    bank.add((60, (2,15)))
    bank.add((300, (10,3)))
    bank.add((396, (6,11)))
    bank.add((252, (6,7)))
    bank.add((180, (6,5)))
    bank.add((108, (6,3)))
    bank.add((8, (2,2)))
    bank.add((136, (2,34)))
    bank.add((152, (2,38)))
    bank.add((184, (2,46)))
    bank.add((232, (2,58)))
    bank.add((248, (2,62)))
    bank.add((296, (2,74)))
    bank.add((328, (2,82)))
    bank.add((344, (2,86)))
    bank.add((376, (2,94)))
    bank.add((104, (2,26)))
    bank.add((88, (2,22)))
    bank.add((56, (2,14)))
    bank.add((392, (14,2)))
    bank.add((40, (2,10)))
    bank.add((280, (2,70)))
    bank.add((200, (10,2)))
    bank.add((24, (2,6)))
    bank.add((312, (2,78)))
    bank.add((264, (2,66)))
    bank.add((168, (2,42)))
    bank.add((120, (2,30)))
    bank.add((72, (6,2)))
    bank.add((360, (6,10)))
    bank.add((216, (6,6)))
    bank.add((208, (4,13)))
    bank.add((176, (4,11)))
    bank.add((112, (4,7)))
    bank.add((80, (4,5)))
    bank.add((48, (4,3)))
    bank.add((336, (4,21)))
    bank.add((240, (4,15)))
    bank.add((32, (4,2)))
    bank.add((352, (4,22)))
    bank.add((224, (4,14)))
    bank.add((160, (4,10)))
    bank.add((96, (4,6)))
    bank.add((288, (12,2)))
    bank.add((320, (8,5)))
    bank.add((192, (8,3)))
    bank.add((128, (8,2)))
    bank.add((384, (8,6)))
	
    i = random.randrange(len(bank))
    pick = random.sample(bank, 1)[0]
    number=pick[0]
    outside=pick[1][0]
    inside=pick[1][1]
    self.problem = "When simplified, $\\sqrt{"+str(number)+"}=a\\sqrt{b}$. What are $a$ and $b$ (separate answer with a comma)?"
    self.ans = "<"+str(pick[1])[1:-1]+">"
    self.prefix = "$a,b=$"
    self.suffix = ''
    self.hint='$\\sqrt{%d}=\\sqrt{%d \\cdot %d}$'%(number, inside, outside**2)
    self.anstex=self.prefix[:-1]+'(%d, %d)$ because $\\sqrt{%d}$ simplifies to $%d\\sqrt{%d}$.'%(outside, inside, number, outside, inside)
	
def main():
  options = sys.argv[1]
  if int(options) == 0: options = '1' + options[1:]

  pick = []
  for i in range(len(options)):
    if options[i] == '1': pick.append(i)
  type1 = pick[random.randrange(0, len(pick))]

  if type1 == 0:
    a = oneeqn()
  if type1 == 1:
    a = syseqn(2)
  if type1 == 2:  #substitution
    a = syseqn(2, True)
  if type1 == 3:
    a = syseqn(3)
  if type1 == 4:
    a = simplifyradicals() 
  if type1 == 5:
    a = counting()  
  if type1 == 6:
    a = exponents()
  if type1 == 7:
    if random.randint(0,1)==0:
      a = nt.gcf() 
    else: 
      a = nt.lcm()     
  if type1 == 8:
    if random.randint(0,1)==0:
      a = numberbase(True) 
    else: 
      a = numberbase(False)  
  if type1 == 9:
    a = wordprob()
	
	  #if type1 == 7:
  #  a = probability() 

  a.prefix = a.prefix.replace('\r', '\\r')
  a.prefix = a.prefix.replace('\f', '\\f')
  a.prefix = a.prefix.replace('\frac', '\displaystyle\frac')

  a.problem = a.problem.replace('\r', '\\r')
  a.problem = a.problem.replace('\f', '\\f')
  a.problem = a.problem.replace('\frac', '\displaystyle\frac')
  a.anstex = a.anstex.replace('\frac', '\displaystyle\frac')
  a.anstex = a.anstex.replace('\r', '\\r')
  a.anstex = a.anstex.replace('\f', '\\f')

	
  print a.problem
  print a.ans
  print a.anstex
  print a.prefix
  print a.suffix
  print a.hint


if __name__ == '__main__':
  main()
