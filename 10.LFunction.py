def LFunction(a):
  a = a.split(' ')
  x1 = int(a[0])
  y1 = int(a[1])
  x2 = int(a[2])
  y2 = int(a[3])
  k = (y2-y1)/(x2-x1)
  b = (y1*x2 - x1*y2)/(x2 - x1)
  res = '(' + str(k) + ' ' + str(b) + ')'
  return res

a = int(input())
c = []
for i in range(a):
  b = raw_input()
  c.append(LFunction(b))
x = ' '.join(c)
print x