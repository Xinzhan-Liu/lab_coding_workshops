#!/bin/bash
for i in *.L001.fastq.gz;
do 
zcat *.L001.fastq.gz | grep -c '+';
done


