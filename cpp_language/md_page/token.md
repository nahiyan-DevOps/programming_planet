# C++ Tokens

As mentioned earlier, C++ is the superset of C and so most constructs of C are legal in C++ with their meaning and usage unchanged. So tokens, expressions, and data types are similar to that of C. It also is preferred to understand the concepts of C before learning C++. However, there are some exceptions and additions in C++ which you will not get in C. In this chapter, you will learn about what are tokens, and the different types of tokens, expressions, and basic data types



## What are Tokens

Each word and punctuation is referred to as a token in C++. Tokens are the smallest building block or smallest unit of a C++ program.



#### These following tokens are available in C++:
1. Identifiers
2. Keywords
3. Constants
4. Operators
5. Strings



### Identifiers

Identifiers are names given to different entries such as variables, structures, and functions. Also, identifier names should have to be unique because these entities are used in the execution of the program.

### Keywords

Keywords are reserved words which have fixed meaning, and its meaning cannot be changed. The meaning and working of these keywords are already known to the compiler. C++ has more numbers of keyword than C, and those extra ones have special working capabilities.

### Operator

C++ operator is a symbol that is used to perform mathematical or logical manipulations.

### Constants

Constants are like a variable, except that their value never changes during execution once defined.

### strings

Strings are objects that signify sequences of characters




## C++ Keywords

The C++ Keywords must be in your knowledge because you can not use them as a variable name

### C++ Keywords List

You can't use keyword as identifier in your C++ programs, its reserved words in C++ library and used to perform an internal operation




| asm	      | else	    | new	       | this      |    
| auto	    | enum	    | operator	 | throw     |
| bool	    | explicit	| private	   | true      |
| break	    | export	  | protected	 | try       |
| case	    | extern	  | public	   | typedef   |
| catch	    | false	    | register	 | typeid    |
| char	    | float	    | namespace  | typename  |
| class	    | for	      | return	   | union     |
| const	    | friend	  | short	     | unsigned  |
| const_cast|	goto	    | signed	   | using     |
| continue	| if	      | sizeof	   | virtual   |
| default	  | inline	  | static	   | void      |
| delete	  | int	      | static_cast| volatile  |
| do	      | long	    | struct	   | wchar_t   |
| double	  | mutable	  | switch	   | while     |




## C++ Constants


Constants are like a variable, except that their value never changes during the program execution once defined


### What are constants

Constants refer to as fixed values, unlike variables whose value can be altered, constants - as the name implies does not change, they remain constant. Constant must have to be initialized at the time of creating it, and new values cannot be assigned later to it


1. Constants are also called literals.
2. Constants can be any of the data types.
3. It is considered best practice to define constants using only upper-case names



### Constant Definition

There are two other different ways to define constants in C++. These are:

1. By using const keyword
2. By using #define preprocessor

### Constant Definition by using **const** keyword

#### syntax:

```
const type constant_name;

```

#### example:

```
#include <iostream>
using namespace std;

int main()
{
  const int SIDE = 50;
  int area;
  area = SIDE*SIDE;
  cout<<"The area of the square with side: " << SIDE <<" is: " << area << endl;
  system("PAUSE");
  return 0;
}

```


output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2015/07/cplusplus-constants.jpg?ezimgfmt=rs:403x185/rscb7/ng:webp/ngcb7)

It is also possible to put const either before or after the type.

```
int const SIDE = 50;

```

or

```
const int SIDE = 50;

```



## Constant Definition by using #define preprocessor

syntax:

```
#define constant_name;

```

example:

```
#include <iostream>
using namespace std;

#define VAL1 20   
#define VAL2  6
#define Newline '\n'

int main()
{
   int tot;
   tot = VAL1 * VAL2;
   cout << tot;
   cout << Newline;
}

```


## C++ Operators

C++ operator is a symbol that is used to perform mathematical or logical manipulations. C++ language is rich with built-in operators.



### Arithmetic Operators



| Operator	| Description   |
|---------: |--------------:|
|     +	    |  Addition     |
|     -     |	Subtraction   |
|     *	    | Multiplication|
|     /     |	Division      |
|     %	    |  Modulus      |


### Increment and decrement operators

|   Operator |	Description |
|-----------:|-------------:|
|       ++	 | Increment    |
|       −−	 |  Decrement   |



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
