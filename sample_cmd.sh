#!/bin/bash
for i in `seq 10000`
do
echo $i
python3 main.py --hide --addSun --addNight --month 1 --addDays 11 18 23 24 25
python3 main.py --hide --addSun --addNight --month 0
sleep 1800
done
