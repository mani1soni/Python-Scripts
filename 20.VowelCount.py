def VowelCount(a):
  vow = ['a', 'o', 'u', 'i', 'e', 'y']
  count = 0
  i = 0
  while (i < len(a)):
    if a[i] in vow:
      count = count + 1
    i = i + 1
  return count

a = int(input())
c = []
for i in range(a):
  b = raw_input().lower()
  count = VowelCount(b)
  c.append(str(count))
x = ' '.join(c)
print x