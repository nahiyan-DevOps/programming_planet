# python list


Dealing with data in a structured format is quite generous, and this is possible if those data are set accordingly in a specific manner. So, Python provides these data structures named 'lists' and 'tuples' that are used to organize data in a single set. Python has six built-in sequences, and among them, the most famous is "lists and tuples".

The lists are containers that hold some other objects in a given order. It usually puts into practice the sequence protocol and allows programmers to add or remove objects from that sequence. Each element of the sequence is assigned a number, i.e., the index and the first index is 0 (zero). This versatile data-type of Python is written in a sequence of the list separated by commas between expressions.


## creating Lists

To build a list, just put some expressions in square brackets. The syntax is:

#### syntax

```
lst1 = [ ]  # lst1 is the name of the list
lst2 = [expression1 , …. , expression_N]

```

example

```
lst1 = ['computersc', 'IT', 'CSE'];
lst2 = [1993, 2016];
lst3 = [2, 4, 6, "g", "k", "s"];

```

## accessing lists values

List apply the standard interface sequence in which len(L) returns the number of items present in the list, and L[i] represents the item at index i. Also L[i:j] returns new list containing objects within 'i' and 'j'.


### program to explain how to access Lists

```
lst1 = ['computersc', 'IT', 'CSE'];
lst2 = [1993, 2016];
lst3 = [2, 4, 6, "g", "k", "s"];

print ("lst1[0]", lst1[0])
print ("lst3[2:4]", lst3[2:4])

```
output

```
lst1[0] computersc
lst3[2:4] [6, 'g'

```

## updating lists

Program to show how to add/update single or multiple elements in a list:

#### example

```
lst1 = ['computersc', 'IT', 'CSE'];

print ("Second value of the list is:")
print (lst1[1])

lst1[1] = 'Robotics'

print ("Updated value in the second index of list is:")
print (lst1[1])

```

output

```
Second value of the list is:
IT
Updated value in the second index of list is:
Robotics

```

## delete elements from lists

To remove an element from the list, we can use the del-statement. The syntax for deleting an element from a list is:

#### syntax

```
del list_name[index_val];

```
