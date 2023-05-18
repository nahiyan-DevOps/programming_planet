# C function

C function is a self-contained block of statements that can be executed repeatedly whenever we need it.

## Benefits of using the function in C

1. The function provides modularity.
2. The function provides reusable code.
3. In large programs, debugging and editing tasks is easy with the use of functions.
4. The program can be modularized into smaller parts.
5. Separate function independently can be developed according to the needs.


## There are two types of function in C

1. Built-in(Library) Functions
   ..* The system provided these functions and stored in the library. Therefore it is also called Library Functions.
    e.g. scanf(), printf(), strcpy, strlwr, strcmp, strlen, strcat etc.
   ..*To use these functions, you just need to include the appropriate C header files.
2. User Defined Functions These functions are defined by the user at the time of writing the program.


### Parts of Function

1. Function Prototype (function declaration)
2. Function Definition
3. Function Call


### Function Prototype
syntex:
```
dataType functionName (Parameter List)

```
example:
```
int addition();

```

### Function Defination

syntex:

```
returnType functionName(Function arguments){
  //body of the function
}

```

example:
```
int addition()
{

}

```

### Calling a function in C

#### Program to illustrate the addition of two numbers using user defined function.


example:
```
#include<stdio.h>

/* function declaration */int addition();

int main()
{   
    //local variable definition
    int answer;

    answer = addition(); //calling a function to get addition value.
    printf("The addition of the two numbers is: %d\n",answer);
    return 0;
}

//function returning the addition of two numbers
int addition()
{
    int num1 = 10, num2 = 5; // local variable definition
    return num1+num2;
}

```

output:
```
The addition of the two numbers is: 15

```




## C function arguments

While calling a function, the arguments can be passed to a function in two ways, **Call by value** and **call by reference**.


### Call by value

1. The actual parameter is passed to a function.
2. New memory area created for the passed parameters, can be used only within the function.
3. The actual parameters cannot be modified here.


### Call by reference

1. Instead of copying variable; an address is passed to function as parameters.
2. Address operator(&) is used in the parameter of the called function.
3. Changes in function reflect the change of the original variables


### call by value

example:

```
#include<stdio.h>

//function declaration
int addition(int num1, int num2);

int main()
{
    //local variable definition
    int answer;
    int num1 = 10;
    int num2 = 5;

    //calling a function to get addition value
    answer = addition(num1,num2);

    printf("The addition of two numbers is: %d\n",answer);
    return 0;
}

//function returning the addition of two numbers
int addition(int a,int b)
{
    return a + b;
}

```

output:

```
The addition of two numbers is: 15

```

### call by reference

example:

```
#include<stdio.h>

//function declaration
int addition(int *num1, int *num2);

int main()
{
    //local variable definition
    int answer;
    int num1 = 10;
    int num2 = 5;

    //calling a function to get addition value
    answer = addition(&num1,&num2);

    printf("The addition of two numbers is: %d\n",answer);
    return 0;
}

//function returning the addition of two numbers
int addition(int *a,int *b)
{
    return *a + *b;
}

```

output:
```
The addition of two numbers is: 15

```


## C Library function

The C library functions are provided by the system and stored in the library. The C library function is also called an inbuilt function in C programming.

To use Inbuilt Function in C, you must include their respective header files, which contain prototypes and data definitions of the function


### C program to demonstrate the use of library function

example:

```
#include<stdio.h>
#include<ctype.h>
#include<math.h>

void main()
{
  int i = -10, e = 2, d = 10; //Variables Defining and Assign values
  float rad = 1.43;
  double d1 = 3.0, d2 = 4.0;

  printf("%d\n", abs(i));
  printf("%f\n", sin(rad));
  printf("%f\n", cos(rad));
  printf("%f\n", exp(e));
  printf("%d\n", log(d));
  printf("%f\n", pow(d1, d2));    
}

```

output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2016/04/c-library-functions.jpg?ezimgfmt=ng%3Awebp%2Fngcb7%2Frs%3Adevice%2Frscb7-1)



## C variable scope

A scope is a region of the program, and the scope of variables refers to the area of the program where the variables can be accessed after its declaration.

In C every variable defined in scope. You can define scope as the section or region of a program where a variable has its existence; moreover, that variable cannot be used or accessed beyond that region.
In C programming, variable declared within a function is different from a variable declared outside of a function. The variable can be declared in three places. These are:

