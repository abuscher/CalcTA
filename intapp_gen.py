#!/usr/bin/python -tt

import sys
import random
import math
from math import *
import re
import latex
from latex import *

# Define a main()
def main():
  options=sys.argv[1]
  #options='0000001'
  if int(options)==0: options='1'+options[1:]

  pick=[]
  for i in range(len(options)):
    if options[i]=='1':pick.append(i)
  type=pick[random.randrange(0,len(pick))]
  #type=4
  #options[0]=Area
  #options[1]=Volume
  #options[2]=Arc Length
  #options[3]=Center of Mass
  #options[4]=Work
  #options[5]=Polar Coordinates
  #options[6]=Differential Equations ##NEW
  master_bank={}
  if type==0:
  #options[0]=Area
#Trig sub
    master_bank['Find the area of the circle bounded by the curve $x^2+y^2=4$']=['','4*pi','Solve for $y$ in terms of $x$, then you will need a trigonometric substitution.']
    master_bank["Find the area of the ellipse bounded by the curve $\displaystyle\\frac{x^2}{4}+\displaystyle\\frac{y^2}{9}=1$"]=['','6*pi','Solve for $y$ in terms of $x$.  You will need a trigonometric substitution']
    master_bank['Find the area of the circle bounded by the curve $x^2+y^2=1$']=['','pi','Solve for $y$ in terms of $x$.  You will need a trigonometric substitution']
    master_bank["Find the area of the ellipse bounded by the curve $\displaystyle\\frac{x^2}{16}+\displaystyle\\frac{y^2}{25}=1$"]=['','20*pi','Solve for $y$ in terms of $x$, then will need a trigonometric substitution.']
    master_bank["Find the area of the ellipse bounded by the curve $\displaystyle\\frac{x^2}{5}+\displaystyle\\frac{y^2}{10}=1$"]=['','5*pi*sqrt(2)','Solve for $y$ in terms of $x$, then will need a trigonometric substitution.']

#Some random curve that doesn't cross the x-axis
    master_bank['Find the area below the curve $y=x^3+x^2+7$ and above x-axis on $x=[-2,3]$']=['','755/12','This curve does not cross the x-axis on $x=[-2,3]$.']
    master_bank['Find the area below the curve $y=x+\sin(x)$ and above x-axis on $x=[0,\pi]$']=['','pi^2/2+2','']
    master_bank['Find the area below the curve $y=e^x-x$ and above x-axis on $x=[1,5]$']=['','e^5-e-12','']
    master_bank['Find the area bounded by the curve $y=x*sin(x)$ and the x-axis on $x=[0,\pi]$']=['','pi','']

#trig
    master_bank['Find the area of the region bounded by $f(x)=\sin(x)$ and the $x$-axis on $x[0,\pi]$.']=['','2','']
    master_bank['Find the area of the region bounded by $f(x)=\sin(x)$ and $g(x)=\cos(x)$ on $x[\pi/4,5\pi/4]$.']=['','sqrt(8)','']
    master_bank['Find the area of the region bounded by $f(x)=-\sin(x)$ and $g(x)=\cos(2*x)$ on $x[-\pi/6,\pi/2]$.']=['','(3*sqrt(3)/4','']
    master_bank['Find the area of the region bounded by $f(x)=-3/2*\sin(x)$ and $g(x)=\cos^2(x)$']=['','(2*pi)/3+7/4*sqrt(3)','The curves intersect at $x=-\pi/6$ and $x=7*\pi/6$.']
