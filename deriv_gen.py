#!/usr/bin/python

import sys
import random
import math
from math import *
import re
import latex
from latex import *
import partial

# Define a main() function that prints a little greeting.
def main():
  options=sys.argv[1]

  #php issues
  #options='00101111'
  options=options[4:8]+options[0:4]
  if int(options[0:4])==0: options='1'+options[1:]
  if int(options[4:8])==0: options=options[:4]+'1'+options[5:]

  #type 1 is functions, type 2 is derivative type
  pick1=[]
  for i in range(4):
    if options[i]=='1':pick1.append(i)
  #makes poly/trig/trans 2x as likely as hypinv
  for i in range(3):
    if options[i]=='1':pick1.append(i)
  pick2=[]
  for i in range(4):
    if options[i+4]=='1':pick2.append(i)
  type1=pick1[random.randrange(0,len(pick1))]
  type2=pick2[random.randrange(0,len(pick2))]
  #type1=1
  #type2=0

  #options[0]=poly
  #options[1]=trig
  #options[2]=trans
  #options[3]=hypinv
  #options[4]=basic
  #options[5]=chain
  #options[6]=product
  #options[7]=implicit
  master_bank={}

  #print options
  poly={}
  if type1==0 and type2==0:
    poly['x']=['1','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^2']=['2*x','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^3']=['3*x^2','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^4']=['4*x^3','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^5']=['5*x^4','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^6']=['6*x^5','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^pi']=['pi*x^(pi-1)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^e']=['e*x^(e-1)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    #fraction
    poly['x^(1/2)']=['1/2*x^(-1/2)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^(1/3)']=['1/3*x^(-2/3)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^(7/3)']=['7/3*x^(4/3)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^(-1/2)']=['-1/2*x^(-3/2)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^(-1/3)']=['-1/3*x^(-4/3)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    #1/over
    poly['1/x']=['-1/x^2','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['1/x^2']=['-2/x^3','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['1/x^1.3']=['-1.3*x^(-2.3)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^100']=['100*x^99','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    #decimal
    poly['x^1.2']=['1.2*x^(.2)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^.1']=['.1*x^(-.9)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    #combination
    poly['x^3+x^(1/3)']=['3*x^2+1/3*x^(-2/3)','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x+1/x']=['1-1/x^2','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    poly['x^2+2*x+1']=['2*x+2','Use the <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=1"  target="_blank">Power rule</a> for derivatives.']
    master_bank.update(poly)
  trig={}
  if type1==1 and type2==0:#options[1]=='1' and options[4]=='1':
    trig['sin(x)']=['cos(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=3" target="_blank">this</a> table for trigonometric derivatives.']
    trig['cos(x)']=['-sin(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=3" target="_blank">this</a> table for trigonometric derivatives.']
    trig['tan(x)']=['sec(x)^2','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=3" target="_blank">this</a> table for trigonometric derivatives.']
    trig['sec(x)']=['sec(x)*tan(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=3" target="_blank">this</a> table for trigonometric derivatives.']
    trig['csc(x)']=['-csc(x)*cot(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=3" target="_blank">this</a> table for trigonometric derivatives.']
    trig['cot(x)']=['-csc(x)^2','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=3" target="_blank">this</a> table for trigonometric derivatives.']
    master_bank.update(trig)

  trans={}
  if type1==2 and type2==0:
    trans=master_bank
    trans['e^x']=['e^x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=4" target="_blank">this</a> rule for exponential derivatives.']
    trans['ln(x)']=['1/x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/basicrules&page_id=4" target="_blank">this</a> rule for logarthmic derivatives.']
    master_bank.update(trans)

  hypinv={}
  if type1==3 and type2==0:
    hypinv['asin(x)']=['1/(1-x^2)^(1/2)','']
    hypinv['acos(x)']=['-1/(1-x^2)^(1/2)','']
    hypinv['atan(x)']=['1/(1+x^2)','']
    hypinv['asec(x)']=['1/(x*(1-x^2)^(1/2))','']
    hypinv['acsc(x)']=['-1/(x*(1-x^2)^(1/2))','']
    hypinv['acot(x)']=['-1/(1+x^2)','']
    hypinv['sinh(x)']=['cosh(x)','']
    hypinv['cosh(x)']=['sinh(x)','']
    hypinv['tanh(x)']=['sech(x)^2','']
    hypinv['sech(x)']=['-sech(x)*tanh(x)','']
    hypinv['csch(x)']=['-csch(x)*coth(x)','']
    hypinv['coth(x)']=['-csch(x)^2','']

    master_bank.update(hypinv)

  #poly(poly)
  chain={}
  if type1==0 and type2==1:
    chain['(3*x-1)^3']=['9*(3*x - 1)^2','']
    chain['(5*x-3)^10']=['50*(5*x - 3)^9','']
    chain['(2*x^2-7*x+1)^3']=['3*(4*x-7)*(2*x^2-7*x+1)^2','']
    chain['1/(3*x^2+1)']=['-(6*x)/(3*x^2 + 1)^2','']
    chain['2/(x^5-x^2)^3']=['(6*(2*x - 5*x^4))/(x^2 - x^5)^4','']
    chain['(x^2-1)^3.1']=['6.2*x*(x^2-1)^(2.1)','']

  #trig(trig)
  if type1==1 and type2==1:
    chain['sin(sin(x))']=['cos(x)*cos(sin(x))','']
    chain['sin(cos(x))']=['-sin(x)*cos(cos(x))','']
    chain['sin(tan(x))']=['sec(x)^2*cos(tan(x))','']
    chain['sin(sec(x))']=['sec(x)*tan(x)*cos(sec(x))','']
    chain['sin(csc(x))']=['-csc(x)*cot(x)*cos(csc(x))','']
    chain['sin(cot(x))']=['-csc(x)^2*cos(cot(x))','']

    chain['cos(cos(x))']=['sin(x)*sin(cos(x))','']
    chain['cos(sin(x))']=['-cos(x)*sin(sin(x))','']
    chain['cos(tan(x))']=['-sec(x)^2*sin(tan(x))','']
    chain['cos(sec(x))']=['-sec(x)*tan(x)*sin(sec(x))','']
    chain['cos(csc(x))']=['csc(x)*cot(x)*sin(csc(x))','']
    chain['cos(cot(x))']=['csc(x)^2*sin(cot(x))','']

    chain['tan(tan(x))']=['sec(x)^2*sec(tan(x))^2','']
    chain['tan(sec(x))']=['sec(x)*tan(x)*sec(sec(x))*tan(sec(x))','']
    chain['tan(csc(x))']=['csc(x)*cot(x)*csc(csc(x))*cot(csc(x))','']
    chain['tan(cot(x))']=['csc(x)^2*csc(cot(x))^2','']

  #ln(ln)
  if type1==2 and type2==1:
    chain['ln(ln(x))']=['1/(x*ln(x))','']
    chain['e^(e^x)']=['e^x*e^(e^x)','']
    chain['2^(2^x)']=['ln(2)^2*2^x*2^(2^x)','']

  #ln(poly)
  if  options[0]=='1' and options[2]=='1' and type2==1:
    chain['ln(2*x)']=['1/x','']
    chain['ln(x^2)']=['2/x','']
    chain['ln(x^3)']=['3/x','']
    chain['ln(3*x^2+2*x)']=['(6*x+2)/(3*x^2 + 2*x)','']
    chain['ln((x-1)^2)']=['2/(x-1)','']
    chain['ln(1/x)']=['-1/x','']

  #poly(ln)
    chain['ln(x)^2']=['2*ln(x)/x','']
    chain['ln(x)^3']=['3*ln(x)^2/x','']
    chain['1/ln(x)']=['-1/(x*ln(x)^2)','']
    chain['1/ln(x)^2']=['-2/(x*ln(x)^3)','']
    chain['ln(x)^1.3']=['ln(x)^.3/x','']

  if  options[1]=='1' and options[2]=='1' and type2==1:
  #ln(trig)
    chain['ln(sin(x))']=['cot(x)','']
    chain['ln(cos(x))']=['-tan(x)','']
    chain['e^(sin(x))']=['cos(x)*e^(sin(x))','']
    chain['e^(sin(x)^2)']=['2*sin(x)cos(x)*e^(sin(x)^2)','']
    chain['e^(cos(x))']=['-cos(x)*e^(cos(x))','']
    chain['2^(sin(x))']=['ln(2)*cos(x)*2^(sin(x))','']

  #trig(ln)
    chain['sin(ln(x))']=['cos(ln(x))/x','']
    chain['sin(e^x)']=['e^x*cos(e^x)','']
    chain['sin(2^x)']=['ln(2)*2^x*cos(2^x)','']

  if options[0]=='1' and options[1]=='1' and type2==1:
  #trig(poly)
    chain['sin(x+1/x)']=['-cos(x + 1/x)*(1/x^2 - 1)','']
    chain['sin(x^2)']=['2*x*2)','']
    chain['sin(x^(1/2))']=['-1/(2*x^(1/2)*cos(x^(1/2)','']
    chain['sin(x^3+x)']=['(3*x^2+1)*cos(x^3+x)','']
    chain['sin(x^4)']=['4*x^3*cos(x^4)','']

    chain['cos(x^2)']=['-2*x*sin(x^2)','']
    chain['cos(x^3)']=['-3*x^2*sin(x^3)','']
    chain['cos(x^4+1/x)']=['-(4*x^3-1/x^2)*sin(x^4+1/x)','']

    chain['tan(x+1)']=['sec(x+1)^2','']
    chain['sec(x^(1/2))']=['1/(2*x^(1/2))*sec(x^(1/2))*tan(x^(1/2))','']
    chain['csc(1-x^2)']=['2*x*csc(1-x^2)*cot(1-x^2)','']
    chain['cot(3*x^3)']=['-9*x^2*csc(3*x^3)^2','']
  #poly(trig)
    chain['sin(x)^2']=['2*x*cos(x^2)','']

  if (int(options[0:3])==111) and type2==1:

  #trig(trig+ln, trig+poly, ln+poly)
    chain['sin(ln(x)+x^2)']=['(1/x+2*x)*cos(ln(x)+x^2)','']

  #ln(trig+ln, trig+poly, ln+poly)
    chain['ln(sin(x)+x)']=['(cos(x)+1)/(sin(x)+x)','']

  #poly(trig+ln, trig+poly, ln+poly)
    chain['(3*sin(x)+ln(x))^2']=['2*(3*cos(x)+1/x)*(3*sin(x)+ln(x))','']

  #trig(poly(poly))
    chain['sin((3*x-2)^2)']=['2*(3*x-2)*cos((3*x-2)^2)','']
    chain['sin((2*x+7)^3)']=['3*(2*x+7)^2*cos((2*x+7)^3)','']

  #ln(poly(poly))
    chain['ln((3-2*x)^2)']=['(8*x - 12)/(2*x - 3)^2','']
    chain['ln(3-2*x)^2']=['(4*ln(3 - 2*x))/(2*x - 3)','']

  #3 same
    chain['ln(ln(ln(x)))']=['1/(x*ln(ln(x))*ln(x))','']
    chain['e^(e^(e^x))']=['e^x*e^(e^x)*e^(e^(e^x))','']
    chain['sin(sin(sin(x)))']=['cos(x)*cos(sin(x))*cos(sin(sin(x)))','']

  if options[3]=='1' and type2==1:
    chain['sinh(cosh(x))']=['cosh(cosh(x))*sinh(x)','']
    chain['cosh(sinh(x))']=['sinh(sinh(x))*cosh(x)','']
    chain['sinh(sinh(x))']=['cosh(sinh(x))*cosh(x)','']
    chain['cosh(cosh(x))']=['sinh(cosh(x))*sinh(x)','']

  master_bank.update(chain)

  product={}
  if type1==2 and type2==2:
  #if options[2]=='1' and options[6]=='1':
  #ln*ln
    product['ln(x)*ln(2*x)']=['(ln(x)+ln(2*x))/x','']
    product['ln(x^3+1)*ln(2*x)']=['ln(x^3+1)/x+(3*x^2*ln(2*x))/(x^3+1)','']
    product['ln(3*x)*e^(2*x^3)']=['e^(2*x^3)*(6*x^2*ln(3*x)+1/x)','']
    product['e^x*ln(2*x)']=['(ln(2*x)+1/x)*e^x','']

  if type1==0 and type2==2:
  #if options[0]=='1' and options[6]=='1':
  #poly*poly
    product['(3*x^7+5*x^2)*(x^2+6*x^3)']=['180*x^9+27*x^8+150*x^4+20*x^3','']
    product['(x+1)*(x^4+5*x)']=['5*x^4+4*x^3+10*x+5','']
    product['(2*x^2+1)*(5*x^3+1)']=['50*x^4 + 15*x^2 + 4*x','']
    product['(1-x^2)*(2*x^5-1)']=['-14*x^6+10*x^4+2*x','']
    product['(2*x^2-3*x+1)*(5*x^2-4*x)']=['40*x^3-69*x^2+34*x-4','']
    product['(3*x^2+1)*(x+7)']=['9*x^2+42*x+1','']
    product['(3*x^5+4)*(x^10-5*x^2)']=['-15*x^4*(5*x^2-x^10)-(10*x-10*x^9)*(3*x^5+4)','']
    product['(x+1)*(x-1)']=['2*x','']

  if type1==1 and type2==2:
  #if options[1]=='1' and options[6]=='1':
  #trig*trig
    product['sin(x)*cos(x)']=['cos(x)^2 - sin(x)^2','']
    product['sin(x)*tan(x)']=['cos(x)*tan(x) + sin(x)*(sec(x)^2)','']
    product['sin(x)*sec(x)']=['tan(x)','']
    product['sin(x)*csc(x)']=['0','']
    product['sin(x)*cot(x)']=['-sin(x)','']
    product['cos(x)*tan(x)']=['cos(x)','']
    product['cos(x)*sec(x)']=['0','']
    product['cos(x)*csc(x)']=['tan(x)','']
    product['cos(x)*cot(x)']=['-cos(x)*(2+cot(x)^2)','']
    product['tan(x)*sec(x)']=['-(cos(x)^2 - 2)/cos(x)^3','']
    product['tan(x)*csc(x)']=['sin(x)/cos(x)^2','']
    product['tan(x)*cot(x)']=['0','']
    product['sec(x)*csc(x)']=['1/cos(x)^2 - 1/sin(x)^2','']
    product['sec(x)*cot(x)']=['-cos(x)/sin(x)^2','']
    product['csc(x)*cot(x)']=['(sin(x)^2 - 2)/sin(x)^3','']


  if options[0]=='1' and options[1]=='1' and type2==2:
  #if options[0]=='1' and options[1]=='1' and options[6]=='1':
  #trig*poly
    product['x*sin(x)']=['x*cos(x)+sin(x)','']
    product['x^2*sin(x)']=['x^2*cos(x)+2*x*sin(x)','']
    product['x*cos(x)']=['cos(x)-x*sin(x)','']
    product['x^2*cos(x)']=['2*x*cos(x)-x^2*sin(x)','']
    product['x*tan(x)']=['tan(x)+sec(x)^2','']
    product['x*sec(x)']=['sec(x)+x*sec(x)*tan(x)','']
    product['x*csc(x)']=['csc(x)-x*csc(x)*cot(x)','']
    product['x*cot(x)']=['cot(x)-x*csc(x)^2','']

  if options[1]=='1' and options[2]=='1' and type2==2:
  #ln*trig
    product['ln(x)*sin(x)']=['ln(x)*cos(x)+sin(x)/x','']
    product['ln(x)*cos(x)']=['-ln(x)*sin(x)+cos(x)/x','']
    product['e^x*sin(x)']=['e^x*(sin(x)+cos(x))','']
    product['e^x*cos(x)']=['e^x*(-sin(x)+cos(x))','']

  if options[0]=='1' and options[2]=='1' and type2==2:
  #poly*ln
    product['x*ln(x)']=['ln(x)+1','']
    product['x^2*ln(x)']=['2*x*ln(x)+x','']
    product['x^3*ln(x)']=['3*x^2*ln(x)+x^2','']
    product['x*e^x']=['(x+1)*e^x','']
    product['x^2*e^x']=['(x^2+2*x)*e^x','']
    product['x^3*e^x']=['(x^3+3*x^2)*e^x','']
  #poly^3

  #trig^3

  #ln^3

  #ln^2* poly or trig

  #poly^2*trig or ln

  #trig^2* ln or poly
  if options[0]=='1' and options[1]=='1' and options[2]=='1'  and type2==2:
  #poly*trig*ln
    product['(x+1)*ln(x)*sin(x)']=['ln(x)*sin(x)+cos(x)*ln(x)*(x+1)+(sin(x)*(x+1))/x','']
  if options[3]=='1' and type2==2:
    product['sinh(x)*cosh(x)']=['cosh(x)^2+sinh(x)^2','']
    product['sinh(x)*(sinh(x)^2+cosh(x))']=['sinh(x)*(sinh(x) + 2*cosh(x)*sinh(x)) + cosh(x)*(sinh(x)^2 + cosh(x))','']
    product['cosh(x)*(sinh(x)+2)']=['cosh(x)^2+sinh(x)^2+2*sinh(x)','']



  quotient={}
  if type1==2 and type2==2:
  #if options[2]=='1' and options[6]=='1':
  #ln*ln

    quotient['\displaystyle\\frac{ln(x)}{ln(2*x)}']=['ln(2)','(x*ln(2*x)^2)','']
    quotient['\displaystyle\\frac{ln(x^3+1)}{ln(3*x)}']=['((3*x^2*ln(3*x))/(x^3 - 1) - ln(x^3 - 1)/x)','(ln(3*x)^2)','']

    #quotient['\displaystyle\\frac{ln(3*x)*e^(2*x^3)}']=['exp(2*x^3)*(6*x^2*ln(3*x)+1/x)','']
    #quotient['\displaystyle\\frac{e^x*ln(2*x)}']=['(ln(2*x)+1/x)*e^x','']

  if type1==0 and type2==2:
  #if options[0]=='1' and options[6]=='1':
  #poly*poly
    quotient['\displaystyle\\frac{7*x^4 + x^3 - 3}{x^2 - 1}']=['(x^2 - 1)*(28*x^3 + 3*x^2) - 2*x*(7*x^4 + x^3 - 3)','(x^2 - 1)^2','']
    quotient['\displaystyle\\frac{x^2 + x}{x - 1}']=['(2*x + 1)*(x - 1) - x - x^2','(x - 1)^2','']
    quotient['\displaystyle\\frac{x}{x^2 - 1/x}']=['x^2 - 1/x - x*(2*x + 1/x^2)','(1/x - x^2)^2','']
    quotient['\displaystyle\\frac{x + 3}{1 - x}']=['4','(x - 1)^2','']
    quotient['\displaystyle\\frac{x^4 + 2*x + 1}{1 - x^3}']=['3*x^2*(x^4 + 2*x + 1) - (x^3 - 1)*(4*x^3 + 2)','(x^3 - 1)^2','']
    quotient['\displaystyle\\frac{x^2 + 2*x + 1}{x + 3}']=['(2*x + 2)*(x + 3) - 2*x - x^2 - 1','(x + 3)^2','']

  if type1==1 and type2==2:
  #if options[1]=='1' and options[6]=='1':
  #trig*trig
    quotient['\displaystyle\\frac{cos(x)}{sin(x) - 1}']=['- cos(x)^2 - sin(x)*(sin(x) - 1)','(sin(x) - 1)^2','']
    quotient['\displaystyle\\frac{sin(x)}{sin(x) + 1}']=['cos(x)*(sin(x) + 1) - cos(x)*sin(x)','(sin(x) + 1)^2','']
    quotient['\displaystyle\\frac{tan(x)}{sin(x) - cos(x)}']=['- tan(x)*(cos(x) + sin(x)) - (cos(x) - sin(x))*(tan(x)^2 + 1)','(cos(x) - sin(x))^2','']
    quotient['\displaystyle\\frac{sin(x) - cos(x)}{cos(x) + sin(x)}']=['2','(cos(x) + sin(x))^2','']

  if options[0]=='1' and options[1]=='1' and type2==2:
  #if options[0]=='1' and options[1]=='1' and options[6]=='1':
  #trig*poly
    quotient['\displaystyle\\frac{sin(x)}{x}']=['x*cos(x) - sin(x)','x^2','']
    quotient['\displaystyle\\frac{tan(x)}{x}']=['x*sec(x)^2 - tan(x)','x^2','']
    quotient['\displaystyle\\frac{cos(x)}{x^2 + 3}']=['- sin(x)*(x^2 + 3) - 2*x*cos(x)','(x^2 + 3)^2','']

    quotient['\displaystyle\\frac{x + sin(x)}{x^2 - 1}']=['(x^2 - 1)*(cos(x) + 1) - 2*x*(x + sin(x))','(x^2 - 1)^2','']
    quotient['\displaystyle\\frac{x - cos(x)}{x^2 + x}']=['(sin(x) + 1)*(x^2 + x) - (x - cos(x))*(2*x + 1)','(x^2 + x)^2','']

    quotient['\displaystyle\\frac{x}{sin(x)}']=['sin(x) - x*cos(x)','sin(x)^2','']
    quotient['\displaystyle\\frac{x}{x + cos(x)}']=['x + cos(x) + x*(sin(x) - 1)','(x + cos(x))^2','']
    #quotient['\displaystyle\\frac{x^2 }{tan(x) - x^3}']=['2*x*(tan(x) - x^3) - x^2*(- 3*x^2 + tan(x)^2 + 1)','(tan(x) - x^3)^2','']


  if options[1]=='1' and options[2]=='1' and type2==2:
  #ln*trig
    quotient['\displaystyle\\frac{sin(x)}{e^(x) - 1}']=['cos(x)*(e^(x) - 1) - e^(x)*sin(x)','(e^(x) - 1)^2','']
    quotient['\displaystyle\\frac{tan(x)}{ln(x)}']=['ln(x)*(tan(x)^2 + 1) - tan(x)/x','ln(x)^2','']
    quotient['\displaystyle\\frac{sin(x) + tan(x)}{e^x+ln(x)}']=['(e^x + ln(x))*(sec(x)^2 + cos(x))-(e^x + 1/x)*(sin(x)+tan(x))','(e^x + ln(x))^2','']
    quotient['\displaystyle\\frac{ln(x)}{cos(x)}']=['cos(x)/x + ln(x)*sin(x)','cos(x)^2','']

    quotient['\displaystyle\\frac{cos(x) + e^(x)}{ln(x)}']=['ln(x)*(e^(x) - sin(x)) - (cos(x) + e^(x))/x','ln(x)^2','']


  if options[0]=='1' and options[2]=='1' and type2==2:
  #poly*ln
    quotient['\displaystyle\\frac{ln(x)}{x}']=['1 - ln(x)','x^2','']
    quotient['\displaystyle\\frac{ln(x)}{x^2 + 1}']=['(x^2 + 1)/x - 2*x*ln(x)','(x^2 + 1)^2','']
    quotient['\displaystyle\\frac{x}{e^(x) + 1}']=['e^(x) - x*e^(x) + 1','(e^(x) + 1)^2','']
    quotient['\displaystyle\\frac{ln(x)}{e^(x) + ln(x)}']=['(e^(x) + ln(x))/x - ln(x)*(e^(x) + 1/x)','(e^(x) + ln(x))^2','']

  #poly^3

  #trig^3

  #ln^3

  #ln^2* poly or trig

  #poly^2*trig or ln

  if options[3]=='1' and type2==2:
    product['sinh(x)*cosh(x)']=['cosh(x)^2+sinh(x)^2','']
    product['sinh(x)*(sinh(x)^2+cosh(x))']=['sinh(x)*(sinh(x) + 2*cosh(x)*sinh(x)) + cosh(x)*(sinh(x)^2 + cosh(x))','']
    product['cosh(x)*(sinh(x)+2)']=['cosh(x)^2+sinh(x)^2+2*sinh(x)','']

  master_bank.update(quotient)
  master_bank.update(product)

 # implicit={}

  if type2==3:
    if int(options[0:3])==111:
      implicit=partial.partial(2,'mixed')
    else:
      if type1==0: #poly
        implicit=partial.partial(2,'poly')
      if type1==1:#trig
        implicit=partial.partial(2,'trig')
      if type1==2: #trans
        implicit=partial.partial(2,'trans')
      if type1==3: #hypinv
        implicit=partial.partial(2,'hypinv')

#  master_bank.update(implicit)

  #print len(master_bank)
  if type2!=3:
    rand1=random.randrange(0,len(master_bank))
    f=master_bank.keys()[rand1]
    if len(master_bank[f])==3:
      ans='(%s)/(%s)'%(master_bank[f][0],master_bank[f][1])
      anstex='The answer is $f\'(x)=\displaystyle\\frac{%s}{%s}$'%(toTEX(master_bank[f][0]),toTEX(master_bank[f][1]))
    else:
      ans=master_bank[f][0]
      anstex='The answer is $f\'(x)='+toTEX(ans)+'$'
    probtex='Given the function $f(x)='+toTEX(f)+'$, find the derivative $f\'(x)$'
    prefix='$f\'(x)=$'
    hint=''

  else:
    f=implicit.f
    ans=implicit.yx
    hint=''
    probtex='Given the equation $'+frac(toTEX(f))+'=0$, find $y\'.$'
    prefix='$y\'=$'
    anstex='The answer is $y\'='+frac(toTEX(ans))+'$'

  suffix=''

  if type2==1:
    hint='Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/chainrule" target="_blank">Chain Rule</a>.'
  elif type2==2 and len(master_bank[f])==3:
    hint='Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/productrule" target="_blank">Product Rule or the Quotient Rule</a>.'
  elif type2==2 and len(master_bank[f])<3:
    hint='Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=derivative/productrule" target="_blank">Product Rule</a>.'

  print probtex
  print ans
  print anstex
  print prefix
  print suffix
  print hint
  #print (len(master_bank))
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
