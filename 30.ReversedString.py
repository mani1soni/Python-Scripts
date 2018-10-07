def Reverse(a):
  return ''.join(reversed(a))

b = raw_input()
b = b.split(' ')
c = []
for i in b:
  c.append(Reverse(i))
x = ' '.join(reversed(c))
print x