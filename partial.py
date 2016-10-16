#-------------------------------------------------------------------------------
# Name:        poly
# Purpose:
#
# Author:      Austin
#
# Created:     16/06/2013
# Copyright:   (c) Austin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import random
class divcurl(object):
  def __init__(self):
    bank={}
    #if numvar==2 and ptype=='poly' or ptype=='mixed':
#     bank['f']=['fx','fy','-fy/fx']
    bank['y^2','x^2','z']=['1','0*i+0*j+(2*x-2*y)*k','']
    bank['ln(x+y)','e^(x*y*z)','sin(x*y)']=['1/(x+y)+x*z*e^(x*y*z)',['(x*cos(x*y)-x*y*e^(x*y*z))','-y*cos(x*y)','(y*z*e^(x*y*z)-1/(x + y))'],'']
    bank['(x^2*y+z)','(x*y*z)','(x-y)']=['2*x*y+x*z',['(-x*y-1)','0','(y*z-x^2)'],'']
    bank['cos(x*y)','(2+x*y^2*z)','(1-z^2)']=['2*x*y*z-y*sin(x*y)-2*z',['-x*y^2','0','(x*sin(x*y)+y^2*z)'],'']
    bank['(x*y-z)','(x+y+z)','x*y*z']=['y+x*y+1',['x*z-1','(-y*z-1)','1-x'],'']
    bank['y*z','x*z','x*y']=['0',['0','0','0'],'']
    bank['y*ln(z)','x*sin(y)+z','x*y']=['x*cos(y)',['x-1','y/z-y','sin(y)-ln(z)'],'']
    bank['x*cos(y)','x+z','z-y']=['cos(y) + 1',['-2','0','x*sin(y) + 1'],'']
    bank['x-cos(y^2)','x+e^z','x*y']=['1',['x-e^z','(-y)','1-2*y*sin(y^2)'],'']
    bank['e^(x*y*z)','x*y','e^(x+2*z)']=['x+2*e^(x+2*z)+y*z*e^(x*y*z)',['0','x*y*e^(x*y*z)-e^(x+2*z)','y-x*z*e^(x*y*z)'],'']
    bank['x^y','y^z','z^x']=['x*z^(x-1)+x^(y-1)*y+y^(z-1)*z',['(-y^z*ln(y))','(-z^x*ln(z))','(-x^y*ln(x))'],'']
    bank['(x+y+z)','z+y*(cos(x^2))^2','tan(x)^2']=['cos(x^2)^2 + 1',['-1','1 - 2*tan(x)*(tan(x)^2 + 1)','- 4*x*y*cos(x^2)*sin(x^2) - 1'],'']
    bank['(x*z+y)^5','(y+z)^x','y/(x*z)']=['x*(y+z)^(x-1)+5*z*(y+x*z)^4-y/(x*z^2)',['1/(x*z) - x*(y + z)^(x - 1)','5*x*(y + x*z)^4 + y/(x^2*z)','ln(y+z)*(y + z)^x-5*(y + x*z)^4'],'']
    bank['e^(x*y*z)','sin(x*y*z)','ln(x*y*z)']=['y*z*e^(x*y*z)+ x*z*cos(x*y*z)+1/z',['1/y-x*y*cos(x*y*z)','x*y*e^(x*y*z) - 1/x','y*z*cos(x*y*z) - x*z*e^(x*y*z)'],'']
    bank['(x+y^2)^5','sin(3*x+y)','4+z']=['5*(y^2 + x)^4 +cos(3*x + y)+ 1',['0','0','3*cos(3*x+y)-10*y*(y^2 + x)^4'],'']
    bank['y+e^(x*y)','e^(x*y)-z','e^(z)']=['e^(z)+x*e^(x*y)+y*e^(x*y)',['1','0','y*e^(x*y)-x*e^(x*y)-1'],'']
    bank['ln(x*y)','ln(x+2*y+3*z)','1/(x+y)']=['1/x + 2/(x + 2*y + 3*z)',['- 1/(x + y)^2 - 3/(x + 2*y + 3*z)','1/(x + y)^2','1/(x + 2*y + 3*z) - 1/y'],'']
    #bank['','','']=['',[],'']
    self.f=bank.keys()[random.randint(0,len(bank)-1)]
    self.div=bank[self.f][0]
    self.curl=bank[self.f][1]
    self.hint=bank[self.f][2]
