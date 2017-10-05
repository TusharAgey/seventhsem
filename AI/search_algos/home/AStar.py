import json
def findChildrensAndGiveMyDistances(elem, opened, eh): #finds childrens and returns distances & add childrens to opened
	elemList = eh[ord(elem) - ord('A')]
	i = 0
	dictRet = []
	for el in elemList: #for OR of the nodes
		elist = []
		try:
			elist = andNodes[elem]
		except Exception as e:
			elist = []
		if (i is not ord(elem) - ord('A')) and (el is not -1) and (chr(i + ord('A')) not in elist):
			dictRet.append([chr(i + ord('A')), eh[ord(elem) - ord('A')][i] + eh[ord(elem) - ord('A')][ord(elem) - ord('A')]])
			opened.append(chr(i + ord('A')))
		i += 1
	return dictRet, opened

def updateMyHeuristics(myDictionary, N, eh, goal): #updates distances using childrens 
	N = N - 1
	while N is not -1:
		i = 0
		elem = chr(ord('A') + N)
		childrens = []
		for data in eh[N]:
			if data is not -1 and N is not i:
				childrens.append(chr(ord('A') + i))
			i += 1
		flag = True
		if elem in myDictionary and len(childrens) is not 0: #the element is in dictionary
			for data in childrens:	#all its childrens are in dictionary
				if data not in myDictionary:
					flag = False
					break
			if flag: #True
				i = 0
				for eachData in myDictionary[elem]:
					sum = 0
					anotherMin = []
					if goal in eachData:
						myDictionary[goal] = [['F', 0]]
					if(len(eachData) == 2): #eachData is a OR node
						for newData in myDictionary[eachData[0]]:
							anotherMin.append(newData[len(newData) - 1])
						myDictionary[elem][i][1] = min(anotherMin) + eh[ord(elem) - ord('A')][ord(eachData[0]) - ord('A')]
					else: #eachData is an AND node
						sum = 0
						for j in range(len(eachData) - 1):
							anotherMin = []
							for newData in myDictionary[eachData[j]]:
								anotherMin.append(newData[len(newData) - 1])
							sum += min(anotherMin) + eh[ord(elem) - ord('A')][ord(eachData[j]) - ord('A')]
						myDictionary[elem][i][len(eachData) - 1] = sum
					i += 1
		N -=1
	return myDictionary

def AStar(eh, N):
	opened = []
	closed = []
	nextOpened = []
	hm = []
	myDictionary = {}
	start = 'A'
	goal = chr((len(eh) - 1) + ord('A'))
	print goal
	opened.append(start)
	nextOpened = opened
	x = 0
	while x is not 10:
		for elem in opened:
			myDictionary[elem], hm = findChildrensAndGiveMyDistances(elem, nextOpened, eh)
			opened.remove(elem)
			for eachNextChild in hm:
				if eachNextChild not in nextOpened and eachNextChild not in closed:
					nextOpened.append(eachNextChild)
			closed.append(elem) #the elem is processed. Hence close it
		opened = nextOpened
		print nextOpened
		nextOpened = []
		for elem in closed:
			flag = True
			i = 0
			childrens = []
			for data in eh[ord(elem) - ord('A')]:
				if data is not -1 and ord(elem) - ord('A') is not i:
					childrens.append(chr(ord('A') + i))
				i += 1
			for data in childrens: #if all my childrens are either in myDictionary, i.e. processed:
				if data not in myDictionary:
					flag = False
					break
			if flag:
				myDictionary = updateMyHeuristics(myDictionary, N, eh, goal)
		x += 1
				#print myDictionary
				#break
	#printing the path from start to goal node!
	print myDictionary
	finalPath = []
	finalPath.append(start)
	while goal not in finalPath:
		previous = finalPath[len(finalPath) - 1]
		minimum = previous
		minVal = 1000000
		for elem in myDictionary[previous]:
			if minVal > elem[len(elem) - 1]:
				minVal = elem[len(elem) - 1]
				minimum = elem[0]
		if minimum not in finalPath:
			finalPath.append(minimum)
	return finalPath

js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
heuristicVals = []
for elem in data['heuristics']:
	heuristicVals.append(elem.values()[0])
eh = data['edges']
i = 0

finalPath['path'] = AStar(eh, data['N'])
print finalPath['path']
with open('./data/AStar.json', 'w') as fp:
    json.dump(finalPath, fp)