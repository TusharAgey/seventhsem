len=$(cat temp.txt | wc -l)
for (( i=0; i<$len; i++ ));
do
	cat temp.txt | head -$(( $len - $i )) | tail -1 >> test
done
awk -F'\t' '{print $2 "\t" $1}' test
rm test
