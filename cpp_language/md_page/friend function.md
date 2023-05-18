# friend function

In C++ a function or an entire class may be declared to be a friend of another class or function. A friend function can also be used for function overloading.

Friend function declaration can appear anywhere in the class. But a good practice would be where the class ends. An ordinary function that is not the member function of a class has no privilege to access the private data members, but the friend function does have the capability to access any private data members. The declaration of the friend function is very simple. The keyword friend in the class prototype inside the class definition precedes it.

### example to demonstrate working of friend function

```
/* C++ program to demonstrate the working of friend function.*/#include <iostream>
using namespace std;

class Distance {
    private:
        int meter;
    public:
        Distance(): meter(0){ }
        friend int func(Distance); //friend function
};

int func(Distance d){
    //function definition
    d.meter=10; //accessing private data from non-member function
    return d.meter;
}

int main(){ Distance D;
    cout<<"Distace: "<<func(D);
    system("pause");
    return 0;
}

```

output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/08/cplusplus-friend-function.jpg?ezimgfmt=rs:309x132/rscb7/ng:webp/ngcb7)



Here, friend function func() is declared inside Distance class. So, the private data can be accessed from this function. Though this example gives you what idea about the concept of friend function.
In C++, friend means to give permission to a class or function. The non-member function has to grant an access to update or access the class.

The advantage of encapsulation and data hiding is that a non-member function of the class cannot access a member data of that class. Care must be taken using friend function because it breaks the natural encapsulation, which is one of the advantages of object-oriented programming. It is best used in the operator overloading.




# Virtual function


Polymorphism refers to the property by which objects belonging to different classes are able to respond to the same message but in different forms. When there are C++ functions with the same name in both superclass as well as a subclass, virtual functions gives programmer capability to call a member function of a different class by the same function call based upon different context. This feature is known as polymorphism which is one of the important features of OOP. The pointer is also one of the key aspects of C++ language similar to that of C. In this chapter, we will be dealing with virtual functions and pointers of C++


## what is virtual function?


A virtual function is a special form of member function that is declared within a base class and redefined by a derived class. The keyword virtual is used to create a virtual function, precede the function's declaration in the base class. If a class includes a virtual function and if it gets inherited, the virtual class redefines a virtual function to go with its own need. In other words, a virtual function is a function which gets override in the derived class and instructs the C++ compiler for executing late binding on that function. A function call is resolved at runtime in late binding and so compiler determines the type of object at runtime



#### program for virtual Function

```

#include
using namespace std;

class b
{
public:
virtual void show()
{
cout<<"\n  Showing base class....";
}
void display()
{
cout<<"\n  Displaying base class...." ;
}
};

class d:public b
{
public:
void display()
{
cout<<"\n  Displaying derived class....";
}
void show()
{
cout<<"\n  Showing derived class....";
}
};

int main()
{
b B;
b *ptr;
cout<<"\n\t P points to base:\n" ; ptr=&B; ptr->display();
ptr->show();
cout<<"\n\n\t P points to drive:\n"; d D; ptr=&D; ptr->display();
ptr->show();
}

```


output:

```

P points to base:

Displaying base class....
Showing base class....

    P points to drive:

Displaying base class....
Showing derived class....

```
