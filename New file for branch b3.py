'''Python Program to Solve the quadratic equation ax**2 + bx + c = 0'''

import cmath
a=float(input("Enter value of first coeffient of quadratic equation (a) : "))
b=float(input("Enter value of second coeffient of quadratic equation (b) : "))
c=float(input("Enter value of third coeffient of quadratic equation (c) : "))

x1= (-b+cmath.sqrt(b**b-4*a*c))/(2*a)
x2= (-b-cmath.sqrt(b**b-4*a*c))/(2*a)

print("Values of x in quadratic equation for entered coefficients are: ",x1," and ",x2)

#Output
'''
Enter value of first coeffient of quadratic equation (a) : 1
Enter value of second coeffient of quadratic equation (b) : 1
Enter value of third coeffient of quadratic equation (c) : 1
Values of x in quadratic equation for entered coefficients are:  (-0.5+0.8660254037844386j)  and  (-0.5-0.8660254037844386j)'''
