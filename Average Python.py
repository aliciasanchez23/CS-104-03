Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> print ("Hello World")
Hello World
>>> a="Hello"
>>> b="World"
>>> a
'Hello'
>>> ab
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ab
NameError: name 'ab' is not defined
>>> a="Goobdye"
>>> print(a+b)
GoobdyeWorld
>>> a="Goodbye"
>>> print (a+b)
GoodbyeWorld
>>> b=" World"
>>> print (a+b)
Goodbye World
>>> a="abc123#$"
>>> print (a)
abc123#$
>>> print ("abc")
abc
>>> type (a)
<class 'str'>
>>> a=1
>>> print (1)
1
>>> type (a)
<class 'int'>
>>> b=2
>>> print (a+b)
3
>>> a=2.5
>>> type (a)
<class 'float'>
>>> 
>>> 
>>> a=True
>>> a=False
>>> type (a)
<class 'bool'>
>>> <class 'bool'>
SyntaxError: invalid syntax
>>> not a
True
>>> or a
SyntaxError: invalid syntax
>>> not a
True
>>> a=True
>>> not a
False
>>> type (a)
<class 'bool'>
>>> a=2.0
>>> type (a)
<class 'float'>
>>> a= (int)
>>> a= int (a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a= int (a)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'type'
>>> a=int(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a=int(a)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'type'
>>> a=2.0
>>> a=int (a)
>>> type (a)
<class 'int'>
>>> print (a)
2
>>> a=2.5
>>> a=int (a)
>>> print (a)
2
>>> a="1"
>>> b="2"
>>> print(a+b)
12
>>> print (int(a)+b)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print (int(a)+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 20
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Traceback (most recent call last):
  File "/Users/aliciaortiz/Documents/CS-104-03 First Python.py", line 1, in <module>
    numberOfScores, score, total, average, scoreCount = 0
TypeError: cannot unpack non-iterable int object
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Traceback (most recent call last):
  File "/Users/aliciaortiz/Documents/CS-104-03 First Python.py", line 4, in <module>
    average
NameError: name 'average' is not defined
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 50
Please enter a test score: 50
Please enter a test score: 50
Traceback (most recent call last):
  File "/Users/aliciaortiz/Documents/CS-104-03 First Python.py", line 10, in <module>
    average = (score1+score2) / 2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 50
Please enter a test score: 50
Please enter a test score: 50
Traceback (most recent call last):
  File "/Users/aliciaortiz/Documents/CS-104-03 First Python.py", line 10, in <module>
    average = (score1+score2)/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 2
Please enter a test score: 50
Please enter a test score: 50
(score1+score2) / 2
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 2
Please enter a test score: 50
Please enter a test score: 50
(score1 + score2) / 2
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 
	50
Please enter a test score: Please enter a test score: 
(intscore1 + intscore2) / 2
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 2
Please enter a test score: 50
Please enter a test score: 30
(int(score1) + int(score2) / 2
>>> 
============== RESTART: /Users/aliciaortiz/Documents/CS-104-03 First Python.py =============
Please enter the number of scores you want to average: 2
Please enter a test score: 90
Please enter a test score: 91
90.5
>>> 