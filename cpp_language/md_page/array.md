# C++ array

An array is a one of the data structure in C++, that can store a fixed-size sequential collection of elements of the same data type.


## Define an array in C++

syntax:
```
type arrayName [ arraySize ];

```
An array type can be any valid C++ data types, and array size must be an integer constant greater than zero.

##### example:

```
double salary[15000];

```


Arrays can be initialized at declaration time:

```
int age[5]={22,25,30,32,35};

```

Initializing each element separately in the loop:

```
int newArray[5];
int n = 0;

// Initializing elements of array seperately
for(n=0;n<sizeof(newArray)/sizeof(newArray[0]);n++)
{
  newArray[n] = n;
}

```

#### A pictorial Representation of the array

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/07/One-Dimensional-array.jpg?ezimgfmt=rs:466x99/rscb7/ng:webp/ngcb7)


## Accessing array elements in C++

```
int newArray[10];
int n = 0;

// Initializing elements of array seperately
for(n=0;n<sizeof(newArray)/sizeof(newArray[0]);n++)
{
  newArray[n] = n;
}

int a = newArray[5]; // Assigning 5th element of array value to integer 'a'.

```

#### example:

```
#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

int main () {

   int newArray[5];
   int n = 0, p =0;

   // Initializing elements of array seperately         
   for (n=0; n<sizeof(newArray)/sizeof(newArray[0]); n++) {
      newArray[n] = n+50;
   }
   // print heading
   cout << "Element" << setw(10) << "Value" << endl;

   // print element's value in loop                    
   for (p=0; p<sizeof(newArray)/sizeof(newArray[0]); p++) {
      cout << setw(5) << p << setw(10) << newArray[p] << endl;
   }
   return 0;
}

```

output:

```
Element     Value
    0        50
    1        51
    2        52
    3        53
    4        54

```




# C++ Strings

In C++, the one-dimensional array of characters are called strings, which is terminated by a null character \0



### There are two ways to declare a string in C++:

example:

Through an array of characters:
```
char greeting[6];

```
Through pointers:

```
char *greeting;

```


### strings initialization in C++

example:

```
char greeting[6] = {'C', 'l', 'o', 'u', 'd', '\0'};

```

or

```
char greeting[] = "Cloud";

```


example:

```
#include <iostream>
using namespace std;

int main ()
{
   char greeting[6] = {'C', 'l', 'o', 'u', 'd', '\0'};

   cout << "Tutorials" << greeting << endl;
   system("pause");
   return 0;
}

```



output:

![alt text] (https://www.w3schools.in/wp-content/uploads/2015/07/cplusplus-strings.jpg?ezimgfmt=rs:335x150/rscb7/ng:webp/ngcb7)




### C++ manipulating string

A string is a sequence of character. As you know that C++ does not support built-in string type, you have used earlier those null character based terminated array of characters to store and manipulate strings. These strings are termed as C Strings. It often becomes inefficient performing operations on C strings. Programmers can also define their own string classes with appropriate member functions to manipulate strings. ANSI standard C++ introduces a new class called string which is an improvised version of C strings in several ways. In many cases, the strings object may be treated like any other built-in data type. The string is treated as another container class for C++.


### string class in C++

The string class is huge and includes many constructors, member functions, and operators.

Programmers may use the constructors, operators and member functions to achieve the following:



1. Creating string objects
2. Reading string objects from keyboard
3. Displaying string objects to the screen
4. Finding a substring from a string
5. Modifying string
6. Adding objects of string
7. Comparing strings
8. Accessing characters of a string
9. Obtaining the size or length of a string, etc...




### manipulate Null - terminated string

C++ supports a wide range of functions that manipulate null-terminated strings. These are:

1. strcpy(str1, str2): Copies string str2 into string str1.
2. strcat(str1, str2): Concatenates string str2 onto the end of string str1.
3. strlen(str1): Returns the length of string str1.
4. strcmp(str1, str2): Returns 0 if str1 and str2 are the same; less than 0 if str1<str2; greater than 0 if str1>str2.
5. strchr(str1, ch): Returns a pointer to the first occurrence of character ch in string str1.
6. strstr(str1, str2): Returns a pointer to the first occurrence of string str2 in string str1




## Important function supported by string classes


1. append(): This function appends a part of a string to another string
2. assign():This function assigns a partial string
3. at(): This function obtains the character stored at a specified location
4. begin(): This function returns a reference to the start of the string
5. capacity(): This function gives the total element that can be stored
6. compare(): This function compares a string against the invoking string
7. empty(): This function returns true if the string is empty
8. end(): This function returns a reference to the end of the string
9. erase(): This function removes character as specified
10. find(): This function searches for the occurrence of a specified substring
11. length(): It gives the size of a string or the number of elements of a string
12. swap(): This function swaps the given string with the invoking one




## Important constructor obtained by strings classes

1. String(): This constructor is used for creating an empty string
2. String(const char *str): This constructor is used for creating string objects from a null-terminated string
3. String(const string *str): This constructor is used for creating a string object from another string object


## Operators used for string Objects

1. =: assignment
2. +: concatenation
3. ==: Equality
4. !=: Inequality
5. <: Less than
6. <=: Less than or equal
7. >: Greater than
8. >=: Greater than or equal
9. []: Subscription
10. <<: Output
11. >>: Input
