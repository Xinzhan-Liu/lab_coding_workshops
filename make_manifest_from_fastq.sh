#!/bin/bash
ls *.fastq.gz
while read i;
do echo "$i";
zcat $i | grep -c '+';
done




for i in *.fastq.gz;
do 
zcat *.L001.fastq.gz | grep -c '+';
done

