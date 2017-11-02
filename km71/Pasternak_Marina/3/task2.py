i=0
j=0
numbers_str=input("Enter numbers ")
lenth=len(numbers_str)
numbers=[]
numbers=int(numbers_str.split(' '))
pairs_count =0
for i in range (1,lenth): 
	for j in range (1,lenth): 
		if(numbers[i]==numbers[j] and i!=j):
			pairs_count+=1
print("Count of equal numbers",pairs_count)
input()
