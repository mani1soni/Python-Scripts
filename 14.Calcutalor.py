n = int(input())
while True:
  a = raw_input()
  a = a.split(' ')
  if(a[0] == '+'):
    n = n + int(a[1])
  if(a[0] == '*'):
    n = n * int(a[1])
  if(a[0] == '%'):
    n = n % int(a[1])
    break
print n