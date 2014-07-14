from random import randint

number=range(1,46)
luck=[]
while(len(luck)<6):
	ran=randint(1,45)
	if luck.count(ran)==0:
		luck.append(ran)
print luck