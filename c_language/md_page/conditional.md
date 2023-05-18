# C Decision Making


C conditional statements allow you to make a decision, based upon the result of a condition. These statements are called Decision Making Statements or Conditional Statements.

So far, we have seen that all set of statements in a C program gets executed sequentially in the order in which they are written and appear. This occurs when there is no jump based statements or repetitions of certain calculations. But some situations may arise where we may have to change the order of execution of statements depending on some specific conditions. This involves a kind of decision making from a set of calculations. It is to be noted that C language assumes any non-zero or non-null value as true and if zero or null, treated as false.
This type of structure requires that the programmers indicate several conditions for evaluation within a program. The statement(s) will get executed only if the condition becomes true and optionally, alternative statement or set of statements will get executed if the condition becomes false

### The flowchart of the Decision-making technique in C can be expressed as:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/07/c-if.png?ezimgfmt=rs:270x330/rscb7/ng:webp/ngcb7)


### Conditional statement in C

1. if statement
2. goto statement
3. switch statement
4. if-else statement
5. nested if-else statement
6. else if- statement


### if statement

If statements in C is used to control the program flow based on some condition, it's used to execute some statement code block if the expression is evaluated to true. Otherwise, it will get skipped. This is the simplest way to modify the control flow of the program

#### The basic format of if statement is:

```
if(test_expression)
{
    statement 1;
    statement 2;
    ...
}

```
'Statement n' can be a statement or a set of statements, and if the test expression is evaluated to true, the statement block will get executed, or it will get skipped.


#### example of a C program to demonstrate if statement

```
#include<stdio.h>

void main()
{
  int a = 15, b = 20;

  if (b > a) {  
    printf("b is greater");
  }
}

```

output:
b is greater


### if-else statement

If else statements in C is also used to control the program flow based on some condition, only the difference is: it's used to execute some statement code block if the expression is evaluated to true, otherwise executes else statement code block

#### The basic format of if else statement is:

```
if(test_expression)
{
   //execute your code
}
else
{
   //execute your code
}

```
#### Figure - Flowchart of if-else Statement:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/07/c-if-else.png?ezimgfmt=rs:270x330/rscb7/ng:webp/ngcb7)

#### example of a C program to demonstrate if else statement

```
#include<stdio.h>

void main()
{
  int a, b;

  printf("Please enter the value for a:");
  scanf("%d", &a);

  printf("\nPlease the value for b:");
  scanf("%d", &b);

  if (a > b) {  
    printf("\n a is greater");
  } else {  
    printf("\n b is greater");
  }
}

```

output:
![alt text](https://www.w3schools.in/wp-content/uploads/2014/08/c-if-else-1.jpg?ezimgfmt=rs:310x156/rscb7/ng:webp/ngcb7)

### nested if-else statement

Nested if else statements play an important role in C programming, it means you can use conditional statements inside another conditional statement

#### The basic format of Nested if else statement is:

```
if(test_expression one)
{
   if(test_expression two) {
      //Statement block Executes when the boolean test expression two is true.
   }
}
else
{
    //else statement block
}

```
#### example of a C program to demonstrate nested if-else statement

```
#include<stdio.h>

void main()
{
int x=20,y=30;

    if(x==20)
    {
        if(y==30)
        {
            printf("value of x is 20, and value of y is 30.");
        }
    }
}

```
output:
```
value of x is 20, and value of y is 30.

```


### C goto statement

So far we have discussed the if statements and how it is used in C to control statement execution based on some decisions or conditions. The flow of execution also depends on other statements which are not based on conditions that can control the flow.

C supports a unique form of a statement that is the **goto** Statement which is used to branch unconditionally within a program from one point to another. Although it is not a good habit to use the **goto** statement in C, there may be some situations where the use of the **goto** statement might be desirable.
The **goto** statement is used by programmers to change the sequence of execution of a C program by shifting the control to a different part of the same program

##### example of goto statement

```
#include<stdio.h>

void main()
{
   int age;

   g: //label name
     printf("you are Eligible\n");
   s: //label name
     printf("you are not Eligible");

   printf("Enter you age:");
   scanf("%d", &age);
   if(age>=18)
        goto g; //goto label g
   else
        goto s; //goto label s
}

```


### switch statement

C switch statement is used when you have multiple possibilities for the if statement. Switch case will allow you to choose from multiple options. When we compare it to a general electric switchboard, you will have many switches in the switchboard but you will only select the required switch, similarly, the switch case allows you to set the necessary statements for the user

###### syntex:

```
switch(variable)
{
case 1:
   //execute your code
break;

case n:
   //execute your code
break;

default:
   //execute your code
break;
}

```

After the end of each block it is necessary to insert a break statement because if the programmers do not use the break statement, all consecutive blocks of codes will get executed from every case onwards after matching the case block


#### example of a C pragram to demonstrate switch statement

```
#include<stdio.h>

void main()
{
    int a;
    printf("Please enter a no between 1 and 5: ");
    scanf("%d",&a);

    switch(a)
    {
    case 1:
    printf("You chose One");
    break;

    case 2:
    printf("You chose Two");
    break;

    case 3:
    printf("You chose Three");
    break;

    case 4:
    printf("You chose Four");
    break;

    case 5:
    printf("You chose Five.");
    break;

    default :
    printf("Invalid Choice. Enter a no between 1 and 5");
    break;
    }

}

```

output:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/08/c-switch.jpg?ezimgfmt=rs:357x169/rscb7/ng:webp/ngcb7)

When none of the cases is evaluated to true, the default case will be executed, and break statement is not required for default statement.
