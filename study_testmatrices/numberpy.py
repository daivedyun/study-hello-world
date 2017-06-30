#!/usr/bin/python
#-*-coding: UTF-8 -*-
a = max(8,9)
print a
var1 = 'Hello World!'
var2 = "Python Runoob"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

str = 'nihao,chengdu'
print str
str = str[:6]+'china'
print str

print "the var1*2=",var1*2
if 'W' in var1:
    print "yes you are good girl!!!"
else:
    print "sb"

print R'\n'

print "zhe ge shu zi is %f my name is %s"%(a*1.0,var1)

str = "this is string example....wow!!!";

print "str.center(40, 'a') : ", str.center(50, '@')

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1,2,3,4,5,6,7,8,9,0]

print list1
del list1[2]
print "After deleting value at index 2 : "
print list1
list1.append('geigeyongbao')
print list1
print list1+list2
list3 = []
list3 = list1+list2
print list3
print cmp(list1,list2)
print max(list2)
yuanzu = ('nihao',2,3,'haode',4)
print yuanzu
print yuanzu[2:]
print yuanzu[1]

# study of the dictionarys !!!!!!!!!!!!!!!!!!
dictionary = {'like':'swimming','unl':2,3:'bad'}
print dictionary
print dictionary[3],dictionary['unl']

dictionary['like'] = 'running'
print dictionary
dictionary.clear()
print dictionary


#the out put of the value of below:
#
#9
#var1[0]:  H
#var2[1:5]:  ytho
#nihao,chengdu
#nihao,china
#the var1*2= Hello World!Hello World!
#yes you are good girl!!!
#\n
#zhe ge shu zi is 9.000000 my name is Hello World!
#str.center(40, 'a') :  @@@@@@@@@this is string example....wow!!!@@@@@@@@@
#['physics', 'chemistry', 1997, 2000]
#After deleting value at index 2 : 
#['physics', 'chemistry', 2000]
#['physics', 'chemistry', 2000, 'geigeyongbao']
#
