f = open('rosalind_ini6.txt', 'r')
lineData = f.read()


ans = {}

formatted = lineData.split()

for i in formatted: 
	if i in ans: 
		ans[i] +=  1 
	else: 
		ans[i] = 1
		

formattedSol = ""

for i in ans: 
	word = i 
	frequency = ans[i]
	print word, frequency

f.close()
