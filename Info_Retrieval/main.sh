len=$(ls -p $1 | grep -v /  | wc -l) #$1 denotes the directory containing documents to be indexed and searched
#store file_name word_name count
for(( i=1; i<=$len; i++ ))
do
	filen=$( ls -p $1 | grep -v /  | head -$i | tail -1 )
	data=$( cat $filen );
	data=$( echo $data | sed "s/[^[a-z_A-Z]]*/ /g" ) #Remove punctuations, is are the they this that a an am etc
	data=$( echo $data | sed "s/\[/ /g" )
	data=$(echo -e " "$(echo $data)" ")
	after_stemming=''
	for word in ${data[@]}
	do
		word=$(echo "from stemming.porter2 import stem ; print stem('$word')" | python) #apply stemming algorithm using python
		after_stemming=$(echo $after_stemming" "$word)
	done
	for word in ${after_stemming[@]} #pick a word, 
	do
		if [ $( cat "./input/stopword.txt" | grep -i $word | wc -c ) -eq 0 ]; #pick non-stopwords only
		then
			count=$(echo $after_stemming | grep -o "$word" | wc -l) #number of occurances
			echo $after_stemming
			statement=$(echo $filen' '$word' '$count )
			echo $statement >> postfile #saving postfile
		fi
	done	
done
cat postfile | sort -f -u
