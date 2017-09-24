import json
def giveSmallestNeighbour(elem, heuristics, edges, and_node_info, closed, opened):#look at all the neighbours of elements in opened list and find neighbour with least f(x) = h(x) + g(x)
	#remove the elements common to and_node_info and my neighbours from the my_neighbours list

	#and substitute it with their combined Element
	#then find f(x) = h(x) + g(x)
def aoStar(input):
	visited = []
	heuristicVals = []
	for elem in input['heuristics']:
		heuristicVals.append(elem.values()[0])
	for elem in input['heuristics']:
		for data in elem:
			if elem[data] == 0:
				goal = data
	start = 'A' #considering A as start node always & element with 0 heuristic as goal node
	finalPath = []
	finalPath.append(start)#get the start node.
	opened = []
	closed = []
	curr = start
	opened.append(start)#add the current node to opened list
	while goal not in finalPath:
		curr,closed,opened = giveSmallestNeighbour(curr, heuristicVals, input['edges'], input['ands'], closed, opened)
		finalPath.append(curr)#Add the selected one to finalPath list
js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
finalPath['path'] = aoStar(data)
with open('./data/AO.json', 'w') as fp:
    json.dump(finalPath, fp)