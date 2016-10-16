#!/usr/bin/python -tt
# -*- coding: cp1252 -*-
import sys
import random
import math
from math import *
import re
import latex
from latex import *
import partial
import vector

#sys.path.append('/home4/maverick/lib/python2.6/site-packages/sympy') 

def is_int(a):
  try:
    int (a)
    return True
  except:
    return False

def reduce(original):

  #NEEDS TO TAKE EVERY NUMBER AND ADD A '.'
  str_replace={}
  str_replace['csc']='1/sin'
  str_replace['sec']='1/cos'
  str_replace['cot']='1/tan'
  str_replace['arc']='a'
  str_replace['ln']='log'
  string=original

  for i in range(1):
    if len(string)<=1:
      return original
    s=string
    for kv in str_replace.keys():
      val=str_replace[kv]
      s=re.sub('(?i)'+kv,val,s)
    new=''
    for j in range(len(s)):
      c=s[j]
      if c=='^': new += '**'
      else: new+=c

    string=new
    new=''
    s=string

    trigger=True
    for j in range(len(s)):
      if j<len(s)-1:
        if s[j]=='.' and is_int(s[j+1]): trigger=False
        elif is_int(s[j]) and s[j+1]=='.': trigger=False
      if is_int(s[j]):
        if j==0:
          if is_int(s[0]) and is_int(s[1])==0 and trigger==True: new+=s[0]+'.'
          else: new+=s[j]
        elif j==len(s)-1:
          if is_int(s[j]) and is_int(s[j-1])==0 and s[j-1]!='.' and trigger==True: new+=s[j]+'.'
          else: new+=s[j]
        else:
          if is_int(s[j-1])==0 and is_int(s[j+1])==0 and s[j-1]!='.'and trigger==True: new += s[j]+'.'
          else: new+=s[j]
      else: new+=s[j]

  return new

