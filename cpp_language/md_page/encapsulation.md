# Encapsulation

As you all know that C++ is rich in Objects and Classes. So, it comes under Object Oriented Programming category. It is the first successful Object Oriented Programming Language, with all the features of OOPs along with some varied concepts. So abstraction and encapsulation were the first basic sets of concepts of OOPs. Here Abstraction deals with the basic characteristics of an object which distinguishes from other types of objects and hence allows crisply defined conceptual boundaries, with respect to the perspective of the viewer


## concept of Encapsulation

Unable to deal with the complexity of an object, human chooses to ignore its non-essential details and concentrate on the details which are essential to our understanding. You can place a simple context of the object model, that abstraction is "looking for what you want" within an object or class. But there is another major concept connected to abstraction which is called encapsulation.
So basically, encapsulation can be defined as the process of hiding all of the details of an object that do not throw in or dealt with its essential characteristics. Encapsulation can also be defined as preventing access to non-essential details of classes or its objects. Abstraction and encapsulation have close bonding among each other. Encapsulation assists abstraction by providing a means of suppressing the non-essential details

## use of access specifier

Access specifiers are used to determining whether any other class or function can access member variables and functions of a particular class or within a program.
#### C++ provides its programmers with three access specifiers. These are

1. public
2. private
3. protected

Access specifiers create the boundaries among the accessible and inaccessible sections of any class. It provides with programmer the privilege to design the class for demarcating which section of the class need to be obscured from the user point of view and further which should be offered to them as an interface for the class



1. **Public**: Here, the class members declared under public has to be obtainable and accessible to everyone. All those data members and member functions acknowledged as the public can be accessed by other classes also.
2. **Private**: Private is used where no one can obtain or access the class members declared as private outside that class. When anyone tries to access or avail the private member of that class a compile-time error gets generated. By default, all members of a class remain in 'private' access mode.
3. **Protected**: It is a special purpose access specifier which is similar to private but it creates class member inaccessible outside that class. But it can get accessed by any subclass of that class


#### example:

```
#include <iostream>
using namespace std;

class rectangle
{
   private:
   int l,b;
   public:
   rectangle(int x=2,int y=4)
   {
      l=x;
      b=y;
      cout<<"i am parametrized";
   }
   /* rectangle()
   {
      cout<<"i am default";
   }*/   void area()
   {
      cout<<"\narea is = "<<l*b;
   }
};

int main()
{
   rectangle r;
   r.area();
   rectangle r1(3,6);
   r1.area();
   rectangle r2(10);
   r2.area();
}


```



# Polymorphism

The term Polymorphism gets derived from the Greek word where poly + morphos where poly means many and morphos means forms.


#### In programming background, polymorphism can be broadly divided into two parts. These are:
1. Static Polymorphism
2. Dynamic Polymorphism

