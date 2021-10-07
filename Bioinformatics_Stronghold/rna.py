#Replacing T with U in RNA sequence 

f = open("rosalind_rna.txt", "r")
dnaString = f.read() 
rnaString = ""

for nucleotide in dnaString: 
	if nucleotide == "T": 
		rnaString += "U" 
	else: 
		rnaString += nucleotide
		
print rnaString