class integral(object):
  def __init__(self,type):
    bank={}
    if type=='double':

      #simple, poly, trans, trig
      bank[0]=['x^2*y^2',('0','1-y'),('0','5'),'xy','-4625/12']
      bank[1]=['4*x + 2',('x^2','2x'),('0','2'),'yx','8']
      bank[2]=['x*y',('x^2','\sqrt{x}'),('0','1'),'yx','1/12']
      bank[3]=['x*y',('0','4 - y^2'),('-2','2'),'xy','0']
      bank[4]=['x+y',('0','x^2'),('0','1'),'yx','7/20']

      bank[5]=['y+ln(x)',('1','y^2'),('1','2'),'xy','ln(256) - 33/8']

      bank[6]=['x',('0','\sin(x)'),('0','pi'),'yx','pi']
      bank[7]=['sin(x)*y',('0','1'),('0','pi'),'yx','1']

      #turns into u sub
      bank[8]=['y^2*e^(x*y)',('0','y'),('0','1'),'xy','e/2 - 1']
      bank[9]=['e^(x^5)',('0','x^4'),('0','1'),'yx','e/5 - 1/5']
      bank[10]=['e^{y/x}',('0','x^3'),('0','1'),'yx','e/2-1']
      bank[11]=['cos(y/x^2)',('0','x^5'),('0','\sqrt[3]{pi}'),'yx','2/3']

      #simplified with change of variable
      #four here
      bank[12]=['sin(y^3)',('\sqrt{x}','2'),('0','4'),'yx','1/3 - cos(8/3)']
      bank[13]=['3*x^2*sin(x*y)',('2y','2'),('0','1'),'xy','6 - 3*sin(2)']
      bank[14]=['e^x/x',('y','1'),('0','1'),'xy','1']

      #Word Problem
      bank[15]=['Find the volume below the the surface $z=x^2+y^2$ and the above $z=0$ on $x=[-1,1]$ and $y=[-1,2]$.','8','']
      bank[16]=['Find the volume below the the surface $z=\sin(x)\cdot\sin(y) + 2$ and the above $z=0$ on $x=[0,\pi]$ and $y=[0,\pi]$.','2*pi^2+4','']
      #two more
      #bank[12]=['',('0','y'),('0','1'),'xy','ans']

      dotr='double'

    elif type=='polar':
      bank[0]=[' ',('-\sqrt{1 - y^2}','\sqrt{1 - y^2}'),('-1','1'),'xy','pi']
      bank[1]=[' ',('0','\sqrt{4 - y^2}'),('0','2'),'xy','4*pi']
      bank[2]=[' ',('0','\sqrt{1-(y-1)^2}'),('0','2'),'xy','pi']
      bank[3]=['y',('0','(1 - y^2)^{1/2}'),('0','1'),'xy','1/3']
      bank[4]=['x^2',('-(1 - x^2)^{1/2}','(1 - x^2)^{1/2}'),('-1','1'),'yx','pi/4']
      bank[5]=['1/(x^2+y^2)^{1/2}',('-(1 - x^2)^{1/2}','(1 - x^2)^{1/2}'),('-1','1'),'yx','2*pi']
      bank[6]=['y^2',('0','\sqrt{4 - x^2}'),('-2','2'),'yx','2*pi']
      bank[7]=['x^3',('0','\sqrt{4 - y^2}'),('0','2'),'xy','64/15']

      bank[8]=['Find the area of the region bounded by the curve $r^2=9\sin(3\\theta)$ on $\\theta=[0,\pi/3]$.','3','']
      bank[9]=['Evaluate the integral $\displaystyle\iint\limits_A{e^{x^2+y^2}\ dA}$ where $A$ is the origin-centered unit circle.','(e-1)*2*pi','']
      bank[10]=['Evaluate the integral $\displaystyle\iint\limits_A{\sin(x^2+y^2)\ dA}$ where $A$ is the region bounded above by $y=\sqrt{4-x^2}$ and below by $y=x$ and $y=-x$.','pi/2*sin(2)^2','']
      bank[11]=['Evaluate the integral $\displaystyle\iint\limits_A{x^2+y^2+1\ dA}$ where $A$ is the origin-centered unit circle.','3/2*pi','']
      bank[12]=['Evaluate the integral $\displaystyle\iint\limits_A{\\frac{1}{x^2}\ dA}$ where $A$ is the region $1\leq x^2+y^2\leq 4$ and $0\leq\\theta\leq\pi/4$.','ln(2)','']
      bank[13]=['Evaluate the integral $\displaystyle\iint\limits_A{xy\ dA}$ where $A$ is the region $x^2+y^2\leq 4$ and $0\leq\\theta\leq\pi/2$.','2','']
      
      #Word problems
      #2
    elif type=='triple':
      #cubic regions
      bank[0]=['x*y*z',('-3','2'),('-2','3'),('-2','1'),'xyz','75']
      bank[1]=['z + y*sin(x)',('0','pi/2'),('-1','1'),('-1','4'),'xyz','(15*pi)/2']
      bank[2]=['x*y*z',('0','3'),('0','1'),('0','2'),'xzy','9/2']
      bank[3]=['x^2*y+z',('0','1'),('0','1'),('0','1'),'xyz','2/3']

      #non-cubic, usub

      #Word Problems
      bank[4]=['Find the volume of the region in the first quadrant bounded by the plane $x+6y+3z=6$','4','']
      bank[5]=['Find the volume of the region in the first quadrant bounded by the plane $2x+y+7z-6=0$','36/7','']
      bank[6]=['Find the volume of the region bounded by the planes $z=0$, $z=1-y$, $z=1+y$, $x=2$, and $x=-3$.','5','']
      bank[7]=['Find the volume of the region above $z=0$ and below $z=e^{x+y}$ over the region $x,y=[-1,1]$.','e^2+e^(-2)-2','']
      bank[8]=['Find the volume of the region bounded by $z=y^2$, $z=4$ $x=-1$ and $x=1$.','128/3','']
      bank[9]=['Find the volume of the region bounded by $z=x^2$, $z=4x-3$ $y=-1$ and $y=1$.','160/3','']

    #p=rho, ph=phi, t=theta,
    elif type=='sphercyn':
      bank[0]=['h*sin(ff)',('0','2*\sin(ff)'),('0','pi'),('0','pi'),'hfg','(8*pi)/3']
      bank[1]=['h',('0','2'),('0','2*pi'),('0','pi'),'hfg','4*pi^2']
      bank[2]=['r',('r^4 - 1','4 - 4*r^2'),('0','1'),('0','2\cdot pi'),'zhg','(8*pi)/3']
      bank[3]=['',('-\sqrt{1- y^2 - z^2}','\sqrt{1- y^2 - z^2}'),('\sqrt{1-z^2}','\sqrt{1- z^2}'),('-1','1'),'xyz','4*pi/3']
      bank[4]=['',('-\sqrt{1- y^2}','\sqrt{1- y^2}'),('-1','1'),('-1','3'),'xyz','4*pi']
      bank[5]=['',('0','\sqrt{x^2+y^2}'),('-\sqrt{1-x^2}','\sqrt{1-x^2}'),('-1','1'),'zyx','4*pi']


    pick=random.randint(0,len(bank)-1)
    #print pick, bank[pick]
    if len(bank[pick])==3:
      self.problem=bank[pick][0]
      self.ans=bank[pick][1]
      hint=bank[pick][2]
      ptype='word'
    else: ptype='bound'
    #print ptype
    if (type=='double' or type=='polar') and ptype=='bound':
      self.ans=bank[pick][4]
      bounds=bank[pick][2]+bank[pick][1]+(toTEX(bank[pick][0]),bank[pick][3][0],bank[pick][3][1])
      self.problem='\int_{%s}^{%s}\int_{%s}^{%s} %s \ d%s \ d%s'%bounds
    elif (type=='sphercyn' or type=='triple') and ptype=='bound':
      self.ans=bank[pick][5]
      bounds=bank[pick][3]+bank[pick][2]+bank[pick][1]+(toTEX(bank[pick][0]),bank[pick][4][0],bank[pick][4][1],bank[pick][4][2])
      bounds=bank[pick][3]+bank[pick][2]+bank[pick][1]+(toTEX(bank[pick][0]),bank[pick][4][0],bank[pick][4][1],bank[pick][4][2])
      self.problem='\int_{%s}^{%s}\int_{%s}^{%s}\int_{%s}^{%s} %s \ d%s \ d%s \ d%s' %bounds
    if type=='sphercyn':
      self.problem=self.problem.replace('h','\\rho')
      self.problem=self.problem.replace('ff','\phi')
      self.problem=self.problem.replace('df','d\phi')
      self.problem=self.problem.replace('g','\\theta')
    if ptype=='bound':
      self.problem=self.problem.replace('pi','\pi')
      self.problem=self.problem.replace('*','\cdot ')
      self.problem=self.problem.replace('\int','\displaystyle\int ')
      self.problem='Evaluate the integral $%s$.'%self.problem
