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
    today = dt_now.day
    if month > 12:
        month -= 12
        year += 1
    youbi = datetime.datetime(year, month, 1).weekday()  # 0が月曜日
    if args.addSun:
        begin = 1 + (6 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, 6):
                if args.month == 0:
                    date = i - today + 1
                    if date < 0 or 30 < date:
                        break
                else:
                    date = i
                time_list.append([date, j])
    if args.addSat:
        begin = 1 + (5 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, 6):
                if args.month == 0:
                    date = i - today + 1
                    if date < 0 or 30 < date:
                        break
                else:
                    date = i
                time_list.append([date, j])
    if len(args.addDays) > 0:
        for date in args.addDays:
            for j in range(1, 6):
                if args.month == 0:
                    date = date - today + 1
                    if date < 0 or 30 < date:
                        break
                else:
                    date = i
                time_list.append([date, j])
    print(today, time_list)
    print("{}件の時間帯の予約を行います。".format(len(time_list)))

    print("observe start")
    observer = Observer(visible=not args.hide)
    result = observer.observe(month=args.month, date_time=time_list)
    if len(result) > 0:
        txt = "@milky9712, 落合中央公園テニスコート予約成功\n"
        for re in result:
            txt = txt + str(re[0]) + "日の," + str(re[1] * 2 + 7) + "時\n"
        txt = txt + "以上の内容になります"
        tweeter.tweet_txt(txt)
    else:
        print("正常に終了(予約は埋めっていました")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", default=0, type=int, help="今月か来月かを0,1で指定.0:今月、1:来月")
    parser.add_argument("--input", default="", help="日時と時間のarrayファイルを指定.形式はcsv(未実装)")
    parser.add_argument("--addSun", action="store_true", help="日曜日を追加,時間は9-19まで")
    parser.add_argument("--addSat", action="store_true", help="土曜日を追加,時間は9-19まで")
    parser.add_argument("--addNight", action="store_true", help="夜(19-)の枠のみを表示")
    parser.add_argument(
        "--repeat", default=60, type=int, help="繰り返しのインターバル[min](未実装)"
    )  # min
    parser.add_argument(
        "--addDays",
        default=[],
        nargs="*",
        type=int,
        help="追加したい日付スペース区切りで羅列.(ex: 10 31)",
    )  # 日付のリスト
    parser.add_argument("--hide", action="store_true", help="ドライバを非表示に設定")
    args = parser.parse_args()
    main(args)
