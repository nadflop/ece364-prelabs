#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################
DataPath=~ee364/DataFolder/Prelab09
ProjPath=${DataPath}/maps/projects.dat
CircPath=${DataPath}/circuits
StudPath=${DataPath}/maps/students.dat

#result=($(grep -h "$1" $ProjPath | cut -d' ' -f 5 | sort -u))
#length=${#result[@]}
#temp=()

#for ((i = 0; i != length; i++));
#do

#    circuit=$CircPath"/circuit_"${result[i]}".dat"
#    temp+=($(egrep -w "[0-9]+\-[0-9]+" $circuit))
    
#done

#IFS=$'\n' ; echo "${temp[*]}" | grep -h "${temp[*]}" $StudPath | cut -d"|" -f1 | sort -u

#IFS=$OLDIFS
cd DataPath"/circuits"
circ_id=$(grep -E "$1" $DataPath"/maps/projects.dat" | cut -d" " -f5)
stud_id=$(cat $(ls | grep -E "$circ_id") | grep -E "[0-9]{5}[-][0-9]{5}" | sort -u)
grep -E "$stud_id" $DataPath"/maps/students.dat" | cut -d"|" -f1 | sort -u