def ln(x):
  return math.log(x)

# Define a main()
def main():
  options=sys.argv[1]
  #options='010000000'
  if int(options)==0: options='1'+options[1:]
  options=options[0:4]+'0'+options[4:10] #extrema
  options=options[0:10]+'0'+options[10]  #work,circulation,flux
  pick=[]
  for i in range(len(options)):
    if options[i]=='1':pick.append(i)
  type1=pick[random.randrange(0,len(pick))]

  #type1=2
#Derivatives
  #0 Partial Derivatives
  #1 Chain Rule
  #2 Directional,  and (need to be added) gradient, Tangent Planes
  #3 Lagrange Multipliers
  ####4 Extrema
#Integrals
  #5-7 Multiple (rectangular, polar, combine spherical/cylindrical) Integrals
#Vectors
  #8 divergence and curl
  ####9 Line Integrals
  ####10 Work, Circulation, Flux
  #11 potential functions

  #Add later
  #4 Extrema and Saddle Points
  #7'Green’s Theorem'
  #8'Divergence/Stokes Theorem'
  

  master_bank={}
  #partial derivatives
  if type1==0:
    subtype=random.randint(1,5)
    if subtype<3:
      implicit=partial.partial(2,'mixed')
      func='f(x,y)'
    if subtype>=3:
      implicit=partial.partial(3,'dummy')
      func='f(x,y,z)'
    f=implicit.f
    if subtype==1 or subtype==3:
      ans=implicit.fx
      der='f_x'
    if subtype==2 or subtype==4:
      ans=implicit.fy
      der='f_y'
    if subtype==5:
      ans=implicit.fz
      der='f_z'
    probtex='Given the function $'+func+'='+frac(toTEX(f))+'$, find $'+der+'$.'
    prefix='$'+der+'=$'
    anstex='The answer is $'+der+'='+frac(toTEX(ans))+'$'
    prefix=''
    hint=''

