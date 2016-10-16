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
    options = sys.argv[1]
    # options='010000'
    if int(options) == 0:
        options = '1' + options[1:]

    pick = []
    for i in range(len(options)):
        if options[i] == '1': pick.append(i)
    type = pick[random.randrange(0, len(pick))]
    # type=2
    # options[0]=Tangent Line
    # options[1]=Optimization
    # options[2]=Min/Max
    # options[3]=Related Rates
    # options[4]=La'Hopital
    # options[5]=Newton's Method
    # options[6]=Derivative Approximations
    # master_bank={}

    # if options[0]=='1':
    if type == 0:
        tangent = {}
        subtype = random.randint(1, 3)
        if subtype < 3:
            # poly
            tangent['Find the line tangent to $y=\sqrt{x}$ at the point $x=25$'] = ['$y=$', 'x/10+5', ' ', 'hint']
            tangent['Find the line tangent to $y=\sqrt[3]{x}$ at the point $x=8$'] = ['$y=$', 'x/12+4/3', ' ', 'hint']
            tangent['Find the line tangent to $y=x^e$ at the point $x=1$'] = ['$y=$', 'e*x-e+1', ' ', 'hint']
            tangent['Find the line tangent to $y=x^4$ at the point $x=2$'] = ['$y=$', '32*x-48', ' ', 'hint']

            # trans
            tangent['Find the line tangent to $y=e^x$ at the point $x=0$'] = ['$y=$', 'x+1', ' ', 'hint']
            tangent['Find the line tangent to $y=e^x$ at the point $x=1$'] = ['$y=$', 'e*x', ' ', 'hint']
            tangent['Find the line tangent to $y=\ln(x)$ at the point $x=1$'] = ['$y=$', 'x-1', ' ', 'hint']

            # trig
            tangent['Find the line tangent to $y=\sin(\pi*x)$ at the point $x=1$'] = ['$y=$', '-pi*x+pi', ' ', 'hint']
            tangent['Find the line tangent to $y=\sin(x)$ at the point $x=\pi$'] = ['$y=$', '-x+pi', ' ', 'hint']
            tangent['Find the line tangent to $y=\cos(x)$ at the point $x=0$'] = ['$y=$', '1', ' ', 'hint']
            tangent['Find the line tangent to $y=\cos(x)$ at the point $x=\pi/2$'] = ['$y=$', '-x+pi/2', ' ', 'hint']
            tangent['Find the line tangent to $y=\tan(x)$ at the point $x=\pi/4$'] = ['$y=$', '2*x-pi/2+1', ' ', 'hint']

            # product (5)
            tangent['Find the line tangent to $y=x^2\cdot\sin(x)$ at the point $x=pi/2$'] = ['$y=$', 'pi*x-pi^2/2', ' ',
                                                                                             'hint']
            tangent['Find the line tangent to $y=\displaystyle\\frac{\ln(x)}{x}$ at the point $x=e$'] = ['$y=$', '1/e',
                                                                                                         ' ', 'hint']
            tangent['Find the line tangent to $y=\\tan(\pi\cdot x)$ at the point $x=1$'] = ['$y=$', 'pi*e*(x-1)', ' ',
                                                                                            'hint']

            # chain (5)
            tangent['Find the line tangent to $y=e^{\sin(x)}$ at the point $x=\pi$'] = ['$y=$', '-x+pi+1', ' ', 'hint']
            tangent['Find the line tangent to $y=\sin(x^2)$ at the point $x=0$'] = ['$y=$', '0', ' ', 'hint']
            tangent['Find the line tangent to $y=\ln(x^2)$ at the point $x=1$'] = ['$y=$', '2*x-2', ' ', 'hint']

        if subtype == 3:
            # 10 more
            tangent['Use a tangent line for $y=\sqrt{x}$ at $x=16$ to approximate $\sqrt{17}$'] = [
                '$\sqrt{17} \\approx$', '4.125', ' ', 'hint']
            tangent['Use a tangent line for $y=\sqrt{x}$ at $x=25$ to approximate $\sqrt{23}$'] = [
                '$\sqrt{23} \\approx$', '4.8', ' ', 'hint']
            tangent['Use a tangent line for $y=\sqrt{x}$ at $x=81$ to approximate $\sqrt{80}$'] = [
                '$\sqrt{80} \\approx$', '8.9444', ' ', 'hint']

            tangent['Use a tangent line for $y=\sqrt[3]{x}$ at $x=8$ to approximate $\sqrt[3]{9}$'] = [
                '$\sqrt[3]{9} \\approx$', '2.0833', ' ', 'hint']
            tangent['Use a tangent line for $y=\sqrt[3]{x}$ at $x=64$ to approximate $\sqrt[3]{60}$'] = [
                '$\sqrt[3]{60} \\approx$', '3.9167', ' ', 'hint']
            tangent['Use a tangent line for $y=\sqrt[3]{x}$ at $x=1$ to approximate $\sqrt[3]{2}$'] = [
                '$\sqrt[3]{2} \\approx$', '1.3333', ' ', 'hint']

            tangent['Use a tangent line for $y=e^x$ at $x=0$ to approximate $e^{.1}$'] = ['$e^{.1} \\approx$', '1.1',
                                                                                          ' ', 'hint']
            tangent['Use a tangent line for $y=e^x$ at $x=0$ to approximate $e^{-.1}$'] = ['$e^{-.1} \\approx$', '0.9',
                                                                                           ' ', 'hint']
            tangent['Use a tangent line for $y=\ln(x)$ at $x=0$ to approximate $\ln(1.1)$'] = ['$\ln(1.1) \\approx$',
                                                                                               '.1', ' ', 'hint']

            tangent['Use a tangent line for $y=\sin(x)$ at $x=0$ to approximate $\sin(.1)$'] = ['$\sin(.1) \\approx$',
                                                                                                '.1', ' ', 'hint']
            tangent['Use a tangent line for $y=\cos(x)$ at $x=0$ to approximate $\cos(.1)$'] = ['$\cos(.1) \\approx$',
                                                                                                '1', ' ', 'hint']
            tangent['Use a tangent line for $y=\\tan(x)$ at $x=0$ to approximate $\\tan(.1)$'] = [
                '$\\tan(.1) \\approx$', '.1', ' ', 'hint']
        master_bank = tangent

    if type == 1:
        optimize = {}

        optimize['Minimize $f(x)=x\cdot (x - 2)$.'] = ['', '-1', '', '', 'The minimum is $f(x)=-1$ at $x=1$.']
        optimize['Find the minimum value of $f(x)=x\cdot \sqrt{x + 1}$.'] = ['', '-(2*3^(1/2))/9', '', '',
                                                                             'The minimum is $f(x)=-(2*\sqrt{3})/9$ at $x=-2/3$.']
        optimize['Find $x$ such that $f(x)=\sqrt{x + 1/x}$ is minimzed.'] = ['', '1', '', '',
                                                                             'The minimum is $f(x)=\sqrt{2}$ at $x=1$.']
        optimize['Find $x$ such that $f(x)=x\cdot e^x$ is minimized.'] = ['', '-1', '', '',
                                                                          'The minimum is $f(x)=-1/e$ at $x=-1$.']
        optimize['Find $x$ such that $x>0$ and $f(x)=x\cdot \ln(x)$ is minimized.'] = ['', '1/e', '', '',
                                                                                       'The minimum is $f(x)=-1/e$ at $x=1/e$.']

        optimize['Maximize the product of two numbers whose sum is $10$.'] = ['', '25', '',
                                                                              'The maximum product is $25$ at $x=y=5$.']
        optimize[
            'Maximize the product of three numbers whose sum is $30$ if the second number must be three times the first number.'] = [
            '', '250', '', 'The maximum product is $250$ at $x=5$ and $y=10$.']
        optimize['Maximize $f(x,y)=x\cdot y$ given $x+y=4$.'] = ['', '4', '', '',
                                                                 'The maximum is $f(x,y)=4$ at $x=2$, $y=2$.']
        optimize['Maximize $f(x,y)=x\cdot y$ given $3\cdot x + y=10$.'] = ['', '25/3', '', '',
                                                                           'The maximum is $f(x,y)=25/3$ at $x=5/3$, $y=5$.']
        optimize['Maximize $f(x,y)=x\cdot y$ given $2\cdot x+y=2$.'] = ['', '1/2', '', '',
                                                                        'The maximum is $f(x,y)=1/2$ at $x=1/2$, $y=1$.']
        optimize['Maximize $f(x,y)=x\cdot y$ given $x^3+y=4$.'] = ['', '3', '', '',
                                                                   'The maximum is $f(x,y)=3$ at $x=1$, $y=3$.']
        optimize['Maximize $f(x,y)=x\cdot \sqrt{\y}$ given $x+y=3$.'] = ['', '2', '', '',
                                                                         'The maximum is $f(x,y)=2$ at $x=2$, $y=1$.']

        # Single variable, arbitary functions...take from derivative practice? product rule, chain rule

        optimize['Find the minimum distance from the curve $x=y$ to the point $(1,0)$.'] = ['', '2^(1/2)/2', '', '',
                                                                                            'The minimum distance from the curve $x=y$ to the point $(1,0)$ is $\sqrt{1/2}$.']
        optimize['Find the minimum distance from the curve $y=x^2$ to the point $(-3,0)$.'] = ['', 'sqrt(5)', '', '',
                                                                                               'The minimum distance from the curve $y=x^2$ to the point $(-3,0)$ is $\sqrt{5}$.']

        optimize['Find the maximum rectangular area if $ft^2$ constrained by 600 $ft$ of fencing'] = ['', '22500',
                                                                                                      '$ft^2$', 'hint']
        optimize[
            'Find the maximum rectangular area if $ft^2$ constrained by 600 $ft$ of fencing if the fence is built against an existing wall (3 sides of fencing).'] = [
            '', '45000', '$ft^2$', 'hint']

        # 3 or for more sally's
        optimize[
            'Sally is running a lemonade stand.  She has determined that if she charges $x$ dollars for lemonade, then she will have $105-50x$ customers that day. What should she charge to maximize revenue?'] = [
            '', '1.05', '', 'hint']

        optimize['Find the maximum volume of a box that is made from $90 ft^2$ of material.'] = ['', '225', '$ft^3$',
                                                                                                 '']
        # optimize=['Find the maximum volume of a box with no top (5 sides) that is made from $90 ft^2$ of material.']=['','','$ft^3$','']

        optimize['Find the minimum surface area of a box that can hold $1000 ft^3$'] = ['', '600', '$ft^2$.', '']
        # optimize=['Find the minimum surface area of a box with no top (5 sides) that can hold $100 ft^3$.']=['','','$ft^2$','']

        # optimize['Find the maximum volume contained by a cylindrical can whose surface area is $20 in^2$.']=['','ans','','']

        master_bank = optimize

    if type == 2:
        minmax = {}
        bank = {}
        # polynomials
        bank['x^3-2x'] = ['-1', '2', '0.816497', '-1.08866', '2', '4']
        bank['x^2'] = ['-3', '1', '0', '0', '-3', '9']
        bank['x^3'] = ['-5', '5', '-5', '-125', '5', '125']
        bank['x^5-5'] = ['0', '2', '1', '-4', '2', '22']
        bank['x^{4/3}-x'] = ['0', '2', '0.421875', '-0.105469', '2', '0.519842']
        bank['x^3-x^2'] = ['0', '5', '0.666667', '-0.148148', '5', '100']
        bank['x^4-x'] = ['-3', '3', '0.629961', '-0.47247', '-3', '84']
        bank['x-x^2'] = ['-3', '3', '-3', '-12', '0.5', '0.25']
        bank[' 2x - 3x^2'] = ['-3', '3', '-3', '-33', '0.33333', '0.33333']
        bank['x^2 - 7x'] = ['-5', '5', '3.5', '-12.25', '-5', '60']
        bank['x^{1/2}-x'] = ['0', '4', '4', '-2', '0.25', '0.25']

        bank['x+\sin(2x)'] = ['-1', '2', '-1', '-1.9093', '1.0472', '1.91322']
        bank['x/2 - \cos(x)'] = ['-2', '1', '-0.523599', '-1.12782', '1', '-0.0403023']
        bank['x-\\tan(x)^2'] = ['-1', '1', '-1', '-3.42552', '0.400899', '0.221247']

        bank['x^2\cdot e^{-x}'] = ['-1', '4', '0', '0', '-1', '2.71828']
        bank['e^{x}/x'] = ['0.5', '2', '1', '2.71828', '2', '3.69453']

        bank['x^2-8\cdot\ln(x)'] = ['1', '4', '2', '-1.54518', '4', '4.90965']
        bank['x-2\cdot\ln(x)'] = ['1', '4', '2', '0.613706', '4', '1.22741']
        bank['\displaystyle\\frac{\ln(x)}{x}'] = ['1', '3', '1', '0', '2.71828', '0.367879']
        bank['\displaystyle\\frac{\ln(x)}{x^2}'] = ['1', '2', '1', '0', '1.64872', '0.18394']
        bank['x\cdot\ln(x)'] = ['0.1', '4', '0.367879', '-0.367879', '4', '5.54518']

        func = bank.keys()[random.randint(0, len(bank) - 1)]
        subtype = random.randint(1, 2)
        sprt = bank[func]

        if subtype == 1:
            prob = 'minimum'
            loc = sprt[2]
            ans = sprt[3]
        if subtype == 2:
            prob = 'maximum'
            loc = sprt[4]
            ans = sprt[5]
        key = 'Find the %s value of the function $f(x)=%s$ on the range $x=[%s,%s]$.' % (prob, func, sprt[0], sprt[1])
        anstex = 'The %s value is $f(x)=%s$ at $x=%s$' % (prob, ans, loc)
        minmax[key] = ['', ans, '', '', anstex]

        master_bank = minmax

    if type == 3:
        relrate = {}

        relrate[
            'A $13 \ ft$ ladder is sliding down a wall on a level surface with the base of the ladder $5 \ ft$ from the wall.  If the top of the ladder slides down at $-1\ ft/s$, at what rate is the bottom sliding out'] = [
            '', '2.4', '$ft/s$', 'hint']
        relrate[
            'A $20 \ ft$ ladder is sliding down a wall on a level surface with the base of the ladder $5 \ ft$ from the wall.  If the top of the ladder slides down at $-1\ ft/s$, at what rate is the bottom sliding out'] = [
            '', '3.3166', '$ft/s$', 'hint']
        relrate[
            'A $25 \ ft$ ladder is sliding down a wall on a level surface with the base of the ladder $8.8 \ ft$ from the wall.  If the top of the ladder slides down at $-1\ ft/s$, at what rate is the bottom sliding out'] = [
            '', '2.65909', '$ft/s$', 'hint']

        relrate[
            'A $25 \ ft$ ladder is sitting against a wall on a level surface with the base of the ladder $7 \ ft$ from the wall.  If the bottom of the ladder slides out at $1\ ft/s$, at what rate is the top sliding down'] = [
            '', '-7/24', '$ft/s$', 'hint']
        relrate[
            'A $17 \ ft$ ladder is sliding down a wall on a level surface with the base of the ladder $8 \ ft$ from the wall.  If the bottom of the ladder slides out at $3.75\ ft/s$, at what rate is the top sliding down'] = [
            '', '-2', '$ft/s$', 'hint']
        relrate[
            'A $10 \ ft$ ladder is sliding down a wall on a level surface with the base of the ladder $6 \ ft$ from the wall.  If the bottom of the ladder slides out at $2\ ft/s$, at what rate is the top sliding down'] = [
            '', '-1.5', '$ft/s$', 'hint']

        relrate[
            'The radius of a circle is decreasing at $1 \ m/s$.  At what rate is the volume changing when the radius is $5m$.'] = [
            '', '-10*pi', '$m^2/s$', '']

        relrate[
            'Water is being poured into a cylindrical container with a radius of $5\ in$ at $20 \pi \ in^3/s$.  At what rate is the height of the fluid changing?'] = [
            '', '.8', '$in/s$', '']
        relrate[
            'A cylinder has dimensions $r=3 \ ft$ and $h=7 \ ft$ that are both increasing at a rate of $1 \ ft/s$.  At what rate is the volume changing?'] = [
            '', '51*pi', '$ft^3/s$', '']

        relrate[
            'Water is being poured into a cone at a rate of $4\pi \ in^3/s$.  At what rate is the depth changing when the depth is $10 \ in$ and the radius is $5 \ in$.'] = [
            '', '.16', '$in/s$', '']
        relrate[
            'Water is being poured into a cone at a rate of $30\pi \ ft^3/s$.  The height is three times the radius.  At what rate is the radius changing when the depth is $15 \ ft$.'] = [
            '', '.1', '$ft/s$', '']

        relrate[
            'The radius of a sphere is increasing at $1\ m/s$.  At what rate is the volume changing when the radius is $2\ m$.'] = [
            '', '16*pi', '$m^3/s$', '']
        relrate[
            'The volume of a sphere is increasing at $24\ m/s$.  At what rate is the radius changing when the radius is $2\ m$.'] = [
            '', '3/(2*pi)', '$m/s$', '']
        relrate[
            'Helium is being pumped into a spherical balloon at $4\ in^3/s$.  At what rate is balloon radius increasing when the balloon radius is $5\ in$.'] = [
            '', '1/(25*pi)', '$in/s$', 'hint']

        relrate[
            'The area of an equilateral triangle is $A=\displaystyle\\frac{s^2\sqrt{3}}{4}$.  At what rate is the area changing if the edge length is $s=5 \ m$ and is increasing at a rate of $\sqrt{3} \ m/s$?'] = [
            '', '3.75', '$m^2/s$', '']
        relrate[
            'A rectangle has side lengths of $10\ ft$ and $5 ft$ that are decreasing at $1 ft/s$ and increasing at $2 \ ft/s$ respectively.  At what rate is the area changing?'] = [
            '', '15', '$ft^2/s$', '']
        relrate[
            'A edge length of a cube is $5\ cm$ and increasing at a rate of $2 \ cm/s$.  At what rate is the volume increasing?'] = [
            '', '150', '$cm^3/s$', '']
        relrate[
            'A volume of a cube is $1000 \ m^3$ and increasing at a rate of $30 \ m^3/s$.  At what rate is the edge length increasing?'] = [
            '', '.1', '$m/s$', '']
        # drain the cone and the balloon

        # moving away problem
        relrate[
            'Jake is running away from a rocket he just launched straight up.  The rocket is travelling at $40 \ ft/s$ and he is running at $9 \ ft/s$.  What rate is the distance between Jake and the rocket changing $5$ seconds later?'] = [
            '', '41', '$ft/s$', '']
        # more running away
        #    relrate=['John is running south at $15 ft/s$ and Jake is filming John run.  If jake is $150 ft$ southwest of John, at what rate is Jake turning to keep the camera focused on John?']=['','','$rad/s$','']
        # john jumping out of an airplane
        # camera problem

        master_bank = relrate

    if type == 4:
        lahopital = {}
        # 0/0
        lahopital['Find $\displaystyle\lim_{x \\to 0} \\frac{\sin(x)}{x} $'] = ['', '1', '', 'hint']
        lahopital['Find $\displaystyle\lim_{x \\to 0} \\frac{(\cos(x)-1)}{x^2} $'] = ['', '-1/2', '', 'hint']
        lahopital['Find $\displaystyle\lim_{x \\to 0} \\frac{\sin(x)}{x^2} $'] = ['', 'inf', '', 'hint']
        lahopital['Find $\displaystyle\lim_{x \\to 0} \\frac{\\tan(x)}{x} $'] = ['', '1', '', 'hint']
        lahopital['Find $\displaystyle\lim_{x \\to \infty} \\frac{\ln(x)}{x} $'] = ['', '0', '', 'hint']

        # 0^inf inf^0
        lahopital['Find $\displaystyle\lim_{x \\to 0} x^{1/x} $'] = ['', '0', '', 'Take the log of this expression']
        lahopital['Find $\displaystyle\lim_{x \\to \infty} x^{1/x} $'] = ['', '1', '',
                                                                          'Take the log of this expression']
        lahopital['Find $\displaystyle\lim_{x \\to 0} \cos(x)^{1/x} $'] = ['', '1', '',
                                                                           'Take the log of this expression']
        lahopital['Find $\displaystyle\lim_{x \\to \infty} \sin(x)^{1/x} $'] = ['', '0', '',
                                                                                'Take the log of this expression']

        # 0*inf
        lahopital['Find $\displaystyle\lim_{x \\to 0} x\cdot\ln(x) $'] = ['', '0', '', 'Rewrite this in the form $0/0$']
        lahopital['Find $\displaystyle\lim_{x \\to -\infty} x\cdot e^x $'] = ['', '0', '',
                                                                              'Rewrite this in the form $0/0$']
        lahopital['Find $\displaystyle\lim_{x \\to 0} \ln(x)\sin(x) $'] = ['', '0', '',
                                                                           'Rewrite this in the form $0/0$']
        lahopital['Find $\displaystyle\lim_{x \\to \pi/2} (x-\pi/2)\cdot\tan(x) $'] = ['', '-1', '',
                                                                                       'Rewrite this in the form $0/0$']

        master_bank = lahopital

    if type == 5:
        newton = {}
        newton[
            "Approximate the solution to $x^2=3$ with three iterations of Newton's Method and an initial guess $x_0=1$"] = [
            '$x_3 = $', '1.7321438', '', '']
        newton[
            "Approximate the solution to $x^2+x-3=0$ with three iterations of Newton's Method and an initial guess $x_0=1$"] = [
            '$x_3 = $', '1.302775655', '', '']
        newton[
            "Approximate a solution to $\cos(x)=x$ with three iterations of Newton's Method and an initial guess $x_0=0$"] = [
            '$x_3 = $', '0.739112891', '', 'Solve the equation $\cos(x)-x=0$']
        newton[
            "Approximate a solution to $\cos(x)-x^2=0$ with three iterations of Newton's Method and an initial guess $x_0=2$"] = [
            '$x_3 = $', '0.82466018', '', '']
        newton[
            "Approximate a solution to $\sin(x)=e^{-x}$ with three iterations of Newton's Method and an initial guess $x_0=0$"] = [
            '$x_3 = $', '0.58852941', '', '']
        # every combo of ln,e,x,sin

        newton["Approximate $\sqrt{7}$ with two iterations of Newton's Method and an initial guess $x_0=3$"] = [
            '$x_2 = $', '2.6458333', '', 'Solve the equation $x^2-7=0$']
        newton["Approximate $\sqrt{17}$ with two iterations of Newton's Method and an initial guess $x_0=4$"] = [
            '$x_2 = $', ' 4.1231061', '', 'Solve the equation $x^2-17=0$']
        newton["Approximate $\sqrt{24}$ with two iterations of Newton's Method and an initial guess $x_0=5$"] = [
            '$x_2 = $', '4.89897959', '', 'Solve the equation $x^2-24=0$']
        newton["Approximate $\sqrt{5}$ with two iterations of Newton's Method and an initial guess $x_0=2$"] = [
            '$x_2 = $', '2.2361111', '', 'Solve the equation $x^2-5=0$']
        newton["Approximate $\sqrt[3]{9}$ with two iterations of Newton's Method and an initial guess $x_0=2$"] = [
            '$x_2 = $', '2.0800888', '', 'Solve the equation $x^3-9=0$']
        # Add more cube roots and random roots, 1/3, 1/5, etc

        newton["Approximate $\sin(1)$ with three iterations of Newton's Method and an initial guess $x_0=.5$"] = [
            '$x_3 = $', '0.84161930', '', 'Solve the equation $arc\sin(x)-1=0$']
        newton["Approximate $\cos(1.5)$ with two iterations of Newton's Method and an initial guess $x_0=0$"] = [
            '$x_3 = $', '0.07073720', '', 'Solve the equation $arc\cos(x)-1.5=0$']
        newton[
            "Use $y=\ln(x)-1$ to approximate $e$ with three iterations of Newton's Method and an initial guess $x_0=3$"] = [
            '$x_2 = $', ' 2.7182451', '', 'Solve the equation $\ln(x)-1=0$']
        newton[
            "Use $y=\sin(x)$ to approximate $\pi$ with three iterations of Newton's Method and an initial guess $x_0=3$"] = [
            '$x_2 = $', '3.14159265', '', 'Solve the equation $\sin(x)=0$']

        master_bank = newton

    rand1 = random.randrange(0, len(master_bank))
    problem = master_bank.keys()[rand1]
    ans = master_bank[problem][1]
    prefix = master_bank[problem][0]
    suffix = master_bank[problem][2]

    hint = master_bank[problem][3]
    if len(master_bank[problem]) == 5 and type != 4:
        anstex = master_bank[problem][4]
    elif type == 4:
        anstex = 'The limit is' + prefix + ' $' + toTEX(ans) + '$ ' + suffix
    else:
        anstex = 'The answer is ' + prefix + ' $' + toTEX(ans) + '$ ' + suffix

    problem = problem.replace('m/s$', '\mathrm{m}/\mathrm{s}$')
    problem = problem.replace('cm/s$', '\mathrm{cm}/\mathrm{s}$')
    problem = problem.replace('in/s$', '\mathrm{in}/\mathrm{s}$')
    problem = problem.replace('ft/s$', '\mathrm{ft}/\mathrm{s}$')

    problem = problem.replace('m^2/s$', '\mathrm{m^2}/\mathrm{s}$')
    problem = problem.replace('cm^2/s$', '\mathrm{cm}^2/\mathrm{s}$')
    problem = problem.replace('in^2/s$', '\mathrm{in^2}/\mathrm{s}$')
    problem = problem.replace('ft^2/s$', '\mathrm{ft^2}/\mathrm{s}$')

    problem = problem.replace('cm^3/s$', '\mathrm{cm}^3/\mathrm{s}$')
    problem = problem.replace('m^3/s$', '\mathrm{m^3}/\mathrm{s}$')
    problem = problem.replace('in^3/s$', '\mathrm{in^3}/\mathrm{s}$')
    problem = problem.replace('ft^3/s$', '\mathrm{ft^3}/\mathrm{s}$')

    problem = problem.replace('in^2$', '\mathrm{in}^2$')
    problem = problem.replace('in^3$', '\mathrm{in}^3$')
    problem = problem.replace('m^2$', '\mathrm{m}^2$')
    problem = problem.replace('m^3$', '\mathrm{m}^3$')
    problem = problem.replace('cm^2$', '\mathrm{cm}^2$')
    problem = problem.replace('cm^3$', '\mathrm{cm}^3$')
    problem = problem.replace('ft^2$', '\mathrm{ft}^2$')
    problem = problem.replace('ft^3$', '\mathrm{ft}^3$')

    problem = problem.replace('m$', '\mathrm{m}$')
    problem = problem.replace('cm$', '\mathrm{cm}$')
    problem = problem.replace('s$', '\mathrm{s}$')
    problem = problem.replace('in$', '\mathrm{in}$')
    problem = problem.replace('ft$', '\mathrm{ft}$')

    suffix = suffix.replace('cm$', '\mathrm{cm}$')
    suffix = suffix.replace('m/s$', '\mathrm{m}/\mathrm{s}$')
    suffix = suffix.replace('in/s$', '\mathrm{in}/\mathrm{s}$')
    suffix = suffix.replace('ft/s$', '\mathrm{ft}/\mathrm{s}$')

    suffix = suffix.replace('cm^2/s$', '\mathrm{cm}^2/\mathrm{s}$')
    suffix = suffix.replace('m^2/s$', '\mathrm{m^2}/\mathrm{s}$')
    suffix = suffix.replace('in^2/s$', '\mathrm{in^2}/\mathrm{s}$')
    suffix = suffix.replace('ft^2/s$', '\mathrm{ft^2}/\mathrm{s}$')

    suffix = suffix.replace('cm^3/s$', '\mathrm{cm}^3/\mathrm{s}$')
    suffix = suffix.replace('m^3/s$', '\mathrm{m^3}/\mathrm{s}$')
    suffix = suffix.replace('in^3/s$', '\mathrm{in^3}/\mathrm{s}$')
    suffix = suffix.replace('ft^3/s$', '\mathrm{ft^3}/\mathrm{s}$')

    suffix = suffix.replace('in^2$', '\mathrm{in}^2$')
    suffix = suffix.replace('in^3$', '\mathrm{in}^3$')
    suffix = suffix.replace('m^2$', '\mathrm{m}^2$')
    suffix = suffix.replace('m^3$', '\mathrm{m}^3$')
    suffix = suffix.replace('cm^2$', '\mathrm{cm}^2$')
    suffix = suffix.replace('cm^3$', '\mathrm{cm}^3$')
    suffix = suffix.replace('ft^2$', '\mathrm{ft}^2$')
    suffix = suffix.replace('ft^3$', '\mathrm{ft}^3$')

    suffix = suffix.replace('m$', '\mathrm{m}$')
    suffix = suffix.replace('s$', '\mathrm{s}$')
    suffix = suffix.replace('in$', '\mathrm{in}$')
    suffix = suffix.replace('ft$', '\mathrm{ft}$')

    anstex = anstex.replace('$inf$', '$\infty$')

    print problem
    print ans
    print anstex
    print prefix
    print suffix
    print hint


if __name__ == '__main__':
    main()