import json
from string import ascii_uppercase
from itertools import permutations
class MyQUEUE: # just an implementation of a queue
	def __init__(self):
		self.elements = []		
	def enqueue(self,val):
		self.elements.append(val)		
	def dequeue(self):
		val = None
		try:
			val = self.elements[0]
			if len(self.elements) == 1:
				self.elements = []
			else:
				self.elements = self.elements[1:]	
		except:
			pass
		return val	
	def IsEmpty(self):
		result = False
		if len(self.elements) == 0:
			result = True
		return result
def getNeighbours(nextElem, arrOfArr, visited):
	elems = []
	i = ord(nextElem) - ord('B')
	x = 0
	for j in arrOfArr[i]:
		if j > 0:
			data = chr(x + ord('B'))
			if data not in visited:
				elems.append(data)
			x +=1
	return elems

def bfs(input):
	count = 0
	visited = []
	start = 'B' 
	finalPath = []
	finalPath.append(start)
	queue = MyQUEUE()
	queue.enqueue(start)
	neighbours = []
	while queue.IsEmpty() == False:
		nextElem = queue.dequeue()
		if nextElem not in finalPath:
			finalPath.append(nextElem)
		neighbours = getNeighbours(nextElem, input['edges'], finalPath)
		for elem in neighbours:
			queue.enqueue(elem)		
		count = count + 1;
		if count == 2:
			break		
	return finalPath
def same(expectedPath, actualPath): #finding if expectedPath and actualPath are same or not
	i = 0
	if len(expectedPath) is not len(actualPath):
		return False
	for i in range(len(expectedPath)):
		if expectedPath[i] is not actualPath[i]:
			return False
	return True

def generateASolution(eh, elem, myList):
	i = 0
	while i < (len(myList) - 1): #creating only valid set of paths
		src = myList[i]
		dest = myList[i + 1]
		if eh[src][dest] is -1 or eh[src][dest] is 0:
			otherData = list(myList)
			otherData.pop(dest)
			myList = tuple(otherData)
		i += 1
	returnableList = []
	for data in myList:
		returnableList.append(elem[data])
	return returnableList

def generateAndTest(eh, elem):
	expectedPath = ['A', 'C', 'E']
	i = 0
	l = list(permutations(range(0, len(elem))))
	actualPath = generateASolution(eh, elem, l[i])
	i += 1
	while (not same(expectedPath, actualPath)) and i < len(l):
		actualPath = generateASolution(eh, elem, l[i])
		print actualPath
		i += 1
	return actualPath

js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
ELE = []
for c in ascii_uppercase: 
	if ord(c) < (data['N'] + ord('A')):
		ELE.append(c);
finalPath['path'] = generateAndTest(data['edges'], ELE) #passing the element list
with open('./data/BLA.json', 'w') as fp:
    json.dump(finalPath, fp)
    print "final Path is:"
    print finalPath
