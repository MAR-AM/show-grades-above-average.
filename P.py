list=[]
n=int(input('the number of students :'))
for i in range (n):
  b=float(input("enter note :"))
  list.append(b)
M=sum(list)/n
print('grades above average are : ')
for b in list:
  if b>M:
    print(b)
