def IsTriangle(a):
  a = a.split(' ')
  b = int(a[0])
  c = int(a[1])
  d = int(a[2])
  if b > c+d:
    return 0;
  elif c > b+d:
    return 0;
  elif d > b+c:
    return 0;
  else:
    return 1;

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(str(IsTriangle(a)))
x = ' '.join(c)
print x