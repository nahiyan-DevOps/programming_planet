# C Pointers

A pointer is a variable in C, and the pointers value is the address of a memory location.

## Pointer definition in C

syntex:
```
type *variable_name;

```

example:

```
int  *width;
char  *letter;

```


## Benefits of using pointers in C

1. Pointers allow the passing of arrays and strings to functions more efficiently.
2. Pointers make it possible to return more than one value from the function.
3. Pointers reduce the length and complexity of a program.
4. Pointers increase the processing speed.
5. Pointers save the memory.



### How to use pointer in C

example:
```
#include<stdio.h>

int main ()
{
   int  n = 20, *pntr;  //actual and pointer variable declaration

   pntr = &n;  //store address of n in pointer variable

   printf("Address of n variable: %x\n", &n  );

   //address stored in pointer variable
   printf("Address stored in pntr variable: %x\n", pntr );

   //access the value using the pointer
   printf("Value of *pntr variable: %d\n", *pntr );

   return 0;
}

```



output:

```
Address of n variable: 2cb60f04
Address stored in pntr variable: 2cb60f04
Value of *pntr variable: 20

```




## C memory management

C language provides many functions that come in header files to deal with the allocation and management of memories. In this tutorial, you will find brief information about managing memory in your program using some functions and their respective header files.

## Management of Memory

Almost all computer languages can handle system memory. All the variables used in your program occupies a precise memory space along with the program itself, which needs some memory for storing itself (i.e., its own program). Therefore, managing memory utmost care is one of the major tasks a programmer must keep in mind while writing codes.
When a variable gets assigned in a memory in one program, that memory location cannot be used by another variable or another program. So, C language gives us a technique of allocating memory to different variables and programs.


#### There are two types used for allocating memory. These are:

1. static memory allocations
2. Dynamic memory allocations


### Static memory allocations


In the static memory allocation technique, allocation of memory is done at compilation time, and it stays the same throughout the entire run of your program. Neither any changes will be there in the amount of memory nor any change in the location of memory


### Dynamic memory allocation

In dynamic memory allocation technique, allocation of memory is done at the time of running the program, and it also has the facility to increase/decrease the memory quantity allocated and can also release or free the memory as and when not required or used. Reallocation of memory can also be done when required. So, it is more advantageous, and memory can be managed efficiently
