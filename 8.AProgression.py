def AProg(a):
  a = a.split(' ')
  a1 = int(a[0])
  n = int(a[2])
  an = a1 + int(a[1])*(n-1)
  sum = ((a1 + an)*n)/2
  return sum

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(AProg(a)))
x = ' '.join(c)
print x