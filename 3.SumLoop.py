def SumLoop(a):
  a = a.split(' ')
  s = 0
  for i in a:
    s = s+int(i)
  return s

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(SumLoop(a)))
x = ' '.join(c)
print x