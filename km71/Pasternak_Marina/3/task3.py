liste=input("Enter list ")
new_list=""
number=0
for i in range (1,len(liste)):
	if liste[i] in liste:
		number+=1
	if number<0
		new_list+=liste[i]
print("Elements that occur once", new_list)
input()
