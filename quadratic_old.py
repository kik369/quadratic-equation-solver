'''
This is the old quadratic equation solver written in Python 2

No Matplotlib graphing yet

The purpose of this repo is to rewrite this program in Python 3
and graph the parabola with Matplotlib
'''

import math #Imports math module

print 'The form of a quadratic equation is ax^2 + bx + c = 0'

a = float(raw_input('a =  ')) #Input prompt
b = float(raw_input('b =  ')) #Input prompt
c = float(raw_input('c =  ')) #Input prompt

print 'Solving %sx^2 + %sx + %s = 0' % (a, b, c)

discriminant = (math.pow(b, 2) - 4*a*c) #Calculate the discriminant

if discriminant > 0:
    print 'Discriminant > 0'
    print 'Discriminant =', discriminant
    print 'Two real solutions!'
    x1 = (- b + math.sqrt(discriminant)) / (2*a)
    x2 = (- b - math.sqrt(discriminant)) / (2*a)
    print 'x1 =', x1
    print 'x2 =', x2

elif discriminant == 0:
    print 'Discriminant =', discriminant
    print 'One real solution!'
    x1 = (- b + math.sqrt(discriminant)) / (2*a)
    print 'x =', x1

else: #Discriminant < 0
    print 'Discriminant < 0'
    print 'Discriminant =', discriminant
    print 'Two complex solutions'

    discriminant = discriminant * (-1)

    imaginary = math.sqrt(discriminant) / (2*a)
    newb = - b / (2*a)
    print 'x1 = %s + %si' % (newb, imaginary)
    print 'x2 = %s - %si' % (newb, imaginary)
