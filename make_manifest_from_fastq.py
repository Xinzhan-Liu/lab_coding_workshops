#!/bin/bash
for i in *.L001.fastq.gz;
while read i;
do 
zcat *.L001.fastq.gz | grep -c '+';
done


