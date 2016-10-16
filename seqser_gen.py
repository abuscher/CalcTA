#!/usr/bin/python -tt

import sys
import random
import math
from math import *
import re
import latex
from latex import *
import fractions

class series(object):
  def __init__(self,type):
    bank=((1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(2,3),(2,5),(2,7),(3,4),(3,5),(3,7),(3,8),(4,5),(4,7),(5,7),(6,7))

    pair1=bank[random.randint(0,len(bank)-1)]
    pair2=bank[random.randint(0,len(bank)-1)]
    i=random.randint(0,1)
    if pair1[i]==1:
      a='%d'%(pair1[(i+1)%2])
    else:
      a='\displaystyle\\frac{%d}{%d}'%(pair1[(i+1)%2],pair1[i])

#do string replaces for '/1'
    if type=='infsum':
      r='\displaystyle\\frac{%d}{%d}'%pair2
      top=pair1[(i+1)%2]*pair2[1]
      bottom=pair1[i]*(pair2[1]-pair2[0])
      div=fractions.gcd(top,bottom)
      sum='%d/%d'%(top/div,bottom/div)
      self.sum=str.replace(sum,'/1','')
      prefix='Find the sum '
      maxr='\infty'
    if type=='psum':
      n=random.randint(3,7)
      if pair2[(i+1)%2]==1:
        r='%d'%pair2[i]
      else:
        r='\displaystyle\\frac{%d}{%d}'%(pair2[i],pair2[(i+1)%2])
      top=pair1[(i+1)%2]*(pair2[(i+1)%2]**n-pair2[i]**n)
      bottom=pair1[i]*pair2[(i+1)%2]**(n-1)*(pair2[(i+1)%2]-pair2[i])
      div=fractions.gcd(top,bottom)
      sum='%d/%d '%(top/div,bottom/div)
      self.sum=str.replace(sum,'/1 ','')
      prefix='Find the sum of the first $%d$ terms '%n
      maxr=str(n-1)

    #if type=='term':
    if a[-2:]=='/1': str.replace(a,'/1','')
    r=str.replace(r,'/1','')
    rand=random.randint(1,3)
    if rand==1: self.problem=prefix+'of the series with $a=%s$ and $r=%s$.'%(a,r)
    elif rand==2: self.problem='Evaluate $\displaystyle\sum_{n=0}^{%s}{%s\cdot \left(%s\\right)^n}$.'%(maxr,a,r)
    elif rand==3: self.problem=prefix+'of the series $%s+%s\cdot%s+%s\cdot\left(%s\\right)^2+...$'%(a,a,r,a,r)

class power_series(object):
  def __init__(self,type):
    coeff_bank=[1,2,3,4,5,6,7,8,-2,-3,-4,-5,-6]
    inner1=coeff_bank[random.randint(0,len(coeff_bank)-1)]
    inner2=coeff_bank[random.randint(0,len(coeff_bank)-1)]
    onerand=random.randint(0,1)
    tworand=random.randint(0,5)
    if onerand==1 and tworand!=0:
      inner='(x+%d)'%inner2
      inner1=1
    elif onerand==1 and tworand==0:
      inner='x'
      inner1=1
      inner2=0
    else: inner='(%d*x+%d)'%(inner1,inner2)

    inner=inner.replace('+-','-')
    center='-%d/%d'%(inner2,inner1)
    c=-float(inner2)/float(inner1)
    bank={}#radius,bounds
    bank['{%s^n}{2^n}']=[2,'()','div']
    bank['{%s^n}{3^n}']=[3,'()','div']
    bank['{n\cdot %s^n}{5^n}']=[5,'()','div']
    bank['{%s^n}{n\cdot 4^n}']=[4,'[)','div']
    bank['%s^n\cdot 2^n']=[.5,'[)','div']
    #bank['{%s^n}{n!}}']=[infity,'[)','infty']


    if onerand==0: 
      probtype='radius'
    else: 
      probtype='interval'

    prob=bank.keys()[random.randint(0,len(bank)-1)]
    [radius,bounds,div]=bank[prob]
    if div=='div':
      
      top = abs(bank[prob][0])
      bottom = abs(int(inner1))
      rfloat = float(top)/float(bottom)

      div = fractions.gcd(top,bottom)
      if bottom==div:
        radius = top/div
      else:  
        radius = '%d/%d'%(top/div,bottom/div)
      
      prob=prob%inner
    if div=='ipoint':
      probtype='interval'
    if prob[0]+prob[-1]=='{}':
      prob='\displaystyle\\frac'+prob
    if probtype=='interval':
      self.answer='%s %g, %g %s'%(bounds[0], c-rfloat, c+rfloat, bounds[1])
    elif probtype=='radius':
      self.answer='%s'%radius
    prob=prob.replace('*','\cdot ')
    self.problem=('Find the %s of convergence for the power series $\displaystyle\sum_{n=0}^{\infty}{%s}$.')%(probtype,prob)
    self.anstex=('The %s of convergence is $%s$.')%(probtype,self.answer)

#if it starts with {, then append \displaystyle\frac to the front

# Define a main()
def main():
  #variable=series('psum')
  options=sys.argv[1]
  #options='0010000'
  if int(options)==0: options='1'+options[1:]
  #0'Sequences',
  #1'Geometric Series',
  #2'Convergence Tests',
  #3'Power Series with IOC',
  #4'Taylor Series'
  #Eventually add Fourier...
  master_bank={}

  pick=[]
  for i in range(len(options)):
    if options[i]=='1':pick.append(i)
  type=pick[random.randrange(0,len(pick))]

  #type=4
  if type==0:
  #sequence
    sequence={}
#    subtype=random.randint(0,1)

    #sequence['Find the first four terms of the sequence $s_n=n^3$ for $n>=1$ (separate terms with a comma).']=['','(1,8,27,64)','',1]

    sequence['Given the sequence $s_n=n^3-2$ for $n>0$, find $s_5$.']=['$s_5=$','123','',2]
    sequence['Given the sequence $s_n=\cos(\pi\cdot n)$ for $n>0$, find $s_3$.']=['$s_3=$','-1','',2]

    sequence['Given the sequence $s_n=2\cdot s_{n-1}+1$ for $n\ge 1$ and $s_0=2$, find $s_4$.']=['$s_4=$','95','',2]
    sequence['Given the sequence $s_n=s_{n-1}+s_{n-2}$ for $n\ge 2$ and $s_0=s_1=1$, find $s_7$.']=['$s_7=$','21','',2]

    sequence['Find the next term in the sequence $1,3,6,10,...$.']=['','15','',2]
    sequence['Find the next term in the sequence $1,5,12,22,...$.']=['','35','',2]
    sequence['Find the next term in the sequence $2,4,10,28,...$.']=['','82','',2]
    sequence['Find the next term in the sequence $2,5,9,17,...$.']=['','33','',2]
    sequence['Find the next term in the sequence $1,1,2,3,5,...$.']=['','8','',2]
    sequence['Find the next term in the sequence $0,2,2,4,6,10,...$.']=['','16','',2]
    sequence['Find the next term in the sequence $1,1,1,3,5,9,17,...$.']=['','31','',2]

    prob=sequence.keys()[random.randint(0,len(sequence)-1)]
    if sequence[prob][2]==1:
      sequence[prob][1]=sequence[prob][2][1:-1]
    anstex='The answer is %s $%s$'%(sequence[prob][0],sequence[prob][1])
    master_bank[prob]=[sequence[prob][0],sequence[prob][1],sequence[prob][2],anstex]

  geometric={}
  if type==1:
  #options[1]=geometric series
    subtype=random.randint(1,2)
    if subtype==1:
      type='infsum'
    else: type="psum"
    foo=series(type)
    master_bank[foo.problem]=['',foo.sum,'']

  converge={}
  if type==2:
  #options[2]=converge
    probprefix='Determine if the following series converges'
    options=['Converges absolutely','Converges conditionally','Diverges']

    #p test
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n}}']=[3,'$p$-series']
    converge['\sum_{n=1}^{\infty}{\\frac{1}{\sqrt{n}}}']=[3,'$p$-series']
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n^2}}']=[1,'$p$-series']
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n^{1.1}}}']=[1,'$p$-series']

    #direct comparison and limit comparison
    converge['\sum_{n=1}^{\infty}{\\frac{1}{(n-2)^2}}']=[1,'direct comparison']
    converge['\sum_{n=1}^{\infty}{\\frac{1}{(n+1)^{4/3}}}']=[1,'limit comparison']
    converge['\sum_{n=1}^{\infty}{\\frac{\sin{n}}{n^2}}']=[1,'limit comparison']

    converge['\sum_{n=1}^{\infty}{\\frac{1}{\sqrt{n+1}\sqrt{n} }}']=[3,'limit comparison']
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n+1}}']=[3,'direct comparison']
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n-2}}']=[3,'limit comparison']

    #integral test
    converge['\sum_{n=1}^{\infty}{\\frac{n}{(n^2+3)^2}}']=[1,'integral']
    converge['\sum_{n=1}^{\infty}{\\frac{ 1 }{n\cdot\ln(n)}}']=[3,'integral']
    converge['\sum_{n=1}^{\infty}{\\frac{ \ln(n) }{n}}']=[3,'integral']

    #alternating (include absolute or conditional convergence)
    #IF ALTERNATING FAILS (3), DONT USE ALTERNATING AS WHY IF POSSIBLE
    converge['\sum_{n=1}^{\infty}{\\frac{(-1)^n}{n}}']=[2,'alternating series','$p$-series']
    converge['\sum_{n=1}^{\infty}{\\frac{(-1)^n}{n^2}}']=[1,'$p$-series']
    converge['\sum_{n=1}^{\infty}{\\frac{(-1)^n}{\sqrt{n}}}']=[2,'alternating series','$p$-series']
    converge['\sum_{n=1}^{\infty}{(-1)^n\cdot\sin(\pi n)}']=[3,'divergence']
    #converge['\sum_{n=1}^{\infty}{\\frac{(-1)^n}{n^2}}']=[2,'alternating series','$p$-series']

    #ratio test
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n!}}']=[1,'ratio']
    converge['\sum_{n=1}^{\infty}{\\frac{2^n}{n!}}']=[1,'ratio']
    converge['\sum_{n=1}^{\infty}{\\frac{n!}{100^{2n}}}']=[3,'ratio']

    #root test
    converge['\sum_{n=1}^{\infty}{\\frac{1}{n^n}}']=[1,'root']
    converge['\sum_{n=1}^{\infty}{\\frac{99^n}{100^n}}']=[1,'root']
    converge['\sum_{n=1}^{\infty}{\left(\\frac{1-n}{n^2}\\right)^n}']=[1,'root']
    converge['\sum_{n=1}^{\infty}{\left(\\frac{n^n}{n!}\\right)^n}']=[3,'root']
    converge['\sum_{n=1}^{\infty}{\left(\\frac{n!}{2^n}\\right)^n}']=[3,'root']


    prob=converge.keys()[random.randint(0,len(converge)-1)]
    problem=probprefix+' $\displaystyle%s$.'%prob
    answer=converge[prob][0]
    hint='<b>Hint:</b> Try using the %s test.' % converge[prob][1]
    prefix=''
    if answer==1:
      anstex= 'The sum converges absolutely by the %s test.' %(converge[prob][1])
    if answer==2:
      anstex='The sum converges conditionally by the alternating series test but the sum of the absolute values of the terms diverges by the %s test.' %(converge[prob][2])
    if answer==3:
      result= 'diverges'
      anstex='The sum %s by the %s test.' %(result,converge[prob][1])
  power={}
  if type==3:
  #options[3]=Power Series and ioc
    foo=power_series('interval')
    #print foo.problem
    #print foo.answer
    master_bank[foo.problem]=['',foo.answer,'',foo.anstex]

  taylor={}
  if type==4:
  #options[4]=Taylor Series
    #identify
    taylor['Identify the function represented by Taylor Series $f(x)=1-\displaystyle\\frac{x^2}{2}+\displaystyle\\frac{x^4}{24}-...$']=['$f(x)=$','cos(x)','']
    taylor['Identify the function represented by Taylor Series $f(x)=x-\displaystyle\\frac{x^3}{6}+\displaystyle\\frac{x^5}{120}+...$']=['$f(x)=$','sin(x)','']
    taylor['Identify the function represented by Taylor Series $f(x)=1+x+\displaystyle\\frac{x^2}{2}+\displaystyle\\frac{x^3}{6}+...$']=['$f(x)=$','e^x','']
    taylor['Identify the function represented by Taylor Series $f(x)=1+x+x^2+x^3+...$ for $ - 1 < x < 1 $.']=['$f(x)=$','1/(1-x)','This is a geometric series']
    taylor['Identify the function represented by Taylor Series $f(x)=x-\displaystyle\\frac{x^2}{2}+\displaystyle\\frac{x^3}{3}-\displaystyle\\frac{x^4}{4}+...$ for $ - 1 < x < = 1 $']=['$f(x)=$','ln(x+1)','This is closely related to a geometric series']
    taylor['Identify the function represented by Taylor Series $f(x)=x-\displaystyle\\frac{x^3}{3}+\displaystyle\\frac{x^5}{5}-\displaystyle\\frac{x^7}{7}+...$ for $ - 1 < x < 1 $']=['$f(x)=$','atan(x)','This is closely related to a geometric series']

    #taylor series
    #e
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=e^x$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$e^x\\approx$','1+x+x^2/2+x^3/6','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=e^{-x}$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$e^{-x}\\approx$','1-x+x^2/2-x^3/6','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=e^{-x^2}$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$e^{x^2}\\approx$','1-x^2+x^4/2-x^6/6','']
#do a few not centered at x=0
    #sin cos
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\sin(x)$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$\sin(x)\\approx$','x-x^3/6+x^5/120-x^7/5040','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\cos(x)$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$\cos(x)\\approx$','1-x^2/2+x^4/24 -x^6/720','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\sin(x)$ at $x=2$ (separate the terms with a "+" or "-" sign).']=['$\sin(x)\\approx$','sin(2)+cos(2)*(x-2)-sin(2)*(x-2)^2-cos(2)*(x-2)^3','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\cos(x)$ at $x=1$ (separate the terms with a "+" or "-" sign).']=['$\cos(x)\\approx$','cos(1)-sin(1)*(x-1)-cos(1)*(x-1)^2+sin(1)*(x-1)^3','']

    #geo series
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\\frac{1}{1-x}$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$\\frac{1}{1-x}\\approx$','1+x+x^2+x^3','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\\frac{1}{1+x}$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$\\frac{1}{1+x}\\approx$','1-x+x^2-x^3','']
    #ln/geo
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\ln(x+1)$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$\ln(x)\\approx$','x-x^2/2+x^3/3-x^4/4','']
    taylor['Find the first 4 terms of the Taylor Series for $f(x)=\ln(\\frac{x+1}{1-x})$ at $x=0$ (separate the terms with a "+" or "-" sign).']=['$\ln\left(\\frac{x+1}{1-x}\\right)\\approx$','2*(x+x^3/3+x^5/5+x^7/7)','You can either take the derivative or use a logartihm rule to simplify the expression into two geometric series']

    #taylor polynomial
    taylor['Find the third degree polynomial Taylor polynomial that approximates $f(x)=\sin(x)$ at $x=0$']=['$\sin(x)\\approx$','x-x^3/6','']
    taylor['Find the third degree polynomial Taylor polynomial that approximates $f(x)=\\tan(x)$ at $x=0$']=['$\\tan(x)\\approx$','x+x^3/3','']
  master_bank.update(taylor)
  #print len(master_bank)
  if type!=2:
    rand1=random.randint(0,len(master_bank)-1)
    problem=master_bank.keys()[rand1]
    prefix=master_bank[problem][0]
    answer=master_bank[problem][1]
    hint=master_bank[problem][2]
    if len(master_bank[problem])==4:
      anstex=master_bank[problem][3]
    else:
      anstex='The answer is %s $%s$.'%(prefix,toTEX(answer))
  suffix=''
  print problem
  print answer
  print anstex
  print prefix
  print suffix
  print hint
  if type==2:
    print 1
    for option in options: print option
  #dftex=toTEX(df)
  #print df
  #print dftex

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
