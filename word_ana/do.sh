#!/bin/bash

i=1  # 這是累計的數值，亦即是 1, 2, 3....
while [ "${i}" != "46" ]
do
	inname="./raw/"${i}".txt"
	outname="./class/"${i}".txt"
	python raw2class.py $inname $outname
	i=$(($i+1))   # 每次 i 都會增加 1 
done

#34365
python fuzzyAddClass.py
