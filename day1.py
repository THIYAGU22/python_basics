print("Hello World")

import keyword
print(keyword.kwlist)

#task 3 : appending 2 tuples
print("task 3:")
print()
a = [1,2,3,4]
b = [5,6,7]
c = a+b
print(c)



#task 4 : tuples are mixed data types
t = [1,"hello",3.133,0.122,98,'character']
print(t)

print(t[2:])

print(t[2:4])

print(t[2:-1])

a=[1,1,2,3,4,5]
b=[1,2,5,7,9]

c = a+b
print(c)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


list1 = [1,2,"hai"]

list2 = list1

print(list2)

list3 = list1[:]

print(list3)

print("appending a number in list2")
add_num = [55]
mod_list2 = list2 + add_num

mod_list3 = list3 + add_num

print(add_num,"is appended to modified list 2",mod_list2)
print(type(mod_list2))

print(add_num,"is appended to modified list 3",mod_list3)

check = 'abcdefghijklmno'

print('z' in check)

set_tup =[0,1,1,1,4,5,6,7,8,9,10]

print(set_tup[::2])

count = 0
#for x in range(set_tup):
 #   if(x == set_tup[x]):
 #       count+1
#print(count)

from collections import Counter
print(Counter(set_tup))

x = 145

def convertDigits(a):
    while(a!=0):
        digit = a%10
        fact(digit)
        a=a/10

def fact(n):
    if(n!=0):
        store = n * fact(n-1);
print(store)

convertDigits(145)

