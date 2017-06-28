#!/usr/bin/python
import random
import pdb
import sys
import time

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
 
print "Good bye!"

numbers  = [12,15,16,17,18,19,20,21,22]
even = []
odd  = []

while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print even
print odd

var = 1
while var == 1 :  # ??????true,?????????
   num = raw_input("Enter a number  :")
   print "You entered: ", num
   if(num == "break"):
       break
   else:
       continue 
print "Good bye!"

count = 0
while count < 10:
    print count, "is less than 10"
    count = count + 1
else:
    print count, "is equal to 10 or is greater than 10"

s = int(random.uniform(1,100))
m = int(input('input int type:'))
while m!=s :
    if m > s:
        print "bigger!!!"
        m = int(input('input int type:'))
    if m < s:
        print "smaller!!!"
        m = int(input('input int type:'))
    if m == s:
        print "good!!!"
        break

while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "stone"
    elif s == 2:
        ind = "jiandao"
    elif s == 3:
        ind = "map"
#    pdb.set_trace()
    m = raw_input('input stone,jiandao,map,input "end" game over:')
    blist = ['stone', "jiandao", "map"]
    if (m not in blist) and (m != 'end'):
        print "input error,inupt again!"
    elif (m not in blist) and (m == 'end'):
        print "\n game is going to over............"
        break
    elif m == ind :
        print "the computer output: " + ind + ",peacefull"
    elif (m == 'stone' and ind =='jiandao') or (m == 'jiandao' and ind =='map')\
                                              or (m == 'map' and ind =='stone'):
        print "the computer output: " + ind +",you are the winner!"
    elif (m == 'stone' and ind =='map') or (m == 'jiandao' and ind =='stone')\
                                            or (m == 'map' and ind =='jiandao'):
        print "the computer output: " + ind +",you are lost! "


result = []
counter_smaller = 0
counter_bigger  = 0
count_total     = 0
while True:
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    print result
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += " "
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + " -> " + "smaller" + "\n")
        counter_smaller = counter_smaller + 1
        print "counter_smaller = ", counter_smaller
        count_total = count_total + 1
     #   time.sleep( 1 )   # ????
    else:
        sys.stdout.write(pointStr + " -> " + "bigger" + "\n")
        counter_bigger = counter_bigger + 1
        print "counter_bigger = ", counter_bigger
        count_total = count_total + 1
    #    time.sleep( 1 )   # ????

    if count_total >= 100000:
        print "\n"
        print "\n"
        print "\n"
        print "the smaller rate is :",counter_smaller*1.0/count_total
        print "the bigger  rate is :",counter_bigger*1.0/count_total
        count_total = 0
        counter_smaller = 0
        counter_bigger  = 0
        time.sleep( 2 )   # ????

    result = []
