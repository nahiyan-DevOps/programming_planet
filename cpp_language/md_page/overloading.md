# overloading

C++ language allows programmers to specify more than one definition for a function name or an operator. This is one of the many exciting features that Object Oriented Language offers programmers. It is one of the important techniques that has extended the power and flexibility of C++. In this chapter, you will learn about the types of overloading and how they are used within a C++ program


## what is overloading?

Overloading is the technique to use a single identifier to define various methods or techniques of a class that differs in their input and output parameters. The concept of overloading is generally used when a program block conceptually executes the same task but with a slight distinctness in a set of parameters.
Overloading is a concept used to avoid redundant code where the same method name or operator is used multiple times but with a different set of parameters or number of operands. The actual method that gets called during runtime is resolved at compile time, thus avoiding runtime errors. Overloading provides code clarity; reduce complexity, and increases runtime presentation of a code.


####There are two types of overloading provided by C++. These are:

1. Operator Overloading
2. Function Overloading





### Here is a program for operator overloading


example:

```
#include <iostream>
using namespace std;

class MinusOverload {
private:
 int a;
 int b;

public:
 void Distance()
 {
 a = 0;
 b = 0;
 }

 MinusOverload(int f, int i)
 {
 int c;
 a = f;
 b = i;
 c = a - b;
 cout << "\nC:" << c;
 }

 void display()
 {
 cout << "A: " << a << " B:" << b << endl;
 }

 MinusOverload operator-()
 {
 a = -a;
 b = -b;
 return MinusOverload(a, b);
 }
};

int main()
{
 MinusOverload M1(6, 8), M2(-3, -4);
 -M1;
 M1.display();
 -M2;
 M2.display();
 return 0;
}


```



If a C++ class have multiple member functions, having the same name but different parameters (with a change in type, sequence or number), and programmers can use them to perform a similar form of operations, then it is known as function overloading. In this case, two functions can have same identifier (name) and if either number of arguments or type of arguments passed to functions are different; then overloading is possible within a C++ program. In other words, it is the ability to create multiple functions with same name and slightly different implementation and depending on the context (type, sequence, and a number of the value passed), the appropriate function gets invoked



#### In case of C++ programs, if the functions are like this:

example:

```
int overloaded() { }
int overloaded (int g){ }
int overloaded (float g){ }
int overloaded (int g, double s){ }
int overloaded (float s, int g, double k){ }

```


Here the function name overloaded is used as overloading functions with the change in argument type and number.



### Function overloading

example:

```
#include <iostream>
using namespace std;

long add(long, long);
float add(float, float);
int main()
{
 long a, b, c;
 float e, f, g;
 cout << "Enter two integers\n";
 cin >> a >> b;
 c = add(a, b);
 cout << "Sum of integers: " << c << endl;
 cout << "Enter two floating point numbers\n";
 cin >> e >> f;
 g = add(e, f);
 cout << "Sum of floats: " << g << endl;
}

long add(long c, long g)
{
 long sum;
 sum = c + g;
 return sum;
}

float add(float c, float g)
{
 float sum;
 sum = c + g;
 return sum;
}

```


#### Rules for Overloading Operators:


1. Only existing operators can be overloaded
2. Programmers cannot change the basic meaning of an operator
3. Overloaded operators will always follow the syntax rules of the original operators
4. Programmers cannot use friend function to overload certain operators
