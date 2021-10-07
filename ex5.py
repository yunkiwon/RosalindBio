f = open('rosalind_ini5.txt', 'r')
lineData = f.readlines()
f.close()

n = open('output.txt', 'w')

for i in range(1, len(lineData), 2): 
	n.write(lineData[i] + '\n')
n.close()	
	
n = open('output.txt', 'r')
n.read()
n.close()