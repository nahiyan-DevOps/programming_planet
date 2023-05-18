# Python data and time


There are various ways Python supplies date and time feature to add to the program. Python's Time and calendar module help in tracking date and time. Also, the 'DateTime' provides classes for controlling date and time in both simple and complex ways.

#### There are two different date and time objects in Python. These are:
1. naive
2. aware


## defining tick

As we all can make an idea that time intervals have to be represented in floating-point numbers. Tick signifies the floating-point numbers in units of seconds in Python. Particular instants of time are represented in seconds from 12:00 am, 1st of January, of the year 1990. A popular module name 'time' is available, which provides functions that let's programmer work with the time and made conversion between time-representation possible.

The pre-defined function time.time() is used to return the current time of the system.


#### example

```
import time;

ticktock = time.time();

print("Number of ticks:", ticktock)

```

output

```
Number of ticks: 1465927104.951356

```


Another program showing datetime module:


```
from datetime import datetime

presentime = datetime.now()

print(" NOW THE TIME IS:", presentime)

print("Todays Date is:", presentime.strftime('%Y-%m-%d') )

print("Year is:", presentime.year)

print("MOnth is:", presentime.month)

print("Day is:", presentime.day)

```

output
```
NOW THE TIME IS: 2016-06-14 18:01:25.831269
Todays Date is: 2016-06-14
Year is: 2016
MOnth is: 6
Day is: 14

```

### Timedelta objects

It is used to represent duration, i.e., the difference between two dates and or times.  For invoking this, the syntax is:

#### Syntax

```
datetime.timedelta([days, [,seconds [,microseconds [,milliseconds [, minutes [,hours [,weeks]]]]]])

```

In the above scenario, all arguments are optional, and their default value is zero (0).


### program to get current times

```
import time;

curtime = time.localtime(time.time())

print("Current Time is:", curtime)

```

output

```
Current Time is: time.struct_time(tm_year=2016, tm_mon=6, tm_mday=14, tm_hour=0, tm_min=4, tm_sec=49, tm_wday=1, tm_yday=166, tm_isdst=0)

```

## calendar of a month

This facility is provided by the "calendar" module, which offers a wide range of methods to deal with monthly calendars. A simple program showing how to use:

#### example
```

import calendar

calndr = calendar.month(2016, 6)

print("The calendar for the month June of Year 2016 is:")

print (calndr)

```

output

```
The calendar for the month June of Year 2016 is:
     June 2016
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30

```
