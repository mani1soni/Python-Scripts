def Func(a):
  if a[0] == 0 and a[1] == 0:
    return 'No'
    
    
  i = 0
  j = 0
  flag = False
  
  while i < len(a)/2:
    while j < len(a)/2:
      if a[i] == 0 and a[i+1] == 0 or a[i] == 0 and a[i+k] == 0: 
        return 'No'
      if len(a) == 0:
        return 'No'
      k = j
      st = a[i:i+k]
      nx = a[i+k+1:i+2*(k+1)]
      if nx - st != 1:
        nx1 = a[i+k+1:i+2*(k+1)+1]
        if nx1 - st != 1:
          j = j+1
        else:
          j = k+1
    
    i = i+1
    
      
  if flag == True:
    return 'Yes ' + str(st)
  return 'No'



a = int(input())
for i in range(a):
  b = raw_input()
  print Func(b)
  print b