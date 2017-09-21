from stemming.porter2 import stem
from os import listdir
from os.path import isfile, join
from operator import itemgetter
import string
import sys
from subprocess import call
def measurePerformance(actualresults):
	directory = [f for f in listdir("/Users/tushar/Downloads/naive_bayes/expected/")]
	if '.DS_Store' in directory:
		directory.remove('.DS_Store')
	expectedresults = {}
	for elem in directory:
		expectedresults[elem] = [f for f in listdir("/Users/tushar/Downloads/naive_bayes/expected/" + elem + "/")]
	print actualresults
	#expectedresults = {'cs':['doc6'], 'bio':['doc5']}
	#actualresults = {'cs':['doc6'], 'bio':['doc5']}
	TP = 0
	for classs in expectedresults: #iterate over the class:
		#if expected document is in this class:
		for i in range(len(expectedresults[classs])):
			if expectedresults[classs][i] in actualresults[classs]:
				TP += 1
	precesionDiv = 0
	for elem in actualresults:
		precesionDiv += len(actualresults[elem])
	if precesionDiv is 0:
		print "couldn't classify any\n"
		return
	recallDiv = 0
	for elem in expectedresults:
		recallDiv += len(expectedresults[elem])
	precision = float(TP)/float(precesionDiv)
	recall = float(TP)/float(recallDiv)
	print "precision is: ",
	print precision
	print "\nRecall is: ",
	print recall
	print "\nF-measure is: ",
	print float(2 * precision * recall) / float(precision + recall)
	#find precision
	#find recall
	#find f-measure
table = string.maketrans(string.punctuation+"0123456789", "                                          ")
#read the folder naive_docs
#read all the directories inside, if the directory is train, then explore this directory
#we will find the classes as the folders
'''
TestPath = "./naive_docs/Test/"
TrainPath = "./naive_docs/Train/"
'''
TestPath = "/Users/tushar/Downloads/naive_bayes/20news-18828/Test/"
TrainPath = "/Users/tushar/Downloads/naive_bayes/20news-18828/Train/"

stopwords = open("./input/stopword.txt", "r").read().split()
classes = [f for f in listdir(TrainPath)] #The training documents in the class are pointed using TrainPath/classes[i]
if '.DS_Store' in classes:
	classes.remove('.DS_Store')
totalFiles = 0
mapfileandclass = {}
for elem in classes:
	files = [f for f in listdir(TrainPath + elem)]#get files
	totalFiles += len(files)
	mapfileandclass[elem] = []

priorProbability = {}
for elem in classes:
	priorProbability[elem] = float(len([f for f in listdir(TrainPath + elem)]))/float(totalFiles)

elementProbability = {}  #the structure:  class: [[elementi, probabilityi], [elementi+1, probabilityi+1]]
for elem in classes:
	elementProbability[elem] = []
	features = []
	new_words = []
	newest_words = []
	filesInElem = files = [f for f in listdir(TrainPath + elem)]
	for file in filesInElem:
		for word in open(TrainPath + elem + "/" + file).read().translate(table).split(): #for each word
			if word.lower() not in stopwords: #remove stopwords
				new_words.append(word.lower())
		for word in new_words: #do stemming
			newest_words.append(stem(word))
		for word in newest_words: #remove stopwords
			if word not in stopwords:
				features.append(word)
		new_words = []
		newest_words = []
	for word in set(features):
		elementProbability[elem].append([word, float(features.count(word))/float(len(features))])
	features = []
	new_words = []
	newest_words = []
#print elementProbability
#now we have both, the class probability as well as the elements probability.
#jsut apply the naive bayes rule now

files = [f for f in listdir(TestPath + "/")]
for file in files:
	newdictionary = {}
	flag = 0
	for word in open(TestPath + "/" + file).read().translate(table).split(): #for each word preprocess the document
		if word.lower() not in stopwords: #remove stopwords
				new_words.append(word.lower())
		for word in new_words: #do stemming
			newest_words.append(stem(word))
		for word in newest_words: #remove stopwords
			if word not in stopwords:
				features.append(word)
		new_words = []
		newest_words = []
	for elem in classes: #now for each possible set of class
		newdictionary[elem] = priorProbability[elem] #newdictionary of this class #its element = prior probability of class multiplied by
		for word in features: #for each word in this document
			for data in elementProbability[elem]:
				if word in data:
					flag = 1
					newdictionary[elem] *= data[1]
			if(flag == 0):
				newdictionary[elem] = 0
			flag = 0
				
			#its probability for this class
	newestdictionary = {}
	for elem in newdictionary:
		if(sum(newdictionary.values()) != 0):
			newestdictionary[elem] = newdictionary[elem]/sum(newdictionary.values())
		else:
			newestdictionary[elem] = 0
	features = []
	if(max(newdictionary.values()) != 0):
		putinthisclass = max(newestdictionary, key=newestdictionary.get) 
		#call(["mv", TestPath + "/" + file, TrainPath + "/" + putinthisclass]) #call this to do actual classification in real example
		mapfileandclass[putinthisclass].append(file)
measurePerformance(mapfileandclass)