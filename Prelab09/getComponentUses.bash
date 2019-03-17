#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################
base=~ee364/DataFolder/Prelab09
CircPath=${base}/circuits

circ=($(grep -l "$1" $CircPath/*.dat | cut -d'_' -f 2 | cut -d'.' -f 1))
echo "${#circ[@]}"
