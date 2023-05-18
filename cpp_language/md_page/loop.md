# C++ Loops

Sometimes it is necessary for the program to execute the statement several times, and C++ loops execute a block of commands a specified number of times until a condition is met. In this chapter, you will learn about all the looping statements of C++ along with their use

### what are loops in C++?

There may arise some situations during programming where programmers need to execute a block of code several times (with slight variations sometimes). In general, statements get executed sequentially with a C++ program, one statement followed by another. C++ provides statements for several control structures along with iteration/repetition capability that allows programmers to execute a statement or group of statements multiple times


####C++ supports following types of loops:
1. while loops
2. do while loops
3. for loops


![alt text] (https://www.w3schools.in/wp-content/uploads/2014/07/c-for.png?ezimgfmt=rs:270x350/rscb7/ng:webp/ngcb7)


### C++ while Loops

C++ while loops statement allows to repeatedly run the same block of code until a condition is met.

while loop is a most basic loop in C++. while loop has one control condition, and executes as long the condition is true.  The condition of the loop is tested before the body of the loop is executed, hence it is called an entry-controlled loop


#### syntax:

```
While (condition)
{
   statement(s);
   Incrementation;
}

```

#### example:

```
#include <iostream>
using namespace std;

int main ()
{
   /* local variable Initialization */   int n = 1,times=5;

   /* while loops execution */   while( n <= times )
   {
      cout << "C++ while loops: " << n <<endl;
      n++;
   }
   return 0;
}

```

output:

![alt text](https://www.w3schools.in/wp-content/uploads/2015/06/cplusplus-while-loop.jpg?ezimgfmt=rs:341x157/rscb7/ng:webp/ngcb7)


### C++ do while Loops

C++ do while loops are very similar to the while loops, but it always executes the code block at least once and furthermore as long as the condition remains true. This is an exit-controlled loop

#### syntax:

```
do
{
   statement(s);

}while( condition );

```

#### example:

```
#include <iostream>
using namespace std;

int main ()
{
   /* local variable Initialization */   int n = 1,times=0;

   /* do-while loops execution */   do
   {
      cout << "C++ do while loops: " << n <<endl;
      n++;
   }while( n <= times );
   return 0;
}

```

output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2015/06/cplusplus-do-while.jpg?ezimgfmt=rs:322x159/rscb7/ng:webp/ngcb7)


### C++ for Loops


C++ for loops is very similar to a while loops in that it continues to process a block of code until a statement becomes false, and everything is defined in a single line. for loop is an entry-controlled loop.


#### syntax:
```
for ( init; condition; increment )
{
   statement(s);
}

```

example:

```
#include <iostream>
using namespace std;

int main ()
{
   /* local variable Initialization */   int n = 1,times=5;

   /* for loops execution */   for( n = 1; n <= times; n = n + 1 )
   {
      cout << "C++ for loops: " << n <<endl;
   }
   return 0;
}

```

output:


![alt text] (https://www.w3schools.in/wp-content/uploads/2015/06/cplusplus-for-loops.jpg?ezimgfmt=rs:322x159/rscb7/ng:webp/ngcb7)
