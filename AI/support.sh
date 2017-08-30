#!/bin/bash
len=$(cat temp.txt | wc -l)
j=0
for i in `seq 1 $len`;
do
    d=`expr $len - $j`
    j=`expr $j + 1`
	cat temp.txt | head -$d | tail -1 >> test
done
awk -F'\t' '{print $2 "\t" $1}' test
rm test
