Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape("turtle")
>>> t.pensize(5)
>>> t.color("red")
>>> t.fillcolor("blue")
>>> t.begin_fill()
>>> t.circle(100)
>>> t.end_fill()
>>> t.penup()
>>> t.goto(-100,300)
>>> t.goto(-200,-300)
>>> t.pendownd()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.pendownd()
AttributeError: 'Turtle' object has no attribute 'pendownd'
>>> t.pendown()
>>> t.color("blue")
>>> t.fillcolor("red")
>>> t.begin_fill()
>>> t.circle(150)
>>> t.end_fill()
>>> t.penup()
>>> t.goto(200,-300)
>>> t.color("yellow")
>>> t.fillcolor("green")
>>> t.pendown()
>>> t.begin_fill()
>>> t.circle(150)
>>> t.end_fill()
>>> 