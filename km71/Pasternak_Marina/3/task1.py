growth=int(input("Enter growth "))
i=0
growth_students_str=input("Enter growth og students ")
growth_students=[]
growth_students=int(growth_students_str.split(' '))
growth_students.append('0')
number =0
while (growth>growth_students[i]):
	number=i+1
	i+=1
print("Number of place", number)
input()