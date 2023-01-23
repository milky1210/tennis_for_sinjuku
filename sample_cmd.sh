#!/bin/bash
for i in `seq 10000`
do
echo $i
python3 main.py --addSun --addNight --month 1
sleep 1800
done
