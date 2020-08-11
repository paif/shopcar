from scripts.parse_paramters import Paramter
from scripts.utils import discount

all_goods = {
    "电子": ["ipad", "iphone", "显示器", "笔记本电脑", "键盘"],
    "食品": ["面包", "饼干", "蛋糕", "牛肉", "鱼", "蔬菜"],
    "日用品": ["餐巾纸", "收纳箱", "咖啡杯", "雨伞"],
    "酒类": ["啤酒", "白酒", "伏特加"]
}
def discount(category, rate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if g_name in all_goods.get(category):
                result = func(g_name, g_num, g_price * rate)

            else:
                result = func(g_name, g_num, g_price)
            return result
        return wrapper
    return decorator



@discount(category, rate)
def one_goods_price(g_name, g_num, g_price):
    """
    一种商品的总价格
    :param g_name:商品名称
    :param g_num: 商品数量
    :param g_price: 商品价格
    :return: {g_name:g_price}
    """
    return {g_name: g_num * g_price}


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
    p = Paramter(s)
    promotions = p.parse_promotion()
    if promotions:
        # 有促销

        for good in p.parse_good():
            g_num, g_name, g_price = good
            for promotion in promotions:
                date, rate, category = promotion
    else:
        # 没有促销


