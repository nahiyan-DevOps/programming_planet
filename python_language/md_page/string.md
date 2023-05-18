# python string

A string is usually a bit of text in programming that is written to be displayed to users. It is known to Python when you want to display a string. This is because programmers use either double quote " or single quote ' to enclose a word or group of words to express a string.

#### example

```
ch = 'HelloPython'

str1 = "String Chapter"

```

## Accessing string values

Characters are not supported by Python, which makes it simpler as characters in Python are treated as strings of length one and hence considered as a sub-string.
The program is showing the use of strings and how they are displayed on-screen.


#### example:

```
ch = 'Hello Python'

str1 = "String Chapter"

print ("First value is: " ,  ch)

print ("Second value is: " ,  str1)


```

output

```
First value is: Hello Python
Second value is: String Chapter

```

If they are considered as a list of characters, then the example shown below will let you understand how they are treated individually:

```
ch = "Hello Python"

str1 = "String Chapter"

print ("First single sub-string is: " ,  ch[0])

print ("Set of sub-string is: " ,  str1[2:5])
```

output

```
First single sub-string is: H
Set of sub-string is: rin
```

### Updating string values

Reassigning the existing string-variable is more straightforward in Python. We have to use + operator along with the sub-string location. Let's show this as an example:

```
ch = "Hello Python"

print ("UPDATED STRING WILL BE: " , ch [:8]+ "Python")

```

output

```
UPDATED STRING WILL BE: Hello PyPython

```


### escape characters

These are special characters represented by a backslash followed by the character(s), and they are used for particular purposes. They can be interpreted using both single and double-quotes. The lists of Escape Characters in Python are:


1. \a: alert
2. \b: backspace
3. \cx: Control X
4. \e: escape
5. \f: Form feed
6. \n: Newline or next line
7. \r: carriage return
8. \s: space
9. \t: tab
10. \v: Vertical Tab
