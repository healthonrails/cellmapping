#!/bin/bash
source ${HOME}/miniconda3/etc/profile.d/conda.sh
conda activate cellmapping
cellfinder -s  ${1} -b ${2} -o ${3} -v ${4} ${5} ${6} --orientation ${7}