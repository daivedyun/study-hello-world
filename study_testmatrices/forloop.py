#!/usr/bin/python
#-*- coding: UTF-8 -*-

for chre in 'Python':     
   print 'current character:', chre
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:       
   print 'current fruits:', fruit

for index in range(len(fruits)): 
   print "this is another way :",fruits[index]

for num in range(10,20):  # ?? 10 ? 20 ?????
   for i in range(2,num): # ??????
      if num%i == 0:      # ???????
         j=num/i          # ???????
         print '%d == %d * %d' % (num,i,j)
         break            # ??????
   else:                  # ??? else ??
      print num, 'is a zhishu'

while True:
    rows = int(raw_input('please input the rows:'))
    if rows > 23 or rows <= 0:
        print 'rows number out of the range!'
        continue
    else:
        break
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print " * ",
        elif i == rows - 1:
            if k % 2 == 0:
                print " * ",
            else:
                print "   ",
        else:
            print "   ",
    print "\n"

s = 'qazxswedcvfr'
for i in range(0,len(s),3):
    print s[i]

for (index,char) in enumerate(s):
    print "index=%s ,char=%s" % (index,char)

print "Good bye!"
