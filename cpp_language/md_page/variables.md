# C++ variables


In C++ variable is used to store data in a memory location, which can be modified or used in the program during program execution.

Variables play a significant role in constructing a program, storing values in memory and dealing with them. Variables are required in various functions of every program. For example, when we check for conditions to execute a block of statements, variables are required. Again for iterating or repeating a block of the statement(s) several times, a counter variable is set along with a condition, or simply if we store the age of an employee, we need an integer type variable. So in every respect, the variable is used. In this tutorial, you will learn about how variables are declared in C++, how to assign values to them, and how to use them within a C++ program



### what are variables?

Variables are used in C++ where you will need to store any type of values within a program and whose value can be changed during the program execution. These variables can be declared in various ways each having different memory requirements and storing capability. Variables are the name of memory locations that are allocated by compilers, and the allocation is done based on the data type used for declaring the variable


#### syntax:

```
data_type variable_name;

```
```
data_type variable_name, variable_name, variable_name;


```


Here data_type means the valid C++ data type which includes int, float, double, char, wchar_t, bool and variable list is the lists of variable names to be declared which is separated by commas


##### example:

```
/* variable definition */int    width, height, age;
char   letter;
float  area;
double d;

```


## Variables initialization in C++

Variables are declared in the above example, but none of them has been assigned any value. Variables can be initialized, and the initial value can be assigned along with their declaration



##### syntax:

```
data_type variable_name = value;

```

##### example:

```
/* variable definition and initialization */int    width, height=5, age=32;
char   letter='A';
float  area;
double d;

/* actual initialization */width = 10;
area = 26.5;

```

There are some rules that must be in your knowledge to work with C++ variables


## Rules of Declaring variables in C++



1. A variable name can consist of Capital letters A-Z, lowercase letters a-z, digits 0-9, and the underscore character.
2. The first character must be a letter or underscore.
3. Blank spaces cannot be used in variable names.
4. Special characters like #, $ are not allowed.
5. C++ keywords cannot be used as variable names.
6. Variable names are case-sensitive.
7. A variable name can be consisting of 31 characters only if we declare a variable more than one characters compiler will ignore after 31 characters.
8. Variable type can be bool, char, int, float, double, void or wchar_t




### Here's a program to show the usage of variable in C++

example:

```
#include <iostream>
using namespace std;

int main()
{
    int x = 5;
    int y = 2;
    int Result;
    Result = x * y;
    cout << Result;
}

```

Another program showing how Global variables are declared and used within a program:


##### example:

```
#include <iostream>
using namespace std;

// Global Variable declaration:
int x, y;
float f;

int main()
{
    // Local variable
    int tot;
    float f;
    x = 10;
    y = 20;
    tot = x + y;

    cout << tot;
    cout << endl;
    f = 70.0 / 3.0;
    cout << f;
    cout << endl;
}

```
