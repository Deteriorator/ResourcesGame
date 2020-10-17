#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    resources.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.10.14   15:39
-------------------------------------------------------------------------------
   @Change:   2020.10.14
-------------------------------------------------------------------------------
"""
from pprint import pprint
import json
import requests
from config import Config


# data = requests.get('https://resources-game.ch/exchange/kurseliste_json.txt').json()
# data_dict = {}
#
# for i in data:
#     data_dict[i.get('NAME_EN')] = i

# print(type(a))
#
# b = json.dumps(a, sort_keys=True, indent=4, separators=(',', ': '))
# print(b)
example_dict = {}

for i in Config.example_data:
    example_dict[i.get('NAME_EN')] = i

# print(example_dict)

# print(len(list(example_dict.keys())))


if __name__ == '__main__':

    from features import Good

    b = Good(Config.Goods, example_dict)
    pprint(b.prod_profit_ordered())
    for i in b.prod_profit_ordered():
        print("{:<8}{:.2%}".format(i.get('name'), i.get('profitrate')))
