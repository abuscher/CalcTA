#!/usr/bin/python -tt

import sys
import random
import math
from math import *
import re
import latex
from latex import *
import polynomial
import fractions

class int_problem(object):
  def __init__(self,type):
    bank={}
    if type=='antider':
      subtype=random.randint(1,3)
      poly={}
      trans={}
      trig={}
      hypinv={}
      poly[ "x+5                                " ]=  ['',''," 1/2*x^2+5*x     ",'hint']
      poly[ "3*x^2+x^4                          " ]=  ['',''," x^3+1/5*x^5     ",'hint']
      poly[ "x^3                                " ]=  ['',''," 1/4*x^4         ",'hint']
      poly[ "2*x^4                              " ]=  ['',''," .4*x^5          ",'hint']
      poly[ "6*x^5                              " ]=  ['',''," x^6             ",'hint']
      poly[ "pi*x^(pi-1)                        " ]=  ['',''," x^pi            ",'hint']
      poly[ "e*x^(e-1)                          " ]=  ['',''," x^e             ",'hint']
      poly[ "1/2*x^(-1/2)                       " ]=  ['',''," x^(1/2)         ",'hint']
      poly[ "1/3*x^(-2/3)                       " ]=  ['',''," x^(1/3)         ",'hint']
      poly[ "7/3*x^(4/3)                        " ]=  ['',''," x^(7/3)         ",'hint']
      poly[ "-1/2*x^(-3/2)                      " ]=  ['',''," x^(-1/2)        ",'hint']
      poly[ "-1/3*x^(-4/3)                      " ]=  ['',''," x^(-1/3)        ",'hint']
      poly[ "-1/x^2                             " ]=  ['',''," 1/x             ",'hint']
      poly[ "-2/x^3                             " ]=  ['',''," 1/x^2           ",'hint']
      poly[ "-1.3*x^(-2.3)                      " ]=  ['',''," 1/x^1.3         ",'hint']
      poly[ "100*x^99                           " ]=  ['',''," x^100           ",'hint']
      poly[ "6*x^(.2)                           " ]=  ['',''," 5*x^1.2         ",'hint']
      poly[ ".1*x^(-.9)                         " ]=  ['',''," x^.1            ",'hint']
      poly[ "3*x^2+1/3*x^(-2/3)                 " ]=  ['',''," x^3+x^(1/3)     ",'hint']
      poly[ "1-1/x^2                            " ]=  ['',''," x+1/x           ",'hint']
      poly[ "2*x+1                              " ]=  ['',''," x^2+x           ",'hint']

      trig[ "cos(x)                             " ]=  ['',''," sin(x)          ",'hint']
      trig[ "-sin(x)                            " ]=  ['',''," cos(x)          ",'hint']
      trig[ "sec(x)^2                           " ]=  ['',''," tan(x)          ",'hint']
      trig[ "sec(x)*tan(x)                      " ]=  ['',''," sec(x)          ",'hint']
      trig[ "-csc(x)*cot(x)                     " ]=  ['',''," csc(x)          ",'hint']
      trig[ "-csc(x)^2                          " ]=  ['',''," cot(x)          ",'hint']

      trans["e^x             " ]=  ['',''," e^x             ",'hint']
      trans["1/x                                " ]=  ['',''," ln(x)           ",'hint']

      hypinv["1/(1-x^2)^(1/2)          " ]=  ['',''," asin(x)         ",'hint']
      hypinv["-1/(1-x^2)^(1/2)                   " ]=  ['',''," acos(x)         ",'hint']
      hypinv["1/(1+x^2)                          " ]=  ['',''," atan(x)         ",'hint']
      hypinv["1/(x*(1-x^2)^(1/2))                " ]=  ['',''," asec(x)         ",'hint']
      hypinv["-1/(x*(1-x^2)^(1/2))               " ]=  ['',''," acsc(x)         ",'hint']
      hypinv["-1/(1+x^2)                         " ]=  ['',''," acot(x)         ",'hint']
      hypinv["cosh(x)                            " ]=  ['',''," sinh(x)         ",'hint']
      hypinv["sinh(x)                            " ]=  ['',''," cosh(x)         ",'hint']
      #hypinv["sech(x)^2                          " ]=  ['',''," tanh(x)         ",'hint']
      #hypinv["-sech(x)*tanh(x)                   " ]=  ['',''," sech(x)         ",'hint']
      #hypinv["-csch(x)*coth(x)                   " ]=  ['',''," csch(x)         ",'hint']
      #hypinv["-csch(x)^2                         " ]=  ['',''," coth(x)         ",'hint']
      if subtype==1:
        bank=poly
      if subtype==2:
        bank=trig
      if subtype==3:
        bank=trans
        bank.update(hypinv)

    if type=='usub':
      usub={}
      usub[ "9*(3*x - 1)^2                      " ]=  ['',''," (3*x-1)^3       ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=3x-1$.']
      usub[ "50*(5*x - 3)^9                     " ]=  ['',''," (5*x-3)^10      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=5x-3$.']
      usub[ "3*(4*x-7)*(2*x^2-7*x+1)^2          " ]=  ['',''," (2*x^2-7*x+1)^3 ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=2x^2-7x+1$.']
      usub[ "-(6*x)/(3*x^2 + 1)^2               " ]=  ['',''," 1/(3*x^2+1)     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=3x^2+1$']
      usub[ "(6*(2*x - 5*x^4))/(x^2 - x^5)^4    " ]=  ['',''," 2/(x^5-x^2)^3   ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^5-x^2$']
      usub[ "6.2*x*(x^2 - 1)^(2.1)              " ]=  ['',''," (x^2-1)^3.1     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^2-1$']
      usub[ "cos(x)*cos(sin(x))                 " ]=  ['',''," sin(sin(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)$']
      usub[ "-sin(x)*cos(cos(x))                " ]=  ['',''," sin(cos(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cos(x)$']
      usub[ "sec(x)^2*cos(tan(x))               " ]=  ['',''," sin(tan(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\\tan(x)$']
      usub[ "sec(x)*tan(x)*cos(sec(x))          " ]=  ['',''," sin(sec(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sec(x)$']
      usub[ "-csc(x)*cot(x)*cos(csc(x))         " ]=  ['',''," sin(csc(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\csc(x)$']
      usub[ "-csc(x)^2*cos(cot(x))              " ]=  ['',''," sin(cot(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cos(x)$']
      usub[ "sin(x)*sin(cos(x))                 " ]=  ['',''," cos(cos(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cos(x)$']
      usub[ "-cos(x)*sin(sin(x))                " ]=  ['',''," cos(sin(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)$']
      usub[ "-sec(x)^2*sin(tan(x))              " ]=  ['',''," cos(tan(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\\tan(x)$']
      usub[ "-sec(x)*tan(x)*sin(sec(x))         " ]=  ['',''," cos(sec(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sec(x)$']
      usub[ "csc(x)*cot(x)*sin(csc(x))          " ]=  ['',''," cos(csc(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\csc(x)$']
      usub[ "csc(x)^2*sin(cot(x))               " ]=  ['',''," cos(cot(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cot(x)$']
      usub[ "sec(x)^2*sec(tan(x))^2             " ]=  ['',''," tan(tan(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\\tan(x)$']
      usub[ "sec(x)*tan(x)*sec(sec(x))*tan(sec(x))" ]=  ['',''," tan(sec(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sec(x)$']
      usub[ "csc(x)*cot(x)*csc(csc(x))*cot(csc(x))" ]=  ['',''," tan(csc(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\csc(x)$']
      usub[ "csc(x)^2*csc(cot(x))^2             " ]=  ['',''," tan(cot(x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cot(x)$']
      usub[ "1/(x*ln(x))                        " ]=  ['',''," ln(ln(x))       ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "e^x*e^(e^x)                        " ]=  ['',''," e^(e^x)         ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=e^x$']
      usub[ "ln(2)^2*2^x*2^(2^x)                " ]=  ['',''," 2^(2^x)         ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=2^x$']
      usub[ "(6*x+2)/(3*x^2 + 2*x)              " ]=  ['',''," ln(3*x^2+2*x)   ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=3x^2+2x$']
      usub[ "2/(x-1)                            " ]=  ['',''," 2*ln(x-1)     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x-1$']
      usub[ "2*ln(x)/x                          " ]=  ['',''," ln(x)^2         ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "3*ln(x)^2/x                        " ]=  ['',''," ln(x)^3         ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "-1/(x*ln(x)^2)                     " ]=  ['',''," 1/ln(x)         ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "-2/(x*ln(x)^3)                     " ]=  ['',''," 1/ln(x)^2       ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "ln(x)^.3/x                         " ]=  ['',''," ln(x)^1.3       ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "cot(x)                             " ]=  ['',''," ln(sin(x))      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)$']
      usub[ "-tan(x)                            " ]=  ['',''," ln(cos(x))      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cos(x)$']
      usub[ "cos(x)*e^(sin(x))                  " ]=  ['',''," e^(sin(x))      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)$']
      usub[ "2*sin(x)cos(x)*e^(sin(x)^2)        " ]=  ['',''," e^(sin(x)^2)    ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)^2$']
      usub[ "-cos(x)*e^(cos(x))                 " ]=  ['',''," e^(cos(x))      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\cos(x)$']
      usub[ "ln(2)*cos(x)*2^(sin(x))            " ]=  ['',''," 2^(sin(x))      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)$']
      usub[ "cos(ln(x))/x                       " ]=  ['',''," sin(ln(x))      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)$']
      usub[ "e^x*cos(e^x)                       " ]=  ['',''," sin(e^x)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=e^x$']
      usub[ "ln(2)*2^x*cos(2^x)                 " ]=  ['',''," sin(2^x)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=2^x$']
      usub[ "-cos(x + 1/x)*(1/x^2 - 1)          " ]=  ['',''," sin(x+1/x)      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x+1/x$']
      usub[ "2*x*2)                             " ]=  ['',''," sin(x^2)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^2$']
      usub[ "-1/2*x^(1/2)*cos(x^(1/2))          " ]=  ['',''," sin(x^(1/2))    ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^{1/2}$']
      usub[ "(3*x^2+1)*cos(x^3+x)               " ]=  ['',''," sin(x^3+x)      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^3+x$']
      usub[ "4*x^3*cos(x^4)                     " ]=  ['',''," sin(x^4)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^4$']
      usub[ "-2*x*sin(x^2)                      " ]=  ['',''," cos(x^2)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^2$']
      usub[ "-3*x^2*sin(x^3)                    " ]=  ['',''," cos(x^3)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^3$']
      usub[ "-(4*x^3-1/x^2)*sin(x^4+1/x)        " ]=  ['',''," cos(x^4+1/x)    ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^4+1/x$']
      usub[ "sec(x+1)^2                         " ]=  ['',''," tan(x+1)        ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x+1$']
      usub[ "1/(2*x^(1/2))*sec(x^(1/2))*tan(x^(1/2))" ]=  ['',''," sec(x^(1/2))    ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=x^{1/2}$']
      usub[ "2*x*csc(1-x^2)*cot(1-x^2)          " ]=  ['',''," csc(1-x^2)      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=1-x^2$']
      usub[ "-9*x^2*csc(3*x^3)^2                " ]=  ['',''," cot(3*x^3)      ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=3*x^3$']
      usub[ "(1/x+2*x)*cos(ln(x)+x^2)           " ]=  ['',''," sin(ln(x)+x^2)  ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(x)+x^2$']
      usub[ "(cos(x)+1)/(sin(x)+x)              " ]=  ['',''," ln(sin(x)+x)    ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(x)+x$']
      usub[ "2*(3*cos(x)+1/x)*(3*sin(x)+ln(x))  " ]=  ['',''," (3*sin(x)+ln(x))",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=3\sin(x)+\ln(x)$']
      usub[ "2*(3*x-2)*cos((3*x-2)^2)           " ]=  ['',''," sin((3*x-2)^2)  ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=(3x-2)^2$']
      usub[ "3*(2*x+7)^2*cos((2*x+7)^3)         " ]=  ['',''," sin((2*x+7)^3)  ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=(2x+7)^3$']
      usub[ "(8*x - 12)/(2*x - 3)^2             " ]=  ['',''," ln((3-2*x)^2)   ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=(3-2x)^2$']
      usub[ "(4*ln(3 - 2*x))/(2*x - 3)          " ]=  ['',''," ln(3-2*x)^2     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=3-2x$']
      usub[ "1/(x*ln(ln(x))*ln(x))              " ]=  ['',''," ln(ln(ln(x)))   ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\ln(\ln(x))$']
      usub[ "e^x*e^(e^x)*e^(e^(e^x))            " ]=  ['',''," e^(e^(e^x))     ",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=e^{e^x}$']
      usub[ "cos(x)*cos(sin(x))*cos(sin(sin(x)))" ]=  ['',''," sin(sin(sin(x)))",'Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/usub" target="_blank">$u$-substitution</a> with $u=\sin(\sin(x))$']


  #trig
      usub['sin(x)*cos(x)']=['','','sin(x)^2/2','hint']
      usub['sin(x)^2*cos(x)']=['','','sin(x)^3/3','hint']
      usub['sin(x)^3*cos(x)']=['','','sin(x)^4/4','hint']
      usub['sin(x)*cos(x)^2']=['','','-cos(x)^3/3','hint']
      usub['sin(x)*cos(x)^3']=['','','-cos(x)^4/4','hint']
      usub['ln(x)/x']=['','','ln(x)^2/2','hint']
      usub['sin(x)^3']=['','','cos(x)^3/3-cos(x),','hint']
      usub['cos(x)^3']=['','','sin(x)-sin(x)^3/3','hint']
      bank=usub


    if type=='trigint':
      trigint={}
      subtype=random.randint(1,4)

      if subtype==1:
      #sin/cos
        trigint['\sqrt{1-x^2}']=['0','1','pi/4','Use the trigonometric substitution $x=\sin(\theta).']
        trigint['\sqrt{1-x^2}']=['','','asin(x)/2 + (x*(1 - x^2)^(1/2))/2','Use the trigonometric substitution $x=\sin(\theta).']
        trigint['\sqrt{1-(x-1)^2}']=['','','asin(x - 1)/2 + ((1 - (x - 1)^2)^(1/2)*(x - 1))/2','Use the trigonometric substitution $x=\sin(\theta).']
        trigint['(1-x^2)^{3/2}']=['0','1','3*pi/16','Use the trigonometric substitution $x=\sin(\theta).']
        trigint['\sqrt{1-4x^2}']=['0','1/2','pi/8','Use the trigonometric substitution $x=1/2\sin(\theta).']
        trigint['x^3\cdot (1-x^2)^{1/2}']=['','','-((1 - x^2)^(3/2)*(3*x^2 + 2))/15','Use the trigonometric substitution $x=\sin(\theta).']
        trigint['x^3/(1-x^2)^{1/2}']=['','','-((1 - x^2)^(1/2)*(x^2 + 2))/3','Use the trigonometric substitution $x=\sin(\theta).']
#        trigint['e^x\cdot sqrt{1-e^{2*x}}']=['','','','']

      if subtype==2:
      #tan
        trigint['\displaystyle\\frac{1}{x^2+9}']=['','','1/3*atan(x/3)','hint']
        trigint['\displaystyle\\frac{1}{x^2+1}']=['','','atan(x)','Use the trigonometric substitution $x=\\tan(\theta).']
        trigint['\displaystyle\\frac{1}{x^2+x+1/2}']=['','','2*atan(2*x + 1)','hint']
        trigint['\displaystyle\\frac{x^2}{x^2+1}']=['-1','1','2-pi/2','hint']
        trigint['\displaystyle\\frac{1}{x^2\cdot\sqrt{x^2+1}}']=['','','-(x^2 + 1)^(1/2)/x','Use the trigonometric substitution $x=\\tan(\theta).']
        trigint['\displaystyle\\frac{x^2+2x}{x^2+2x+2}']=['','','x - 2*atan(x + 1)','hint']

      if subtype==3:
      #tan
        c=random.randint(1,9)
        c2=c*c
        obj=polynomial.poly(1,2)
        obj.make_quad()
        (a,b)=obj.coeff
        ac=fractions.gcd(a,c)
        bc=fractions.gcd(b,c)
        coeff=(a*c,a/ac,c/ac,b/bc,c/bc)
        pcoeff=(obj.quadratic[0],obj.quadratic[1],obj.quadratic[2]+c2)
        ans="1/%d*arctan(%d/%d*x+%d/%d)" % coeff
        problem="\displaystyle\\frac{1}{%dx^2+%dx+%d}" % pcoeff
        hint='Complete the square in the denominator and integrate.  You can find a similar example '
        lower=''
        upper=''
        trigint[problem]=[lower,upper,ans,hint]
      if subtype==4:
      #sin
        c=random.randint(1,9)
        c2=c*c
        obj=polynomial.poly(1,2)
        obj.make_quad()
        (a,b)=obj.coeff
        ac=fractions.gcd(a,c)
        bc=fractions.gcd(b,c)
        coeff=(a,a/ac,c/ac,b/bc,c/bc)
        pcoeff=(-obj.quadratic[2]+c2,-obj.quadratic[0],-obj.quadratic[1])
        ans="1/%d*arcsin(%d/%d*x+%d/%d)" % coeff
        problem="\displaystyle\\frac{1}{\sqrt{%d+%dx^2+%dx}}" % pcoeff
        hint='Complete the square in the denominator and integrate'
        lower=''
        upper=''
        trigint[problem]=[lower,upper,ans,hint]
      bank=trigint

#Integration by parts

    if type=='ibp':
      ibp={}
    #Integration by parts
#ln
      ibp['x*ln(x)']=['','','1/2*x^2*ln(x) - x^2/4','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=x$.']
      ibp['x^(2)*ln(x)']=['','','1/3*x^3*ln(x) - x^3/9','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=x^2$.']
      ibp['x^(pi)*ln(x)']=['','','1/(pi+1)*x^(pi+1)*ln(x) - x^(pi+1)/(pi+1)^2','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=x^{\pi}$.']
      ibp['x^2*ln(5*x)']=['','','1/3*(x^3*ln(5*x))-x^3/9','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(5x)$ and $v\'=x^2$.']
      ibp['x^3*ln(2*x)']=['','','1/4*x^4*ln(2*x) - x^4/16','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(2x)$ and $v\'=x^3$.']
      ibp['x^e*ln(x)']=['','',' x^(e + 1)*ln(x) - x^(e + 1)/(e + 1)^2','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=x^e$.']
      ibp['x^(1/2)*ln(x)']=['','','2/3*x^(3/2)*ln(x) - 4/9*x^(3/2)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=x^{1/2}$.']
      ibp['x^(1.3)*ln(x)']=['','','1/2.3*x^(2.3)*ln(x) - 1/5.29*x^(2.3)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=x^{1.3}$.']
      ibp['ln(x)']=['','','x*ln(x)-x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=\ln(x)$ and $v\'=1$.']

#e^x and poly
      ibp['x*e^x']=['','','(x-1)*e^x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=x$ and $v\'=e^x$.']
      ibp['x*e^(2*x)']=['','','1/4*(2*x-1)e^(2*x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=x$ and $v\'=e^{2x}$.']
      ibp['x*e^(-x)']=['','','-(x+1)*e^(-x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=x$ and $v\'=e^{-x}$.']
      ibp['x^2*e^(5*x)']=['','','1/125*(25*x^2 - 10*x + 2)*e^(5*x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> with $u=x^2$ and $v\'=e^{5x}$.']

#e^x and trig/ln
      ibp['cos(x)*e^x']=['','','1/2*(cos(x)+sin(x))*e^x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $v\'=e^x$.']
      ibp['sin(x)*e^x']=['','','1/2*(sin(x)-cos(x))*e^x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $v\'=e^x$.']
      ibp['sin(2*x)*e^x']=['','','1/5*(sin(2*x) - 2*cos(2*x))*e^x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $v\'=e^x$.']
      ibp['cos(3*x)*e^x']=['','','1/10*(3*sin(3*x) + cos(3*x))*e^x','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $v\'=e^x$.']
      ibp['cos(3*x)*e^(x/2)']=['','','1/37*(6*sin(3*x) + 2*cos(3*x))*e^(x/2)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $v\'=e^{x/2}$.']

#poly
    #ibp['x*(x-1)^(1/2)']=''
    #ibp['x*(2*x^3+7)^2']=''
    #ibp['x*(x+1)^(1/3)']=''
    #ibp['x^2*(x+1)^10']=''

#poly and trig
      ibp['x*sin(x)']=['','','sin(x) - x*cos(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $u=x$ and $v=\sin(x)$.']
      ibp['x*cos(x)']=['','','cos(x) + x*sin(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $u=x$ and $v=\cos(x)$.']
      ibp['x*sin(3*x)']=['','','sin(3*x)/9 - x*cos(3*x)/3','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $u=x$ and $v=\sin(3x)$.']
      ibp['x*cos(.5*x)']=['','','4*cos(.5*x) + 2*x*sin(.5*x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $u=x$ and $v=\cos(.5\cdot x)$.']
      ibp['x^2*sin(x)']=['','','2*cos(x) - x^2*cos(x) + 2*x*sin(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $u=x^2$.']
      ibp['x^2*cos(x)']=['','','x^2*sin(x) - 2*sin(x) + 2*x*cos(x)','Use <a class="hintlink" href="http://www.calcta.com/tutorial.php?page=integral/ibp" target="_blank">integration by parts</a> twice with $u=x^2$.']
      bank=ibp

#ibp and u sub
    #ibp['x*sec(x)^2']=''
    #ibp['x*sec(x)*tan(x)']=''
    #ibp['x*csc(x)*cot(x)']=''
    #ibp['x*csc(x)^2']=''

#Improper Integrals (numeric)
    if type=='improper':
      improper={}

      improper['\displaystyle\\frac{1}{x^{1/2}}']=  ['0','1','2','']
      improper['\\frac{1}{x}']=  ['0','1','div','']
      improper['\\frac{1}{x^2}']=['0','1','div','']
      improper['\\frac{1}{x^2}']=['1','\infty','1','']
      improper['\\frac{x}{(x^2+3)^2}']=['0','\infty','1/6','']

      improper['\\frac{1}{x}']=  ['1','\infty','div','']
      improper['\\frac{1}{x^2}']=['1','\infty','1','']
      improper['\\frac{1}{x^(3/2)}']=['1','\infty','2','']
      improper['\\frac{2}{x^3}']=['1','\infty','1','']
      improper['\\frac{1}{x^4}']=['1','\infty','1/3','']
      improper['\\frac{2}{x^5}']=['1','\infty','1/2','']
      improper['\\frac{x}{x^2+1}']=  ['1','\infty','div','']

      improper['e^{-x}']=['0','\infty','1','']
      improper['x\cdot e^{-x}']=['0','\infty','1','']

      improper['x\cdot e^{-x^2}']=['0','\infty','1/2','']

      improper['\displaystyle\\frac{1}{sqrt{16-x^2}}']=['0','4','pi/2','']
      improper['\displaystyle\\frac{1}{1+x^2}']=['0','1','pi/4','']

      improper['\displaystyle\\frac{cos(x)}{sqrt{sin(x)}}']=['0','\pi/2','2','']

      bank=improper

    self.problem=bank.keys()[random.randint(0,len(bank)-1)]
    self.answer=bank[self.problem][2]
    self.lower=bank[self.problem][0]
    self.upper=bank[self.problem][1]
    self.hint=bank[self.problem][3]

# Define a main()
def main():
  options=sys.argv[1]
  #options='000001'
  if int(options)==0: options='1'+options[1:]
  pick=[]
  for i in range(len(options)):
    if options[i]=='1':pick.append(i)
  type=pick[random.randrange(0,len(pick))]
  #type=5
  #options[0]=antiderivatives
  #options[1]=u substitution
  #options[2]=trig integral
  #options[3]=integration by parts
  #options[4]=improper integrals
  #options[5]=partial fractions
  master_bank={}

  if type==0:
    intprob=int_problem('antider')
  elif type==1:
    intprob=int_problem('usub')
  elif type==2:
    intprob=int_problem('trigint')
  elif type==3:
    intprob=int_problem('ibp')
  elif type==4:
    intprob=int_problem('improper')
  if type<5:
    problem=intprob.problem
    ans=intprob.answer
    lower=intprob.lower
    upper=intprob.upper
    hint=intprob.hint

#Partial Fractions

#ln with poly(2,2)
#ln with poly(2,1)
#arctan x^2+b^2
#arctan complete the square
#arctan x^2+bx (+b^2/4) - b^2/4
#ln a^2*x^2-b^2
#split linear/quadratic into usub with log and arctan (only if usub is checked?)

  partial={}
  if type==5:
    subtype=random.randint(1,3)
    if subtype==1:
    #ln with poly(2,2)
      obj=polynomial.poly(2,1)
    #ln with poly(2,1)
    if subtype==2:
      obj=polynomial.poly(2,2)
    #ln
    if subtype==1 or subtype==2:
      obj.make_rquad()
      coeff=obj.rcoeff[6:8]+ obj.rcoeff[1:3]+ obj.rcoeff[4:6]
      c=[fractions.gcd(obj.rcoeff[0],obj.rcoeff[1]),fractions.gcd(obj.rcoeff[3],obj.rcoeff[4])]
      anscoeff=tuple([obj.rcoeff[0]/c[0]]+[obj.rcoeff[1]/c[0]]+list(obj.rcoeff[1:3])+[obj.rcoeff[3]/c[1]]+[obj.rcoeff[4]/c[1]]+list(obj.rcoeff[4:6]))
      ans="%d/%d*ln(%d*x+%d)+%d/%d*ln(%d*x+%d)" % anscoeff
      problem="\displaystyle\\frac{%dx+%d}{(%dx+%d)(%dx+%d)}" % coeff
      hint='Do a partial fraction expansion'
    #artan
    if subtype==3:
      a=random.randint(1,7)
      b=random.randint(1,7)
      b2=b**2
      c=random.randint(1,7)
      d=random.randint(1,7)
      e=random.randint(1,7)

      ab=fractions.gcd(a,b)
      cd=fractions.gcd(c,d)

      coeff=(c,a*d,c*b2+a*e,b2,d,e)
      anscoeff=(a/ab,b/ab,b,c/cd,d/cd,d,e)

      ans="%d/%d*atan(x/%d)+%d/%d*ln(%d*x+%d)" % anscoeff
      problem="\displaystyle\\frac{%dx^2+%dx+%d}{(x^2+%d)(%dx+%d)}" % coeff
      hint='Do a partial fraction expansion'

    lower=''
    upper=''

  #ans=ans.replace("(1/1",'(1')
  ans=ans.replace('/1+','+')
  ans=ans.replace('/1-','-')
  ans=ans.replace('/1*','*')
  ans=ans.replace('/1)',')')
  ans=ans.replace('+-','-')
  ans=ans.replace('(1*x','(x')
  ans=ans.replace('(-1*x','(-x')
  ans=ans.replace('+1*x','x')
  ans=ans.replace('-1*x','-x')
  ans=ans.replace('+0*x','+')
  ans=ans.replace('-0*x','-')
  problem=problem.replace("/1",' ')
  problem=problem.replace('+-','-')
  problem=problem.replace('(1x','(x')
  problem=problem.replace('{1x','{x')
  problem=problem.replace('+1x','x')
  problem=problem.replace('-1x','-x')
  problem=problem.replace('{0x','{')
  problem=problem.replace('{0+','{')
  problem=problem.replace('{0-','{-')
  problem=problem.replace('+0x','')
  problem=problem.replace('-0x','')
  problem=problem.replace('+0','')
  problem=problem.replace('-0','')

  if type==2: integral='\displaystyle\int_{%s}^{%s} %s\,dx' % (lower, upper, problem)
  else: integral='\displaystyle\int_{%s}^{%s} %s\,dx' % (lower, upper, toTEX(problem))
  probtex='Take the integral $'+integral+'$.'

  if type==4:
    probtex=probtex+'  If the integral diverges, type "diverge".'
  prefix=''
  if len(lower)+len(upper)<2:
    suffix=' $+c$'
  else:
    suffix=''
  if ans[0:3]!='div':
    #if type==2: 'The answer is $'+integral+'='+ans+'$'+suffix
    anstex='The answer is $'+integral+'='+toTEX(ans)+'$'+suffix
    #anstex=anstex.replace('$ 1\cdot','$')
  else:
    anstex='The integral diverges.'

  print probtex
  print ans
  print anstex
  print prefix
  print suffix
  print hint

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()