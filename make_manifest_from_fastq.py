#!/bin/bash
for i in *.fastq.gz;
do 
zcat *.L001.fastq.gz | grep -c '+';
done


