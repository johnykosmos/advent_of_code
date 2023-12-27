#!/bin/sh

mkdir $1
touch $1/input.txt
cat template.py > $1/solve.py

python3 -m aocd
aocd $1 2023 > $1/input.txt




