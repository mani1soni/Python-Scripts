def ArrayCount(a, b):
  a = a.split(' ')
  c = []
  i = 1
  while (i <= b):
    count = 0
    for j in a:
      if int(j) == i:
        count = count + 1
    c.append(str(count))
    i = i + 1
  x = ' '.join(c)
  return x

a = raw_input()
a = a.split(' ')
b = raw_input()
x = ArrayCount(b, int(a[1]))
print x