#!/usr/bin/python3
'''
Divisibility checking without modulo operator.
'''

def reminder(num,divisor):
    return (num - divisor * (num // divisor))
num = int(input("Enter number for divisibility test: "))
divisor = int(input("give any number: "))

result = reminder(num,divisor)
number = str(num)
if result == 0:
    print ("This number is divided by "+number)
else:
    print ("Not divided by "+number)