#poly
    master_bank['Find the area of the region bounded by $f(x)=x^2+7*x+1$ and $g(x)=5-x^2$']=['','243/8','The curves intersect at $x=-4$ and $x=1/2$.']
    master_bank['Find the area of the region bounded by $f(x)=2*x^2-5*x-3$ and $g(x)=x^2-7*x$']=['','32/3','The curves intersect at $x=-3$ and $x=1$.']
    master_bank['Find the area of the region bounded by $f(x)=x^2$ and $g(x)=7*x$']=['','343/6','The curves intersect at $x=0$ and $x=7$.']
    master_bank['Find the area of the region bounded by $f(x)=x^2+4*x+1$ and $g(x)=x-x^2$']=['','1/24','The curves intersect at $x=-1$ and $x=-1/2$.']
    master_bank['Find the area of the region bounded by $f(x)=x^4$ and $g(x)=2*x^2-1$']=['','16/15','The curves intersect at $x=-1$ and $x=1$.']
    master_bank['Find the area of the region bounded by $f(x)=x^2$ and $g(x)=2*x+8$']=['','36','The curves intersect at $x=-2$ and $x=4$.']

  if type==1:
  #options[1]=Volume
    #Around the x-axis
    master_bank['Find the volume when the region bounded by $y=x$ and $y=\sqrt{x}$ is rotated around the x-axis.']=['','pi/6','']
    master_bank['Find the volume when the region bounded by $y=x$ and $y=x^2$ is rotated around the x-axis.']=['','2*pi/15','']
    master_bank['Find the volume when the region bounded by $y=x^4$ and $y=x$ is rotated around the x-axis.']=['','2*pi/9','']
    master_bank['Find the volume when the region bounded by $y=\sin(x)$ and the x-axis on $x=[0,\pi]$ is rotated around the x-axis.']=['','pi^2/2','']
    master_bank['Find the volume when the region bounded by $y=\sqrt{1-x^2}$ and the x-axis is rotated around the x-axis.']=['','4*pi/3','']
    master_bank['Find the volume when the region bounded by $y=x$ and the x-axis on $x=[0,2]$  is rotated around the x-axis.']=['','8*pi/3','']
    master_bank['Find the volume when the region bounded by $y=e^x$ and the x-axis on $x=[-1,1]$  is rotated around the x-axis.']=['','pi/2*(e^2-e^(-2)','']

    #Around the y-axis
    master_bank['Find the volume when the area bounded above by $y=\ln(x)$ and below by the $y$-axis on $x=[1,e]$  is rotated around the $y$-axis.']=['','pi/2*(e^2-1)','']
    master_bank['Find the volume when the region bounded by $y=x$ and $y=\sqrt{x}$ is rotated around the $y$-axis.']=['','(2*pi)/15','']
    master_bank['Find the volume when the region bounded by $y=0$, $x=0$, $y=\sqrt{x}$, and $y=4$ is rotated around the $y$-axis.']=['','1024*pi/5','']
    master_bank['Find the volume when the region bounded by $y=\ln(x)$, $y=0$, $x=0$, and $y=1$ is rotated around the $y$-axis.']=['','pi/2*(e^2-1)','']

    #Around a line
    master_bank['Find the volume when the region bounded by $y=4-x^2$ and the $x$-axis is rotate around the line $y=-2$.']=['','384*pi/5','']
    master_bank['Find the volume when the region bounded by $y=\sin(\pi*x)$ and the x-axis on $x=[0,1]$ is rotated around the line $y=-1$.']=['','pi/2+4','']
    master_bank['Find the volume when the region bounded by $y=x$, $x=6$, and the $x$-axis is rotated around the line $y=-3$.']=['','180*pi','']
    master_bank['Find the volume when the region bounded by $y=x^(1/3)$, $x=8$, and the $x$-axis is rotated around the line $y=-2$.']=['','336*pi/5','']

    #Cross section is square, equilateral triangle, isoceles right triangle, or semicircle

    master_bank['Find the volume of the region whose base is bounded by the $x$-axis and $y=4-x^2$ with cross-sections that are squares perpendicular to the $x$-axis with a side in the $xy$-plane.']=['','34.133','']
    master_bank['Find the volume of the region whose base is bounded by the $x$-axis, $y=\sqrt{x}$, and $x=9$ with cross-sections that are squares perpendicular to the $x$-axis with a side in the $xy$-plane.']=['','40.5','']
    master_bank['Find the volume of the region whose base is bounded by the $x$-axis and $y=\sqrt(1-x^2)$ with cross-sections that are squares perpendicular to the $x$-axis with a side in the $xy$-plane.']=['','4/3','']

    master_bank['Find the volume of the region whose base is bounded by the $x$-axis and $y=\sqrt(1-x^2)$ with cross-sections that are semi-circles with a diameter in the $xy$-plane and perpendicular to the $x$-axis.']=['','pi/6','']
    master_bank['Find the volume of the region whose base is bounded by $x^2+y^2=4$ with cross-sections that are circles with a diameter in the $xy$-plane and perpendicular to the $x$-axis.']=['','32*pi/3','This is a sphere with radius $r=2$']
    master_bank['Find the volume of the region whose base is bounded by the $x$-axis, the line $x=3$ and the line $y=x/3$ with cross-sections that are semi-circles with a diameter in the $xy$-plane and perpendicular to the $x$-axis.']=['','pi/8','']

    master_bank['Find the volume of a pyramid with a square base with side length $10$ and a height from that base of $20$.']=['','2000/3','']
    master_bank['Find the volume of a pyramid with a square base with side length $7$ and a height from that base of $30$.']=['','490','']
    master_bank['Find the volume of a pyramid with a square base with side length $9$ and a height from that base of $15$.']=['','405','']

    master_bank['Find the volume of a tetrahedron with a equilateral triangule base with side length $5$ and a height from that base of $10$.']=['','36.0844','The area of an equilateral triangle is $A=s^2\sqrt{3}/4$']
    master_bank['Find the volume of a tetrahedron with a equilateral triangule base with side length $4$ and a height from that base of $6$.']=['','13.8564','The area of an equilateral triangle is $A=s^2\sqrt{3}/4$']

  if type==2:
  #options[2]=Arc Length
    master_bank['Find the arc length of the curve $y=.75*x$ from $x=0$ to $x=5$.']=['','6.25','']
    master_bank['Find the arc length of the curve $y=(x+5)^{3/2}$ from $x=0$ to $x=8$.']=['','988/27','']
    master_bank['Find the arc length of the curve $y=\sinh(x)$ from $x=0$ to $x=1$.']=['','(e^2-1)/(2*e)','']

    master_bank['Find the arc length of the parametric curve $x=\cos(t)$ $y=\sin(t)$ from $t=0$ to $t=\pi$']=['','pi','']
    master_bank['Find the arc length of the parametric curve $x=t^{3/2}$ $y=t$ from $t=0$ to $t=1$']=['','61/27','']
    master_bank['Find the arc length of the parametric curve $x=3*t^2$ $y=1/2*t^3$ from $t=0$ to $t=3$']=['','30.5','']
    master_bank['Find the arc length of the parametric curve $x=t^3$ $y=t^{4.5}$ from $t=0$ to $t=1$']=['','1.43971','']

  if type==3:
  #options[3]=Center of Mass
    master_bank['Find the center of mass of the region bounded by $f(x)=x^2$ and $g(x)=\sqrt{x}$ on $x=[0,1]$.']=['','(9/20,9/20)','']
    master_bank['Find the center of mass of the region bounded by $f(x)=x$ and $g(x)=\sqrt{x}$ on $x=[0,1]$.']=['','(2/5,1/2)','']
    master_bank['Find the center of mass of the region bounded by $f(x)=x^2$ and $g(x)=x$ on $x[0,1]$.']=['','(1/2,2/5) ','']
    master_bank['Find the center of mass of the region bounded by $f(x)=x^2+3x-1$ and $g(x)=3*x$ on $x[-1,1]$.']=['','(0,-2/5)','']
    master_bank['Find the center of mass of the region bounded by $f(x)=2x^2-5x-3$ and $g(x)=x^2-7*x$ on $x[-3,1]$.']=['','(-1,36/5)','']
    master_bank['Find the center of mass of the region bounded by $f(x)=x^2+5x+1$ and $g(x)=1-x$ on $x[0,6]$.']=['','21/5,478/25','']
    master_bank['Find the center of mass of the region bounded by $f(x)=x^3$ and $g(x)=x$ on $x[0,1]$.']=['','(8/15,8/21)','']
    master_bank['Find the center of mass of the region bounded by $f(x)=x$ and $g(x)=-2x$ on $x[0,3]$.']=['','(2,-1)','']

    master_bank['Find the center of mass of the region bounded by $f(x)=\sin(x)$ and the $x$-axis on $x[0,\pi]$.']=['','(pi/2,pi/8) ','']
    master_bank['Find the center of mass of the region bounded by $f(x)=\sin(x)$ and $g(x)=\cos(x)$ on $x[\pi/4,5\pi/4]$.']=['','(3*pi/4,0) ','']
    master_bank['Find the center of mass of the region bounded by $f(x)=\cos(x)$ and $x=-1$ on $x[-\pi,-\pi]$.']=['','(0,-1/4)','']
    master_bank['Find the center of mass of the region bounded by $\sqrt{1-x^2}$ and the x-axis on $x[-1,1]$.']=['','(0,4/(3*pi))','']
    master_bank['Find the center of mass of the region bounded by $\sqrt{4-x^2}$ and the x-axis on $x[-1,3]$.']=['','(0,8/(3*pi))','']
    master_bank['Find the center of mass of the region bounded by $\sqrt{4-x^2}$ and $4-x^2$ on $x[-2,2]$.']=['','(0,-88/(15*pi + 80))','']

    master_bank['Find the center of mass of the triangle with vertice at $(0,0)$, $(0,4)$ and $(2,0)$.']=['','(2/3,4/3) ','']
    master_bank['Find the center of mass of the triangle with vertice at $(1,1)$, $(5,1)$ and $(3,4)$.']=['','(3,2) ','']
    master_bank['Find the center of mass of the triangle with vertice at $(7,7)$, $(1,1)$ and $(-2,7)$.']=['','(2,5) ','']
    master_bank['Find the center of mass of the triangle with vertice at $(0,0)$, $(0,7)$ and $(3,4)$.']=['','(1,11/3) ','']


    #master_bank['Find the center of mass of the region bounded by $f(x)=x^2$ and $g(x)=x$ on $x[0,1]$.']=['','(1/2,2/5) ','']

  if type==4:
  #options[4]=Work
    #Lifting an object on a chain
    master_bank['How much work is required to lift a $20 \ lb$ pail $10 \ ft$ with a chain that weighs $1 \ lb/ft$ ']=['','250','','ft-lb']
    master_bank['How much work is required to lift a $2000 \ lb$ payload with a $100 \ ft$ chain that weighs $3 \ lb/ft$ up the first $50 \ ft$ of a $100 \ ft$ shaft?']=['','111250','','ft-lb']
    master_bank['How much work is required to lift a $900 \ N$ person up a $100 \ m$ cliff rope that weighs $1 \ N/m$ ']=['','95000','','N-m']
    master_bank['How much work is required to lift a $10 \ lb$ weight $50 \ ft$ with a chain that weighs $5 \ lb/ft$ ']=['','6750','','ft-lb']

    #Pump out of a cylinder/cone/trough/etc
    master_bank['A tank in the shape of an inverted cone with height $10 \ m$ and radius $r=5 \ m$ is filled with water.  How much work does it take to pump all the water to the top (use $9800 \  N/m^3$ for the weight of water)?']=['','(6125000*pi)/3','','$J$']
    master_bank['A tank in the shape of an inverted cone with height $15 \ m$ and radius $r=2 \ m$ is filled $6 \ m$ high with water.  How much work does it take to pump all the water to the top (use $9800 \ N/m^3$ for the weight of water)?']=['','131712*pi','','$J$']
    master_bank['A tank in the shape of an inverted cone with height $12 \ ft$ and radius $r=3 \ ft$ is filled with water.  How much work does it take to pump all the water to the top (use $62 \ lb/ft^3$ for the weight of water)? ']=['','6696*pi','','$ft-lb$']
    master_bank['A tank in the shape of an inverted cone with height $8 \ ft$ and radius $r=4 \ ft$ is filled $6 \ m$ high with water.  How much work does it take to pump all the water to the top (use $62 \ lb/ft^3$ for the weight of water)?']=['','3906*pi','','$ft-lb$']
    master_bank['A tank in the shape of an cylinder with height $12 \ m$ and radius $r=3 \ m$ is filled $6 \ m$ high with water.  How much work does it take to pump all the water to the top (use $9800 \ N/m^3$ for the weight of water)?']=['','330750*pi','','$J$']

    #Hydrostatic Force/Pressure
    master_bank['Find the total force on a rectangular dam with height $100 \ ft$ and width $300 \ ft$ (use $62 \ lb/ft^3$ for the weight of water).']=['','93000000','','lb']
    master_bank['Find the total force on a rectangular dam with height $80 \ m$ and width $200 \ m$ (use $9800 \ N/m^3$ for the weight of water).']=['','6272000000','','N']

    master_bank['Find the total force on a trapezoidal dam with height $50 \ m$, top width $100 \ m$ and a bottom width of $75 \ m$ (use $9800 N/m^3$ for the weight of water).']=['',' 1.020833*10^9','','N']
    master_bank['Find the total force on a trapezoidal dam with height $100 \ m$, top width $300 \ m$ and a bottom width of $200 \ m$ (use $9800 N/m^3$ for the weight of water).']=['',' 1.1433333*10^10','','N']
    master_bank['Find the total force on a trapezoidal dam with height $20 \ ft$, top width $200 \ ft$ and a bottom width of $140 \ ft$ (use $62 lb/ft^3$ for the weight of water).']=['',' 1984000','','lb']

    master_bank['An upright square plate with side length $s=1 \ m$ is submerged in water such that the top edge is $1 \ km$ below the surface.  What is the force acting on the plate (use $9800 \ N/m^3$ for the weight of water)?']=['','9804900','','N']
    master_bank['An upright rectangular plate with base $b=70 \ cm$ and height $b=130 \ cm$ is submerged in water such that the edge top edge is $1 \ m$ below the surface.  What is the force acting on the plate (use $9800 \ N/m^3$ for the weight of water)?']=['','14714.7','','N']
