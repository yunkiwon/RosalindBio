#fibonacci sequence with variable offspring and duration 

#let's say that we have a 

print "Number of months?"

terms = input()


print "Pairs / generation?"

breedingRate = input()

	
#Basic fibonacci sequence 


total = 1 
prevTerm = 0 

for i in range(terms-1): 
	temp = total 
	total += prevTerm * breedingRate
	prevTerm = temp 
	
print total 	
	