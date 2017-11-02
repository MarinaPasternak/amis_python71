first_number=input("Enter first_number:")
second_number=input("Enter second_number:")
third_number=input("Enter third_number:")
answer=0
if int(first_number) < int(second_number):
	answer=int(first_number)
else:
    answer=int(second_number)
if int(answer) > int(third_number):
    answer=int(third_number)
print('Minimum is:', answer)
input()
