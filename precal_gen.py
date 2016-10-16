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

# Define a main()
def main():
  options=sys.argv[1]
  #options='0000001'
  if int(options)==0: options='1'+options[1:]
  pick=[]
  for i in range(len(options)):
    if options[i]=='1':pick.append(i)

  if 0 in pick:
    pick.append(0.1)
    pick.append(0.2)
    pick.append(0.3)
  if 1 in pick:
    pick.append(1.1)
  if 2 in pick:
    pick.append(2.1)
  if 4 in pick:
    pick.append(4.1)
  type=pick[random.randrange(0,len(pick))]

  #Add difference of Squares?
  #options[0]=Partial Fractions
  # 2 linear
  # 1 linear, 1 quadratic
  # 3 linear
  #options[1] Factoring
  # Quadratics (a=1)
  # Quadratics (a!=1)
  # Cubics with GCF
  # Cubic product of 3 linears
  #options[2]=Equation of a Line (3D)
  #options[3]=Dot and Cross Product
  #options[4]=Angle
  #type 5=Equation of a Plane
  #type=6
  if type==0: #2 linear
    a=polynomial.poly(2,2)
  if type==.1:
    a=polynomial.poly(2,1)
  if type==0 or type==.1:
    a.make_rquad()
    coeff=a.rcoeff[6:8]+ a.rcoeff[1:3]+ a.rcoeff[4:6]
    ans="{%d/(%d*x+%d),%d/(%d*x+%d)}" % a.rcoeff[0:6]
    problem="Separate $\displaystyle\\frac{%dx+%d}{(%dx+%d)(%dx+%d)}$" % coeff
    anstex= "The answer is $\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%d}{%dx+%d}$" % a.rcoeff[0:6]

  if type==.2:#1 linear 1 quad
    a=polynomial.poly(2,2)
    a.make_rcubic()
    coeff=a.rcoeff[7:10]+ a.rcoeff[1:3]+ a.rcoeff[5:7]
    ans="{%d/(%d*x+%d),(%d*x+%d)/(%d*x^2+%d)}" % a.rcoeff[0:7]
    problem="Separate $\displaystyle\\frac{%dx^2+%dx+%d}{(%dx+%d)(%dx^2+%d)}$" % coeff
    anstex= "The answer is $\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%dx+%d}{%dx^2+%d}$" % a.rcoeff[0:7]

  if type==.3:#3 linear
    a=polynomial.poly(3,2)
    a.make_rcubic()
    coeff=a.rcoeff[9:12]+ a.rcoeff[1:3]+ a.rcoeff[4:6]+a.rcoeff[7:9]
    ans="{%d/(%d*x+%d),%d/(%d*x+%d),%d/(%d*x+%d)}" % a.rcoeff[0:9]
    problem="Separate $\displaystyle\\frac{%dx^2+%dx+%d}{(%dx+%d)(%dx+%d)(%dx+%d)}$" % coeff
    anstex= "The answer is $\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%d}{%dx+%d}+\displaystyle\\frac{%d}{%dx+%d}$" % a.rcoeff[0:9]
  if type>=0 and type<1: problem=problem+'. <br> <br> In your answer, separate the fractions with commas (e.g. "2/(x+1)<b> , </b>1/(x+2)" ).'
  if type==1: #quad a=1
    a=polynomial.poly(2,1)
  if type==1.1: #quad a not 1
    a=polynomial.poly(2,2)

  if type==1 or type==1.1:
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

  if type==2.1: #cubic GCF
    a=polynomial.poly(2,2)
    a.make_cubic()
    problem="Factor $%dx^3+%dx^2+%dx+%d$" % a.cubic
    ans="{(%d*x^2+%d),(%d*x+%d)}" % a.coeff
    anstex="The polynomial can be factored into $(%dx^2+%d)\cdot (%dx+%d)$" % a.coeff

  if type>=1 and type<3:
    problem=problem+'.  <br> <br>In your answer, separate the factors with commas (e.g. "(x+1)<b> , </b>(x+2)").'
  if type>=0 and type<3:

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

  if type==3:
  #options[4]=Equation of a Line (3D)
    a = vector.vector(3)
    a.makeline()
    #print a.point, a.point2, a.line
    problem='Find the line segment from $'+str(a.point)+'$ to $'+str(a.point2)+'$ '
    problem=problem.replace('[','(')
    problem=problem.replace(']',')')
    problem=problem+'for $t=[0,1]$.'
    ans=a.line
    ans=ans.replace('(','<')
    ans=ans.replace(')','>')
    #problem=problem.replace('[','\langle')
    #problem=problem.replace(']','\\rangle')
    anstex='The equation of the line is $'+toTEX(str(a.line))+'$ for $t=[0,1]$.'
    #anstex='The equation of the line is $ \langle x(t), y(t), z(t)\\rangle ='+toTEX(str(a.line))+'$.'
    anstex=anstex.replace('(','\langle ')
    anstex=anstex.replace(')','\\rangle ')
    anstex=anstex.replace('\cdot ','')
    anstex=anstex.replace('+1t','+t')
    anstex=anstex.replace('-1t','-t')
    anstex=anstex.replace('+-','-')
    prefix='$ \left\langle x(t), y(t), z(t) \\right\\rangle = \langle$'
    suffix='$\\rangle$'

  if type==4:
  #options[3]=Dot Product
    a = vector.vector(3)
    a.dotproduct()
    problem='Take the dot product of $'+str(a.vec1)+'$ and $'+str(a.vec2)+'$.'
    ans=a.dot
    anstex='The dot product is $'+str(a.dot)+'$.'

  if type==4.1:
  #options[3]=Cross Product
    a = vector.vector(3)
    problem='Take the cross product of $'+str(a.vec1)+'$ and $'+str(a.vec2)+'$.'
    a.crossproduct()
    ans=str(a.cross)[1:-1]
    anstex='The cross product is $\langle '+ans+' \\rangle$.'
    ans='<'+str(ans)+'>'
    prefix='$\langle$'
    suffix='$\\rangle$'
  if type==4 or type==4.1:
    problem=problem.replace('[','\langle ')
    problem=problem.replace(']','\\rangle ')
  if type==5:
  #Angle
    a = vector.vector(3)
    #print a.vec1, a.vec2
    a.calcangle()
    #print a.angle
    problem='Calculate the angle $\\theta$ (in degrees) between the vectors $'+str(a.vec1)+'$ and $'+str(a.vec2)+'$.'
    problem=problem.replace('[','\langle ')
    problem=problem.replace(']','\\rangle ')

    ans=a.angle
    anstex='$\\theta='+str(round(ans,3))+'^o$.'

    prefix='$\\theta = $'
    suffix=''
    hint=''
  #eqnplane={}
  if type==6:
  #options[5]=Equation of a Plane
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