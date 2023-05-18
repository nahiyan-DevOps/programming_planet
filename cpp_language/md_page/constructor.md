# C++ constructor & destructor

Providing the initial value as described in the earlier chapters of C++ does not conform to the philosophy of C++. So C++ provides a special member function called the constructor which enables an object to initialize itself at the time of its creation. This is known as automatic initialization of objects. This concept of C++ also provides another member function called destructor which is used to destroy the objects when they are no longer required. In this chapter, you will learn about how constructors and destructors work, types of constructors and how they can be implemented within C++ program

## what are constructors?

The process of creating and deleting objects in C++ is a vital task. Each time an instance of a class is created the constructor method is called. Constructors is a special member function of class and it is used to initialize the objects of its class. It is treated as a special member function because its name is the same as the class name. These constructors get invoked whenever an object of its associated class is created. It is named as "constructor" because it constructs the value of data member of a class. Initial values can be passed as arguments to the constructor function when the object is declared


#### This can be done in two ways:

1. By calling constructor explicitly
2. By calling constructor implicitly



### The declaration and definition of constructor is as follows

syntax:

```
class class_name
{
 int g, h;
 public:
 class_name(void);  // Constructor Declared
 . . .
 };
class_name :: class_name()
{
 g=1; h=2;  // Constructor defined
}

```

###Special characteristics of Constructors:

1. They should be declared in the public section
2. They do not have any return type, not even void
3. They get automatically invoked when the objects are created
4. They cannot be inherited though derived class can call the base class constructor
5. Like other functions, they can have default arguments
6. You cannot refer to their address
7. Constructors cannot be virtual



### C++ offers four types of constructors. These are:

1. Do nothing constructor
2. Default constructor
3. Parameterized constructor
4. Copy constructor


### Do nothing constructor

Do nothing constructors are that type of constructor which does not contain any statements. Do nothing constructor is the one which has no argument in it and no return type.


### Default Constructor

The default constructor is the constructor which doesn't take any argument. It has no parameter but a programmer can write some initialization statement there.

#### syntax:

```
class_name()
{
 // Constructor Definition ;
}

//Code Snippet:
#include <iostream>
using namespace std;

class Calc {
 int val;

public:
 Calc()
 {
 val = 20;
 }
};
int main()
{
 Calc c1;
 cout << c1.val;
}

```

A default constructor is very important for initializing object members, that even if we do not define a constructor explicitly, the compiler automatically provides a default constructor implicitly.


### parameteerized constructor

A default constructor does not have any parameter, but programmers can add and use parameters within a constructor if required. This helps programmers to assign initial values to an object at the time of creation

```

#include <iostream>
using namespace std;

 class Calc
 {
  int val2;
  public:
  Calc(int x)
  {
   val2=x;
 }
};

 int main()
 {
  Calc c1(10);
  Calc c2(20);
  Calc c3(30);
  cout << c1.val2;
  cout << c2.val2;
  cout << c3.val2;
}

```


### copy constructor


C++ provides a special type of constructor which takes an object as an argument and is used to copy values of data members of one object into another object. In this case, copy constructors are used to declaring and initializing an object from another object


```
Calc C2(C1);
Or
Calc C2 = C1;

```

The process of initializing through a copy constructor is called the **copy initialization**


####syntax:
```

class-name (class-name &)
{
 . . .
}
```


example:

```
#include <iostream>
using namespace std;

class CopyCon {
 int a, b;

public:
 CopyCon(int x, int y)
 {
 a = x;
 b = y;
 cout << "\nHere is the initialization of Constructor";
 }
 void Display()
 {
 cout << "\nValues : \t" << a << "\t" << b;
 }
};

void main()
{
 CopyCon Object(30, 40);
 //Copy Constructor
 CopyCon Object2 = Object;
 Object.Display();
 Object2.Display();
}

```


## What are destructor?

As the name implies, destructors are used to destroy the objects that have been created by the constructor within the C++ program. Destructor names are same as the class name but they are preceded by a tilde (~). It is a good practice to declare the destructor after the end of using constructor. Here's the basic declaration procedure of a destructor


```

~Cube()
{

}

```

The destructor neither takes an argument nor returns any value and the compiler implicitly invokes upon the exit from the program for cleaning up storage that is no longer accessible
