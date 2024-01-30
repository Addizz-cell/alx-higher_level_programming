0x09. Python - Everything is an Object
In this directory, you'll find solutions to Python programming tasks related to the concept that "Everything is an Object" in Python.

Files
0-answer.txt
What function would you use to get the type of an object?
Answer: type

1-answer.txt
How do you get the variable identifier (memory address in the CPython implementation)?
Answer: id

2-answer.txt
In the following code, do a and b point to the same object?
Answer: No

3-answer.txt
In the following code, do a and b point to the same object?
Answer: Yes

4-answer.txt
In the following code, do a and b point to the same object?
Answer: Yes

5-answer.txt
In the following code, do a and b point to the same object?
Answer: No

6-answer.txt
What do these 3 lines print?

python

s1 = "Best School"
s2 = s1
print(s1 == s2)
Answer: True

7-answer.txt
What do these 3 lines print?

python

s1 = "Best"
s2 = s1
print(s1 is s2)
Answer: True

8-answer.txt
What do these 3 lines print?

python

s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
Answer: True

9-answer.txt
What do these 3 lines print?

python

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
Answer: False

10-answer.txt
What do these 3 lines print?

python

l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)
Answer: True

11-answer.txt
What do these 3 lines print?

python

l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)
Answer: False

12-answer.txt
What do these 3 lines print?

python

l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
Answer: True

13-answer.txt
What do these 3 lines print?

python

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
Answer: True

14-answer.txt
What does this script print?

python

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
15-answer.txt
What does this script print?

python

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
16-answer.txt
What does this script print?

python

def increment(n):
    n += 1

a = 1
increment(a)
print(a)
17-answer.txt
What does this script print?

python

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
18-answer.txt
What does this script print?

python

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
19-copy_list.py
Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects.
Your file should be maximum 3-line long (no documentation needed).
You are not allowed to import any module.

20-answer.txt
Is a a tuple? Answer: No

21-answer.txt
Is a a tuple? Answer: Yes

22-answer.txt
Is a a tuple? Answer: No

23-answer.txt
Is a a tuple? Answer: Yes

24-answer.txt
What does this script print?

python

a = (1)
b = (1)
a is b
25-answer.txt
What does this script print?

python

a = (1, 2)
b = (1, 2)
a is b
26-answer.txt
What does this script print?

python

a = ()
b = ()
a is b
27-answer.txt
Will the last line of this script print 139926795932424? Answer: No
