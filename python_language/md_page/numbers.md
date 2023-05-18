# python numbers

As we know, programming languages have their prime things - **Numbers**, **Data types**, **Strings**, **Variables**, etc., which play a significant role in constructing a program.

When we say Numbers, we mean to say Python programming supports integers, floating-point numbers, and complex numbers. These are number-based data types that store various types of numeric values. Number objects get generated when programmers assign a value to them. For example:


```
variable_name1 = 10

variable_name2 = 6.2

```
These reference to number objects can also be deleted by using del statement. The syntax for "del" statement is:

####syntax

```
del variable_name[, variable_name2[….variable_name-N]

```

In Python, the numeric variables are defined as:
1. int
2. float
3. complex

All of them act as a class in Python, where integers and floating-point/decimal values are separated based on the presence or absence of decimal point between the values. 6 is an integer, whereas 6.2 is a floating-point value.


### types of numerical datatypes

Python provides four distinctive numerical types. These are:

1. **signed int**: include the range of both positive as well as negative numbers along with whole numbers without the decimal point.
2. **long int**: a special type of integer is having an unlimited size and is written like integer value before the letter L (either uppercase or lowercase).
3. **float (real values)**: They are used with a decimal point to represent real numbers, and that decimal point (dot) is used to divide the integer and the fraction.
4. **complex**: are complex numbers that take the structure a+bJ where a and b are floating-point numbers and that 'J' represent the square root of -1 (imaginary number).


### type conversion

Python has the capability and feature to convert within an expression containing the mixture of different types of values internally.

1. **int(v)**: is used to convert any value 'v' to a plain integer
2. **long(v)**: is used to convert a value 'v' to a long integer
3. **float(v)**: is used to convert a value 'v' to floating-point value
4. **complex(v)**: is used convert a value 'v' to the complex number having real part 'v' and imaginary part as 0
5. **complex(u,v)**: is used convert values u and v to the complex number with real part 'u' and imaginary part



```
x = 10.5
y = 5

#without type cast
print (x + y)

#after type cast
print (int(x) + y)

```
output:

```
15.5
15
```
The above example shows how float converted to an integers
