first_number=int(input("Enter first_number:"))
second_number=int(input("Enter second_number:"))
third_number=int(input("Enter third_number:"))
if first_number==second_number and second_number==third_number:print("Answer 3")
if first_number!=second_number and second_number!=third_number:print("Answer 0")
if first_number==second_number or second_number==third_number or first_number==third_number:print("Answer 2")
input()