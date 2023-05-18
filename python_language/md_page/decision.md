# python decision making

Decisions in a program are used when the program has conditional choices to execute a code block. Let's take an example of traffic lights, where different colors of lights lit up in different situations based on the conditions of the road or any specific rule.

It is the prediction of conditions that occur while executing a program to specify actions. Multiple expressions get evaluated with an outcome of either TRUE or FALSE. These are logical decisions, and Python also provides decision-making statements that to make decisions within a program for an application based on the user requirement.



![alt text](https://www.w3schools.in/wp-content/uploads/2014/07/c-if.png?ezimgfmt=rs:270x330/rscb7/ng:webp/ngcb7)

#### example

```
a = 15

if a > 10:
   print("a is greater")

```

output
```
a is greater
```



# python Loops

In programming, loops are a sequence of instructions that does a specific set of instructions or tasks based on some conditions and continue the tasks until it reaches certain conditions.

It is seen that in programming, sometimes we need to write a set of instructions repeatedly - which is a tedious task, and the processing also takes time. So in programming, we use iteration technique to repeat the same or similar type of tasks based on the specified condition.
Statements are executed sequentially, but there sometimes occur such cases where programmers need to execute a block of code several times. The control structures of programming languages allow us to execute a statement or block of statements repeatedly.


## for loops

example
```
for x in range (0,3) :
    print ('Loop execution %d' % (x))

```

output
```
Loop execution 0
Loop execution 1
Loop execution 2

```

example

```
for letter in 'TutorialsCloud':
   print ('Current letter is:', letter)

```

output

```
Current letter is : T
Current letter is : u
Current letter is : t
Current letter is : o
Current letter is : r
Current letter is : i
Current letter is : a
Current letter is : l
Current letter is : s
Current letter is : C
Current letter is : l
Current letter is : o
Current letter is : u
Current letter is : d

```

## while Loops


example

```
#initialize count variable to 1
count =1

while count < 6 :
    print (count)
    count+=1
#the above line means count = count + 1

```
output

```
1
2
3
4
5

```


## nested loop

example

```
for g in range(1, 6):
    for k in range(1, 3):
        print ("%d * %d = %d" % ( g, k, g*k))

```

output
```
1 * 1 = 1
1 * 2 = 2
2 * 1 = 2
2 * 2 = 4
3 * 1 = 3
3 * 2 = 6
4 * 1 = 4
4 * 2 = 8
5 * 1 = 5
5 * 2 = 10

```



## break statement

example

```
count = 0

while count <= 100: print (count) count += 1 if count >= 3:
      break

```
output

```
0
1
2

```


## continue statement

example
```
for x in range(10):
   #check whether x is even
   if x % 2 == 0:
      continue
   print (x)

```

output

```
1
3
5
7
9

```


## pass statement

example
```
for letter in 'TutorialsCloud':
   if letter == 'C':
      pass
      print ('Pass block')
   print ('Current letter is:', letter)

```

output

```
Current letter is : T
Current letter is : u
Current letter is : t
Current letter is : o
Current letter is : r
Current letter is : i
Current letter is : a
Current letter is : l
Current letter is : s
Pass block
Current letter is : C
Current letter is : l
Current letter is : o
Current letter is : u
Current letter is : d

```
