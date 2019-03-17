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

files=($(ls "$CircPath"))
circ=()

for i in "${files[@]}"
do
    circuit=$CircPath/$i
    circ+=($(grep -l "$1" $circuit | cut -d'_' -f 2 | cut -d'.' -f 1))
done

echo "${#circ[@]}"
