from stemming.porter2 import stem
from os import listdir
from os.path import isfile, join
from operator import itemgetter
import string
import sys
from subprocess import call
from fractions import Fraction

def findPriorProbability(classs, classDocsMatrix, totalTrainDocs): #function to return prior probability of the class, which is num(docs in this class)/num(total docs)
	#classDocsMatrix = {"class1": [doc1, doc2], "class2": [doc1, doc2]}
	#classs is the class whose prior probability is to be found
	#totalTrainDocs is total number of documents in training set
	thisClassCount = len(classDocsMatrix[classs])
	return float(thisClassCount)/float(totalTrainDocs)

def isFeatureUnavailable(classFeatures, documentFeatures): #returns 1 is all the docFeatures are in the classFeatures, else returns 0
	for elem in documentFeatures:
		if elem not in classFeatures:
			return 0
	return 1

def findClassProbabilityWithFeaturesAvailable(classs, classDocsMatrix, totalTrainDocs, documentFeatures, classFeatures): #returns the probability of document(documentFeatures) of being in class(classs)
	#classs = string: find probability of a document being in this class
	#classDocsMatrix = {}: documents in a class in train dataset
	#totalTrainDocs = num: total number of training documnents across the train dataset
	#documentFeatures[]: Features in this document
	#classFeatures[]: Features in this class
	probability = findPriorProbability(classs, classDocsMatrix, totalTrainDocs)
	for elem in documentFeatures:
		probability *= float(classFeatures.count(elem))/float(len(classFeatures))
	return probability

def findClassProbabilityWithFeaturesUnAvailable(classs, classDocsMatrix, totalTrainDocs, documentFeatures, classFeatures): #doing laplase smoothning
	probability = findPriorProbability(classs, classDocsMatrix, totalTrainDocs) #find prior probability of class
	for elem in documentFeatures:
		try:
			probability *= float(classFeatures.count(elem) + 1)/float(len(classFeatures) + len(classFeatures)) #if the feature is in the Training Dataset
		except Exception as e:
			probability *= float(1)/float(len(classFeatures) + len(classFeatures)) #if the feature is not in Training Dataset
	return probability
def startProcessing(testOrActual):
	#testOrActual if is 0, then takes data from test path else from newsgroup dataset
	table = string.maketrans(string.punctuation+"0123456789", "                                          ")
	TestPath = ""
	TrainPath = ""
	if(testOrActual == 1):
		TestPath = "/Users/tushar/Downloads/naive_bayes/20news-18828/Test/"
		TrainPath = "/Users/tushar/Downloads/naive_bayes/20news-18828/Train/"
	else:
		TestPath = "./naive_docs/Test/"
		TrainPath = "./naive_docs/Train/"
	stopwords = open("./input/stopword.txt", "r").read().split()
	classDocsMatrix = {}
	classFeatures = {}
	totalTrainDocs = 0
	allClasses = [f for f in listdir(TrainPath)] #The training documents in the class are pointed using TrainPath/classes[i]
	if '.DS_Store' in allClasses:
		allClasses.remove('.DS_Store')
	for elem in allClasses:
		classDocsMatrix[elem] = [f for f in listdir(TrainPath + elem)]
		totalTrainDocs += len(classDocsMatrix[elem])

	#building feature list in Training document
	for elem in allClasses:
		classFeatures[elem] = []
		features = []
		new_words = []
		newest_words = []
		filesInElem = [f for f in listdir(TrainPath + elem)]
		for file in filesInElem:
			for word in open(TrainPath + elem + "/" + file).read().translate(table).split(): #for each word
				if word.lower() not in stopwords: #remove stopwords
					new_words.append(word.lower())
			for word in new_words: #do stemming
				newest_words.append(stem(word)) #removed stemmer for a while
			for word in newest_words: #remove stopwords
				if word not in stopwords:
					features.append(word)
			new_words = []
			newest_words = []
		classFeatures[elem] = features
		features = []
		new_words = []
		newest_words = []

	TestDocs = [f for f in listdir(TestPath + "/")]
	finalClassification = {}
	for elem in allClasses:
		finalClassification[elem] = []
	for file in TestDocs: #for each file
		#build the feature list
		#find its probability to fall under certain class
		beingInClassProbability = {}
		documentFeatures = []
		for word in open(TestPath + "/" + file).read().translate(table).split(): #for each word preprocess the document
			if word.lower() not in stopwords: #remove stopwords
					new_words.append(word.lower())
			for word in new_words: #do stemming
				newest_words.append(stem(word)) #removed stemmer for a while
			for word in newest_words: #remove stopwords
				if word not in stopwords:
					documentFeatures.append(word)
			new_words = []
			newest_words = []
		for elem in allClasses:
			if isFeatureUnavailable(classFeatures[elem], documentFeatures) == 1:
				beingInClassProbability[elem] = findClassProbabilityWithFeaturesAvailable(elem, classDocsMatrix, totalTrainDocs, documentFeatures, classFeatures[elem])
			else:
				beingInClassProbability[elem] = findClassProbabilityWithFeaturesUnAvailable(elem, classDocsMatrix, totalTrainDocs, documentFeatures, classFeatures[elem])
		finalProbability = {}
		for elem in allClasses:
			if sum(beingInClassProbability.values()) != 0.0:
				finalProbability[elem] = float(beingInClassProbability[elem])/float(sum(beingInClassProbability.values()))
		if(finalProbability):
			finalClassification[max(finalProbability, key=finalProbability.get) ].append(file)

	print finalClassification
if(len(sys.argv) == 1):
	print "usage: python nb.py caseId"
	exit()

startProcessing(int(sys.argv[1]))