![alt text] (https://www.w3schools.in/wp-content/uploads/2016/12/Polymorphism.png?ezimgfmt=ng%3Awebp%2Fngcb7%2Frs%3Adevice%2Frscb7-1)


Polymorphism is another concept of object-oriented programming (OOPs). The attitude which lies beneath this concept is "single interface having multiple implementations." This provides a single interface for controlling access to a general class of actions. Polymorphism can be gained in both ways:

1. compile time and
2. runtime

A common and simple example of polymorphism is when you used >> and << as operator overloading in C++, for cin and cout statements respectively. This bitwise shift operator at that time acts as a inclusion operator and its overloaded meaning is defined in iostream header file.


### static polymorphism


####In static polymorphism or early binding, there you will get two subcategories like:

1. Function overloading which is the process of using the same name for two or more functions.
2. Operator overloading which is the process of using the same operator for two or more operands

### code snippet for function Overloading

```
class funcOl {
public:
      funcOl ();
      funcOl (int i);
      int add(int a, int b);
      int add(float a, float b);
};

```


## Dynamic polymorphism

This refers to the entity which changes its form depending on circumstances at runtime. This concept can be adopted as analogous to a chameleon changing its color at the sight of an approaching object


## what is virtual function?

A virtual function can be defined as the member function within a base class which you expect to redefine in derived classes. For creating a virtual function, you have to precede your function's declaration within the base class with a **virtual keyword**


```
#include <iostream>
using namespace std;

class Game
{
   int g;
   public:
       Game()
       {
          g = 1;
       }
       virtual void show()
       {
          cout <<g;
       }
};

class Anim: public Game
{
   int k;
   public:
       Anim()
       {
          k = 2;
       }
       virtual void show()
       {
          cout <<k; } }; int main() { Game *g; Anim a; g = &a; g->show();
   return 0;
}

```




# Inheritance

Reusability is one of the important characteristics of Object Oriented Programming (OOP). Instead of trying to write programs repeatedly, using existing code is a good practice for the programmer to reduce development time and avoid mistakes. In C++, reusability is possible by using Inheritance.


## what is Inheritance?

The technique of deriving a new class from an old one is called inheritance. The old class is referred to as base class and the new class is referred to as derived class or subclass. Inheritance concept allows programmers to define a class in terms of another class, which makes creating and maintaining application easier. When writing a new class, instead of writing new data member and member functions all over again, programmers can make a bonding of the new class with the old one that the new class should inherit the members of the existing class. A class can get derived from one or more classes, which means it can inherit data and functions from multiple base classes



### what are Base class and derived class?

The existing class from which the derived class gets inherited is known as the base class. It acts as a parent for its child class and all its properties i.e. public and protected members get inherited to its derived class.

A derived class can be defined by specifying its relationship with the base class in addition to its own details, i.e. members


### form of inheritance

1. Single Inheritance
2. Multiple Inheritance
3. Hierarchical Inheritance
4. Multilevel Inheritance
5. Hybrid Inheritance (also known as Virtual Inheritance)



![alt text] (https://www.w3schools.in/wp-content/uploads/2014/07/inheritanc-cpp.jpg?ezimgfmt=rs:753x469/rscb7/ng:webp/ngcb7)


### single inheritance

In single inheritance, there is only one base class and one derived class. The Derived class gets inherited from its base class. This is the simplest form of inheritance. In the above figure, fig(a) is the diagram for single inheritance.


### multiple inheritance

In this type of inheritance, a single derived class may inherit from two or more base classes. In the above list of figures, fig(b) is the structure of Multiple Inheritance

```
#include <iostream>
using namespace std;

class stud {
protected:
    int roll, m1, m2;

public:
    void get()
    {
        cout << "Enter the Roll No.: "; cin >> roll;
        cout << "Enter the two highest marks: "; cin >> m1 >> m2;
    }
};
class extracurriculam {
protected:
    int xm;

public:
    void getsm()
    {
        cout << "\nEnter the mark for Extra Curriculam Activities: "; cin >> xm;
    }
};
class output : public stud, public extracurriculam {
    int tot, avg;

public:
    void display()
    {
        tot = (m1 + m2 + xm);
        avg = tot / 3;
        cout << "\n\n\tRoll No    : " << roll << "\n\tTotal      : " << tot;
        cout << "\n\tAverage    : " << avg;
    }
};
int main()
{
    output O;
    O.get();
    O.getsm();
    O.display();
}

```


output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/08/Multiple-Inheritance.jpg?ezimgfmt=rs:417x160/rscb7/ng:webp/ngcb7)




### Hierarchical inheritance

In this type of inheritance, multiple derived classes get inherited from a single base class. In the above list of figures, fig(c) is the structure of Hierarchical Inheritance

```

class base_classname {
    properties;
    methods;
};
class derived_class1 : visibility_mode base_classname {
    properties;
    methods;
};
  class derived_class2 : visibility_mode base_classname {
    properties;
    methods;
};
   ... ... ...
   ... ... ...
  class derived_classN : visibility_mode base_classname {
    properties;
    methods;
};

```


Program for Hierarchical inheritance

```
#include <iostream>
#include <string.h>
using namespace std;

class member {
    char gender[10];
    int age;

public:
    void get()
    {
        cout << "Age: "; cin >> age;
        cout << "Gender: "; cin >> gender;
    }
    void disp()
    {
        cout << "Age: " << age << endl;
        cout << "Gender: " << gender << endl;
    }
};
class stud : public member {
    char level[20];

public:
    void getdata()
    {
        member::get();
        cout << "Class: "; cin >> level;
    }
    void disp2()
    {
        member::disp();
        cout << "Level: " << level << endl;
    }
};
class staff : public member {
    float salary;

public:
    void getdata()
    {
        member::get();
        cout << "Salary: Rs."; cin >> salary;
    }
    void disp3()
    {
        member::disp();
        cout << "Salary: Rs." << salary << endl;
    }
};
int main()
{
    member M;
    staff S;
    stud s;
    cout << "Student" << endl;
    cout << "Enter data" << endl;
    s.getdata();
    cout << endl
         << "Displaying data" << endl;
    s.disp();
    cout << endl
         << "Staff Data" << endl;
    cout << "Enter data" << endl;
    S.getdata();
    cout << endl
         << "Displaying data" << endl;
    S.disp();
}

```


output:


![alt text] (https://www.w3schools.in/wp-content/uploads/2014/08/Hierarchical-Inheritance.jpg?ezimgfmt=rs:258x275/rscb7/ng:webp/ngcb7)


### Multilevel inheritance

The classes can also be derived from the classes that are already derived. This type of inheritance is called multilevel inheritance.


####example:

```

#include <iostream>
using namespace std;

class base {
public:
    void display1()
    {
        cout << "\nBase class content.";
    }
};
class derived : public base {
public:
    void display2()
    {
        cout << "1st derived class content.";
    }
};

class derived2 : public derived {
    void display3()
    {
        cout << "\n2nd Derived class content.";
    }
};

int main()
{
    derived2 D;
    //D.display3();
    D.display2();
    D.display1();
}

```


output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/08/Multilevel-Inheritance.jpg?ezimgfmt=rs:248x110/rscb7/ng:webp/ngcb7)


### Hybrid inheritance

This is a Mixture of two or More Inheritance and in this Inheritance, a Code May Contains two or Three types of inheritance in Single Code. In the above figure, the fig(5) is the diagram for Hybrid inheritance.
