class Paramter(object):
    def __init__(self, strings):
        self.strings = strings

    def parse_promotion(self):
        """
        处理促销参数
        :return:
        """
        # 无促销信息
        if self.strings[:2] == "\n\n":
            return None
        # 有促销信息
        else:
            result = []
            promotions = self.strings.strip().split("\n\n")[0]
            promotion_list = promotions.split("\n")
            goods = map(lambda x: x.strip(), promotion_list)
            for g in goods:
                date, rate, category = g.split("|")
                result.append([date.strip(), float(rate), category.strip()])
            return result

    def parse_good(self):
        result = []
        if self.strings[:2] == "\n\n":
            goods = self.strings.strip().split("\n\n")[0]
        else:
            goods = self.strings.strip().split("\n\n")[1]
        good_list = goods.split("\n")
        for good in good_list:
            _, g_price = good.split(":")
            g_num, g_name = _.strip().split("*")
            result.append([int(g_num), g_name.strip(), float("%2.f"%float(g_price))])
        return result

    def parse_other(self):
        if self.strings[:2] == "\n\n":
            other = self.strings.strip().split("\n\n")[1]
        else:
            other = self.strings.strip().split("\n\n")[2]
        other_list = other.split("\n")
        if len(other_list) > 1:
            deadline, coupons = other_list[0], other_list[1]
            return deadline.strip(), coupons.strip()
        else:
            deadline = other_list[0]
            return deadline, None


if __name__ == '__main__':
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
    s1 = """

  
1 * ipad : 2399.00
1 * 显示器 : 1799.00
12 * 啤酒 : 25.00
5 * 面包 : 9.00

2013.11.11


"""
    s2 = """


    1 * ipad : 2399.00
    1 * 显示器 : 1799.00
    12 * 啤酒 : 25.00
    5 * 面包 : 9.00

2013.11.11


"""

    p1 = Paramter(s1)
    p = Paramter(s)
    print(list(p.parse_promotion()))
    print(p1.parse_promotion())
