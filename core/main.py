from scripts.parse_paramters import Paramter
from scripts.utils import parse_date

s = """
2013.11.11 | 0.7 | 电⼦
2013.12.22 | 0.8 | 食品

1 * ipad : 2399.00
1 * 显示器 : 1799.00
12 * 啤酒 : 26.00
5 * 面包 : 9.00

2013.11.11
2014.3.2 1000 200

"""

strings = s
p = Paramter(strings)
# print(p.parse_other())
promotions = p.parse_promotion()
if promotions:
    # 有促销
    deadline, coupons = p.parse_other()  # deadline结算日期，coupons优惠券信息
    deadline = parse_date(deadline)
    for promotion in promotions:
        date, rate, category = promotion
        date = parse_date(date)
        if deadline <= date:
            # 结算日期在促销日期内
            pass
        else:
            # 结算日期已经过了促销日期
            pass

else:
    # 无促销
    pass


