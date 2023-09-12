import argparse
import csv
import time
import tweeter
from observe import Observer
import datetime


def main(args):
    # 処理開始
    startTime = datetime.datetime.now()
    time_list0 = []
    time_list1 = []
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = dt_now.month  # 取る対象の月
    today = dt_now.day
    youbi = datetime.datetime(year, month, 1).weekday()  # 0が月曜日
    misoka = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yutori = 6  # 6日よりあとは取らない
    if args.month in [1, 2, 3, 10, 11, 12]:  # 朝がない
        date_len = 6
    else:
        date_len = 7
    if args.addNight:
        for i in range(1, 31, 1):
            if args.month == month and i < 3:
                break
            time_list0.append([i, date_len])
    if args.addSun:
        begin = 1 + (6 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, date_len):
                if args.month == month:
                    date = i - today + 1
                    if date < yutori or 30 < date:
                        break
                else:
                    date = i
                    if today + yutori - misoka[month - 1] > date:
                        break

                time_list0.append([date, j])
            for j in range(1, 4):
                if args.month == month:
                    date = i - today + 1
                    if date < yutori or 30 < date:
                        break
                else:
                    date = i
                    if today + yutori - misoka[month - 1] > date:
                        break
                time_list1.append([date, j])
    if args.addSat:
        begin = 1 + (5 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, date_len):
                if args.month == month:
                    date = i - today + 1
                    if date < yutori or 30 < date:
                        break
                else:
                    date = i
                    if today + yutori - misoka[month - 1] > date:
                        break
                time_list0.append([date, j])
            for j in range(1, 4):
                if args.month == month:
                    date = i - today + 1
                    if date < yutori or 30 < date:
                        break
                else:
                    date = i
                    if today + yutori - misoka[month - 1] > date:
                        break
                time_list1.append([date, j])
    if len(args.addDays) > 0:
        for i in args.addDays:
            for j in range(1, date_len):
                if args.month == month:
                    date = i - today + 1
                    if date < yutori or 30 < date:
                        break
                else:
                    date = i
                    if today + yutori - misoka[month - 1] >= date:
                        break
                time_list0.append([date, j])
            for j in range(1, 4):
                if args.month == month:
                    date = i - today + 1
                    if date < yutori or 30 < date:
                        break
                else:
                    date = i
                    if today + yutori - misoka[month - 1] >= date:
                        break
                time_list1.append([date, j])

    print("{}件の時間帯の予約を行います。".format(len(time_list0) + len(time_list1)))

    print("observe start")
    observer = Observer(visible=not args.hide)
    result0 = observer.observe(park=0, month=args.month - month, date_time=time_list0)
    observer = Observer(visible=not args.hide)
    result1 = observer.observe(park=1, month=args.month - month, date_time=time_list1)
    endTime = datetime.datetime.now()
    if len(result0) > 0:
        txt = "@milky9712, 落合中央公園テニスコート予約成功\n"
        for re in result0:
            if args.month == month:
                date = today + re[0] - 1
            else:
                date = re[0]
            txt = txt + str(date) + "日の," + str(re[1] * 2 + date_len + 1) + "時\n"
        txt = txt + "以上の内容になります\n"
        txt = txt + "アクセスログ：{:02}:{:02}:{:02}アクセス開始、{:02}:{:02}:{:02}アクセス完了\n".format(
            startTime.hour,
            startTime.minute,
            startTime.second,
            endTime.hour,
            endTime.minute,
            endTime.second,
        )
        tweeter.tweet_txt(txt)
        print(txt)
    elif len(result1) > 0:
        txt = "@milky9712, 西落合公園テニスコート予約成功\n"
        for re in result1:
            if args.month == month:
                date = today + re[0] - 1
            else:
                date = re[0]
            txt = txt + str(date) + "日の," + str(re[1] * 2 + 7) + "時\n"
        txt = txt + "以上の内容になります\n"
        txt = txt + "アクセスログ：{:02}:{:02}:{:02}アクセス開始、{:02}:{:02}:{:02}アクセス完了\n".format(
            startTime.hour,
            startTime.minute,
            startTime.second,
            endTime.hour,
            endTime.minute,
            endTime.second,
        )
        tweeter.tweet_txt(txt)
        print(txt)
    else:
        txt = "@milky9712, 正常に終了(予約は埋めっていました\n"
        txt = (
            txt
            + "アクセスログ：{}/{}-{:02}:{:02}:{:02}アクセス開始、{:02}:{:02}:{:02}アクセス完了\n".format(
                startTime.month,
                startTime.day,
                startTime.hour,
                startTime.minute,
                startTime.second,
                endTime.hour,
                endTime.minute,
                endTime.second,
            )
        )
        if args.errTweet:
            tweeter.tweet_txt(txt)
        print(txt)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", default=0, type=int, help="月を入力")
    parser.add_argument("--input", default="", help="日時と時間のarrayファイルを指定.形式はcsv(未実装)")
    parser.add_argument("--addSun", action="store_true", help="日曜日を追加,時間は9-19まで,3日後から")
    parser.add_argument("--addSat", action="store_true", help="土曜日を追加,時間は9-19まで,3日後から")
    parser.add_argument("--addNight", action="store_true", help="夜(19-)の枠のみを表示, 3日後から")
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
    parser.add_argument("--errTweet", action="store_true", help="エラーでもlogをツイートする")
    args = parser.parse_args()
    main(args)
