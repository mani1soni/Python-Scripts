def MinThree(a):
  a = a.split(' ')
  return min(int(a[0]), int(a[1]), int(a[2]))

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(MinThree(a)))
x = ' '.join(c)
print x