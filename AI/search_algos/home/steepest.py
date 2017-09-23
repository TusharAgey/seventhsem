import json
def getSmallestNeighbours(nextElem, arrOfArr, visited, heuristic):
	elems = []
	i = ord(nextElem) - ord('A')
	x = 0
	p = 0
	smallest = max(heuristic)
	for j in arrOfArr[i]:
		if j > 0:
			if smallest > heuristic[x]:
				smallest = heuristic[x]
				p = x
		x += 1
	data = chr(p + ord('A'))
	if data not in visited:
		return data
	return -1
def bfs(input):
	visited = []
	heuristicVals = []
	for elem in input['heuristics']:
		heuristicVals.append(elem.values()[0])
	start = 'A' #considering A as start node always & element with 0 heuristic as goal node
	#{"edges": [[0, 3, 4, -1, -1], [-1, 0, 5, 6, 7], [-1, -1, 0, 1, 2], [-1, -1, -1, 0, 1], [-1, -1, -1, -1, 0]]}
	for elem in input['heuristics']:
		for data in elem:
			if elem[data] == 0:
				goal = data
	finalPath = []
	finalPath.append(start)
	neighbours = []
	curr = start
	while goal not in finalPath:
		curr = getSmallestNeighbours(curr, input['edges'], finalPath, heuristicVals)
		if(curr == -1):
			break
		finalPath.append(curr)
	print finalPath
	return finalPath
js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
finalPath['path'] = bfs(data)
with open('./data/SAHC.json', 'w') as fp:
    json.dump(finalPath, fp)