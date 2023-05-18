# C++ Datatype

Data types in any of the language mean that what are the various type of data the variables can have in that particular language. Information is stored in computer memory with different data types. Whenever a variable is declared it becomes necessary to define a data type that what will be the type of data that variable can hold.


#### Data Types available in C++:

### primary (Built-in) Data Types:
1. character
2. integer
3. floating point
4. boolean
5. double floating point
6. void
7. wide character


### User defined Datatype:

1. Structure
2. Union
3. Class
4. Enumeration


### Derived Datatype:

1. Array
2. Function
3. Pointer
4. Reference



Both C and C++ compilers support the fundamental, i.e., the built-in data types. Taking void as an exception the basic data types may have several modifiers, and these modifiers are used to serve the data types in various situations


#### The lists of modifiers used in C++ are:


1. signed
2. unsigned
3. long
4. short


### character Datatypes


| Data Type (Keywords)    |  Size	|          Typical Range      |
| ---------------------:  | :----:| ---------------------------:|
|       char              | 1 byte|  	-128 to 127 or 0 to 255   |
|  signed char            | 1 byte|	   -128 to 127              |
|   unsigned char	        |	1 byte|	     0 to 255               |
|     wchar_t		          | 2bytes|	    1 wide character        |



### integer Datatype

| Datatype    |  size   |     range                  |
| ----------: |:-------:|--------------------------: |
|    int      | 4 bytes |  -2147483648 to 2147483647 |
| signed int  | 4 bytes |  -2147483648 to 2147483647 |
|unsigned int | 4 bytes |  -2147483648 to 2147483647 |
|short        | 2 bytes |    -32768 to 32767         |
|signed short | 2 bytes |    -32768 to 32767         |
| long        | 4 bytes |  -2147483648 to 2147483647 |
|signed long  | 4 bytes |  -2147483648 to 2147483647 |
|unsigned long| 4 bytes |  -2147483648 to 2147483647 |




#### Below example will produce the correct size of various data type on your computer.


example:

```
#include <iostream>
using namespace std;

int main() {
 cout << "Size of char is " << sizeof(char) << endl;
 cout << "Size of int is " << sizeof(int) << endl;
 cout << "Size of float is " << sizeof(float) << endl;
 cout << "Size of short int is " << sizeof(short int) << endl;
 cout << "Size of long int is " << sizeof(long int) << endl;
 cout << "Size of double is " << sizeof(double) << endl;
 cout << "Size of wchar_t is " << sizeof(wchar_t) << endl;
 return 0;
}

```

output:

```
Size of char is 1

Size of int is 4

Size of float is 4

Size of short int is 2

Size of long int is 4

Size of double is 8

Size of wchar_t is 4

```


## Enum Datatype

This is a user-defined data type having a finite set of enumeration constants. The keyword 'enum' is used to create an enumerated data type.


##### syntax:

```
enum enum-name {list of names}var-list;

```

```
enum mca(software, internet, seo);

```

## typedef

It is used to create a new data type. But it is commonly used to change the existing data type with another name

##### syntax:

```
typedef [data_type] synonym;

```
example:

```

typedef int integer;
integer rollno;
```
