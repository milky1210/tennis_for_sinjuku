#!/bin/bash
for i in `seq 10000`
do
echo $i
python3 main.py --addSun --addNight --month 1 --addDays 11 18 23 24 25
sleep 1800
done
