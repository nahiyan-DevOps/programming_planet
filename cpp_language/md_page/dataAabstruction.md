# Data Abstraction

Object-oriented programming offers various features to write programs with various concepts that help to minimize problems and increase flexibility in the program. One of the features of object-oriented programming is Data abstraction. In this chapter, you will learn about how the concept data abstraction is carried out within the C++ program



## what is data abstraction?

Data abstraction allows a program to ignore the details of how a data type is represented. Abstraction (derived from a Latin word abs, meaning away from and trahere, meaning to draw) refers to the act of representing essential features without including the background details or explanations. C++ classes use the technique of abstraction and are defined as a list of abstract attributes such as width, cost, size etc and functions to operate on these attributes. They put in a nutshell all the essential properties of an object that are required to be created. The attributes are therefore called data members as they hold information. The functions that operate on those data members are termed as member functions. Since C++ classes use the data abstraction concept, they are also termed as abstract data types.
While classifying a class, both data members and member functions are expressed in the code. But, while using an object (that is an instance of a class) the built-in data types and the members in the class get ignored which is known as data abstraction.  It is a programming design technique that depends on the separation of an interface to that of implementation. So while designing your component, you being a programmer must keep interface independent of the implementation because if you change the underlying implementation then interface would remain intact. C++ provides a great level of data abstraction. In C++, we use classes to define our own abstract data types (ADT). Programmers can use the "cout" object of class ostream for data streaming to standard output like this





#### example:
```
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello World" << endl;
}

```


## what is abstraction Class


Abstract class in C++ is the one which is not used to create objects. These type of classes are designed only to treat like a base class (to be inherited by other classes). It is a designed technique for program development which allows making a base upon which other classes may be built



### Program to show the use of data abstraction in C++:

Here is an example of declaring Public members of C++ class:

```
#include <iostream>
using namespace std;

class sample {
public:
    int gl, g2;

public:
    void val()
    {
        cout << "Enter Two values : "; cin >> gl >> g2;
    }
    void display()
    {
        cout << gl << " " << g2;
        cout << endl;
    }
};
int main()
{
    sample S;
    S.val();
    S.display();
}


```


output:

```
Enter Two values : 20
50
20 50

```

Here is a Private member example in which member data cannot be accessed outside the class:

```

#include <iostream>
using namespace std;

class sample {
public:
    int gl, g2;

public:
    void val()
    {
        cout << "Enter Two values : "; cin >> gl >> g2;
    }

private:
    void display()
    {
        cout << gl << " " << g2;
        cout << endl;
    }
};
int main()
{
    sample S;
    S.val();
    S.display();
}

```

If you execute the above program, the private member function will not be accessible and hence the following error message will appear like this in some compiler:

##### output:

```
error: 'void sample::display()' is private
     void display()
          ^

```

## Advantage of data Abstraction

1. Class internals get protected from inadvertent user-level errors
2. Programmer does not have to write the low-level code
3. Code duplication is avoided and so programmer does not have to go over again and again fairly common tasks every time to perform similar operation
4. The main idea of abstraction is code reuse and proper partitioning across classes
5. For small projects, this may not seem useful but for large projects, it provides conformity and structure as it provides documentation through the abstract class contract
6. It allows internal implementation details to be changed without affecting the users of the abstraction
