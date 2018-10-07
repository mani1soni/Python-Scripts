def BMI(a):
  a = a.split(' ')
  bmi = int(a[0])/(float(a[1])*float(a[1]))
  if bmi < 18.5 :
    return "under"
  elif bmi < 25.0:
    return "normal"
  elif bmi < 30.0:
    return "over"
  else:
    return "obese"

a = int(input())
c = []
for i in range(a):
  b = raw_input()
  count = BMI(b)
  c.append(str(count))
x = ' '.join(c)
print x