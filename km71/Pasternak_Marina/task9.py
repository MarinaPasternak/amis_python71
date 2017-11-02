i1=int(input("Line number of the first cell "))
j1=int(input("Column number of the first сell "))
i2=int(input("Line number of the second cell "))
j2=int(input("Column number of the second cell "))
if (i2==i1+1 and j2==j1+1) or (i2==i1-1 and j2==j1-1):
	print("YES")
else:
	print("NO")
input()