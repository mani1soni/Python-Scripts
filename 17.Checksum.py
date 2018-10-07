def Checksum(a):
  result = 0
  i = 0
  seed = 113
  limit = 10000007
  a = a.split(' ')
  while i < len(a):
    result = (result + int(a[i])) * seed
    if result > limit:
      result = result % limit
    i = i + 1
  return result
  
  
b = input()
c = []
a = raw_input()
print Checksum(a)