import datetime
import json


def j_print(j):
    print(json.dumps(j, indent=4, ensure_ascii=False))


def time_str_handler(utc_str):
    utc_format = "%Y-%m-%d %H:%M:%S"
    shanghai_format = "%Y-%m-%d %H:%M:%S"
    utc = datetime.datetime.strptime(utc_str, utc_format)
    # 格林威治时间+8小时变为上海时间
    shanghai = utc + datetime.timedelta(hours=8)
    shanghai = shanghai.strftime(shanghai_format)
    return shanghai


def localtime_str():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S")
