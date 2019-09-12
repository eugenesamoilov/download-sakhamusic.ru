#!/bin/bash
for (( i=1; i <= 7000; i++ ))
do
wget -t 2 -nc --content-disposition http://sakhamusic.ru/download/$i
done
