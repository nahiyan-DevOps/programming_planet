# C++ program structure

This tutorial describes the program structure of the C++ program.


### C++ program involves the following section:

1. Documentation
2. Preprocessor Statements
3. Global Declarations
4. The main() function
5. Local Declarations
6. Program Statements & Expressions
7. User Defined Functions


Let's begin with a simple C++ program code


### C++ program which outputs a line of text.


```
#include <iostream>

int main()
{
 std::cout<<"This is my first C++ Program.";
 std::cout<<std::endl<<"and its very easy";
}

```


output:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/08/first-cplusplus-program.jpg?ezimgfmt=rs:330x154/rscb7/ng:webp/ngcb7)



#### The above example has been used to print text on the screen


### Let's look into various parts of the above C++ program

1. #include<iostream>
    ..* This is a preprocessor directive. It tells the preprocessor to include the contents of iostream header file in the program before compilation. This file is required for input-output statements
2. int/void
    ..* int/void is a return value, which will be explained in a while
3. main()
    ..* The main() is the main function where program execution begins. Every C++ program must contain only one main function
4. Braces
    ..* Two curly brackets "{…}" are used to group all statements.



### std:: cout<< "This is my first C++ Program";

The above line is a statement in C++. A statement must always terminate with a semicolon; otherwise, it causes a syntax error. This statement introduces two new features of C++ language, cout and << operator.

You will also notice that the words are inside inverted commas because they are what is called a string. Each letter is called a character, and a series of characters that are grouped is called a string. Strings must always be put between inverted commas.

We used std:: before cout. This is required when we use #include <iostream >.
It specifies that we are using a name cout which belongs to namespace std. A namespace is a new concept introduced by ANSI C++ which defines the scope of identifiers which are used in the program. std is the namespace where C++ standard libraries are defined.
Operator << is the insertion stream operator. It sends contents of the variable on its right to the object on its left. In our case, the right operand is the string "This is my first c++ Program" and left operand is a cout object. So it sends the string to the cout object, and cout object then displays it on the output screen.



### namespace

```
using namespace std;

```

If you specify using namespace std then you don't have to put std:: throughout your code. The program will know to look in the std library to find the object. Namespace std contains all the classes, objects and functions of the standard C++ library


##### example

```
#include <iostream>
using namespace std;

int main()
{
 cout<<"This is my first C++ Program.";
 cout<<std::endl<<"and its very easy";
}

```


### Return statement

| return 0 | At the end of the main function returns value 0|


#### In new C++ you have to use:

1. int main() instead of void main()
2. After you import your headers you required to use using namespace std;
3. There is no header file like iostream.h, you only required to use this as #include <iostream>
