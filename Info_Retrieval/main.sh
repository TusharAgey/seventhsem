rm output.txt
timeit=$(date "+%Y-%m-%d-%H:%M:%S") #unique milestone for this search
len=$(ls -p $1 | grep -v /  | wc -l) #$1 denotes the directory containing documents to be indexed and searched
#Database table header	time_it	file_name	unique_word	count_it //time is to milestone the run
for(( i=1; i<=$len; i++ ))
do
	filen=$( ls -p $1 | grep -v /  | head -$i | tail -1 )
	data=$( cat $filen );
	data=$( echo $data | sed "s/[^[a-z_A-Z]]*/ /g" ) #Remove punctuations, is are the they this that a an am etc
	data=$( echo $data | sed "s/\[/ /g" )
	data=$(echo -e " "$(echo $data)" ")
	for thing in ${data[@]} #pick a word, 
	do
		oldthings=$thing #preserving the original document word
		thing=$(echo "from stemming.porter2 import stem ; print stem('$thing')" | python) #apply stemming algorithm using python
		if [ $( cat "./input/stopword.txt" | grep -i $thing | wc -c ) -eq 0 ]; #pick non-stopwords only
		then
			count=$(grep -o " $thing " <<< "$data" | wc -l) #number of occurances
			statement="insert into word_count(time_it, file_name, unique_word, count_it) values ('$timeit', '$filen', '$thing', $count );" #preparing sql statements
			echo $statement >> tmp.sql #saving sql statements
		fi
	done	
done
#run sql on Database
cat tmp.sql | sort -f -u > tmp2.sql
mysql ir_assignment_1 -uroot -hlocalhost -p < tmp2.sql
#done running sql
rm tmp.sql
rm tmp2.sql
#/Applications/Firefox.app/Contents/MacOS/firefox localhost/mysite/IR/Assignment1 & #invoke query processor ui
words=$(echo "select distinct unique_word from word_count;" |mysql -sN ir_assignment_1 -uroot -hlocalhost -pqwerty1@)
for word in $words;
do
	data=$(echo "select file_name, count_it from word_count where unique_word = '$word'" | mysql -sN ir_assignment_1 -uroot -hlocalhost -pqwerty1@)
	echo $word >> output.txt
	echo '['$data']' >> output.txt
done
