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

def fix_negatives(arr):#given a array, this returns an array which is fixing negatives by MOD 26
	length = len(arr)
	for i in range(length):
		for j in range(length):
			if arr[i][j] < 0: #just for the negative number
				p = 0
				while p < abs(arr[i][j]):
					p = p + 26
				arr[i][j] = p + arr[i][j]
	return arr

def findAdjoint(arr): #returns a adjoinct of a NxN matrix
	length = len(arr) #order of the matrix
	for i in range(2): #adding extra rows
		arr.append(arr[i])
	for i in range(length):
		for j in range(2): #adding extra columns
			arr[i].append(arr[i][j])
	mat = []
	length += 2
	for i in range(length - 1):
		mat.append([])
	for i in range(1, length): #remove first row
		for j in range(1, length): #remove first column	
			mat[i-1].append(arr[i][j])
	length -= 2
	adj = []
	for i in range(length): #creating adjoinct matrix
		adj.append([])
	for i in range(length):
		for j in range(length):
				adj[i].append(mat[j][i]*mat[j+1][i+1] - mat[j][i+1]*mat[j+1][i])
	return adj
def findModularMultiplicativeInverse(val):
	i = 0
	p = 0
	for i in range(3000): #checking at least for 3000 times
		p = p + 26
		if((p + 1) % val == 0) :
			return (p + 1)/val
	return -1
def giveKInverse(arr): #given a matrix, this method returns a modular multiplicative inverse of it
	det = findDeterminant(arr, -1) #get determinant
	adj = findAdjoint(arr)	#find adjoint
	fix_negatives(adj)	#fix negatives if any in adjoint matrix
	if det < 0:	#if determinant is negative, then find its modular subtractive inverse
		p = 0
		while p < abs(det):
			p = p + 26
		det = p + det
	detInverse = findModularMultiplicativeInverse(det) #finding modular multiplicative inverse of the determinant
	if(detInverse == -1): #solution is not possible
		return -1
	length = len(adj)
	for i in range(length):
		for j in range(length):
			adj[i][j] = (adj[i][j] * detInverse) % 26
	return adj
def mapToNormal(key):
	if(ord(key) < 91): #capital letters
		return (ord(key) - ord('A'))
	else: #small letters
		return (ord(key) - ord('a'))
def notInMatrix(mat):#return next unavailable element in mat in range of 0 to 25
	data = 0
	i = 0
	while data < 26:
		if data in mat[i]:
			data += 1
			i = 0
		else:
			i += 1
		if i == len(mat):
			break;
	return data

def createK(key, N): #builds the matrix from given string "key" with matrix order N
	mat = []
	index = 0
	for i in range(N):
		mat.append([])
	for i in range(N): #prepare a key matrix from fiven key
		for j in range(N):
			if(index < len(key)):
				if(key[index] == ' '): #Bug: Responsible -> Tushar, won't work if key contains more than 1 spaces
					index += 1
				mat[i].append(mapToNormal(key[index]))
			if index >= len(key): #if the key is finished
				mat[i].append(notInMatrix(mat))
			index += 1
	return mat
def multiplyNNandNOne(mat, data, N): #multiplies N x N matrix with N X 1 matrix & result is returned back as a list
	ret = []
	tmp = 0
	for i in range(N):
		for j in range(N):
			tmp += mat[i][j] * data[j]
		ret.append((tmp) % 26)
		tmp = 0
	return ret
def main():
	print "1)Encrypt\n2)Decrypt"
	option = input()
	if option == 1:
		#get key and matrix length
		print "Enter the key: ",
		key = str(raw_input())
		print "Enter matrix order (less then or equal to 5)"
		N = input()
		if(N >= 5):
			print "Please enter key below less than or equal to 5"
			return 1
		#create matrix
		mat = createK(key, N)
		if(giveKInverse(mat) == -1):
			print "Solution with this key is not possible. Please change the key. Stopping.."
			return 1
		#get file
		print "Enter input file name"
		file_name = raw_input()
		file = open(str(file_name), "r")
		data = file.read()
		file.close()
		j = 0
		p = N
		#divide input into matrix_length X 1 matrix
		for i in range(len(data) / N): #Bug: responsible-> Tushar (if input data is not divisible by N, some data < N size won't be processed by this logic)
			data_of_N_Size = []
			New_Data = []
			while(j < p):
				data_of_N_Size.append(data[j])
				j += 1
			for elements in data_of_N_Size:
				New_Data.append(mapToNormal(elements))
			cipher = multiplyNNandNOne(mat, New_Data, N)
			for i in range(len(cipher)):
				print chr(cipher[i] + ord('A')),
			p = p + N
		#done
	elif option == 2:
		#get key and matrix length
		print "Enter the key: ",
		key = str(raw_input())
		print "Enter matrix order (less then or equal to 5)"
		N = input()
		if(N >= 5):
			print "Please enter key below less than or equal to 5"
			return 1
		#create matrix
		mat = createK(key, N)
		mat = giveKInverse(mat)
		#get file
		print "Enter input file name"
		file_name = raw_input()
		file = open(str(file_name), "r")
		data = file.read()
		file.close()
		p = N
		j = 0
		#divide input into matrix_length X 1 matrix
		for i in range(len(data) / N): #Bug: responsible-> Tushar (if input data is not divisible by N, some data < N size won't be processed by this logic)
			data_of_N_Size = []
			New_Data = []
			while(j < p):
				data_of_N_Size.append(data[j])
				j += 1
			for elements in data_of_N_Size:
				New_Data.append(mapToNormal(elements))
			cipher = multiplyNNandNOne(mat, New_Data, N)
			for i in range(len(cipher)):
				print chr(cipher[i] + ord('A')),
			p = p + N
		#done
	else:
		print "Please enter a valid option"
if __name__ == '__main__':
	main()
