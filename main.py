import argparse
import csv
import time
import tweeter
from observe import Observer
import datetime


def main(args):
    time_list = []
    if args.addNight:
        for i in range(1, 31, 1):
            time_list.append([i, 6])
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = dt_now.month + args.month  # 取る対象の月
    if month > 12:
        month -= 12
        year += 1
    youbi = datetime.datetime(year, month, 1).weekday()  # 0が月曜日
    if args.addSun:
        begin = 1 + (6 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, 6):
                time_list.append([i, j])
    if args.addSat:
        begin = 1 + (5 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, 6):
                time_list.append([i, j])
    if len(args.addDays) > 0:
        for date in args.addDays:
            for j in range(1, 6):
                time_list.append([date, j])
    print("{}件の時間帯の予約を行います。".format(len(time_list)))

    print("observe start")
    observer = Observer()
    result = observer.observe(month=args.month, date_time=time_list)
    if len(result) > 0:
        txt = "@milky9712, 落合中央公園テニスコート予約成功\n"
        for re in result:
            txt = txt + str(re[0]) + "日の," + str(re[1] * 2 + 7) + "時\n"
        txt = txt + "以上の内容になります"
        tweeter.tweet_txt(txt)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", default=0, type=int)
    parser.add_argument("--input", default="")
    parser.add_argument("--addSun", action="store_true")
    parser.add_argument("--addSat", action="store_true")
    parser.add_argument("--addNight", action="store_true")
    parser.add_argument("--repeat", default=60, type=int)  # min
    parser.add_argument("--addDays", default=[], nargs="*", type=int)  # 日付のリスト
    args = parser.parse_args()
    main(args)
