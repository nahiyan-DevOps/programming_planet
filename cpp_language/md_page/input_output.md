# C++ Basic input/output

In every program, there is some data which is taken as input and generate the processed data as output following the input > process > output cycle. Therefore it is essential to know how to provide data as input and how to present the output in the desired form. C++ supports a rich set of I/O functions and operations to do this. As these functions use the advanced features of C++, programmers need to know a lot about them before implementing them in any program. It is to be noted that C++ supports all of C's rich sets of I/O functions. Programmers can use any of them within a C++ program. In this chapter, you will learn about how to manage the input/output capabilities of a C++ program


### The input/output in C++

C does not have built-in input/output facilities. Instead, it left the I/O to the compiler as external library functions (such as printf and scanf) in stdio (standard input-output) library. The ANSI C standard formalized these IO functions into Standard IO package (stdio.h). Likewise, C++ continues this approach and formalizes IO in iostream and fstream libraries


### features of I/O in C++

1. C++ IO is type safe.
2. C++ IO operations are based on streams of bytes and are device independent.


### stream in C++

C++ IO is based on streams, which are a sequence of bytes flowing in and out of the programs (just like water and oil flowing through a pipe). I/O systems in C++ are designed to work with a wide variety of devices including terminals, disks and tape drives. The input-output system supplies an interface to the programmer that is independent of the actual device being accessed. This interface is known as a stream. A stream is a sequence of bytes which acts either as a source from which input data can be obtained or as a destination to which output data can be sent. The source stream which provides data to the program is called the input stream and the destination stream which receives output from the program is called the output stream.


##### Follow the steps below to perform input and output:

1. Construct a stream object.
2. Connect (Associate) the stream object to an actual IO device
3. Perform input/output operations on the stream, via the functions defined in the stream's public interface in a device-independent manner.
4. Disconnect (Dissociate) the stream to the actual IO device (e.g., close the file).
5. Free the stream object.


### Unformatted input/output operations


You have already used the cin and cout (pre-defined in the iostream file) for input and output of data of various types. This has been made possible by overloading the operators << and >> to recognize all the basic C++ types


1. cin standard input stream
2. cout standard output stream

##### example

```
#include <iostream>
using namespace std;

void main()
  {
    int g;
    cin>>g;
    cout << "Output is: "<< g;
  }

```



### put() and get() functions

The classes istream and ostream defines two member functions get() and put() respectively to handle single character input/output operations.


##### Get() function is of two types:

1. get(char *)
2. get(void)


Both of them can be used to fetch a character including blank space, tab or new-line character


### Code snippet

```
char ch;
cin.get(ch);
 while(ch != '\n')
  {
    cout<<ch;
    cin.get(ch);
  }

```

Similarly, the function put(), a member of a stream class can be used to output a line of text character by character.

##### example:

```
cout.put ('g');
char ch;
cout.put(ch);

```



## getline() and write()

You can read and display lines of text more efficiently using the lie oriented input/output functions. They are:

1. getline()
2. write()


The getline() function reads the entire line of texts that ends with a newline character. The general form of getline() is:

```
cin.getline (line, size);

```

The write() function displays the entire line of text, and the general form of writing this function is:

```
cout.write (line, size);

```
