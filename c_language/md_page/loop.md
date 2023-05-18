# C Loop

Sometimes it is necessary for the program to execute the statement several times. A loop executes a block of commands a specified number of times until a condition is met. In this tutorial, you will learn about all the looping statements of C programming along with their use

## What is loop?

A computer is the most suitable machine for performing repetitive tasks, and it can perform a task thousands of times. Every programming language has the feature to instruct to do such repetitive tasks with the help of certain statements. The process of repeatedly executing a collection of statements is called looping. The statements get executed many numbers of times based on the condition. But if the condition is given in such logic that the repetition continues any number of times with no fixed condition to stop looping those statements, then this type of looping is called **infinite** looping

## C supports the following types of loops:

1. while loops
2. do-while loops
3. for loops

##### Figure - Flowchart of Looping

![alt text](https://www.w3schools.in/wp-content/uploads/2014/07/c-for.png?ezimgfmt=rs:270x350/rscb7/ng:webp/ngcb7)


## C while loops
C while loops statement allows to repeatedly run the same block of code until a condition is met.

while loop is a most basic loop in C programming. while loop has one control condition, and executes as long the condition is true.  The condition of the loop is tested before the body of the loop is executed, hence it is called an entry-controlled loop

### The basic format of while loop statement:

syntex:

```
While (condition)
{
   statement(s);
   Incrementation;
}

```

#### Figure - Flowchart of while loop

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/07/c-while.png?ezimgfmt=rs:270x350/rscb7/ng:webp/ngcb7)

#### example of a c pragram demonstrate while loops

```
#include<stdio.h>

int main ()
{
   /* local variable Initialization */   int n = 1,times=5;

   /* while loops execution */   while( n <= times )
   {
      printf("C while loops: %d\n", n);
      n++;
   }

   return 0;
}

```

output:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/08/c-while-loop.jpg?ezimgfmt=rs:341x157/rscb7/ng:webp/ngcb7)



## C do while loop

C do while loops are very similar to the while loops, but it always executes the code block at least once and furthermore as long as the condition remains true. This is an exit-controlled loop.

####
The basic format of do while loop statement is:

```
do
{
   statement(s);

}while( condition );

```

#### example of a c program to demonstrate do while Loop

example:

```
#include<stdio.h>

int main ()
{
   /* local variable Initialization */   int n = 1,times=5;

   /* do loops execution */   do
   {
       printf("C do while loops: %d\n", n);
       n = n + 1;
   }while( n <= times );

   return 0;
}

```

output:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/08/c-do-while-loop.jpg?ezimgfmt=rs:341x157/rscb7/ng:webp/ngcb7)


## C for loop


C for loops is very similar to a while loops in that it continues to process a block of code until a statement becomes false, and everything is defined in a single line. The for loop is also entry-controlled loop


#### The basic format of for loop statement is:

```
for ( init; condition; increment )
{
   statement(s);
}

```
### example of a C program to demonstrate for loop

```
#include<stdio.h>

int main ()
{
  /* local variable Initialization */  int n,times=5;;

   /* for loops execution */   for( n = 1; n <= times; n = n + 1 )
   {
      printf("C for loops: %d\n", n);
   }

   return 0;
}

```

output:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/08/c-for-loop.jpg?ezimgfmt=rs:341x157/rscb7/ng:webp/ngcb7)
