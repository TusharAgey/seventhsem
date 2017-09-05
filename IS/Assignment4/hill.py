
def remove_curr_row_col(arr, row, col):
	mat = [] #creating a new matrix
	length = len(arr)
	for i in range(length - 1): #new matrix will have one less row
		mat.append([])
	for i in range(1, length): # remove 1st row(because its always the case)
		for j in range(length):
			if j != col: #the column to be excluded
				mat[i - 1].append(arr[i][j])
	return mat #the new matrix
def findDeterminant(arr, x):
	if len(arr) == 2: #terminating condition
		return (arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0])
	i = 0
	length = len(arr)#degree of matrix
	p = 0#storing the result
	for i in range(length):
		if x == -1: #for changing signs alternatively
			x = 1
		else:
			x = -1
		p += x*arr[0][i]*findDeterminant(remove_curr_row_col(arr, 0, i), -1)
	return p
a = [[1, 2, 3, 4], [1, 0, 2, 0], [0, 1, 2, 3], [2, 3, 0, 0]]
print findDeterminant(a, -1)