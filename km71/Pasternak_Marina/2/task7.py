i1=int(input("Line number of the first cell "))
j1=int(input("Column number of the first cell "))
i2=int(input("Line number of the second cell "))
j2=int(input("Column number of the second cell "))
if i2==i1+2  or j2==j1+2:
	print("YES")
else:
	print("NO")
input()