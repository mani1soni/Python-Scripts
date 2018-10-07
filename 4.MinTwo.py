def MinTwo(a):
  a = a.split(' ')
  return min(int(a[0]), int(a[1]))

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(MinTwo(a)))
x = ' '.join(c)
print x