import datetime

def parse_date(date_string):
    year, month, day = date_string.split(".")
    return datetime.date(int(year), int(month), int(day))

def parse_goods_list(goods_list):
    result = {}
    for _ in goods_list:
        result[_[1]] = float("%.2f" % (_[0]*_[2]))
    return result

if __name__ == '__main__':
    print(parse_date("2013.11.12"))
