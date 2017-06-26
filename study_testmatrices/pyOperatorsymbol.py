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

