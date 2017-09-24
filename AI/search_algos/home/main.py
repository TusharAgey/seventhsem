import json
from subprocess import call
print "enter number of nodes: "
myInput = {}
myInput['N'] = input()
print myInput
if myInput['N'] > 26:
	print "please enter nodes less than 26"
	exit()
curChar = 'A'
myInput['heuristics'] = []
myInput['edges'] = []
for i in range (myInput['N']):
	tmp = {}
	print "enter heuristic value of " + curChar + " : ",
	tmp[curChar] = input()
	myInput['heuristics'].append(tmp)
	curChar = chr(ord(curChar) + 1)
for i in range (myInput['N']):
	mylist = []
	for j in range (myInput['N']):
		print "enter distance between " + chr(ord('A') + i)+", " + chr(ord('A') + j)+ " : ",
		mylist.append(input())
	myInput['edges'].append(mylist)
option = 'n'
andNodes = []
aDict = {}
while option is "n":
	print "enter values such as B and C are And Nodes with respect to A: ",
	b = str(raw_input())
	c = str(raw_input())
	a = str(raw_input())
	print "stop? n/y:",
	option = str(raw_input())
	aDict[a] = []
	aDict[a].append(b)
	aDict[a].append(c)
myInput['ands'] = aDict
#also input information of and nodes.
with open('./data/input.json', 'w') as fp:
    json.dump(myInput, fp)
#call(["firefox", "index.html"])
call(["python", "bfs.py"])