#Chain Rule
  if type1==1:
    subtype=random.randint(1,4)
    if subtype%2==0:
      option='t'
    else:
      option='uv'
    uorv=random.randint(0,len(option)-1)
    der='f_%s'%option[uorv]
    if subtype<3:
      implicit=partial.partial(2,'short')
      implicit.tuv(option,2)
      f=[implicit.fx,implicit.fy]
      func='f(x,y)'
      df='('+f[0]+')'+'*'+implicit.dtuv[0][uorv]+'+'+'('+f[1]+')'+'*'+implicit.dtuv[1][uorv]
      df=df.replace('x','('+implicit.tuv[0]+')')
      df=df.replace('y','('+implicit.tuv[1]+')')
    if subtype>=3:
      implicit=partial.partial(3,'short')
      f=[implicit.fx,implicit.fy,implicit.fz]
      implicit.tuv(option,3)
      func='f(x,y,z)'
      df='('+f[0]+')'+'*'+implicit.dtuv[0][uorv]+'+'+'('+f[1]+')'+'*'+implicit.dtuv[1][uorv]+'+'+f[2]+'*'+implicit.dtuv[2][uorv]
      df=df.replace('x',implicit.tuv[0])
      df=df.replace('y',implicit.tuv[1])
      df=df.replace('z',implicit.tuv[2])
    if subtype==1: probtex='Given the function $'+func+'='+toTEX(implicit.f)+'$, <br>with $x(u,v)='+toTEX(implicit.tuv[0])+'$ and $y(u,v)='+toTEX(implicit.tuv[1])+'$ find $'+der+'$.'
    if subtype==2: probtex='Given the function $'+func+'='+toTEX(implicit.f)+'$, <br>with $x(t)='+toTEX(implicit.tuv[0])+'$ and $y(t)='+toTEX(implicit.tuv[1])+'$ find $'+der+'$.'
    if subtype==3: probtex='Given the function $'+func+'='+toTEX(implicit.f)+'$, <br>with $x(u,v)='+toTEX(implicit.tuv[0])+'$, $y(u,v)='+toTEX(implicit.tuv[1])+'$ and $z(u,v)='+toTEX(implicit.tuv[2])+'$ find $'+der+'$.'
    if subtype==4: probtex='Given the function $'+func+'='+toTEX(implicit.f)+'$, <br>with $x(t)='+toTEX(implicit.tuv[0])+'$, $y(t)='+toTEX(implicit.tuv[1])+'$ and $z(t)='+toTEX(implicit.tuv[2])+'$ find $'+der+'$.'
    

    import sympy 
    from sympy.parsing.sympy_parser import parse_expr
    t, u, v, x, y, z = sympy.symbols('t u v x y z')
    df=df.replace('^','**')
    sympy_exp = parse_expr(df)
    ans=str(sympy_exp)
    ans=ans.replace('**','^')
    ans=ans.replace('log','ln')
    
    #ans=df
    prefix='$'+der+'=$'
    anstex='The answer is $'+der+'='+toTEX(ans)+'$'
    prefix=''
    hint=''

#Directional Derivatives
  if type1==2:
    subtype=random.randint(1,2)
    if subtype==1:
      grad=partial.partial(2,'mixed')
      vect=vector.vector(2)
      (x,y)=vect.point
      evalfx=grad.fx.replace('^','**')
      evalfy=grad.fy.replace('^','**')
      evalfx=evalfx.replace('x',str(vect.point[0]))
      evalfy=evalfy.replace('y',str(vect.point[1]))
      totalder=(eval(reduce(evalfx)),eval(reduce(evalfy)))
      func='f(x,y)'
      probtex='Given the function $'+func+'='+toTEX(grad.f)+'$, find the derivative at $(%d,%d)$ in the direction $ \left\langle %d,%d \\right\\rangle $.'% tuple(vect.point+vect.vec1)
    if subtype==2:
      grad=partial.partial(3,'dummy')
      vect=vector.vector(3)
      (x,y,z)=vect.point
      grad.fx=grad.fx.replace('x',str(vect.point[0]))
      grad.fy=grad.fy.replace('y',str(vect.point[1]))
      grad.fz=grad.fz.replace('z',str(vect.point[2]))
      totalder=(eval(reduce(grad.fx)),eval(reduce(grad.fy)),eval(reduce(grad.fz)))
      func='f(x,y,z)'
      probtex='Given the function $'+func+'='+toTEX(grad.f)+'$, find the derivative at $(%d,%d,%d)$ in the direction $\left\langle %d,%d,%d \\right\\rangle$.'% tuple(vect.point+vect.vec1)
    roundlim=4
    ans=str(float(vector.Dot(totalder,vect.vec1))/float(vect.norm1))
    ans=str(round(vector.Dot(totalder,vect.vec1)/vect.norm1,roundlim))
    prefix=''
    anstex='The answer is %s $ %s $.'%(prefix,toTEX(ans))
    hint=''

