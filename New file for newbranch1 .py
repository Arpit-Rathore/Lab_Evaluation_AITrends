'''Python Program to make a simple calculator that can add, subtract, multiply and divide'''
import math
input1=float(input("Enter first number as input for calculator: "))
input2=float(input("Enter second number as input for calculator: "))

#Addition
print("Sum of entered numbers: ",input1+input2)

#Substraction
print("Difference of entered numbers: ",abs((input1-input2)))

#Multiplication
print("Product of entered numbers: ",input1*input2)

#Division
print("Quotient when first number divided by second number : ",input1/input2)

#Output
'''
Enter first number as input for calculator: 1
Enter second number as input for calculator: 2
Sum of entered numbers:  3.0
Difference of entered numbers:  1.0
Product of entered numbers:  2.0
Quotient when first number divided by second number :  0.5
'''
