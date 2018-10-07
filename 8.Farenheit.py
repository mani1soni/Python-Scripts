import math

def Celcium(a):
  return int(round(float(a)*9/5)+32)

def Farenheit(a):
  return int(round((float(a) - 32)*5/9))

a = raw_input()
a = a.split(' ')
c = []
i = 1
while (i < len(a)):
  c.append(str(Farenheit(a[i])))
  i = i + 1
x = ' '.join(c)
print x