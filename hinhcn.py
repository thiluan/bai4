Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> t.pensize(5)
>>> t.shape("fish")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.shape("fish")
  File "C:\Users\ACER\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named fish
>>> t.shape("pen")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.shape("pen")
  File "C:\Users\ACER\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named pen
>>> t.shape("turtle")
>>> t.color("red")
>>> t.fillcolor("grey")
>>> t.begin_fill()
>>> t.forward(150)
>>> t.left(90)
>>> t.forward(150)
>>> t.forward(150)
>>> t.left(90)
>>> t.forward(150)
>>> t.left(90)
>>> t.forward(300)
>>> t.end_fill()
>>> 