# Lagrange Multipliers
  if type1==3:
    bank={}
    #bank['problem']=['ans','prefix','hint','anstex'] 
    bank['Find the maximum volume of a box with a surface area of $24$.']=['8','$V=$','Optimize $f=xyz$ constrained by $g=2xy+2yz+2xz-24=0$.'] 
    bank['Find the maximum volume contained by a box with a surface area of $12$ with the top missing (5 sides).']=['4','$V=$','Optimize $f=xyz$ constrained by $g=2xy+2yz+xz-12=0$.'] 
#more geo? cylinder?
    bank['Find the maximum volume of a cylinder inscribed in a sphere with radius $r_s=5$.']=['32*pi','$V=$','Use the constraint $r_s=\sqrt{r^2+(h/2)^2}$.'] 
    bank['Find the maximum volume of a rectangular prism inscribed in a sphere with a diameter $d_s=3$.']=['1','$V=$','Use the constraint $d_s=\sqrt{x^2+y^2+z^2}$.'] 

    bank['Maximize the equation $f=xy$, subject to the constraints $x,y>0$ and $x^2+4y^2=50$.']=['25/2','',''] 
    bank['Maximize the equation $f=xy$, subject to the constraint $x+4y=16$.']=['16','',''] 
    
    bank['Maximize the equation $f=xy^3z$, subject to the constraints $x,y,z>0$ and $x+y+z=5$.']=['27','',''] 
    bank['Maximize the equation $f=xy\sqrt{z}$, subject to the constraints $x,y,z>0$ and $x+y+z=20$.']=['128','',''] 
    bank['Maximize the equation $f=x^2+y^2+z^2$, subject to the constraints $x,y,z>0$ and $x+y+z=6$.']=['12','',''] 
    
    bank['Maximize the equation $2x-3y$ subject to the constraint $x^2+y^2=13$.']=['13','',''] 
    bank['Maximize the equation $3x-y$ subject to the constraint $x^2+y^2=40$.']=['20','',''] 
    bank['Minimize the equation $x-2y$ subject to the constraint $x^2+y^2=45$.']=['15','',''] 
   
    bank['Find the minimum distance from the surface $xyz=1$ to the origin']=['3^(1/2)','','Let $f=x^2+y^2+z^2$'] 
    bank['Find the minimum distance from the surface $x^2y=1$ to the origin']=['(2^(1/3)+2^(-2/3))^(1/2)','',''] 
    bank['Find the minimum distance from the surface $x^3y=1$ to the origin']=['(3^(1/4)+3^(-3/4))^(1/2)','',''] 


#to finish (2 each)
    bank['Find the maximum value of $x+y+z$ if the points lie on the sphere $x^2+y^2+z^2=5$.']=['ans','prefix','hint','anstex'] 
    #bank['Find the point on the plane $$ closest to the point $$.']=['ans','prefix','hint','anstex'] 

    probtex=random.choice(bank.keys())
    ans_set=bank[probtex]
    ans=ans_set[0]
    prefix=ans_set[1]
    hint=ans_set[2]
    if len(ans_set)==3:
      if prefix!='': prefix+=' '
      anstex='The answer is %s$%s$.'%(prefix,toTEX(ans))
    else: anstex=ans_set[3]

#Extrema
  if type==4:
    pass

