def DRand(a):
  res = 1 + int(float(a)*6)

  return str(res)
  
b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(DRand(str(a)))
x = ' '.join(c)
print x