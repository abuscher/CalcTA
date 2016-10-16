import sys
import random
import math
from math import *
import re


def frac(s):
  while ')/(' in s:
    #match = re.search(r"[^a-zA-Z](\)\/\()[^a-zA-Z]", s) #determine location of ')/(
    #i=match.start(1)
    i=s.find(')/(')
    i1=i-1
    i2=i+3
    count=0
    while count>=0 and i1>=0: #move left
      if s[i1]==')':count+=1
      if s[i1]=='(':count-=1
      i1-=1
    count=0
    while count>=0 and i2<len(s): #move right
      if s[i2]=='(':count+=1
      if s[i2]==')':count-=1
      i2+=1
    s='%s\\displaystyle\\frac{%s}{%s}%s'%(s[:i1+1], s[i1+2:i],s[i+3:i2-1],s[i2:])
  return s

def toTEX(s):
   
  if len(s)==0:
    return ''  

  #replace "trig" with \"trig
  str_replace={}
  str_replace[1]=['asin','arcsin']
  str_replace[2]=['acos','arccos']
  str_replace[3]=['atan','arctan']
  str_replace[4]=['acsc','arccsc']
  str_replace[5]=['asec','arcsec']
  str_replace[6]=['acot','arccot']
  str_replace[7]=['sin','\sin']
  str_replace[8]=['cos','\cos']
  #str_replace[9]=['arc\sin','\\arcsin']
  #str_replace[10]=['arc\cos','\\arccos']
  str_replace[11]=['sqrt','\sqrt']
  #str_replace[1]=['tan']='\tan'
  #need to replace coth, csch and sech too
  str_replace[12]=['csc','\csc']
  str_replace[13]=['sec','\sec']
  str_replace[14]=['cot','\cot']


  str_replace[15]=['ln','\ln ']
  str_replace[16]=['pi','\pi ']
  for i in range(len(str_replace)):
    (kv,val)=str_replace[str_replace.keys()[i]]
    s=re.sub('(?i)'+kv,val,s)
  s=s.replace('tan','\\tan')
  s=s.replace('arc\sin','\\arcsin')
  s=s.replace('arc\cos','\\arccos')
  s=s.replace('arc\\tan','\\arctan')
  #replace tan with \\tan and
  #occur=[m.start() for m in re.finditer('tan', s)]
  #for i in range(len(occur)):
  #  j=occur[i]
  #  s=s[0:(i+j)]+'\\'+s[(i+j):]

  ##REPEAT PROCESS FOR HYPERBOLIC csc and sec


  #replace ^() with ^{}
  new=''
  trigger=0
  if s[0]=='(':
    hold=1
  else: hold=0
  skip=0
  rbrace=0
  for j in range(len(s)-1):
    c=s[j:j+2]
    #print c[0:2], trigger,hold
    #print c[0]!='^', c[1]=='('
    if c=='^(':
      new += '^{'
      trigger+=1
      skip=1
      if hold>0: hold-=1
    elif  c[0]!='^' and c[1]=='(':
      hold+=1
      new+=c[0]
    elif c[0]=='^' and c[1]!='(' and j<len(s)-2:
      if s[j+2]!='-' and s[j+2]!='+' and s[j+2]!='*' and s[j+2]!='/':
        rbrace+=1
        new+='^{'
        trigger+=1
      else: new+=c[0]
    elif skip==1 and c[0]=='(':
      new+=''
      skip=0
    elif hold>0 and c[0]==')':
      new+=')'
      if hold>0: hold-=1
    elif trigger>0 and hold<=0 and c[0]==')':
      new+='}'
      trigger-=1
    #elif c[0:2]=='\t':
    #  new += '\\t'
    #elif c[0:2]=='\f':
    #  new += '\\f'
    else: new+=c[0]

    if rbrace>0 and (c[1]=='+' or c[1]=='-' or c[1]=='*' or c[1]=='/' or c[1]=='(' or c[1]==')' or c[1]=='=' ):
      new+='}'
      rbrace=0
      #hold+=1
      trigger-=1
      #print 'here'
  if s[-1]==')':
    if trigger>0:
      new+='}'
      rbrace-=1
    else: new+=')'
  else: new+=s[-1]
  if rbrace>0: new+='}'

  s=new
  new=''
  for j in range(len(s)):
    if s[j]=='*':new+='\cdot '
    else: new+=s[j]

  #new+='$'
  return new
def main():
  print frac('(1)/(2)')
if __name__ == '__main__':
  main()