class partial(object):
  def __init__(self,numvar,ptype):
    bank={}
    if numvar==2 and (ptype=='poly' or ptype=='mixed'):
#     bank['f']=['fx','fy','-fy/fx']
      bank['(1)/(x+y)']=['-(1)/((x+y)^2)','-(1)/((x+y)^2)','-1']
      bank['(x)/(y)']=['(1)/(y)','(-x)/(y^2)','(y)/(x)']
      bank['(x)/(x+y)']=['(y)/((x + y)^2)','(-x)/((x + y)^2)','(y)/(x)']
      bank['(x^2)/(y^2)']=['(2*x)/(y^2)','-(2*x^2)/(y^3)','(y)/(x)']
      bank['(x^2+y^2)^1.1']=['2.2*x*(x^2+y^2)^(.1)','2.2*y*(x^2+y^2)^(.1)','-(x)/(y)']
      bank['(x^4+y^2)^{1/2}']=['((2*x^3))/((x^4 + y^2)^(1/2))','(y)/((x^4 + y^2)^(1/2))','-(2*x^3)/(y)']

    if numvar==2 and (ptype=='trans' or ptype=='mixed'):
      bank['ln(x+y)']=['(1)/(x + y)','(1)/(x + y)','-1']
      bank['ln(x+2*y)']=['(1)/(x + 2*y)','(2)/(x + 2*y)','-1/2']
      bank['e^x*ln(y)+x']=['e^x*ln(y)+1','(e^x)/(y)','-y*(e^(-x) + ln(y))']
      bank['ln(x^2+y^2)']=['(2*x)/(x^2 + y^2)','(2*y)/(x^2 + y^2)','-x/y']
      bank['e^(x^2-y)+y']=['2*x*e^(x^2-y)','1-e^(x^2-y)','(2*x)/(1-e^(y-x^2))']
      bank['ln(y)+e^(x*y)']=['y*e^(x*y)','x*e^(x*y) + 1/y','-(y^2)/(e^(-x*y)+x*y)']
      bank['x^y+y^x']=['y*x^(y-1)+y^x*ln(y)','x*y^(x-1)+x^y*ln(x)','-(y*x^(y-1)+y^x*ln(y))/(x*y^(x-1)+x^y*ln(x))']

    if numvar==2 and (ptype=='trig' or ptype=='mixed'):
      bank['sin(x)*cos(y)']=['cos(x)*cos(y)','-sin(x)*sin(y)','cot(x)*cot(y)']
      bank['sin(x*y+y)']=['y*cos(x*y+y)','(x+1)*cos(x*y+y)','-(y)/(x + 1)']
      bank['(sin(x))/(cos(y))']=['(cos(x))/(cos(y))','(sin(x)*sin(y))/(cos(y)^2)','-cot(x)*cot(y)']
      bank['(cos(x))/(sin(y))']=['-(sin(x))/(sin(y))','-(cos(x)*cos(y))/(sin(y)^2)','-tan(x)*tan(y)']
      bank['sin(x)^2*y+cos(x*y)']=['2*y*cos(x)*sin(x)-y*sin(x*y)','sin(x)^2-x*sin(x*y)','-(y*sin(2*x)-y*sin(x*y))/(sin(x)^2-x*sin(x*y))']
      bank['cos(x)*cos(x+y)']=['-cos(x+y)*sin(x)-sin(x + y)*cos(x)','-sin(x + y)*cos(x)','- cot(x + y)/cot(x) - 1']
      bank['sin(x*sin(y))']=['cos(x*sin(y))*sin(y)','x*cos(x*sin(y))*cos(y)','-tan(y)/x']
      bank['sin(x/y)']=['(cos(x/y))/(y)','-(x*cos(x/y))/(y^2)','y/x']

    if numvar==2 and ptype=='hypinv':
      bank['sinh(x*y+y)']=['y*cosh(y+x*y)','(x+1)*cosh(y+x*y)','-(y)/(x+1)']
      bank['sinh(x*y+3)']=['y*cosh(x*y + 3)','x*cosh(x*y + 3)','-(y)/(x)']
      bank['cosh(x)*sinh(y^2)']=['sinh(y^2)*sinh(x)','2*y*cosh(y^2)*cosh(x)','-(sinh(y^2)*sinh(x))/(2*y*cosh(y^2)*cosh(x))']
      bank['sinh(x^2-y^2)+y*cosh(x)']=['2*x*cosh(x^2-y^2)+y*sinh(x)','cosh(x)-2*y*cosh(x^2 - y^2)','(2*x*cosh(x^2-y^2)+y*sinh(x))/(2*y*cosh(x^2-y^2)-cosh(x))']
      bank['cosh(x*sinh(y))']=['sinh(x*sinh(y))*sinh(y)','x*sinh(x*sinh(y))*cosh(y)','-tanh(y)/x']

    if numvar==2 and ptype=='mixed':
      bank['sin(x)*ln(y)']=['cos(x)*ln(y)','(sin(x))/(y)','-y*cot(x)*ln(y)']
      #bank['cos(x*y)*ln(y+x)']=['(cos(x*y))/(x + y)-y*ln(x+y)*sin(x*y)','(cos(x*y))/(x+y)-x*ln(x+y)*sin(x*y)','-(cos(x*y)/(x+y)-x*ln(x+y)*sin(x*y))/(cos(x*y)/(x + y)-y*ln(x+y)*sin(x*y))']
      bank['cos(x*y)*e^x']=['e^x*(cos(x*y)-y*sin(x*y))','-x*e^x*sin(x*y)','(cos(x*y)-y*sin(x*y))/(x*sin(x*y))']
      bank['sin(y)*e^(sin(x))']=['e^(sin(x))*cos(x)*sin(y)','e^(sin(x))*cos(y)','-tan(y)*cos(x)']
      bank['tan(x^y)']=['y*x^(y - 1)*(sec(x^y)^2)','x^y*ln(x)*(sec(x^y)^2)','-(y)/(x*ln(x))']
      bank['x^2*sin(x*y)']=['2*x*sin(x*y)+x^2*y*cos(x*y)','x^3*cos(x*y)','-(2*x*sin(x*y)+x^2*y*cos(x*y))/(x^3*cos(x*y))']
      bank['cos(x^2*y)*sin(x)']=['cos(x^2*y)*cos(x)-2*x*y*sin(x^2*y)*sin(x)','-x^2*sin(x^2*y)*sin(x)','(cos(x^2*y)*cos(x)-2*x*y*sin(x^2*y)*sin(x))/(x^2*sin(x^2*y)*sin(x))']
      bank['x*y+ln(x)*e^y']=['y + e^y/x','x+e^y*ln(x)','-(e^y + x*y)/(x^2+e^y*x*ln(x)))']
      bank['x^2*sin(y)+e^y']=['2*x*sin(y)','cos(y)*x^2+e^y','-(2*x*sin(y))/(cos(y)*x^2 + e^y)']
      bank['x^(sin(y))']=['x^(sin(y) - 1)*sin(y)','x^sin(y)*cos(y)*ln(x)','-tan(y)/(x*ln(x))']
    if numvar==3 and ptype!='short':
      #poly
      bank['x^y*z']=['x^(y-1)*y*z','x^y*z*ln(x)','x^y']
      bank['sin(x*y)+x*z']=['z + y*cos(x*y)','x*cos(x*y)','x']
      bank['cos(y*z)*sin(x)']=['cos(y*z)*cos(x)','-z*sin(y*z)*sin(x)','-y*sin(y*z)*sin(x)']
      bank['e^(x+y*z)']=['e^(x+y*z)','z*e^(x+y*z)','y*e^(x+y*z)']
      bank['x^2*z*sin(y)']=['2*x*z*sin(y)','x^2*z*cos(y)','x^2*sin(y)']
      bank['x^2*y^3*z']=['2*x*y^3*z','3*x^2*y^2*z','x^2*y^3']
      bank['x*z*sin(y + z)']=['z*sin(y+z)','x*z*cos(y+z)','x*sin(y+z)+x*z*cos(y+z)']
      bank['z + y*e^(x^2)']=['2*x*y*e^(x^2)','e^(x^2)','1']
      bank['(x^2 + y^2 + z^2)^(1/2)']=['(x)/(x^2 + y^2 + z^2)^(1/2)','(y)/(x^2 + y^2 + z^2)^(1/2)','(z)/(x^2 + y^2 + z^2)^(1/2)']

    if numvar==2 and (ptype=='trig' or ptype=='mixed' or ptype=='short'):
      bank['sin(x*y)']=['y*cos(x*y)','x*cos(x*y)','-(y)/(x)']
      bank['x*sin(y)']=['sin(y)','x*cos(y)','-tan(y)/x']
      bank['cos(2*x + y)']=['-2*sin(2*x + y)','-sin(2*x + y)','-2']
      bank['cos(x/y)']=['-(sin(x/y))/(y)','(x*sin(x/y))/(y^2)','(y)/(x)']
    if numvar==2 and (ptype=='poly' or ptype=='mixed' or ptype=='short'):
      bank['x^2+y^2']=['2*x','2*y','-x/y']
      bank['x+y^2']=['1','2*y','-1/(2*y)']
      bank['x^3+y^2']=['3*x^2','2*y','-3*x^2/(2*y)']
      bank['x-y+x*y']=['y+1','x-1','(1+y)/(1-x)']
      bank['x^2-y^2']=['2*x','-2*y','(x)/(y)']
      bank['4*x+x^2*y']=['2*x*y+4','x^2','-(2*x*y+4)/(x^2)']
      bank['x^2+y']=['2*x','1','-2*x']
    if numvar==2 and (ptype=='trans' or ptype=='mixed' or ptype=='short'):
      bank['ln(x*y)']=['(1)/(x)','(1)/(y)','(-y)/(x)']
    if numvar==3 and (ptype=='short' or ptype=='dummy'):
      #poly
      #bank['x*y*z']=['y*z','x*z','x*y']
      bank['x+y+z']=['1','1','1']
      bank['ln(x*y*z)']=['(1)/(x)','(1)/(y)','(1)/(z)']

    self.f=bank.keys()[random.randint(0,len(bank)-1)]
    self.fx=bank[self.f][0]
    self.fy=bank[self.f][1]
    if numvar==2: self.yx=bank[self.f][2]
    if numvar==3: self.fz=bank[self.f][2]

  def tuv(self,option,numvar):
    sbank={}
    if option=='t':
      sbank['t']=['1']
      sbank['t^2']=['2*t']
      sbank['sin(t)']=['cos(t)']
      sbank['cos(t)']=['-sin(t)']
      sbank['ln(t)']=['(1/t)']
      sbank['e^t']=['e^t']

    if option=='uv':
      sbank['u*v']=['v','u']
      sbank['u^2*v']=['2*u*v','u^2']
      sbank['(u/v)']=['(1/v)','(-u/v^2)']
      sbank['v*ln(u)']=['(v/u)','ln(u)']

    chooserange=range(len(sbank))
    random.shuffle(chooserange)
    picks=chooserange[0:numvar]
    self.tuv=[sbank.keys()[i] for i in range(numvar)]
    self.dtuv=[sbank[i] for i in self.tuv]

def main():
  #a=partial(2)
  #print a.f,a.fx, a.fy, a.yx
  a=partial(2,'mixed')
  #a.tuv('uv',3)
  #print a.tuv
  #print a.dtuv
  print a.f, a.fx, a.fy, a.yx
  #a=divcurl()
  #print a.f
  #print a.div
  #print a.curl
if __name__ == '__main__':
  main()
