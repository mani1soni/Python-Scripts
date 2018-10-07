import math

def Average(a):
  sum = 0
  count = 0
  for i in a:
    sum = sum + int(i)
  #return reduce(lambda x, y: int(x) + int(y), a) / len(a)
  for i in a:
    if int(i) != 0:
      count = count + 1
  return int(round(sum/(float(count))))
  
n = int(input())
c = []
i = 0
while (i < n):
  a = raw_input()
  a = a.split(' ')
  c.append(str(Average(a)))
  i = i + 1
x = ' '.join(c)
print x