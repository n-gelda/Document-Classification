''' returns a dictionary of the top 100 occuring words '''

def top100 (filePath):

	top100 = dict()
	temp = [] 

	with open('filePath', 'r') as f:
		for line in f:
			temp = line.split()
			top100[temp[0]] = temp[1]

	return top100