# C++ decision making

C++ conditional statements allow you to make a decision, based upon the result of a condition. These statements are called Decision Making Statements or Conditional Statements

So far, we have seen that all set of statements in a C++ program gets executed sequentially in the order in which they are written and appear. This occurs when there is no jump based statements or repetitions of certain calculations. But some situations may arise where we may have to change the order of execution of statements depending on some specific conditions. This involves a kind of decision making from a set of calculations. It is to be noted that C++ assumes any non-zero or non-null value as true and if zero or null, treated as false.
This type of structure requires that the programmers indicate several conditions for evaluation within a program. The statement(s) will get executed only if the condition becomes true and optionally, alternative statement or set of statements will get executed if the condition becomes false


#### The flowchart of the Decision-making technique in C++ can be expressed as

![alt text](https://www.w3schools.in/wp-content/uploads/2014/07/c-if.png?ezimgfmt=rs:270x330/rscb7/ng:webp/ngcb7)


C++ languages have such decision-making capabilities within its program by the use of following the decision making statements:

1. if statement
2. if-else statement
3. else-if statement
4. goto statement
5. switch statement
6. Conditional Operator


## C++ if statement


If statements in C++ is used to control the program flow based on some condition, it's used to execute some statement code block if the expression is evaluated to true. Otherwise, it will get skipped. This is the simplest way to modify the control flow of the program.

The if statement in C++ can be used in various forms depending on the situation and complexity.

#### There are four different types of if statement in C++. These are:

1. Simple if Statement
2. if-else Statement
3. Nested if-else Statement
4. else-if Ladder


syntax:

```
if(test_expression)
{
    statement 1;
    statement 2;
    ...
}

```

'Statement n' can be a statement or a set of statements, and if the test expression is evaluated to true, the statement block will get executed, or it will get skipped


##### example:

```
#include <iostream>
using namespace std;

int main()
{
 int a = 15, b = 20;

 if (b > a) {
 cout << "b is greater" << endl;
 }
 system("PAUSE");
}

```

output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2015/06/cpp-if-condition1.jpg?ezimgfmt=rs:317x127/rscb7/ng:webp/ngcb7)



## C++ if else statement

If else statements in C++ is also used to control the program flow based on some condition, only the difference is: it's used to execute some statement code block if the expression is evaluated to true, otherwise executes else statement code block.

##### syntax:

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

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/07/c-if-else.png?ezimgfmt=rs:270x330/rscb7/ng:webp/ngcb7)


### example of a c++ program to demonstrate if else statement

example:


```
#include <iostream>
using namespace std;

int main()
{
  int a = 15, b = 20;

  if (b > a) {  
    cout << "b is greater" << endl;
  } else {  
    cout << "a is greater" << endl;
  }  
  system("PAUSE");
}

```


output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2015/06/cplusplus-if-else.jpg?ezimgfmt=rs:349x162/rscb7/ng:webp/ngcb7)


example:

```

#include <iostream>
using namespace std;

int main()
{
    char name;
    int password;

    cout << "Enter the name: "; cin >> name;
    cout << " Enter your password: "; cin >> password;
    if (name == 'GG') {
        if (password == 1346) {
            cout << "Login successful";
        }
        else {
            cout << "Incorrect PASSWORD, Try again.";
        }
    }
    else {
        cout << " Incorrect Login Details, Try again.";
    }
}

```

output:

```
Enter the name: GG
Enter your password: 1346
Login successful


```


## C++ switch statement

The C++ switch statement is used when you have multiple possibilities for the if statement.


##### syntax:

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

After the end of each block it is necessary to insert a break statement because if the programmers do not use the break statement, all consecutive blocks of codes will get executed from each and every case onwards after matching the case block.


#### example:

```

#include <iostream>
using namespace std;

main()
{
    int a;
    cout << "Please enter a no between 1 and 5: " << endl; cin >> a;

    switch(a)
    {
    case 1:
    cout << "You chose One" << endl;
    break;

    case 2:
    cout << "You chose Two" << endl;
    break;

    case 3:
    cout << "You chose Three" << endl;
    break;

    case 4:
    cout << "You chose Four" << endl;
    break;

    case 5:
    cout << "You chose Five" << endl;
    break;

    default :
    cout << "Invalid Choice. Enter a no between 1 and 5" << endl;
    break;
    }
system("PAUSE");
}

```

output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2015/06/cplusplus-switch.jpg?ezimgfmt=rs:349x162/rscb7/ng:webp/ngcb7)

When none of the cases is evaluated to true, the default case will be executed, and break statement is not required for default statement.
