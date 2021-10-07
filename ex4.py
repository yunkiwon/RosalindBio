from sys import argv 

script, number1, number2 = argv

number1 = int(number1)
number2 = int(number2)

total = 0 

for i in range(number1, number2): 
	if i%2 == 1: 
		total += i


print total 