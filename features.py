#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     features.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.10.17   20:20
-------------------------------------------------------------------------------
   @Change:   2020.10.17
-------------------------------------------------------------------------------
"""

from config import Config


class Good(object):

    def __init__(self, goods: dict, price: dict):
        self.goods = goods
        self.price = price

    def profit(self):
        result = {}
        for good in self.goods.keys():
            if good in Config.Mine:
                result[good] = self.mine_cost(good)
            if good in Config.Units:
                continue
            if good in Config.Recycling:
                continue
            if good in Config.Buff:
                continue
            if good in Config.Production:
                pass
        return result

    def profitRate(self):
        result = {}
        for good in self.goods.keys():
            if good in Config.Mine:
                result[good] = 0
            if good in Config.Units:
                continue
            if good in Config.Recycling:
                continue
            if good in Config.Buff:
                continue
            if good in Config.Production:
                pass
        return result

    def cost(self):
        pass

    def mine_profit(self, item):
        return 0

    def mine_cost(self, item) -> int:
        """ 矿产资源的成本 """
        mine_price = self.price.get(item).get('NORMKURS')
        return int(mine_price)

    def prod_profit_ordered(self):
        result = []
        for item in Config.Production:
            item_info = {}
            name = Config.Goods.get(item).get('name')
            price = self.price.get(item).get('NORMKURS')
            cost = self.prod_cost(item)
            profit = int(self.price.get(item).get('NORMKURS')) - self.prod_cost(item)
            profitrate = self.prod_profit(item)
            item_info['name'] = name
            item_info['price'] = price
            item_info['cost'] = cost
            item_info['profit'] = profit
            item_info['profitrate'] = profitrate
            result.append(item_info)
        new = sorted(result, key=lambda a: a.get('profitrate'), reverse=True)
        return new

    def prod_profit(self, item):
        a = int(self.price.get(item).get('NORMKURS')) - self.prod_cost(item)
        a = a / self.prod_cost(item)
        return round(a, 2)

    def prod_cost(self, item) -> float:
        """ 一个产品的成本价格，四舍五入 """
        part = self.goods.get(item).get('part')
        prod_num = part.get('num')
        prod_costs = 0
        for key, val in part.items():
            if key in Config.Mine:
                prod_costs += self.mine_cost(key) * val
            if key == 'money':
                prod_costs += val
            if key in Config.Production:
                prod_costs += self.prod_cost(key) * val
        return round(prod_costs / prod_num, 2)

    def units_profit(self, item):
        pass

    def unit_cost(self, item):
        pass

    def buff_profit(self, item):
        pass

    def buff_cost(self, item):
        pass

    def recycling_profit(self, item):
        pass

    def recycling_cost(self, item):
        pass
