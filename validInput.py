import re
import datetime
import json

# return list
# 時間以外のチェックを行う
def check(message):
    list = message.split(" ")

    # /sceから始まっていない場合continue
    if list[0] != "/sce":
        return

    # /sceは削除
    del list[0]
    # 日付型に変換できるかのチェックは変換時にチェック

    # xxd or xxh 2d 1h
    pattern = "^([0-9])+(d|h)$"

    # matchした場合listをreturnする
    if re.match(pattern,list[1]):
        return list
    else:
        return

def conversion_time(list):
    unshaped_time = str(datetime.datetime.now().year) + "-" + list[0]
    try:
        encodetime = datetime.datetime.strptime(unshaped_time, '%Y-%m-%d-%H')
    except Exception as e:
        return

    list[0] = str(encodetime)
    return list

#
def list_to_json(list):
    f = open('test.json','w')
    keys = ['date', 'remind', 'value']
    d = dict(zip(keys,list))

    json.dump(d, f, ensure_ascii=False, indent=4)


string = "/sce 2-1-12 1d aavaa"
list_to_json(conversion_time(check(string)))
