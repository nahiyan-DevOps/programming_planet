
# python function

Using a 'def' statement for defining a function is the corner store of a majority of programs in Python. To group a set of statements, programmers use functions, and they can be run more than once in a program. They act like a pack of instructions that is invoked by a name.

## what are the function in python?

In simple words, Python functions are techniques used to combine a set of statements within a program. Functions also let programmers compute a result-value and give parameters that serve as function inputs that may change each time the code runs. Functions prove to be a useful tool when the operations are coded in it and can be used in a variety of scenarios.
Functions are an alternative method of cutting-and-pasting codes rather than typing redundant copies of the same instruction or operation, which further reduces the future work for programmers. They are the most basic structure of a program, and so Python provides this technique for code re-use.

Let's make a program using a function to make the average of any quantity of numbers.



#### example

```
def avrg(first, *rests):
    return (first + sum(rests)) / (1 + len(rests))

# Sample use, Putting values

print (avrg(1, 2))
print (avrg(1, 2, 3))
print (avrg(1,2,3,4))

```
 output

 ```
 1.5
2.0
2.5

 ```

The keyword 'def' introduces a function definition. The statements that form the body of the function starts from the next line of function definition and needs indentation. The execution of the function introduces a new symbol table that is used for the function's local variable. In other words, all the variables that are assigned to the function store their value in the local symbol table. So global variables cannot be assigned with a value within a function; unless it is named under 'global' statement. To accept any number of keyword arguments, the arguments have to start with *. A * argument can appear only in the last position of function's argument. A fine concept of a function definition is that arguments can still appear after the * argument.


#### example
```
def g(a, *arg, b):

```
Such arguments are known as a keyword-only argument


## python program for calculate fibonacci series by using function


example

```
def fibo(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# Show the first 13 Fibonacci numbers.
for c in range(0, 13):
    print(fibo(c)) #Function call

```

output

```
0
1
1
2
3
5
8
13
21
34
55
89
144

```

If you compare with other programming languages, you might notice that 'fibo' is not a function, rather it's a procedure that is a function that doesn't return a value. It has to be kept in mind that every function without a return statement does return a value which is called 'none'; which usually gets suppressed by the interpreter


## calling function

Functions can be called in different ways.

1. Providing the mandatory argument only
2. Providing one of the optional argument
3. By giving all the arguments


### function related statement


1. Call Expression: myfun ('karl', 'os', *rest)
2. def : def display(message):
print ('Hi' +  message)
3. return : def sum(a, b=2)
return a+b
4. global : x = 'hello'
def printer():
global x; x='hi'
5. nonlocal : def outer():
a = 'old'
 def inner():
nonlocal a; a = 'new'
6. yield : def sq(k)
for I in range(k): yield i**2



## advantage of python function

1. Maximizing code reusability
2. Minimizing redundancy
3. Procedural decomposition
4. Make programs simpler to read and understand


### Python program that return multiple values from functions

To return multiple values, we can use normal values or return a tuple

#### example
```
def karlos():
    return 1, 2, 3

a, b, c = karlos()

print (a)
print (b)
print (c)

```

outer

```
1
2
3


```
