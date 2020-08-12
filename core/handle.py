from scripts.utils import parse_date, parse_goods_list
from date.goods import all_goods


class Handle:
    @staticmethod
    def promotion(promotions, goods_infos, deadline):
        if promotions:
            deadline, parse_date(deadline)
            for promotion in promotions:
                date, rate, category = promotion
                date = parse_date(date)
                if deadline <= date:
                    # 结算日期在促销日期里
                    i = 0
                    while i < len(goods_infos):
                        if goods_infos[i][1] in all_goods.get(category):
                            goods_infos[i][2] = goods_infos[i][2] * rate
                        i += 1
                else:
                    # 结算日期超过促销日期
                    pass
                
        return parse_goods_lists(goods_infos)
    
    @staticmethod
    def coupons(deadline, coup, total_price):
        if coup:
            # 如果有优惠券
            date, base_price, derates = coup.strip().split(" ")
            if total_price > float(base_price):
                if parse_date(deadline) <= parse_date(date):
                    total_price = total_price -float(derates)
        return "%.2f" % total_price
    
    

