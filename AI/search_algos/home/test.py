import math
def AStar(start, goal, eh, heuristics):
	opened = [] #make an openlist containing only the starting node
	opened.append([start, 1000]) #considering 1000 as the infinity, data structure: [[elem1, f-score1], [elem2, f-score2]]
	closed = [] #make an empty closed list
	finalPath = []
	while goal not in closed:
			 #consider the node with the lowest f score in the open list
			max = opened[0][1]
			for elem in opened:
				if max > elem[1]:
					bestNode = elem[0]
					max = elem[1]
					break
			if (bestNode is goal) :
				return finalPath
			else:
				finalPath.append(bestNode)
				closed.append(bestNode)#put the current node in the closed list and look at all of its neighbors
				i = 0
				neighbors = []
				for elem in eh[ord(bestNode) - ord('A')]:
					if elem is not -1 and elem is not 0:
						neighbor.append(chr(ord('A') + i))
					i += 1
				for neighbour in neighbours:
					if (neighbor has lower g value than current and is in the closed list) :
						replace the neighbor with the new, lower, g value 
						current node is now the neighbor ka parent            
					elif (current g value is lower and this neighbor is in the open list ) :
						replace the neighbor with the new, lower, g value 
						change the neighbor ka parent to our current node
					elif neighbor not in opened and neighbor not in closed:
						opened.append([neighbour, eh[ord(bestNode) - ord('A')][ord(neighbour) - ord('A')] + heuristics[ord(neighbour) - ord('A')]])
AStar('A', 'E', eh, heuristicVals)