#Multiple Integrals
  if type1==5 or type1==6 or type1==7:
    if type1==5:
      rando=random.randint(1,4)
      if rando==1: type2='triple'
      else: type2='double'
    elif type1==6: #polar
      type2='polar'
    elif type1==7: #cylindrical integrals
      type2='sphercyn'
    intprob=integral(type2)
    probtex=intprob.problem
    ans=intprob.ans
    anstex='The answer is $%s$.'%toTEX(ans)
    prefix=''
    hint=''
#Divergence and Curl
  if type1==8:
    dc=partial.divcurl()
    subtype=random.randint(1,2)
    if subtype==1:
      dc.prob='divergence'
      ans=dc.div
      anstex='The divergence is $'+toTEX(ans)+'$.'
    if subtype==2:
      dc.prob='curl'
      ans='<%s,%s,%s>'%(dc.curl[0],dc.curl[1],dc.curl[2])
      anstex='The curl is $ \left\langle %s, \ %s, \ %s \\right\\rangle $.'% (toTEX(dc.curl[0]) , toTEX(dc.curl[1]) , toTEX(dc.curl[2]))
    dcftex=[]
    for i in range(3):dcftex.append(toTEX(dc.f[i]))
    probtex='Find the '+dc.prob+' of the field described by $ \left\langle %s,%s,%s \\right\\rangle $.'% tuple(dcftex)
    prefix=''
    hint=''


