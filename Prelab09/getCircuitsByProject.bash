#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################

DataPath=~ee364/DataFolder/Prelab09/maps/projects.dat

grep -h "$1" $DataPath | cut -d' ' -f 5 | sort -u
