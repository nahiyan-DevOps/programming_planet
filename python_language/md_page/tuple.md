# python tuples

Tuples are immutable lists and cannot be changed in any way once it is created.

Some of the characteristics features of Tuples are:

1. Tuples are defined in the same way as lists.
2. They are enclosed within parenthesis and not within square braces.
3. Elements of the tuple must have a defined order.
4. Negative indices are counted from the end of the tuple, just like lists.
5. Tuple also has the same structure where commas separate the values.


An example showing how to build tuples in Python:


#### example

```
tupl1 = ('computersc', 'IT', 'CSE');
tup2 = (6,5,4,3,2,1);

```


### Accessing value in tuples

```
tupl1 = ('computersc', 'IT', 'CSE');
tupl2 = (1993, 2016);
tupl3 = (2, 4, 6, 8, 10, 12, 14, 16);

print ("tupl1[0]", tupl1[0])
print ("tupl3[2:4]", tupl3[2:4])

```

output

```
tupl1[0] computersc
tupl3[2:4] (6, 8)

```

### updating tuples

They are immutable, i.e., the values can't be changed directly. So we can just update by joining tuples. Let's demonstrate this with an example:

#### example

```
tupl1 = (2, 3, 4);
tupl2 = ('ab', 'cd');
tupl3 = tupl1 + tupl2

print (tupl3)

```

This code snippet will execute a combination of two tuples using the "+" operator.

#### output

```
(2, 3, 4, 'ab', 'cd'

```

### delete elements from tuples

```
del tuple_name
```


example

```
tupl3 = (2, 4, 6, 8, 10, 12, 14, 16);

del tupl3;

```
