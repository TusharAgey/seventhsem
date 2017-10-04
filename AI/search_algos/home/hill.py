import json
def hill_climb(start_node, eh, N, heuristics):
	current_node = start_node
	finalPath = []
	i = 0
	for i in range(len(eh)): #for each node
		j = 0
		for children in eh[ord(current_node) - ord('A')]:
			if current_node not in finalPath:
				finalPath.append(current_node)
			if children is not 0 and children is not -1 and heuristics[j] < heuristics[ord(current_node) - ord('A')]:
				current_node = chr(j + ord('A'))
				break
			j += 1
		i += 1
	return finalPath

js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
heuristicVals = []
for elem in data['heuristics']:
	heuristicVals.append(elem.values()[0])
finalPath['path'] = hill_climb('A', data['edges'], data['N'], heuristicVals)
with open('./data/SHC.json', 'w') as fp:
    json.dump(finalPath, fp)