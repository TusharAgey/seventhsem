import json
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
def bfs(input):
	visited = []
	start = 'A' #considering A as start node always & element with 0 heuristic as goal node
	{"edges": [[0, 3, 4, -1, -1], [-1, 0, 5, 6, 7], [-1, -1, 0, 1, 2], [-1, -1, -1, 0, 1], [-1, -1, -1, -1, 0]]}
	for elem in input['heuristics']:
		for data in elem:
			if elem[data] == 0:
				goal = data
	finalPath = []
	finalPath.append(start)
	queue = MyQUEUE()
	queue.enqueue(start)
	while q.IsEmpty() == False:
		pass

js=open('./data/input.json')
data=json.load(js)
finalPath = {"path" : []}
finalPath['path'] = bfs(data)
with open('./data/BFS.json', 'w') as fp:
    json.dump(finalPath, fp)