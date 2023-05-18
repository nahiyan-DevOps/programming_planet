# Python keywords


The Python Keywords must be in your information because you can not use them as a variable name or any other identifier name.

## Python reserved keywords list

Keywords are reserved words in Python and used to perform an internal operation. All the keywords of Python contain lower-case letters only.


|and	   |assert	 |in       |
|del	   |else	   |raise    |
|from	   |if	     |continue |
|not	   |pass	   |finally  |
|while	 |yield	   |is       |
|as	     |break	   |return   |
|elif	   |except	 |def      |
|global	 |import	 |for      |
|or	     |print	   |lambda   |
|with	   |class	   |try      |


## operators

Operators provide a vital role in programming, and in combination with values and other identifiers form expressions and statements, which is also an essential building block for Python programming.

### Types of python Operators

Python supports the following types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison (Relational) Operators
4. Logical Operators
5. Identity Operators
6. Bitwise Operators
7. Membership Operators


### Arithmetic Operators



| Operator	| Description   |
|---------: |--------------:|
|     +	    |  Addition     |
|     -     |	Subtraction   |
|     *	    | Multiplication|
|     /     |	Division      |
|     %	    |  Modulus      |



### Relational operators

|   Operator	 |       Description    |
|------------: |---------------------:|
|       ==	   |       Is equal to    |
|       !=	   |     Is not equal to  |
|       >	     |      Greater than    |
|       <	     |        Less than     |
|      >=      |Greater than or equal |
|      <=	     |Less than or equal to |



### Logical Operators

1. &&
  ..* And operator. Performs a logical conjunction of two expressions.
(if both expressions evaluate to True, result is True. If either expression evaluates to False, result is False)
2. ||
  ..*Or operator. Performs a logical disjunction on two expressions.
(if either or both expressions evaluate to True, result is True)
3. !
  ..*Not operator. Performs logical negation on an expression.




### Bitwise Operator

| Operator |     	Description          |
| --------:| -------------------------:|
|     <<	 | Binary Left Shift Operator|
|     >>	 |Binary Right Shift Operator|
|     ~	   | Binary One's Complement   |
|     &	   | Binary AND Operator       |
|     ^	   |  Binary XOR Operator      |



### Assignment Operators

| Operator 	|        Description    |
|----------:| ---------------------:|
|     =	    |        Assign         |
|    +=	    |Increments then assigns|
|    -=	    |Decrements then assigns|
|    *=	    |Multiplies then assigns|
|    /=	    |  Divides then assigns |
|    %=	    | Modulus, then assigns |
|    <<=	  |Left shift and assigns |
|    >>=	  |Right shift and assigns|
|     &=	  |Bitwise AND assigns    |
|     ^=	  |Bitwise XOR and assigns|



### checking Membership in python

In Python, we can check whether a string or character is a member of another string or not using "in" or "not in" operators.

In Python, we can check whether a string or character is a member of another string or not using "in" or "not in" operators.


### a python program to know weather a string exist in a main string or Not

```
str1 = input('Please enter first string: ')
str2 = input('Please enter second string: ')
if str2 in str1:
    print(str2+' found in the first string.')
else:
    print(str2+' not found in the first string.')

```

output:

```
Please enter first string: We are writing core python
Please enter second string: python
python found in the first string.
```


The above program takes two inputs from the keyboard and checks whether the second string found in the first string or not
