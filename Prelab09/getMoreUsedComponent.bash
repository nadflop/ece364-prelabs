#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################
base=~ee364/DataFolder/Prelab09
CircPath=${base}/circuits

circ1=($(grep -l "$1" $CircPath/*.dat | cut -d'_' -f 2 | cut -d'.' -f 1))
circ2=($(grep -l "$2" $CircPath/*.dat | cut -d'_' -f 2 | cut -d'.' -f 1))

if [[ "${#circ1[@]}" > "${#circ2[@]}"  ]]; then echo "$1"; else echo "$2"; fi
