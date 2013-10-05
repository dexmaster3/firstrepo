#print positive integers

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

def roundpos(numlist):

	newlist = []
	finallist = []

	for x in numlist:
		if x >= 0:
			newlist.append(x)

	for f in newlist:
		d = f % 1
		f = f - d

		if d >= .5:
			d = 1
		else:
			d = 0
		f += d

		finallist.append(f)
	
	return(finallist)
	
	
if __name__ == "__main__":
	print(roundpos(numbers))
