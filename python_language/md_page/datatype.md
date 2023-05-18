# python datatypes

Python data types are different in some aspects from other programming languages. It is simple to understand and easy to use. Because Python is interpreted programming language and Python interpreter can determine which type of data is storing, so no need to define the data type of memory location.


#### The data type determines:
1. The possible values for that type.
2. The operations that can be done with that values.
3. Conveys the meaning of data.
4. The way values of that type can be stored.


## datatypes available in python

Everything in Python programming is an object, and each object has its own unique identity(a type and a value).

There are many native(built-in) data types available in Python.


#### Some important are:

1. Numbers: An are integers (such as 1, 2, 3…), floats (such as 2.6, 4.8, etc.), fractions (such as ½. ¾, etc.), or even complex numbers.
  ..*int (signed integer)
  ..*float
  ..*long
  ..*complex

  2. Sequences:
      ..*Strings: Sequence of Unicode characters, like an HTML document.
      ..*Bytes/Byte array: Any type of file.
      ..*Lists: An ordered sequence of values.
      ..*Tuples: An ordered, immutable sequence of value
  3.  Boolean: Holds either true or false values.
  4.  Sets: An unordered container of values.
  5.  Dictionaries: A key-paired values set in an unordered way.

Because Python is a pure object-oriented programming language,  so other data types are also available


1. Module
2. Function
3. Class
4. Method
5. File


# python variables

Variables are identifiers of a physical memory location, which is used to hold values temporarily during program execution.

Python interpreter allocates memory based on the values data type of variable, different data types like integers, decimals, characters, etc. can be stored in these variables.

## what are variables?

Before learning about variables, you must know about values.

A value is one of the essential parts of a program, like a letter or a number.


### python variable declaration

In Python, like many other programming languages, there is no need to define variables in advance. As soon as a value is assigned to a variable, it is automatically declared. This is why Python is called a dynamically typed language.

The syntax for creating variables in Python is given below:

#### syntax

```
<variable-name> = <value>

```

### Assigning value to variables

Python interpreter can determine what type of data is stored, so before assigning a value, variables do not need to be declared.

Usually, in all programming languages, equal sign = is used to assign values to a variable. It assigns the values of the right side operand to the left side operand.

The left side operand of = operator is the name of a variable, and the right side operand is value


#### example

```
name = "Packing box" # A string
height = 10 # An integer assignment
width = 20.5 # A floating point

print (name)
print (height)
print (width)

```
output

```
Packing box
10
20.5

```

In the above code snippet, the variable name 'height' is storing a value 10, and since the value is of type integer, the variable is automatically assigned the type integer.
Another variable name 'width' is assigned with floating type value. Then both the values are printed or displayed using the 'print' statement.

### common rule for naming variable in python

1. Variable names are case-sensitive.
2. Variable names must begin with a letter or underscore.
3. A variable name can only contain alphanumeric characters and underscore, such as (a-z, A-Z, 0-9, and _ ).
4. A variable name can not contents space.
5. Reserved words cannot be used as a variable name.


### python variable deletion

Python also provides the facility to delete a variable from memory. For this, the del command is used. The following is the general syntax for deleting a variable in Python:


#### syntax

```
del <variable-name>

```
