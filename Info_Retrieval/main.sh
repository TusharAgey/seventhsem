len=$(ls -p $1 | grep -v /  | wc -l) #$1 denotes the directory containing documents to be indexed and searched
#store file_name word_name count
for(( i=1; i<=$len; i++ ))
do
	filen=$( ls -p $1 | grep -v /  | head -$i | tail -1 )
	data=$( cat $1/$filen )
	data=$( echo $data | sed "s/[^[a-z_A-Z]]*/ /g" ) #Remove punctuations, is are the they this that a an am etc
	data=$( echo $data | sed "s/\[/ /g" )
	data=$(echo -e " "$(echo $data)" ")
	after_stemming=' '
	after_stemming=$(echo "from stemming.porter2 import stem; a = ''; wordlist='$data'.split(); exec(\"for word in wordlist: \n \t a += ' '; \n \t a += stem(word)  \nprint a\")" | python)
	for word in ${after_stemming[@]} #pick a word, 
	do
		if [ $( cat "./input/stopword.txt" | grep -i $word | wc -c ) -eq 0 ]; #pick non-stopwords only
		then
			count=$(echo -e "  "$after_stemming"  " | grep -o " $word " | wc -l) #number of occurances
			word=$(echo $word)
			statement=$(echo $filen' '$word' '$count )
			echo $statement >> postfile #saving postfile
		fi
	done	
done
cat postfile | sort -f -u > postfile2
rm postfile
mv postfile2 postfile
data=$(cat postfile | awk '{print $2}' | sort -f -u) #get all the unique list of words
for word in $data;
do
        lines=$(cat postfile | grep " $word ")
        len=$(echo $word | wc -c)
        len=$(( 20 - $len ))
        echo -n $word' : ' >> inverted_index.txt
        for (( i=0;i<len;i++ ))
        do
        	echo -n ' ' >> inverted_index.txt
        done
        len=$(echo -e $lines | wc -l)
        for(( i=1; i<=$len; i++ ))
        do
                line=$(echo $lines | head -$i | tail -1 )
                filename=$(echo $line | awk '{print $1}')
                count=$(echo $line | awk '{print $3}')
                echo -n '( '$filename', '$count' )' >> inverted_index.txt
        done
        echo '' >> inverted_index.txt
        #now lines is each line data
        #now, for each such line, do processing
        #That means, put generate the inverted index.
done