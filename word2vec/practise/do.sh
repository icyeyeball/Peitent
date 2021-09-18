#!/bin/bash

i=0  # 這是累計的數值，亦即是 1, 2, 3....
while [ "${i}" != "10" ]
do
	inname="./input/wiki_00000"${i}
	outname="./output/wiki_00000"${i}
	python s2zh.py $inname $outname
	i=$(($i+1))   # 每次 i 都會增加 1 

done
while [ "${i}" != "100" ]
do
        inname="./input/wiki_0000"${i}
        outname="./output/wiki_0000"${i}
        python s2zh.py $inname $outname
        i=$(($i+1))   # 每次 i 都會增加 1
done
while [ "${i}" != "1000" ]
do
        inname="./input/wiki_000"${i}
        outname="./output/wiki_000"${i}
        python s2zh.py $inname $outname
        i=$(($i+1))   # 每次 i 都會增加 1
done
while [ "${i}" != "10000" ]
do
        inname="./input/wiki_00"${i}
        outname="./output/wiki_00"${i}
        python s2zh.py $inname $outname
        i=$(($i+1))   # 每次 i 都會增加 1
done
while [ "${i}" != "34366" ]
do
        inname="./input/wiki_0"${i}
        outname="./output/wiki_0"${i}
        python s2zh.py $inname $outname
        i=$(($i+1))   # 每次 i 都會增加 1
done
#34365
