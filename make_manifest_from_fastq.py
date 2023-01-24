#!/bin/bash
ls *.fastq.gz
for file in *.fastq.gz;
do echo "$file";
zcat "$file" | grep -c '+';
done


