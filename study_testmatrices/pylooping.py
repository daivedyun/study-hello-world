#!/usr/bin/python
import random
 
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

s = int(random.uniform(1,10))
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











