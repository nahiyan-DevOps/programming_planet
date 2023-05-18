# Function in C++

As we all know functions play an important role in programming. Driving programs into functions are one of the major principles of programming. In C, they are called functions but in C++ they are termed as member functions. In this tutorial, you will learn about the member function and its concept used in C++.


## what are the member function in C++?

Member functions are C++ functions that have their declarations inside the class definition and these member functions work on the data member of the class. Member function definition can be written inside or outside the definition of the class. If the definition of the member function is inside the class definition, then it can define directly, but if it is defined outside the class then a special operator name scope resolution operator (::) is used along with the name of the class and the function name.



##### example:

```
class Sq {
public:
    int a;
    int square(); // Declaring function square with no argument and having return type 'int'.
};

int Sq::square()
{
    return a * a;
}

```

In this case, if you define the member function outside the class definition, then you must declare the function inside the class definition and then define it outside using the scope resolution operator.

or


```
class Sq {
public:
    int a;
    int square()
    {
        return a * a; //returns square of a number
    }
};

```

In the above program, the function is defined inside the class, and so you do not need to declare it first and can directly define the function


### main() function of C++

The main() function is called when the program starts after initialization of the non-local objects with static storage duration. It is the primary entry point of any C++ program that is executed in a hosted environment. In C++, the main() function is written after the class definition. The main function of C++ has several special properties. These are:


1. The main() function cannot be used anywhere within the program
    ..*In particular, cannot be called recursively
    ..*Its address cannot be taken for reuse
2. The main() function cannot be predefined and cannot be overloaded.
3. The main() function cannot be declared as static, inline or constexpr
4. The return type of the main() function cannot be deduced (i.e., auto main() {... is not allowed in C++).


The main() function for both the function definition (discussed above) will be same. You have to create objects of the class inside the main() and using that object along with the dot (.) operator member functions will be called.

##### syntax:

```
return_type main()
{
    class_name object - declaration;
    object_name.memberfunction1_name();
    object_name.memberfunction2_name();
    ........
}

```

example:

```
int main()
{
    Sq S1;
    S1.a = 6;
    S1.square();
    cout << " Square of the number is :"<< S1.square();
}

```


## types of member function in C++

As we are now familiar with what are member function and how they are declared and defined, how they are used in a C++ program to handle data member and member functions, and how they are called from the main(); it is time to know what are the different types of member function provided by C++.


#### Listed below are the special types of member functions that can be used within the class.


1. Simple member function
2. Static Member function
3. Const function
4. Inline function
5. Friend function


### simple member function

As discussed earlier, these are simple functions of C++ with or without return type and with or without parameters. The basic structure of a simple member function is:


##### syntax:

```
return_type functionName(parameter_list)
{
    // function body;
}

```


### static member function

The keyword 'static' is used with such member functions. Static is used primarily to hold its positions. These functions work for the whole class rather than for a particular object of the class


##### syntax:

```
class X {
public:
    static void k(){};
};
int main()
{
    G::k(); // calling member function directly with class name
}

```

The static member functions cannot access ordinary data members and member functions, but can only access the static data members and static member functions of a class



### cont member function

Const keyword makes variable constant, which means once defined, their value cannot be changed. The basic syntax of const member function is:

##### example:

```
void fun() const{}

```


### inline function

When a function is declared as inline, the compiler places a copy of the code of that specific function at each point where the function is called at compile time


### friend function

Functions are declared as a friend using the keyword 'friend' to give private access to non-class functions. Programmers can declare a global function as a friend, or a member function of other class as the friend
