def SumLoop(a):
  a = a.split(' ')
  print a
  s = 0
  for i in a:
    s = s+int(i)
  return s

b = input()
a = raw_input()
print SumLoop(a)