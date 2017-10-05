import json
import copy
def getChildrens(elem, eh):
	childrens = []
	i = 0
	for data in eh[ord(elem) - ord('A')]:
		if data is not -1 and data is not 0:
			childrens.append(chr(i + ord('A')))
		i += 1
	return childrens
def AStar(eh, N, heuristics, start, goal):
	opened = []
	closed = []
	finalPath = []
	opened.append([[start], heuristics[ord(start) - ord('A')]])
	finalPath.append(start)
	while goal not in finalPath:
		#get next processable element
		max = 1000 #considering 1000 as infinity
		i = 0
		j = 0
		for element in opened:
			if max > element[1]:
				max = element[1]
				nextBest = element[0][len(element[0]) - 1] #last node of the best list
				finalPath = element[0]
				j = i
			i += 1
		childrens = getChildrens(nextBest, eh)
		#i is the index of the best children
		myElem = []
		hell = []
		for elem in opened[j][0]:
			hell.append(elem)
		myElem = [hell, opened[j][1]]

		for child in childrens:
			cpy = []
			print myElem
			for x in myElem:
				cpy.append(x)
			#print myElem
			#cpy[1] = cpy[1] + heuristics[ord(child) - ord('A')] + eh[ord(cpy[0][len(cpy[0]) - 1]) - ord('A')][ord(child) - ord('A')]
			cpy[0].append(child)
			#print cpy
			opened.append(cpy)
		break
		#print opened
		#nextBest is the element to be processed further
		#get childrens of element in opened.
	#print opened
	return finalPath
js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
heuristicVals = []
for elem in data['heuristics']:
	heuristicVals.append(elem.values()[0])
eh = data['edges']
i = 0
finalPath['path'] = AStar(eh, data['N'], heuristicVals, 'A', 'E')
print finalPath['path']
with open('./data/A.json', 'w') as fp:
    json.dump(finalPath, fp)