#Line Integrals
  if type1==9:
    bank={}
    #answer, prefix, hint
    #circle x,y
    bank['Evaluate the integral $\int_C{xy^2 \ ds}$ where $C$ is the path from $(2,0)$ to $(0,2)$ clockwise on $x^2+y^2=4$.']=['16/3','','']
    bank['Evaluate the integral $\int_C{xy \ ds}$ where $C$ is the clockwise path from $\\theta=0$ to $\\theta=\pi/2$ on the unit circle.']=['1/2','','']
    bank['Evaluate the integral $\int_C{\\frac{1}{x^2} \ ds}$ where $C$ is the clockwise path from $\\theta=0$ to $\\theta=\pi/4$ on the unit circle.']=['1','','']
    bank['Evaluate the integral $\int_C{\\frac{y}{x}\cdot \\frac{1}{x^2} \ ds}$ where $C$ is the clockwise path from $\\theta=0$ to $\\theta=\pi/3$ on the unit circle.']=['1','','After substituting $x(t)=\cos(t)$ and $y(t)=\sin(t)$, you can put the integrand in the form $\sec^2(t)\\tan(t)$, or $\sin(t) / \cos^3(t)$, either of which can be integrated with $u$-substitution.']

    #line segment
    bank['Evaluate the integral $\int_C{x-y^2z \ ds}$ where $C$ is the line segment from $(0,0,0)$ to $(2,1,2)$.']=['3/2','','']
    bank['Evaluate the integral $\int_C{\pi\cdot\sin(\pi x)-xy \ ds}$ where $C$ is the line segment from $(0,0)$ to $(3,4)$.']=['-50/3','','']
    bank['Evaluate the integral $\int_C{xy+z \ ds}$ where $C$ is the line segment from $(-2,-1,0)$ to $(1,3,12)$.']=['169/2','','']
    bank['Evaluate the integral $\int_C{\\frac{x}{y}+z \ ds}$ where $C$ is the line segment from $(1,2,1)$ to $(3,6,5)$.']=['21','','']
    bank['Evaluate the integral $\int_C{\\frac{z}{xy} \ ds}$ where $C$ is the line segment from $(1,2,3)$ to $(2,3,5)$.']=['sqrt(6)*ln(3)','','']
    bank['Evaluate the integral $\int_C{x\cdot\sin(y) \ ds}$ where $C$ is the line segment from $(0,0)$ to $(1,\pi)$.']=['1/pi*sqrt(pi^2 + 1)','','']

    #more complex
    bank['Evaluate the integral $\int_C{ds}$ where $C$ is the path from $(0,0)$ to $(1,1)$ on $y=x^4$.']=['(17^(3/2)-1)/144','','']
    """
    master_bank['Find the arc length of the curve $y=.75*x$ from $x=0$ to $x=5$.']=['','6.25','']
    master_bank['Find the arc length of the curve $y=(x+5)^{3/2}$ from $x=0$ to $x=8$.']=['','988/27','']
    master_bank['Find the arc length of the curve $y=\sinh(x)$ from $x=0$ to $x=1$.']=['','(e^2-1)/(2*e)','']

    master_bank['Find the arc length of the parametric curve $x=\cos(t)$ $y=\sin(t)$ from $t=0$ to $t=\pi$']=['','pi','']
    master_bank['Find the arc length of the parametric curve $x=t^{3/2}$ $y=t$ from $t=0$ to $t=1$']=['','61/27','']
    master_bank['Find the arc length of the parametric curve $x=3*t^2$ $y=1/2*t^3$ from $t=0$ to $t=3$']=['','30.5','']
    master_bank['Find the arc length of the parametric curve $x=t^3$ $y=t^{4.5}$ from $t=0$ to $t=1$']=['','1.43971','']

    """

    #helix
    bank['Evaluate the integral $\int_C{ xy^2+z \ ds}$ where $C$ is the path along the helix  $\\vec{r}(t)=\langle\cos(t), \sin(t), t \\rangle$ for $t=[0,2\pi]$.']=['2*sqrt(2)*pi^2','','You may need to use the identity $\sin^2(x)+\cos^2(x)=1$.']
    bank['Evaluate the integral $\int_C{\displaystyle\\frac{x^2z}{1-y^2} \ ds}$ where $C$ is the path along the helix  $\\vec{r}(t)=\langle\cos(t), \sin(t), t \\rangle$ for $t=[0,2\pi]$.']=['2*sqrt(2)*pi^2','','You may need to use the identity $\sin^2(x)+\cos^2(x)=1$.']
    bank['Evaluate the integral $\int_C{xy+z \ ds}$ where $C$ is the path along the helix  $\\vec{r}(t)=\langle\cos(t), \sin(t), t/2 \\rangle$ for $t=[0,4\pi]$.']=['2*sqrt(5)*pi^2','','You may need to use the identity $\sin^2(x)+\cos^2(x)=1$ and you will need integration by parts.']
    bank['Evaluate the integral $\int_C{x^2 \ ds}$ where $C$ is the path along the helix  $\\vec{r}(t)=\langle\cos(t), \sin(t), 2t \\rangle$ for $t=[0,2\pi]$.']=['pi*sqrt(5)','','You may need to use the identity $\sin^2(x)+\cos^2(x)=1$ and $\cos^2(t)=1/2(\cos(2t)+1)$.']
    #split integrals intdx+intdy+intdz

    probtex=random.choice(bank.keys())
    ans_set=bank[probtex]
    ans=ans_set[0]
    prefix=ans_set[1]
    hint=ans_set[2]
    anstex='The answer is %s $%s$.'%(prefix,toTEX(ans))
    probtex=probtex.replace('\int','\displaystyle\int') 
#Work, Circulation, Flux
  if type1==10:
    pass

#Potential Functions
  if type1==11:
    subtype=random.randint(1,2)
    if subtype==1: #(2 variables)
      grad=partial.partial(2,'mixed')
      func='f(x,y)'
      probtex='Given the conservative vector field $\\vec{F}=\left(%s\\right)\hat{i}+\left(%s\\right)\hat{j}$, find the potential function $f(x,y)$.'%(toTEX(grad.fx),toTEX(grad.fy))
    if subtype==2: #(3 variables)
      grad=partial.partial(3,'dummy')
      func='f(x,y,z)'
      probtex='Given the conservative vector field $\\vec{F}=\left(%s\\right)\hat{i}+\left(%s\\right)\hat{j}+\left(%s\\right)\hat{k}$, find the potential function $f(x,y,z)$.'%(toTEX(grad.fx),toTEX(grad.fy),toTEX(grad.fz))
    prefix='$'+func+'=$'
    suffix=' $+c$ '
    ans=grad.f
    anstex='The answer is %s $%s$.'%(prefix,toTEX(grad.f))
    hint=''
  if type1!=11: suffix=''
  print probtex
  print ans
#  anstex=toTEX(ans)
  print anstex
  print prefix
  print suffix
  print hint
  #dftex=toTEX(df)
  #print df
  #print dftex

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
