#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################
base=~ee364/DataFolder/Prelab09
ProjPath=${base}/maps/projects.dat
CircPath=${base}/circuits
StudPath=${base}/maps/students.dat

id=$(grep -h "$1" $StudPath | cut -d'|' -f2 | tr -d '[:space:]')

files=($(ls "$CircPath"))

for i in "${files[@]}"
do
    circuit=$CircPath/$i
    grep -l "$id" $circuit | cut -d'_' -f 2 | cut -d'.' -f 1
done
