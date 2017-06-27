#!/usr/bin/python
# -*- coding: UTF-8 -*-
#http://www.360doc.com/content/17/0406/07/5633793_643233897.shtml vim config
#

a = 21
b = 10
c =0

c = a + b
print "1-c the value is ",c
c = a/b 
print "2-c a/b the value is ",c

d = 1/2
print "1-d a/b the value is ",d

f = 1.0/2
print "1-f a/b the value is ",f

if (a==b):
  print "a =b  "
else:
  print "a!=b"

if (b>c):
  print "a is real bigger than c"
else:
  print "c<b"
if (b!=c):
  print "b is not equal to c"
else:
  print "b is greater than c"




#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100
print "1 - c ???:", c
 
c = a | b;        # 61 = 0011 1101 
print "2 - c ???:", c
 
c = a ^ b;        # 49 = 0011 0001
print "3 - c ???:", c
 
c = ~a;           # -61 = 1100 0011
print "4 - c ???:", c
 
c = a << 2;       # 240 = 1111 0000
print "5 - c ???:", c
 
c = a >> 2;       # 15 = 0000 1111
print "6 - c ???:", c


a = 10
b = 20
 
if ( a and b ):
    print "1 - ?? a ? b ?? true"
else:
    print "1 - ?? a ? b ????? true"
 
if ( a or b ):
    print "2 - ?? a ? b ?? true,???????? true"
else:
    print "2 - ?? a ? b ??? true"
 
# ???? a ??
a = 0
if ( a and b ):
    print "3 - ?? a ? b ?? true"
else:
    print "3 - ?? a ? b ????? true"
 
if ( a or b ):
    print "4 - ?? a ? b ?? true,???????? true"
else:
    print "4 - ?? a ? b ??? true"
 
if not( a and b ):
    print "5 - ?? a ? b ?? false,???????? false"
else:
    print "5 - ?? a ? b ?? true"


p = 10
t = 20
list1 = [10, 2, 3, 4, 5 ];
if(p in list1):
    print "p is in the list1"
else:
    print "p is not in the list1"

if(t not in list1):
    print "t is not in the list1"
else:
    print "t is in the list1"


m = 100
n = 100
if (m is n):
    print "m is the same as b!"
else:
    print "m is not the same as b!"

if (m is not n):
    print "m is not  the same as b!"
else:
    print "m is the same as b!"

yy = 66666666
tt = 66666666

if (tt is yy):
    print "tt is the same as yy666666666!"
else:
    print "tt is not the same as yy!"

if (tt == yy):
    print "tt is the same as yy!"
else:
    print "tt is not the same as yy!"

flag = False
name = 'python'
if name == 'python':         # ??????'python'
    flag = True          # ???????????
    print 'welcome boss'    # ???????
else:
    print name              # ????????????

num = 5     
if num == 3:            # ??num??
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # ???????
    print 'error'
else:
    print 'roadman'     # ?????????


# ?3:if??????
 
num = 9
if num >= 0 and num <= 10:    # ??????0~10??
    print 'hello'
# ????: hello
 
num = 10
if num < 0 or num > 10:    # ????????0???10
    print 'hello'
else:
    print 'undefine'
# ????: undefine
 
num = 8
# ??????0~5??10~15??
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'
# ????: undefine
