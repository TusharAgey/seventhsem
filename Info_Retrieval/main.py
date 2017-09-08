from stemming.porter2 import stem
from os import listdir
from os.path import isfile, join
from operator import itemgetter
import string
import sys
table = string.maketrans(string.punctuation+"0123456789", "                                          ")
if len(sys.argv) != 2:
	print "Usage: python main.py input_directory"
	exit()

files = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))] #get files
words = []
new_words = []
newest_words = []
inverted_index = {}
unique_word_list = []
stopwords = open("./input/stopword.txt", "r").read().split()
for file in files: #for each file do
	for word in open(sys.argv[1]+'/'+file).read().translate(table).split(): #for each word
		if word.lower() not in stopwords: #remove stopwords
			new_words.append(word.lower())
	for word in new_words: #do stemming
		newest_words.append(stem(word))
	new_words = []
	for word in newest_words: #remove stopwords
		if word not in stopwords:
			new_words.append(word)
	newest_words = []
	for word in new_words:
		if word not in unique_word_list:
			unique_word_list.append(word)
			try:
				data = inverted_index[word] #if the word is already available\
				inverted_index[word].append([file, new_words.count(word)])
			except Exception as e:
				inverted_index[word] = []
				inverted_index[word].append([file, new_words.count(word)])
	unique_word_list = []
	new_words = []
flag = 0 #adding entries of files with 0 count of words
tf_index_on_disk = inverted_index
for file in files:
	for word in tf_index_on_disk:
			for element in tf_index_on_disk[word]:
				if file in element:
					flag = 1
					break
			if flag == 0:
				tf_index_on_disk[word].append([file, 0])
			flag = 0
x = 0
new_index = {}
for i in sorted(inverted_index):
	print i,
	d = 10 - len(i)
	while x < d:
		print "",
		x = x + 1
	x = 0
	new_index[i] = sorted(inverted_index[i], key=itemgetter(0))
	print sorted(inverted_index[i], key=itemgetter(1), reverse=True)
write_file = open("./input/tf_modelDemo", "w")
write_file.write(str(new_index))
write_file.close()