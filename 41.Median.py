def Med(a):
  a = a.split(' ')
  i = 0
  while i < len(a):
    a[i] = int(a[i])
    i+=1
  a.sort()
  return int(a[1])

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(Med(a)))
x = ' '.join(c)
print x