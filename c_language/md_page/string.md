# C String

In C programming, the one-dimensional array of characters are called strings, which is terminated by a null character '\0'.


## String declaration in C

There are two ways to declare a string in C programming:

##### example
Through an array of characters.
```
char name[6];

```
Through pointers.
```
char *name;

```

## String Initialization in C

example:

```
char name[6] = {'C', 'l', 'o', 'u', 'd', '\0'};

```

or

```
char name[] = "Cloud";

```

### Memory Representation of above defined string in C

![alt text] (https://www.w3schools.in/wp-content/uploads/2014/07/c-strings.jpg?ezimgfmt=rs:320x99/rscb7/ng:webp/ngcb7)

example:
```
#include<stdio.h>

int main ()
{
   char name[6] = {'C', 'l', 'o', 'u', 'd', '\0'};

   printf("Tutorials%s\n", name );

   return 0;
}

```

output:

```
TutorialsCloud

```
