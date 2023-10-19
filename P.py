list=[]
n=int(input('the number of students :'))
for i in range (n):
  b=int(input("enter note :"))
  list.append(b)
for j in range(0, n):
      min = list[j]
      for i in range(j, n):
          if min > list[i]:
              min = list[i]
              list[i] = list[j]
              list[j] = min
print(list)