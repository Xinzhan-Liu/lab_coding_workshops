#!/bin/bash
read 
ls *.L001.fastq.gz|
while read i;
do echo "$i";
zcat $i | grep -c '+';
done


