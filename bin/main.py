from scripts.parse_paramters import Paramter
from core.handle import Handle


def main(strings):
    parse_strings = Paramter(strings)
    promotion_infos = parse_strings.parse_promotion()
    goods_infos = parse_strings.parse_goods()
    deadline, coupons = parse_strings.parse_other()
    
    goods_dict = Handle.promotion(promotion_infos, goods_infos, deadline)
    total_price = sum(goods_dict.values())
    result = Handle.coupons(deadline, coupons, total_price)
    return result


s = """


1 * ipad : 2399.00
1 * 显示器 : 1799.00
12 * 啤酒 : 25.00
5 * 面包 : 9.00

2013.11.11


"""

print(main(s))

