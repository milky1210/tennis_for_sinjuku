#!/bin/bash
python3 main.py --hide --addNight --month 1 --addDays 11 12 18 19 21 26  --timer 20 0 0
for i in `seq 30`
do
echo $i
python3 main.py --hide --addNight --month 1 --addDays 11 12 18 19 21 26
sleep 20
done
