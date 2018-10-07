a = raw_input()
a = a.split(' ')

min = int(a[0])
max = int(a[0])
for i in a:
  if int(i) < min:
    min = int(i)
  if int(i) > max:
    max = int(i)
c = []
c.append(str(max))
c.append(str(min))
x = ' '.join(c)
print x