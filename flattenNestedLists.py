def flatten(l):
	output = []
	for i in l:
		if type(i) is not list:
			output.append(i)
		else:
			output += flatten(i)
	return output


print(flatten([1, 2, [3, [4, 5]]]))
