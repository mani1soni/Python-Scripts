def WSum(a):
  sum = 0
  i = 0
  while i < len(a):
    b = i+1
    count = int(a[i])*b
    sum = sum + count
    #print a[i], b, count, sum
    i+= 1
  return str(sum)

b = input()
c = []
a = raw_input()
a = a.split(' ')
for i in a:
  c.append(str(WSum(str(i))))
x = ' '.join(c)
print x