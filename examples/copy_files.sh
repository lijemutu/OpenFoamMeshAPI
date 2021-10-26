#!/bin/bash

for file in $(find openfoam-master-tutorials/tutorials/ -type f -name blockMeshDict)
do
    #echo $file | "/" "\n"
    arrIN=(${file//\// })
    echo ${arrIN[2]}_${arrIN[3]}_${arrIN[4]}_${arrIN[5]}_${arrIN[6]}_${arrIN[7]}_${arrIN[8]}_${arrIN[9]}
    cp $file ${arrIN[2]}_${arrIN[3]}_${arrIN[4]}_${arrIN[5]}_${arrIN[6]}_${arrIN[7]}_${arrIN[8]}_${arrIN[9]}
    # echo $file    
done