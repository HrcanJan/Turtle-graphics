def polylinel(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polyliner(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)
def polygon(t, r, angle, d):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4)
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    if(d=='l'):
        polylinel(t, n, step_length, step_angle)
    if(d=='r'):
        polyliner(t, n, step_length, step_angle)
    t.rt(step_angle/2)
def circle(t, r, n, p, k):
    for i in range (1,p+1):
        polygon(t, r, 360.0/p, 'l')
        t.lt(180-360/p)
        polygon(t, r, 360.0/p, 'l')
        t.setheading(0)
        t.lt(i*(360.0/p)+k)
def stem(bob, n, r, k, k1, p, x, y):
    for i in range(0,n+1,x):
        l=2*r*3.14
        bob.fd((l/n)*k)
        bob.lt(360.0/n)
    bob.setheading(y)
    for i in range (2):
        polygon(bob, r, 360.0/p, 'l')
        bob.lt(180-360/p)
    bob.setheading(180-y)
    for i in range (2):
        polygon(bob, r, 360.0/p, 'r')
        bob.rt(180-360/p)


import turtle
import math
bob = turtle.Turtle()
bob.speed(0)
r=300.0
n=100
p=20
k=0
circle(bob, r, n, p, k)
bob.setheading(0)
y=45
bob.lt(240)
k=1
k1=1
x=6
stem(bob, n, r, k, k1, p, x, y)

bob.pu()
bob.setposition(360,0)
bob.setheading(0)
bob.pd()
r=100.0
n=100
p=6
k=0
circle(bob,r, n, p, k)
k=30
bob.lt(k)
circle(bob,r, n, p, k)
bob.setheading(0)
y=15
bob.lt(225)
k=2
k1=1
x=4
stem(bob, n, r, k, k1, p, x, y)

bob.pu()
bob.setposition(-360,0)
bob.setheading(0)
bob.pd()
p=7
r=100.0
n=100
k=0
circle(bob, r, n, p, k)
bob.setheading(0)
y=0
bob.lt(210)
k=2
k1=2
x=3
stem(bob, n, r, k, k1, p, x, y)
