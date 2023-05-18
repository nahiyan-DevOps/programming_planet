# python overview

Python is a general-purpose, object-oriented programming language with high-level programming capabilities. It has become famous because of its apparent and easily understandable syntax, portability, and easy to learn.

Python is a programming language that includes features of C and Java. It provides the style of writing an elegant code like C, and for object-oriented programming, it offers classes and objects like Java.
In Python, the program to add two numbers will be as follows:

```

#program to add two numbers in python
a = b = 20 #declare two variables and store 20 into them
print (a+b) #final output

```

output:
```
40

```

## some facts about Python

1. Python was developed in the late eighties, i.e., the late 1980's by Guido van Rossum at the National Research Institute for Mathematics and Computer Science in the Netherlands as a successor of ABC language capable of exception handling and interfacing.
2. Python is derived from programming languages such as ABC, Modula 3, small talk, Algol-68.
3. Van Rossum picked the name Python for the new language from a TV show, Monty Python's Flying Circus.
4. Python page is a file with a .py extension that contains could be the combination of HTML Tags and Python scripts.
5. In December 1989, the creator developed the 1st python interpreter as a hobby, and then on 16 October 2000, Python 2.0 was released with many new features.
6. On 3rd December 2008, Python 3.0 was released with more testing and included new features.
7. Python is an open-source scripting language.
8. Python is open-source, which means that anyone can download it freely from www.python.org and use it to develop programs. Its source code can be accessed and modified as required in the project.
9. Python is one of the official languages at Google



## Characteristics and features of python

Python is gaining good popularity in the programming community; there are many reasons behind this.
1. **Interpreted Language**: Python is processed at runtime by Python Interpreter.
2. **Object-Oriented Language**: It supports object-oriented features and techniques of programming.
3. **Interactive Programming Language**: Users can interact with the python interpreter directly for writing programs.
4. **Easy language**: Python is easy to learn, especially for beginners.
5. **Straightforward Syntax**: The formation of python syntax is simple and straightforward, which also makes it popular.
6. **Easy to read**: Python source-code is clearly defined and visible to the eyes.
7. **Portable**: Python codes can be run on a wide variety of hardware platforms having the same interface.
8. **Extendable**: Users can add low level-modules to Python interpreter.
9. **Scalable**: Python provides an improved structure for supporting large programs then shell-scripts.



### What can we do with python


Python is used to create web and desktop applications, and some of the most popular web applications like Instagram, YouTube, Spotify all have been developed in Python. You can also develop the next big thing by using Python



# Basic of python Programming

Python is an interpreted programming language. Python source code is compiled to bytecode as a .pyc file, and this bytecode can be interpreted


#### There are two modes for using the Python interpreter:

1. Interactive Mode
2. Script Mode

## Interactive mode

Without passing the python script file to the interpreter, directly execute code to Python prompt

#### example:

```
>>>2+6

```
output:
```
8
```

![alt text] (https://www.w3schools.in/wp-content/uploads/2016/05/python-Interactive-mode.png?ezimgfmt=rs:580x139/rscb7/ng:webp/ngcb7)


The chevron at the beginning of the 1st line, i.e., the symbol >>> is a prompt the python interpreter uses to indicate that it is ready. If the programmer types 2+6, the interpreter replies 8.



## script mode

Alternatively, programmers can store Python script source code in a file with the .py extension, and use the interpreter to execute the contents of the file. To execute the script by the interpreter, you have to tell the interpreter the name of the file. For example, if you have a script name MyFile.py and you're working on Unix, to run the script you have to type:


```
python MyFile.py

```
Working with the interactive mode is better when Python programmers deal with small pieces of code as you can type and execute them immediately, but when the code is more than 2-4 lines, using the script for coding can help to modify and use the code in future.


### single line comment

A single-line comment begins with a hash (#) symbol and is useful in mentioning that the whole line should be considered as a comment until the end of the line.


```
#Defining a variable to store number.
n = 50 #Store 50 as value into variable n.
```

1. In the above example program, the first line starts with the hash symbol, so the entire line is considered a comment.
2. In the second line of code, "N = 50" is a statement, and after the statement, the comment begins with the # symbol. From the # symbol to the end of this line, the line will be treated as a comment.


### Docstrings

Triple double coat (""") and single coat (''') are actually docstrings, which are also used as comments. The key usage of docstrings is explained in the Python API Documentation chapter, and we will learn more about it in the further chapters.

### Multi line comments

Multi-line comment is useful when we need to comment on many lines. You can also use a single-line comment, but using a multi-line instead of single-line comment is easy to comment on multiple lines.

In Python Triple double quote (""") and single quote (''') are used for Multi-line commenting. It is used at the beginning and end of the block to comment on the entire block. Hence it is also called block comments.


```
"""
Author: www.w3schools.in
Description:
Writes the words Hello World on the screen
"""

```
