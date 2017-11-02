min = int(input("Enter minutes: "))
days = min//1440
hours = (min - days*1440)//60
min = min - (days*1440 + hours*60)
print("Ответ: ", hours, ":", min )
input()