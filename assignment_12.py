# -*- coding: utf-8 -*-
"""Assignment 12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s1fHj9JiWkJVcRBR8ZnKc9COih-gqxcn
"""

#Write a Python program to Extract Unique values dictionary values?
dict = {'a':1,'b':2,'c':3,'d':4, 'e':1,'f':4}
dict.values()
set(dict.values())

list=[]
list1 =[]
for i in dict.values():
  list.append(i)
print(list)
for j in list:
  if j not in list1:
    list1.append(j)

list1

#Write a Python program to find the sum of all items in a dictionary?
dict = {3:1,4:2,7:3,4:4, 9:1,1:4}
l1 = dict.keys()
l2 = dict.values()
l3 =[]
l4 =[]
for i in l1:
  l3.append(i)
for j in l2:
  l4.append(j)
l5 = l3+l4
sum(l5)

#Write a Python program to Merging two Dictionaries?
dict1 = {'a':1,'b':2,'c':3,'d':4, 'e':1,'f':4}
dict2 = {3:1,4:2,7:3,4:4, 9:1,1:4}
dict3= {**dict1,**dict2}
dict3

#Write a Python program to sort Python Dictionaries by Key or Value
dict2
res1 = sorted(dict2.keys())
print(res1)
res2 = sorted(dict2.values())
print(res2)
