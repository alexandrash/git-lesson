a = [1, 2, 3, 8, 14, 89, 45]
n=len(a)
m=n-1
while m>0:
 for i in range(m):
  if (a[i]>a[i+1]):
      a[i], a[i + 1] = a[i + 1], a[i]
 m=m-1
print(a)