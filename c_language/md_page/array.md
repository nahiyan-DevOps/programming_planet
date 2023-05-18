# C Array

The array is a data structure in C programming, which can store a fixed-size sequential collection of elements of the same data type.

For example, if you want to store ten numbers, it is easier to define an array of 10 lengths, instead of defining ten variables.
In the C programming language, an array can be:
1. **One-Dimensional**
2. **Two-Dimensional**
3. **Multidimensional**


## Define an Array in C

syntex:

```
type arrayName [ size ];

```
This is called a one-dimensional array. An array type can be any valid C data types, and array size must be an integer constant greater than zero.

#### example:

```
double amount[5];

```


## Initialize an array in C

Arrays can be initialized at declaration time:

```
int age[5]={22,25,30,32,35};

```

Initializing each element separately in a loop:

```
int myArray[5];
int n = 0;

// Initializing elements of array seperately
for(n=0;n<sizeof(myArray)/sizeof(myArray[0]);n++)
{
  myArray[n] = n;
}

```


## A Pictorial Representation of the Array:

![alt text](https://www.w3schools.in/wp-content/uploads/2014/07/One-Dimensional-array.jpg?ezimgfmt=rs:466x99/rscb7/ng:webp/ngcb7)


### Accession Array element in C

example:

```
int myArray[5];
int n = 0;

// Initializing elements of array seperately
for(n=0;n<sizeof(myArray)/sizeof(myArray[0]);n++)
{
  myArray[n] = n;
}

int a = myArray[3]; // Assigning 3rd element of array value to integer 'a'.

```