| POSITION                  | TYPE                    |
|--------------------------:|------------------------ |
| Inside a function         | local variable          |
|out of all functions       | Global variable         |
| In the function parameters| Formal parameters       |



### Local Variables
Variables that are declared within the function block and can be used only within the function is called local variables.

### Local scope or Block scope

A local scope or block is collective program statements put in and declared within a function or block (a specific region enclosed with curly braces) and variables lying inside such blocks are termed as local variables. All these locally scoped statements are written and enclosed within left ({) and right braces (}) curly braces. There's a provision for nested blocks also in C which means there can be a block or a function within another block or function. So it can be said that variable(s) that are declared within a block can be accessed within that specific block and all other inner blocks of that block, but those variables cannot be accessed outside the block

###### example

```
#include <stdio.h>

int main ()
{
    //local variable definition and initialization
    int x,y,z;

    //actual initialization
    x = 20;
    y = 30;
    z = x + y;

    printf ("value of x = %d, y = %d and z = %d\n", x, y, z);

    return 0;
}

```

### Global variables

Variables that are declared outside of a function block and can be accessed inside the function is called global variables


#### Global scope

Global variables are defined outside a function or any specific block, in most of the case, on the top of the C program. These variables hold their values all through the end of the program and are accessible within any of the functions defined in your program.

Any function can access variables defined within the global scope, i.e., its availability stays for the entire program after being declared.

###### example

```
#include <stdio.h>

//global variable definition
int z;

int main ()
{
    //local variable definition and initialization
    int x,y;

    //actual initialization
    x = 20;
    y = 30;
    z = x + y;

    printf ("value of x = %d, y = %d and z = %d\n", x, y, z);

    return 0;
}

```

#### Global variable initialization

 After defining a local variable, the system or the compiler won't be initializing any value to it. You have to initialize it by yourself. It is considered good programming practice to initialize variables before using. Whereas in contrast, global variables get initialized automatically by the compiler as and when defined. Here's how based on datatype; global variables are defined


|  dataType      |  initial default  |
|---------------:| :---------------- |
| int            |   0               |
| char           |   '\0'            |
| float          |    0              |
| double         |    0              |  
| pointer        |    NULL           |





## C Recursion

C is a powerful programming language having capabilities like an iteration of a set of statements 'n' number of times. The same concepts can be done using functions also. In this chapter, you will be learning about recursion concept and how it can be used in the C program


### What is Recursion?

Recursion can be defined as the technique of replicating or doing again an activity in a self-similar way calling itself again and again, and the process continues till specific condition reaches. In the world of programming, when your program lets you call that specific function from inside that function, then this concept of calling the function from itself can be termed as recursion, and the function in which makes this possible is called recursive function.
Here's an example of how recursion works in a program:

```
void rec_prog(void) {
  rec_prog(); //function calls itself
}

int main(void) {
  rec_prog();
  return 0;
}

```

C program allows you to do such calling of function within another function, i.e., recursion. But when you implement this recursion concept, you have to be cautious in defining an exit or terminating condition from this recursive function, or else it will continue to an infinite loop, so make sure that the condition is set within your program

#### Factorial program in C using Recursion

example:

```
#include<stdio.h>
#include<conio.h>

int fact(int f) {
  if (f==0 || f==1) {
    printf("Calculated Factorial");
    return 1;
  }
  return f * fact(f - 1);
}

int main(void) {
  int f = 12;
  printf("The factorial of %d is %d \n", f, fact(f));
  getch();
  return 0;
}

```

 output:

 ```
 Calculated Factorial
The factorial of 12 is 479001600

 ```


### Fibonacci Program in C using Recursion

example:
```
#include<stdio.h>
#include<conio.h>

int fibo(int g) {
  if (g == 0) {
    return 0;
  }

  if (g == 1) {
    return 1;
  }
  return fibo(g - 1) + fibo(g - 2);
}

int main(void) {
  int g;
  printf("Calculated Fibonacci\n");
  for (g = 0; g < 10; g++) {
    printf("%d \t ", fibo(g));
  }
  getch();
  return 0;
}

```

output:

```
Calculated Fibonacci
0        1       1       2       3       5       8       13      21      34

```
