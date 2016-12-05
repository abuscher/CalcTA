#!/usr/bin/python -tt

import sys
import random
import math
from math import *
import re
import latex
from latex import *
import vector
import polynomial
from polynomial import *
import fractions

# Define a main()
def main():
  options=sys.argv[1]
  if int(options)==0: options='1'+options[1:]
  pick=[]
  for i in range(len(options)):
    if options[i]=='1':pick.append(i)
  type=random.choice(pick)
  if type==0: #quad a=1
    a=polynomial.poly(2,1)
  
  if type==1: #quad a not 1
    a=polynomial.poly(2,2)
  
  if type==0 or type==1:
    a.make_quad()
    problem="Factor $%dx^2+%dx+%d$" % a.quadratic
    ans="{(%d*x+%d),(%d*x+%d)}" % a.coeff
    anstex="The polynomial can be factored into $(%dx+%d)\cdot (%dx+%d)$" % a.coeff

  if type==2: #cubic 3 linear
    a=polynomial.poly(3,2)
    a.make_cubic()
    problem="Factor $%dx^3+%dx^2+%dx+%d$" % a.cubic
    ans="{(%d*x+%d),(%d*x+%d),(%d*x+%d)}" % a.coeff
    anstex="The polynomial can be factored into $(%dx+%d)\cdot (%dx+%d)\cdot (%dx+%d)$" % a.coeff

  if type==3: #cubic GCF
    a=polynomial.poly(2,2)
    a.make_cubic()
    problem="Factor $%dx^3+%dx^2+%dx+%d$" % a.cubic
    ans="{(%d*x^2+%d),(%d*x+%d)}" % a.coeff
    anstex="The polynomial can be factored into $(%dx^2+%d)\cdot (%dx+%d)$" % a.coeff

  if type>=0 and type<=3:
    problem=problem+'.  <br> <br>In your answer, separate the factors with commas (e.g. "(x+1)<b> , </b>(x+2)").'

  if type==4: #2 linear
    choose=random.randrange(10)
    a=polynomial.poly(2,(choose%2+1))
    a.make_rquad()
    coeff=a.rcoeff[6:8]+ a.rcoeff[1:3]+ a.rcoeff[4:6]
    ans="{%d/(%d*x+%d),%d/(%d*x+%d)}" % a.rcoeff[0:6]
    problem="Separate $\displaystyle\\frac{%dx+%d}{(%dx+%d)(%dx+%d)}$" % coeff
    anstex= "The answer is $\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%d}{%dx+%d}$" % a.rcoeff[0:6]

  if type==5:#3 linear
    a=polynomial.poly(3,2)
    a.make_rcubic()
    coeff=a.rcoeff[9:12]+ a.rcoeff[1:3]+ a.rcoeff[4:6]+a.rcoeff[7:9]
    ans="{%d/(%d*x+%d),%d/(%d*x+%d),%d/(%d*x+%d)}" % a.rcoeff[0:9]
    problem="Separate $\displaystyle\\frac{%dx^2+%dx+%d}{(%dx+%d)(%dx+%d)(%dx+%d)}$" % coeff
    anstex= "The answer is $\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%d}{%dx+%d}$" % a.rcoeff[0:9]

  if type==6:#1 linear 1 quad
    a=polynomial.poly(2,2)
    a.make_rcubic()
    coeff=a.rcoeff[7:10]+ a.rcoeff[1:3]+ a.rcoeff[5:7]
    ans="{%d/(%d*x+%d),(%d*x+%d)/(%d*x^2+%d)}" % a.rcoeff[0:7]
    problem="Separate $\displaystyle\\frac{%dx^2+%dx+%d}{(%dx+%d)(%dx^2+%d)}$" % coeff
    anstex= "The answer is $\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%dx+%d}{%dx^2+%d}$" % a.rcoeff[0:7]

  if type in range(4,7): 
    problem=problem+'. <br> <br> In your answer, separate the fractions with commas (e.g. "2/(x+1)<b> , </b>1/(x+2)" ).'

  if type==7:
  #options[3]=Dot Product
    a = vector.vector(3)
    a.dotproduct()
    problem='Take the dot product of $'+str(a.vec1)+'$ and $'+str(a.vec2)+'$.'
    ans=a.dot
    anstex='The dot product is $'+str(a.dot)+'$.'

  if type==8:
  #options[3]=Cross Product
    a = vector.vector(3)
    problem='Take the cross product of $'+str(a.vec1)+'$ and $'+str(a.vec2)+'$.'
    a.crossproduct()
    ans=str(a.cross)[1:-1]
    anstex='The cross product is $\langle '+ans+' \\rangle$.'
    ans='<'+str(ans)+'>'
    prefix='$\langle$'
    suffix='$\\rangle$'
  if type==7 or type==8:
    problem=problem.replace('[','\langle ')
    problem=problem.replace(']','\\rangle ')
  if type==9:
  #Angle
    a = vector.vector(3)
    a.calcangle()
    problem='Calculate the angle $\\theta$ (in degrees) between the vectors $'+str(a.vec1)+'$ and $'+str(a.vec2)+'$.'
    problem=problem.replace('[','\langle ')
    problem=problem.replace(']','\\rangle ')
    ans=a.angle
    anstex='$\\theta='+str(round(ans,3))+'^{\circ}$.'
    prefix='$\\theta = $'
    suffix=''
    hint=''
  if type==10:
  #Equation of a Plane
    a = vector.vector(3)
    a.makeplane()
    problem="Find the equation of the plane through the points $"+str(a.point)+'$, $'+str(a.point2)+'$, and $'+str(a.point3)+'$. <br> (Answer in the form $ax+ by+cz +d=0$.)'
    problem=problem.replace('[','(')
    problem=problem.replace(']',')')
    ans=a.plane
    anstex='The equation is $'+toTEX(ans+'=0')+'$.'
    anstex=anstex.replace('\cdot ','')
    anstex=anstex.replace('$0x+','$')
    anstex=anstex.replace('$0x-','$-')
    anstex=anstex.replace('$1x','$x')
    anstex=anstex.replace('-1x','-x')
    anstex=anstex.replace('+1y','+y')
    anstex=anstex.replace('-1y','-y')
    anstex=anstex.replace('+0y','')
    anstex=anstex.replace('+1z','+z')
    anstex=anstex.replace('-1z','-z')
    anstex=anstex.replace('+0z','')
    suffix='$=0$'

  if type==11:
  #eqn of line...make more than 0 to 1
    a = vector.vector(3)
    boundpick=[-7,-5,-4,-1,0,1,2,3,5,6]
    bounds=random.sample(boundpick,2)
    a.makeline(bounds)
    problem='Find the line segment from $'+str(a.point)+'$ to $'+str(a.point2)+'$ '
    problem=problem.replace('[','(')
    problem=problem.replace(']',')')
    problem=problem+'for $t=[%d,%d]$.'%tuple(bounds)
    ans=a.line
    ans=ans.replace('(','<')
    ans=ans.replace(')','>')
    anstex='The equation of the line is $'+toTEX(str(a.line))+'$ for $t=[%d,%d]$.'%tuple(bounds)
    #anstex='The equation of the line is $ \langle x(t), y(t), z(t)\\rangle ='+toTEX(str(a.line))+'$.'
    anstex=anstex.replace('(','\langle ')
    anstex=anstex.replace(')','\\rangle ')
    anstex=anstex.replace('\cdot ','')
    anstex=anstex.replace('+1t','+t')
    anstex=anstex.replace('-1t','-t')
    anstex=anstex.replace('+-','-')
    prefix='$ \left\langle x(t), y(t), z(t) \\right\\rangle = \langle$'
    suffix='$\\rangle$'

  if type==12: #rational to infinity, either goes to 0, inf, or ratio
    if 1==1:
      subsubtype=random.randint(1,3)
      coeff_bank=[-4, -3, -2, 1, 2, 3, 4, 5, 6]#[i-4 for i in range(3)]+[i+1 for i in range(6)]#[i-10 for i in range(10)]+[i+1 for i in range(10)]
      num_top=random.randint(2,4)
      num_bot=random.randint(2,4)
      pm=random.randint(0,1)
      pm=0
      subsubtype=2
      top_coeff=[random.choice(coeff_bank) for i in range(num_top)]
      bot_coeff=[random.choice(coeff_bank) for i in range(num_bot)]

      highest=random.randint(max(num_top,num_bot),7)

      n=sorted(random.sample(range(highest), num_top-1))+[highest]
      d=sorted(random.sample(range(highest), num_bot-1))+[highest]
      n.reverse()
      d.reverse()
      top=''
      bottom=''
      diff=random.randint(1,4)

      if subsubtype==2: #inf
        n[0]+=diff
        n[1]+=diff/2
        if diff%2==1 and pm==1:
          switch=True
        else: 
          switch=False
        if len(n)>2: n[2]+=diff/3
        if (top_coeff[0]>0 and bot_coeff[0]<0) or (top_coeff[0]<0 and bot_coeff[0]>0):
          if switch==False: ans='-inf'
          else: ans='inf'
        else:
          if switch==False: ans='inf'
          else: ans='-inf'
        
      if subsubtype==3: #0
        d[0]+=diff
        d[1]+=diff/2
        if len(d)>2: d[2]+=diff/3
        ans='0'

      for i in range(num_top):
        top=top+'%sx^{%s}+'%(top_coeff[i],n[i])
      for i in range(num_bot):
        bottom=bottom+'%sx^{%s}+'%(bot_coeff[i],d[i])
      top=top[:-1]
      bottom=bottom[:-1]
      probtex='Find $\lim_{x \\to +%s\infty} \displaystyle\\frac{%s}{%s}$.'%(['','-'][pm],top,bottom)
      tb=fractions.gcd(top_coeff[0],bot_coeff[0])
      if subsubtype==1:
        if bot_coeff[0]/tb==1:
          ans='%d'%(top_coeff[0]/tb)
        else:
          ans='%d/%d'%(top_coeff[0]/tb,bot_coeff[0]/tb)
      if '/' in ans:
        anstex='The limit is $\\frac{%d}{%d}$.'%(top_coeff[0]/tb,bot_coeff[0]/tb)
      else:
        anstex='The limit is $'+str(ans)+'$.'
        anstex=anstex.replace('inf','\infty')
      prefix=''
      suffix=''
      hint=''

      probtex=probtex.replace('1x','x')
      probtex=probtex.replace('+x^{0}','+1')
      probtex=probtex.replace('-x^{0}','-1')
      probtex=probtex.replace('x^{0}','')
      probtex=probtex.replace('x^{1}+','x+')
      probtex=probtex.replace('x^{1}-','x-')
      probtex=probtex.replace('x^{1}}','x}')
      problem=probtex.replace('+-','-')
      anstex=anstex.replace('/1','')

  if type==13 or type==14:
      #subsubtype=random.randint(0,9)
      achoose=[2,3,-2,-3,4,5,6,-5,-6] #length 10 so random 0-9
      bchoose=[1,2,3,-1,-2,-3,4,-4]
      nchoose=[2,3]
      asel=random.randrange(10)
      bsel=random.randrange(10)
      nsel=random.randrange(10)
      a=achoose[asel%len(achoose)]
      b=bchoose[bsel%len(bchoose)]
      n=nchoose[nsel%len(nchoose)]
      if a==b: a=7

  if type==13: #difference of squares with root
    if 1==1:
      if 1==1:
        if a>0: pm='+-'
        else:   pm='-+'
        c=-a-b
        d=-a*b
        problem='Find $\lim_{x \\to +%d} \\frac{x%s\sqrt{%dx+%d}}{x+%d}$.'%(-a,pm[0],c,d,a)
        tb=fractions.gcd((b-a),-2*a)
        ans='%d/%d'%((b-a)/tb,-2*a/tb)
        if ans[-2:]=='/1':
          ans=ans.replace('/1','')
        #if a<0: ans='-'+ans
        anstex='The answer is $%s$.'%ans
        hint='Multiply the numerator and denominator by $x%s\sqrt{%dx+%d}$'%(pm[1],c,d)
        problem=problem.replace('{1x','{x')
        problem=problem.replace('{-1x','{-x')
        problem=problem.replace('+-','-')
        problem=problem.replace('--','+')

        hint=hint.replace('{1x','{x')
        hint=hint.replace('{-1x','{-x')
        hint=hint.replace('+-','-')
        hint=hint.replace('--','+')
  if type==14: #factor and expand
    subtype=random.randint(0,9)
    subtype=3
    if subtype in range(4): #factor polynomial
        #half of problems are (x+a)(x+b), 1/4 are ax+b and x+c, 1/4 ax+b, cx+d
        ptype=random.randint(1,4)
        if ptype==1: c=[1,1]
        if ptype==2: c=[1,1]
        if ptype==3: c=[1,2]
        if ptype==4: c=[2,2]

        a=poly(2,c[0])
        b=poly(2,c[1])
        b.coeff=a.coeff[0:2]+b.coeff[0:2]
        a.make_quad()
        b.make_quad()
        probco=(-a.coeff[1],a.coeff[0])+a.quadratic+b.quadratic
        problem='Find $\lim_{x \\to %d/%d} \\frac{%dx^2+%dx+%d}{%dx^2+%dx+%d}$.'%probco#%(-a.coeff[3],a.coeff[2])+a.quadratic+b.quadratic
        
        #pick up here!!!
        top=a.coeff[1]*a.coeff[2]-a.coeff[0]*a.coeff[3]
        bottom=a.coeff[1]*b.coeff[2]-a.coeff[0]*b.coeff[3]
        
        tb=fractions.gcd(top,bottom)
        
        ans='%d/%d'%(top/tb,bottom/tb)
        anstex='The answer is $%s$.'%(toTEX(ans))

    if subtype in range(4,8): #a(x+b)^n-ab^n / x
      problem='Find $\lim_{x \\to 0} \\frac{%d(x+%d)^%d-%d}{x}$'%(a,b,n,a*b**n)
      ans=str(a*n*b**(n-1))
      anstex='The answer is $%s$.'%ans
      if n==2: hint='Expand (x+%d)^2=x^2+%dx+%d, then simplify the numerator and divide each terms by the denominator.'%(b,2*b,b**2)
      if n==3: hint='Expand (x+%d)^3=x^3+%dx^2+%dx+%d, then simplify the numerator and divide each term by the denominator.'%(b,3*b,3*b**2,b**3)

    if subtype==8: # (x-a)^2-(x-b)^2+b^2-a^2 / x
      problem='Find $\lim_{x \\to 0} \\frac{(x+%d)^2-(x+%d)^2+%d}{x}$.'%(a,b,b**2-a**2)
      ans=str(2*a-2*b)
      anstex='The answer is $%s$.'%ans
    if subtype==9: # (x-a)^2+(x-b)^2-b^2-a^2 / x
      problem='Find $\lim_{x \\to 0} \\frac{(x+%d)^2+(x+%d)^2-%d}{x}$.'%(a,b,b**2+a**2)
      ans=str(2*a+2*b)
      anstex='The answer is $%s$.'%ans

  if type==15: #definition of derivative
    if 1==1:
      bank={}
      bank['x^2']=['2*x']
      bank['x^(-1/3)']=['-1/3*x^(-4/3)']
      bank['x^1.5']=['1.5*x^(.5)']
      bank['x^pi']=['pi*x^(pi-1)']

      bank['sin(x)']=['cos(x)']
      bank['cos(x)']=['-sin(x)']
      bank['tan(x)']=['sec(x)^2']
      bank['sec(x)']=['sec(x)*tan(x)']
      bank['csc(x)']=['-csc(x)*cot(x)']
      bank['cot(x)']=['-csc(x)^2']

      bank['2^(x)']=['2^x*ln(2)']
      bank['pi^(x)']=['pi^x*ln(pi)']
      bank['e^(x)']=['e^x']
      bank['ln(x)']=['1/x']

      rand_num=random.randrange(0,len(bank))
      limtype=random.randrange(1,3)
      term=bank.keys()[rand_num]
      ans=bank[term][0]
      if limtype==1:
        first=term.replace('x','(x+h)')
        first=first.replace('((','(')
        first=first.replace('))',')')
        problem='Find the $\lim_{h \\to 0} \displaystyle\\frac{%s-%s}{h}$.'%(toTEX(first),toTEX(term))
      else:
        first=term.replace('x','z')
        problem='Find the $\lim_{z \\to x} \displaystyle\\frac{%s-%s}{z-x}$.'%(toTEX(first),toTEX(term))
      #anstex=''
      anstex='The answer is $%s$.'%toTEX(ans)
      hint='This is the definition of a derivative'
      prefix=''
      suffix=''

  if type in range(12,16):
    problem=problem.replace('\lim','\displaystyle\lim')
  if type==12: problem=problem+'<br><br>Enter \'inf\' for $\infty$ or \'-inf\' for $-\infty$.'
  if (type>=0 and type<7) or type==14:
    problem=problem.replace('/1$','$')
    problem=problem.replace('/1}','}')
    problem=problem.replace('$--','$')
    problem=problem.replace('(--','(')
    problem=problem.replace('{--','{')
    problem=problem.replace('--','+')

    problem=problem.replace('$1x','$x')
    problem=problem.replace('+1x','+x')
    problem=problem.replace('-1x','-x')
    problem=problem.replace('{1x','{x')
    problem=problem.replace('(1x','(x')
    problem=problem.replace('+-','-')
    problem=problem.replace('{0x+','{')
    problem=problem.replace('{0x-','{-')
    problem=problem.replace('+0x+','+')
    problem=problem.replace('+0x-','-')
    problem=problem.replace('{0x^2+','{')
    problem=problem.replace('{0x^2-','{-')


    anstex=anstex.replace('{1x+','{x+')
    anstex=anstex.replace('(1x+','(x+')
    anstex=anstex.replace('{1x^2+','{x^2+')
    anstex=anstex.replace('(1x^2+','(x^2+')
    anstex=anstex.replace('{1x-','{x-')
    anstex=anstex.replace('(1x-','(x-')
    anstex=anstex.replace('{1x^2-','{x^2-')
    anstex=anstex.replace('(1x^2-','(x^2-')
    anstex=anstex.replace('+-','-')

  if 'prefix' not in locals(): prefix=''
  if 'suffix' not in locals(): suffix=''
  if 'hint' not in locals(): hint=''
  print problem
  print ans
  print anstex
  print prefix
  print suffix
  print hint

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
