#!/bin/sh

mkdir $1
touch $1/input.txt
cat template.py > $1/solve.py

#Automated input download
cd $1
python3 - <<EOF 
from aocd import get_data

with open("input.txt", 'w') as f:
	f.write(get_data(day = $1, year = 2023))
EOF