#    master_bank['An circular plate with radius $r=1 m$ is submerged in water perpendicular to the surface such that the edge top edge is adjacent the surface.  What is the force acting on the plate?']==['','14714.7','','N']
#add circular plate...be careful

    #spring
    master_bank['A spring has a constant $k=20 \ N/m$ and natural length $1 \ m$.  How much work does it take to stretch the string from $1 \ m$ to $1.2 \ m$?']=['','0.4','','N-m']
    master_bank['A spring has a natural length $1.7 \ m$ and it takes $20 \ N$ to hold it at $2.2 \ m$.  How much work does it take to stretch the string from $2 \ m$ to $3 \ m$?']=['','32','','N-m']
    master_bank['It takes $100 \ N$ to hold a spring at $.5 \ m$ and $150 \ N$ to hold it at $.6 \ m$.  How much work does it take to stretch the string from $.5 \ m$ to $1 \ m$?']=['','112.5','','N-m']

    master_bank['A spring has a constant $k=200 \ N/m$ and natural length $30 \ cm$.  How much work does it take to stretch the string from $30 \ cm$ to $50 \ cm$?']=['','4','','N-m']
    master_bank['A spring has a constant $k=170 \ N/m$ and natural length $40 \ cm$.  How much work does it take to stretch the string from $47 \ cm$ to $61 \ cm$?']=['','3.332','','N-m']
    master_bank['A spring has a natural length $33 \ cm$ and it takes $20 \ N$ to hold it at $35 \ cm$.  How much work does it take to stretch the string from $35 \ cm$ to $40 cm$?']=['','2.25','','N-m']
    master_bank['It takes $100 \ N$ to hold a spring at $37 \ cm$ and $200 \ N$ to hold it at $42 \ m$.  How much work does it take to stretch the string from $40 \ cm$ to $ 50 cm$?']=['','26','','N-m']

    master_bank['A spring has a constant $k=10 \ lb/ft$ and natural length $5 \ in$.  How much work does it take to stretch the string from $6 \ in$ to $8 \ in$?']=['','5/18','','ft-lb']
    master_bank['A spring has a constant $k=36 \ lb/ft$ and natural length $14 \ in$.  How much work does it take to stretch the string from $17 \ in$ to $23 \ in$?']=['','9','','ft-lb']
    master_bank['A spring has a natural length $8 \ in$ and it takes $6 \ lb$ of force to hold it at $9 \ in$.  How much work does it take to stretch the string from $8 \ in$ to $12 \ in$?']=['','72','','ft-lb']
    master_bank['It takes $9 lb$ to hold a spring at $9 \ in$ and $15 \ lb$ to hold it at $12 \ in$.  How much work does it take to stretch the string from $5 \ in$ to $10 \ in$?']=['','2.5','','ft-lb']

  if type==5:
  #options[5]=Polar Coordinates
    #Arc Length
    master_bank['Find the arc length of the curve $r= 3\sin(\\theta)$ for $\\theta=[0,\pi ]$']=['','3*pi','You can simplify the integrand with the pythagorean identity.']
    master_bank['Find the arc length of the curve $r= 2\cos(\\theta)$ for $\\theta=[0,\pi/2 ]$']=['','pi','You can simplify the integrand with the pythagorean identity.']
    master_bank['Find the arc length of the curve $r= 1+\cos(\\theta)$ for $\\theta=[0,\pi]$']=['','4','']

    #Area
    master_bank['Find the area enclosed by the curve $r=3+2 \cdot \cos(\\theta)$ for $\\theta=[0,2\pi ]$']=['','11*pi','You may need to use a trigonometric identity']
    master_bank['Find the area enclosed by the curve $r=2+\sin(\\theta)$ for $\\theta=[0,2\pi ]$']=['','9*pi/2','You may need to use a trigonometric identity']
    master_bank['Find the area enclosed by the curve $r= 3\sin(\\theta)$ for $\\theta=[0,\pi]$']=['','9*pi/4','You may need to use a trigonometric identity']
    master_bank['Find the area enclosed by the curve $r= \sin^2(\\theta)$ for $\\theta=[0,\pi]$']=['','(3*pi)/16','']
    master_bank['Find the area enclosed by the curve $r= \cos^2(\\theta)$ for $\\theta=[0,2*\pi]$']=['','(3*pi)/8','']
    master_bank['Find the area enclosed by the curve $r= \sin(2\\theta)$ for $\\theta=[0,\pi/2]$']=['','pi/8','You may need to use a trigonometric identity']
    master_bank['Find the area enclosed by the curve $r= \sin(3\\theta)$ for $\\theta=[0,\pi]$']=['','pi/4','You may need to use a trigonometric identity']
    master_bank['Find the area enclosed by the curve $r= 2\cos(\\theta)$ for $\\theta=[0,\pi ]$']=['','pi','']
    master_bank['Find the area enclosed by the curve $r= \cos(3\\theta)$ for $\\theta=[\pi/6,\pi/2]$']=['','pi/12','']

  if type==6:
  #options[6]=Differential Equations
  #dy/dx=f(x)
    #master_bank['Solve for $y(x)$ in the equation $\displaystyle\\frac{dy}{dx}=\ln(x)/x$, $y(1)=1$']=['$y(x)=$','ln(x)^2/2+1','']
    import diffeq_gen
    a=diffeq_gen.SOV()
    master_bank[a.problem]=[a.prefix,a.ans,a.hint]
    #master_bank['Solve for $y(x)$ in the equation $\displaystyle\\frac{dy}{dx}=x$, $y(0)=0$']=['$y(x)=$','','']

  #print len(master_bank)
  rand1=random.randrange(0,len(master_bank))
  problem=master_bank.keys()[rand1]
  prefix=master_bank[problem][0]
  answer=master_bank[problem][1]
  hint=master_bank[problem][2]
  problem=problem.replace('*','\cdot ')
  #f='e^(e^(e^x))'
  #ftex=toTEX(f)
  try:
    suffix='$%s$'%master_bank[problem][3]
  except:
    suffix=''



  problem=problem.replace('m/s$','\mathrm{m}/\mathrm{s}$')
  problem=problem.replace('cm/s$','\mathrm{cm}/\mathrm{s}$')
  problem=problem.replace('in/s$','\mathrm{in}/\mathrm{s}$')
  problem=problem.replace('ft/s$','\mathrm{ft}/\mathrm{s}$')
  problem=problem.replace('ft/lb$','\mathrm{ft}/\mathrm{lb}$')
  problem=problem.replace('lb/ft$','\mathrm{lb}/\mathrm{ft}$')
  problem=problem.replace('lb/ft^3$','\mathrm{lb}/\mathrm{ft}^3$')

  problem=problem.replace('m^2/s$','\mathrm{m^2}/\mathrm{s}$')
  problem=problem.replace('cm^2/s$','\mathrm{cm}^2/\mathrm{s}$')
  problem=problem.replace('in^2/s$','\mathrm{in^2}/\mathrm{s}$')
  problem=problem.replace('ft^2/s$','\mathrm{ft^2}/\mathrm{s}$')

  problem=problem.replace('cm^3/s$','\mathrm{cm}^3/\mathrm{s}$')
  problem=problem.replace('m^3/s$','\mathrm{m^3}/\mathrm{s}$')
  problem=problem.replace('in^3/s$','\mathrm{in^3}/\mathrm{s}$')
  problem=problem.replace('ft^3/s$','\mathrm{ft^3}/\mathrm{s}$')

  problem=problem.replace('N/m$','\mathrm{N}/\mathrm{m}$')
  problem=problem.replace('N-m$','\mathrm{N}-\mathrm{m}$')
  problem=problem.replace('N/m^2$','\mathrm{N}/\mathrm{m^2}$')
  problem=problem.replace('N/m^3$','\mathrm{N}/\mathrm{m^3}$')

  problem=problem.replace('in^2$','\mathrm{in}^2$')
  problem=problem.replace('in^3$','\mathrm{in}^3$')
  problem=problem.replace('m^2$','\mathrm{m}^2$')
  problem=problem.replace('m^3$','\mathrm{m}^3$')
  problem=problem.replace('cm^2$','\mathrm{cm}^2$')
  problem=problem.replace('cm^3$','\mathrm{cm}^3$')
  problem=problem.replace('ft^2$','\mathrm{ft}^2$')
  problem=problem.replace('ft^3$','\mathrm{ft}^3$')

  problem=problem.replace('m$','\mathrm{m}$')
  problem=problem.replace('km$','\mathrm{km}$')
  problem=problem.replace('cm$','\mathrm{cm}$')
  problem=problem.replace('s$','\mathrm{s}$')
  problem=problem.replace('in$','\mathrm{in}$')
  problem=problem.replace('ft$','\mathrm{ft}$')
  problem=problem.replace('lb$','\mathrm{lb}$')
  problem=problem.replace('Pa$','\mathrm{Pa}$')
  problem=problem.replace('N$','\mathrm{N}$')

  suffix=suffix.replace('cm$','\mathrm{cm}$')
  suffix=suffix.replace('m/s$','\mathrm{m}/\mathrm{s}$')
  suffix=suffix.replace('in/s$','\mathrm{in}/\mathrm{s}$')
  suffix=suffix.replace('ft/s$','\mathrm{ft}/\mathrm{s}$')
  suffix=suffix.replace('ft/lb$','\mathrm{ft}/\mathrm{lb}$')
  suffix=suffix.replace('lb/ft$','\mathrm{lb}/\mathrm{ft}$')

  suffix=suffix.replace('cm^2/s$','\mathrm{cm}^2/\mathrm{s}$')
  suffix=suffix.replace('m^2/s$','\mathrm{m^2}/\mathrm{s}$')
  suffix=suffix.replace('in^2/s$','\mathrm{in^2}/\mathrm{s}$')
  suffix=suffix.replace('ft^2/s$','\mathrm{ft^2}/\mathrm{s}$')

  suffix=suffix.replace('cm^3/s$','\mathrm{cm}^3/\mathrm{s}$')
  suffix=suffix.replace('m^3/s$','\mathrm{m^3}/\mathrm{s}$')
  suffix=suffix.replace('in^3/s$','\mathrm{in^3}/\mathrm{s}$')
  suffix=suffix.replace('ft^3/s$','\mathrm{ft^3}/\mathrm{s}$')

  suffix=suffix.replace('in^2$','\mathrm{in}^2$')
  suffix=suffix.replace('in^3$','\mathrm{in}^3$')
  suffix=suffix.replace('m^2$','\mathrm{m}^2$')
  suffix=suffix.replace('m^3$','\mathrm{m}^3$')
  suffix=suffix.replace('cm^2$','\mathrm{cm}^2$')
  suffix=suffix.replace('cm^3$','\mathrm{cm}^3$')
  suffix=suffix.replace('ft^2$','\mathrm{ft}^2$')
  suffix=suffix.replace('ft^3$','\mathrm{ft}^3$')

  suffix=suffix.replace('ft-lb$','\mathrm{ft}-\mathrm{lb}$')
  suffix=suffix.replace('N/m$','\mathrm{N}/\mathrm{m}$')
  suffix=suffix.replace('N-m$','\mathrm{N}-\mathrm{m}$')
  suffix=suffix.replace('N/m^2$','\mathrm{N}/\mathrm{m^2}$')
  suffix=suffix.replace('N/m^3$','\mathrm{N}/\mathrm{m^3}$')

  suffix=suffix.replace('m$','\mathrm{m}$')
  suffix=suffix.replace('km$','\mathrm{km}$')
  suffix=suffix.replace('cm$','\mathrm{cm}$')
  suffix=suffix.replace('s$','\mathrm{s}$')
  suffix=suffix.replace('in$','\mathrm{in}$')
  suffix=suffix.replace('ft$','\mathrm{ft}$')
  suffix=suffix.replace('lb$','\mathrm{lb}$')
  suffix=suffix.replace('Pa$','\mathrm{Pa}$')
  suffix=suffix.replace('N$','\mathrm{N}$')
  suffix=suffix.replace('J$','\mathrm{J}$')


  print problem
  print answer
  if type==0:
    anstype='area'
  elif type==1:
    anstype='volume'
  elif type==2:
    anstype='arc length'
  elif type==3:
    anstype='center of mass'
  else: anstype='answer'
  anstex='The %s is %s $%s$ %s.'%(anstype,prefix,toTEX(answer),suffix)
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
