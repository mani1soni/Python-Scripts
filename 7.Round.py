import math

def Rr(a):
  a = a.split(' ')
  return int(round(float(a[0])/int(a[1])))

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(Rr(a)))
x = ' '.join(c)
print x