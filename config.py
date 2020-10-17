#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     config.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.10.17   20:38
-------------------------------------------------------------------------------
   @Change:   2020.10.17
-------------------------------------------------------------------------------
"""


class Config:

    Mine = [
        'Bauxite',
        'Iron ore',
        'Gold ore',
        'Ilmenite',
        'Limestone',
        'Gravel',
        'Coal',
        'Chalcopyrite',
        'Clay',
        'Lithium ore',
        'Quartz sand',
        "Rough diamonds",
        'Crude oil',
        'Silver ore',
    ]

    Production = [
        'Aluminium',
        'Batteries',
        'Concrete',
        'Fertilizer',
        'Electronics',
        'Fossil fuel',
        'Glass',
        'Gold',
        'Insecticides',
        'Plastics',
        'Copper',
        "Trucks",
        'Lithium',
        'Medical technology',
        'Scan drones',
        'Jewellery',
        'Silver',
        'Silicon',
        'Steel',
        'Titanium',
        'Weapons',
        'Bricks'
    ]

    Units = [
        'Elite force',
        'Gangster',
        'Attack dogs',
        'Private army',
        'Watch dogs',
        'Security staff'
    ]

    Buff = [
        'Guest workers',
        'Wage subsidy',
        'Night shift',
        'Overtime',
    ]

    Recycling = [
        'Old tires',
        'Waste glass',
        'Scrap metal',
        'Used oil',
        'Drone wreckage',
        'Electronic scrap',
        'Fossils',
        'Plastic scrap',
        'Copper coins',
        'Giant diamond',
        'Roman coins',
        'Tech upgrade 1',
        'Tech upgrade 2',
        'Tech upgrade 3',
        'Tech upgrade 4',
        'Maintenance kit',
    ]

    Goods = {
        'Old tires': {
            'name': '旧轮胎',
            'buy': True,
            'sell': True,
        },
        'Waste glass': {
            'name': '废玻璃',
            'buy': True,
            'sell': True,
        },
        'Scrap metal': {
            'name': '废金属',
            'buy': True,
            'sell': True,
        },
        'Used oil': {
            'name': '废油',
            'buy': True,
            'sell': True,
        },
        'Drone wreckage': {
            'name': '无人机残骸',
            'buy': True,
            'sell': True,
        },
        'Electronic scrap': {
            'name': '废电器',
            'buy': True,
            'sell': True,
        },
        'Fossils': {
            'name': '化石',
            'buy': True,
            'sell': True,
        },
        'Plastic scrap': {
            'name': '废塑料',
            'buy': True,
            'sell': True,
        },
        'Copper coins': {
            'name': '铜币',
            'buy': True,
            'sell': True,
        },
        'Giant diamond': {
            'name': '大钻石',
            'buy': True,
            'sell': False,
        },
        'Roman coins': {
            'name': '罗马币',
            'buy': True,
            'sell': True,
        },
        'Tech upgrade 1': {
            'name': 'Tech upgrade 1',
            'buy': True,
            'sell': True,
        },
        'Tech upgrade 2': {
            'name': 'Tech upgrade 2',
            'buy': True,
            'sell': True,
        },
        'Tech upgrade 3': {
            'name': 'Tech upgrade 3',
            'buy': True,
            'sell': True,
        },
        'Tech upgrade 4': {
            'name': 'Tech upgrade 4',
            'buy': True,
            'sell': False,
        },
        'Maintenance kit': {
            'name': '维修工具',
            'buy': True,
            'sell': True,
        },


        'Bauxite': {
            'name': '铝矿',
            'buy': True,
            'sell': True,
        },
        'Iron ore': {
            'name': '铁矿',
            'buy': True,
            'sell': True,
        },
        'Gold ore': {
            'name': '金矿',
            'buy': True,
            'sell': True,
        },
        'Ilmenite': {
            'name': '钛铁矿',
            'buy': True,
            'sell': True,
        },
        'Limestone': {
            'name': '石灰',
            'buy': True,
            'sell': True,
        },
        'Gravel': {
            'name': '砾石',
            'buy': True,
            'sell': True,
        },
        'Coal': {
            'name': '煤炭',
            'buy': True,
            'sell': True,
        },
        'Chalcopyrite': {
            'name': '黄铜矿',
            'buy': True,
            'sell': True,
        },
        'Clay': {
            'name': '黏土矿',
            'buy': True,
            'sell': True,
        },
        'Lithium ore': {
            'name': '锂矿',
            'buy': True,
            'sell': True,
        },
        'Quartz sand': {
            'name': '石英砂',
            'buy': True,
            'sell': True,
        },
        "Rough diamonds": {
            'name': '原钻',
            'buy': True,
            'sell': True,
        },
        'Crude oil': {
            'name': '原油',
            'buy': True,
            'sell': True,
        },
        'Silver ore': {
            'name': '银矿',
            'buy': True,
            'sell': True,
        },


        'Aluminium': {
            'name': '铝',
            'buy': True,
            'sell': True,
            'part': {
                'num': 4,
                'money': 5000,
                'Bauxite': 24
            }
        },
        'Batteries': {
            'name': '电池',
            'buy': True,
            'sell': True,
            'part': {
                'num': 10,
                'money': 75000,
                'Lithium': 20,
                'Plastics': 40,
                'Aluminium': 10
            }
        },
        'Concrete': {
            'name': '水泥',
            'buy': True,
            'sell': True,
            'part': {
                'num': 14,
                'money': 20,
                'Gravel': 3,
                'Limestone': 2
            }
        },
        'Fertilizer': {
            'name': '肥料',
            'buy': True,
            'sell': True,
            'part': {
                'num': 11,
                'money': 90,
                'Limestone': 8
            }
        },
        'Electronics': {
            'name': '电子元件',
            'buy': True,
            'sell': True,
            'part': {
                'num': 8,
                'money': 5000,
                'Plastics': 4,
                'Copper': 3,
                'Silicon': 1
            }
        },
        'Fossil fuel': {
            'name': '燃料',
            'buy': True,
            'sell': True,
            'part': {
                'num': 4,
                'money': 150,
                'Crude oil': 4
            }
        },
        'Glass': {
            'name': '玻璃',
            'buy': True,
            'sell': True,
            'part': {
                'num': 8,
                'money': 3000,
                'Quartz sand': 6,
                'Fossil fuel': 8,
                'Limestone': 4
            }
        },
        'Gold': {
            'name': '金条',
            'buy': True,
            'sell': True,
            'part': {
                'num': 3,
                'money': 20000,
                'Gold ore': 20
            }
        },
        'Insecticides': {
            'name': '杀虫剂',
            'buy': True,
            'sell': True,
            'part': {
                'num': 35,
                'money': 2400,
                'Copper': 1,
                'Limestone': 3
            }
        },
        'Plastics': {
            'name': '塑胶',
            'buy': True,
            'sell': True,
            'part': {
                'num': 10,
                'money': 400,
                'Crude oil': 1
            }
        },
        'Copper': {
            'name': '铜',
            'buy': True,
            'sell': True,
            'part': {
                'num': 3,
                'money': 2500,
                'Chalcopyrite': 9
            }
        },
        "Trucks": {
            'name': '货车',
            'buy': True,
            'sell': True,
            'part': {
                'num': 50,
                'money': 2500000,
                'Steel': 100,
                'Batteries': 25,
                'Silver': 50
            }
        },
        'Lithium': {
            'name': '锂',
            'buy': True,
            'sell': True,
            'part': {
                'num': 5,
                'money': 5000,
                'Lithium ore': 115
            }
        },
        'Medical technology': {
            'name': '医疗科技',
            'buy': True,
            'sell': True,
            'part': {
                'num': 10,
                'money': 90000,
                'Titanium': 4,
                'Plastics': 2,
                'Electronics': 2
            }
        },
        'Scan drones': {
            'name': '无人机',
            'buy': True,
            'sell': True,
            'part': {
                'num': 1,
                'money': 25000000,
                'Electronics': 25,
                'Titanium': 50,
                'Batteries': 250
            }
        },
        'Jewellery': {
            'name': '珠宝',
            'buy': True,
            'sell': True,
            'part': {
                'num': 2,
                'money': 50000,
                'Rough diamonds': 1000,
                'Gold': 1,
                'Silver': 1
            }
        },
        'Silver': {
            'name': '银',
            'buy': True,
            'sell': True,
            'part': {
                'num': 50,
                'money': 10000,
                'Silver ore': 8
            }
        },
        'Silicon': {
            'name': '硅',
            'buy': True,
            'sell': True,
            'part': {
                'num': 2,
                'money': 49500,
                'Quartz sand': 20,
                'Clay': 1,
                'Fossil fuel': 5
            }
        },
        'Steel': {
            'name': '钢铁',
            'buy': True,
            'sell': True,
            'part': {
                'num': 1,
                'money': 350,
                'Iron ore': 7,
                'Coal': 10
            }
        },
        'Titanium': {
            'name': '钛',
            'buy': True,
            'sell': True,
            'part': {
                'num': 4,
                'money': 10000,
                'Ilmenite': 8
            }
        },
        'Weapons': {
            'name': '武器',
            'buy': True,
            'sell': True,
            'part': {
                'num': 25,
                'money': 250000,
                'Steel': 1,
                'Aluminium': 1,
                'Batteries': 1
            }
        },
        'Bricks': {
            'name': '红砖',
            'buy': True,
            'sell': True,
            'part': {
                'num': 2,
                'money': 10,
                'Clay': 3
            }
        },


        'Elite force': {
            'name': '精英部队',
            'buy': True,
            'sell': True,
        },
        'Gangster': {
            'name': '黑道份子',
            'buy': True,
            'sell': True,
        },
        'Attack dogs': {
            'name': '攻击犬',
            'buy': True,
            'sell': True,
        },
        'Private army': {
            'name': '私人军队',
            'buy': True,
            'sell': True,
        },
        'Watch dogs': {
            'name': '看门狗',
            'buy': True,
            'sell': True,
        },
        'Security staff': {
            'name': '保全人员',
            'buy': True,
            'sell': True,
        },


        'Guest workers': {
            'name': 'Guest workers',
            'buy': True,
            'sell': True,
        },
        'Wage subsidy': {
            'name': 'Wage subsidy',
            'buy': True,
            'sell': True,
        },
        'Night shift': {
            'name': 'Night shift',
            'buy': True,
            'sell': True,
        },
        'Overtime': {
            'name': 'Overtime',
            'buy': True,
            'sell': True,
        },
    }

    example_data = [
        {
            "0": "57",
            "1": "Alte Reifen",
            "2": "Old tires",
            "3": "21559",
            "4": "23020",
            "5": "1602738841",
            "ITEM_ID": "57",
            "NAME_DE": "Alte Reifen",
            "NAME_EN": "Old tires",
            "NORMKURS": "21559",
            "SMKURS": "23020",
            "TS": "1602738841"
        },
        {
            "0": "115",
            "1": "Altglas",
            "2": "Waste glass",
            "3": "26670",
            "4": "36235",
            "5": "1602738841",
            "ITEM_ID": "115",
            "NAME_DE": "Altglas",
            "NAME_EN": "Waste glass",
            "NORMKURS": "26670",
            "SMKURS": "36235",
            "TS": "1602738841"
        },
        {
            "0": "70",
            "1": "Altmetall",
            "2": "Scrap metal",
            "3": "15923",
            "4": "16765",
            "5": "1602738841",
            "ITEM_ID": "70",
            "NAME_DE": "Altmetall",
            "NAME_EN": "Scrap metal",
            "NORMKURS": "15923",
            "SMKURS": "16765",
            "TS": "1602738841"
        },
        {
            "0": "74",
            "1": "Alt\u00f6l",
            "2": "Used oil",
            "3": "6401",
            "4": "7257",
            "5": "1602738841",
            "ITEM_ID": "74",
            "NAME_DE": "Alt\u00f6l",
            "NAME_EN": "Used oil",
            "NORMKURS": "6401",
            "SMKURS": "7257",
            "TS": "1602738841"
        },
        {
            "0": "32",
            "1": "Aluminium",
            "2": "Aluminium",
            "3": "92609",
            "4": "94745",
            "5": "1602738841",
            "ITEM_ID": "32",
            "NAME_DE": "Aluminium",
            "NAME_EN": "Aluminium",
            "NORMKURS": "92609",
            "SMKURS": "94745",
            "TS": "1602738841"
        },
        {
            "0": "93",
            "1": "Batterien",
            "2": "Batteries",
            "3": "264520",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "93",
            "NAME_DE": "Batterien",
            "NAME_EN": "Batteries",
            "NORMKURS": "264520",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "12",
            "1": "Bauxit",
            "2": "Bauxite",
            "3": "2771",
            "4": "2990",
            "5": "1602738841",
            "ITEM_ID": "12",
            "NAME_DE": "Bauxit",
            "NAME_EN": "Bauxite",
            "NORMKURS": "2771",
            "SMKURS": "2990",
            "TS": "1602738841"
        },
        {
            "0": "7",
            "1": "Beton",
            "2": "Concrete",
            "3": "5142",
            "4": "5505",
            "5": "1602738841",
            "ITEM_ID": "7",
            "NAME_DE": "Beton",
            "NAME_EN": "Concrete",
            "NORMKURS": "5142",
            "SMKURS": "5505",
            "TS": "1602738841"
        },
        {
            "0": "120",
            "1": "Drohnenwrack",
            "2": "Drone wreckage",
            "3": "11448352",
            "4": "13053575",
            "5": "1602738841",
            "ITEM_ID": "120",
            "NAME_DE": "Drohnenwrack",
            "NAME_EN": "Drone wreckage",
            "NORMKURS": "11448352",
            "SMKURS": "13053575",
            "TS": "1602738841"
        },
        {
            "0": "22",
            "1": "D\u00fcngemittel",
            "2": "Fertilizer",
            "3": "1996",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "22",
            "NAME_DE": "D\u00fcngemittel",
            "NAME_EN": "Fertilizer",
            "NORMKURS": "1996",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "13",
            "1": "Eisenerz",
            "2": "Iron ore",
            "3": "2401",
            "4": "2605",
            "5": "1602738841",
            "ITEM_ID": "13",
            "NAME_DE": "Eisenerz",
            "NAME_EN": "Iron ore",
            "NORMKURS": "2401",
            "SMKURS": "2605",
            "TS": "1602738841"
        },
        {
            "0": "66",
            "1": "Elektronik",
            "2": "Electronics",
            "3": "69650",
            "4": "69620",
            "5": "1602738841",
            "ITEM_ID": "66",
            "NAME_DE": "Elektronik",
            "NAME_EN": "Electronics",
            "NORMKURS": "69650",
            "SMKURS": "69620",
            "TS": "1602738841"
        },
        {
            "0": "78",
            "1": "Elektronikschrott",
            "2": "Electronic scrap",
            "3": "191775",
            "4": "219390",
            "5": "1602738841",
            "ITEM_ID": "78",
            "NAME_DE": "Elektronikschrott",
            "NAME_EN": "Electronic scrap",
            "NORMKURS": "191775",
            "SMKURS": "219390",
            "TS": "1602738841"
        },
        {
            "0": "99",
            "1": "Elitetruppe",
            "2": "Elite force",
            "3": "56686634",
            "4": "66562326",
            "5": "1602738841",
            "ITEM_ID": "99",
            "NAME_DE": "Elitetruppe",
            "NAME_EN": "Elite force",
            "NORMKURS": "56686634",
            "SMKURS": "66562326",
            "TS": "1602738841"
        },
        {
            "0": "38",
            "1": "Foss. Brennstoffe",
            "2": "Fossil fuel",
            "3": "29041",
            "4": "35185",
            "5": "1602738841",
            "ITEM_ID": "38",
            "NAME_DE": "Foss. Brennstoffe",
            "NAME_EN": "Fossil fuel",
            "NORMKURS": "29041",
            "SMKURS": "35185",
            "TS": "1602738841"
        },
        {
            "0": "41",
            "1": "Fossilien",
            "2": "Fossils",
            "3": "7418",
            "4": "8460",
            "5": "1602738841",
            "ITEM_ID": "41",
            "NAME_DE": "Fossilien",
            "NAME_EN": "Fossils",
            "NORMKURS": "7418",
            "SMKURS": "8460",
            "TS": "1602738841"
        },
        {
            "0": "103",
            "1": "Gangster",
            "2": "Gangster",
            "3": "14564752",
            "4": "15865000",
            "5": "1602738841",
            "ITEM_ID": "103",
            "NAME_DE": "Gangster",
            "NAME_EN": "Gangster",
            "NORMKURS": "14564752",
            "SMKURS": "15865000",
            "TS": "1602738841"
        },
        {
            "0": "160",
            "1": "Gastarbeiter",
            "2": "Guest workers",
            "3": "35168928266",
            "4": "39154474265",
            "5": "1602738841",
            "ITEM_ID": "160",
            "NAME_DE": "Gastarbeiter",
            "NAME_EN": "Guest workers",
            "NORMKURS": "35168928266",
            "SMKURS": "39154474265",
            "TS": "1602738841"
        },
        {
            "0": "60",
            "1": "Glas",
            "2": "Glass",
            "3": "49583",
            "4": "50415",
            "5": "1602738841",
            "ITEM_ID": "60",
            "NAME_DE": "Glas",
            "NAME_EN": "Glass",
            "NORMKURS": "49583",
            "SMKURS": "50415",
            "TS": "1602738841"
        },
        {
            "0": "79",
            "1": "Gold",
            "2": "Gold",
            "3": "65834",
            "4": "66205",
            "5": "1602738841",
            "ITEM_ID": "79",
            "NAME_DE": "Gold",
            "NAME_EN": "Gold",
            "NORMKURS": "65834",
            "SMKURS": "66205",
            "TS": "1602738841"
        },
        {
            "0": "14",
            "1": "Golderz",
            "2": "Gold ore",
            "3": "959",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "14",
            "NAME_DE": "Golderz",
            "NAME_EN": "Gold ore",
            "NORMKURS": "959",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "49",
            "1": "Ilmenit",
            "2": "Ilmenite",
            "3": "766",
            "4": "775",
            "5": "1602738841",
            "ITEM_ID": "49",
            "NAME_DE": "Ilmenit",
            "NAME_EN": "Ilmenite",
            "NORMKURS": "766",
            "SMKURS": "775",
            "TS": "1602738841"
        },
        {
            "0": "28",
            "1": "Insektizide",
            "2": "Insecticides",
            "3": "4258",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "28",
            "NAME_DE": "Insektizide",
            "NAME_EN": "Insecticides",
            "NORMKURS": "4258",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "20",
            "1": "Kalkstein",
            "2": "Limestone",
            "3": "1079",
            "4": "1165",
            "5": "1602738841",
            "ITEM_ID": "20",
            "NAME_DE": "Kalkstein",
            "NAME_EN": "Limestone",
            "NORMKURS": "1079",
            "SMKURS": "1165",
            "TS": "1602738841"
        },
        {
            "0": "102",
            "1": "Kampfhunde",
            "2": "Attack dogs",
            "3": "1528820",
            "4": "1796631",
            "5": "1602738841",
            "ITEM_ID": "102",
            "NAME_DE": "Kampfhunde",
            "NAME_EN": "Attack dogs",
            "NORMKURS": "1528820",
            "SMKURS": "1796631",
            "TS": "1602738841"
        },
        {
            "0": "3",
            "1": "Kies",
            "2": "Gravel",
            "3": "854",
            "4": "880",
            "5": "1602738841",
            "ITEM_ID": "3",
            "NAME_DE": "Kies",
            "NAME_EN": "Gravel",
            "NORMKURS": "854",
            "SMKURS": "880",
            "TS": "1602738841"
        },
        {
            "0": "8",
            "1": "Kohle",
            "2": "Coal",
            "3": "2279",
            "4": "2485",
            "5": "1602738841",
            "ITEM_ID": "8",
            "NAME_DE": "Kohle",
            "NAME_EN": "Coal",
            "NORMKURS": "2279",
            "SMKURS": "2485",
            "TS": "1602738841"
        },
        {
            "0": "58",
            "1": "Kunststoffe",
            "2": "Plastics",
            "3": "7705",
            "4": "8570",
            "5": "1602738841",
            "ITEM_ID": "58",
            "NAME_DE": "Kunststoffe",
            "NAME_EN": "Plastics",
            "NORMKURS": "7705",
            "SMKURS": "8570",
            "TS": "1602738841"
        },
        {
            "0": "77",
            "1": "Kunststoffschrott",
            "2": "Plastic scrap",
            "3": "12936",
            "4": "16660",
            "5": "1602738841",
            "ITEM_ID": "77",
            "NAME_DE": "Kunststoffschrott",
            "NAME_EN": "Plastic scrap",
            "NORMKURS": "12936",
            "SMKURS": "16660",
            "TS": "1602738841"
        },
        {
            "0": "36",
            "1": "Kupfer",
            "2": "Copper",
            "3": "85863",
            "4": "85863",
            "5": "1602738841",
            "ITEM_ID": "36",
            "NAME_DE": "Kupfer",
            "NAME_EN": "Copper",
            "NORMKURS": "85863",
            "SMKURS": "85863",
            "TS": "1602738841"
        },
        {
            "0": "26",
            "1": "Kupferkies",
            "2": "Chalcopyrite",
            "3": "1321",
            "4": "1350",
            "5": "1602738841",
            "ITEM_ID": "26",
            "NAME_DE": "Kupferkies",
            "NAME_EN": "Chalcopyrite",
            "NORMKURS": "1321",
            "SMKURS": "1350",
            "TS": "1602738841"
        },
        {
            "0": "55",
            "1": "Kupferm\u00fcnzen",
            "2": "Copper coins",
            "3": "15787",
            "4": "17120",
            "5": "1602738841",
            "ITEM_ID": "55",
            "NAME_DE": "Kupferm\u00fcnzen",
            "NAME_EN": "Copper coins",
            "NORMKURS": "15787",
            "SMKURS": "17120",
            "TS": "1602738841"
        },
        {
            "0": "124",
            "1": "Lastwagen",
            "2": "Trucks",
            "3": "355317",
            "4": "360570",
            "5": "1602738841",
            "ITEM_ID": "124",
            "NAME_DE": "Lastwagen",
            "NAME_EN": "Trucks",
            "NORMKURS": "355317",
            "SMKURS": "360570",
            "TS": "1602738841"
        },
        {
            "0": "2",
            "1": "Lehm",
            "2": "Clay",
            "3": "629",
            "4": "630",
            "5": "1602738841",
            "ITEM_ID": "2",
            "NAME_DE": "Lehm",
            "NAME_EN": "Clay",
            "NORMKURS": "629",
            "SMKURS": "630",
            "TS": "1602738841"
        },
        {
            "0": "92",
            "1": "Lithium",
            "2": "Lithium",
            "3": "44541",
            "4": "47550",
            "5": "1602738841",
            "ITEM_ID": "92",
            "NAME_DE": "Lithium",
            "NAME_EN": "Lithium",
            "NORMKURS": "44541",
            "SMKURS": "47550",
            "TS": "1602738841"
        },
        {
            "0": "90",
            "1": "Lithiumerz",
            "2": "Lithium ore",
            "3": "994",
            "4": "1055",
            "5": "1602738841",
            "ITEM_ID": "90",
            "NAME_DE": "Lithiumerz",
            "NAME_EN": "Lithium ore",
            "NORMKURS": "994",
            "SMKURS": "1055",
            "TS": "1602738841"
        },
        {
            "0": "161",
            "1": "Lohnzuschuss",
            "2": "Wage subsidy",
            "3": "46870825501",
            "4": "50326299105",
            "5": "1602738841",
            "ITEM_ID": "161",
            "NAME_DE": "Lohnzuschuss",
            "NAME_EN": "Wage subsidy",
            "NORMKURS": "46870825501",
            "SMKURS": "50326299105",
            "TS": "1602738841"
        },
        {
            "0": "75",
            "1": "Medizintechnik",
            "2": "Medical technology",
            "3": "175381",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "75",
            "NAME_DE": "Medizintechnik",
            "NAME_EN": "Medical technology",
            "NORMKURS": "175381",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "158",
            "1": "Nachtschicht",
            "2": "Night shift",
            "3": "13816182256",
            "4": "14700000000",
            "5": "1602738841",
            "ITEM_ID": "158",
            "NAME_DE": "Nachtschicht",
            "NAME_EN": "Night shift",
            "NORMKURS": "13816182256",
            "SMKURS": "14700000000",
            "TS": "1602738841"
        },
        {
            "0": "104",
            "1": "Privatarmee",
            "2": "Private army",
            "3": "15447141",
            "4": "17198255",
            "5": "1602738841",
            "ITEM_ID": "104",
            "NAME_DE": "Privatarmee",
            "NAME_EN": "Private army",
            "NORMKURS": "15447141",
            "SMKURS": "17198255",
            "TS": "1602738841"
        },
        {
            "0": "53",
            "1": "Quarzsand",
            "2": "Quartz sand",
            "3": "1037",
            "4": "1095",
            "5": "1602738841",
            "ITEM_ID": "53",
            "NAME_DE": "Quarzsand",
            "NAME_EN": "Quartz sand",
            "NORMKURS": "1037",
            "SMKURS": "1095",
            "TS": "1602738841"
        },
        {
            "0": "42",
            "1": "Riesendiamant",
            "2": "Giant diamond",
            "3": "951060404",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "42",
            "NAME_DE": "Riesendiamant",
            "NAME_EN": "Giant diamond",
            "NORMKURS": "951060404",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "81",
            "1": "Rohdiamanten",
            "2": "Rough diamonds",
            "3": "3200",
            "4": "3570",
            "5": "1602738841",
            "ITEM_ID": "81",
            "NAME_DE": "Rohdiamanten",
            "NAME_EN": "Rough diamonds",
            "NORMKURS": "3200",
            "SMKURS": "3570",
            "TS": "1602738841"
        },
        {
            "0": "10",
            "1": "Roh\u00f6l",
            "2": "Crude oil",
            "3": "3920",
            "4": "4195",
            "5": "1602738841",
            "ITEM_ID": "10",
            "NAME_DE": "Roh\u00f6l",
            "NAME_EN": "Crude oil",
            "NORMKURS": "3920",
            "SMKURS": "4195",
            "TS": "1602738841"
        },
        {
            "0": "40",
            "1": "R\u00f6mische M\u00fcnzen",
            "2": "Roman coins",
            "3": "44665",
            "4": "51985",
            "5": "1602738841",
            "ITEM_ID": "40",
            "NAME_DE": "R\u00f6mische M\u00fcnzen",
            "NAME_EN": "Roman coins",
            "NORMKURS": "44665",
            "SMKURS": "51985",
            "TS": "1602738841"
        },
        {
            "0": "117",
            "1": "Scandrohnen",
            "2": "Scan drones",
            "3": "113490427",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "117",
            "NAME_DE": "Scandrohnen",
            "NAME_EN": "Scan drones",
            "NORMKURS": "113490427",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "84",
            "1": "Schmuck",
            "2": "Jewellery",
            "3": "2040369",
            "4": "2037756",
            "5": "1602738841",
            "ITEM_ID": "84",
            "NAME_DE": "Schmuck",
            "NAME_EN": "Jewellery",
            "NORMKURS": "2040369",
            "SMKURS": "2037756",
            "TS": "1602738841"
        },
        {
            "0": "35",
            "1": "Silber",
            "2": "Silver",
            "3": "1882",
            "4": "1905",
            "5": "1602738841",
            "ITEM_ID": "35",
            "NAME_DE": "Silber",
            "NAME_EN": "Silver",
            "NORMKURS": "1882",
            "SMKURS": "1905",
            "TS": "1602738841"
        },
        {
            "0": "15",
            "1": "Silbererz",
            "2": "Silver ore",
            "3": "1500",
            "4": "1505",
            "5": "1602738841",
            "ITEM_ID": "15",
            "NAME_DE": "Silbererz",
            "NAME_EN": "Silver ore",
            "NORMKURS": "1500",
            "SMKURS": "1505",
            "TS": "1602738841"
        },
        {
            "0": "67",
            "1": "Silizium",
            "2": "Silicon",
            "3": "128781",
            "4": "131904",
            "5": "1602738841",
            "ITEM_ID": "67",
            "NAME_DE": "Silizium",
            "NAME_EN": "Silicon",
            "NORMKURS": "128781",
            "SMKURS": "131904",
            "TS": "1602738841"
        },
        {
            "0": "30",
            "1": "Stahl",
            "2": "Steel",
            "3": "55997",
            "4": "63195",
            "5": "1602738841",
            "ITEM_ID": "30",
            "NAME_DE": "Stahl",
            "NAME_EN": "Steel",
            "NORMKURS": "55997",
            "SMKURS": "63195",
            "TS": "1602738841"
        },
        {
            "0": "44",
            "1": "Tech-Upgrade 1",
            "2": "Tech upgrade 1",
            "3": "71905756",
            "4": "76186370",
            "5": "1602738841",
            "ITEM_ID": "44",
            "NAME_DE": "Tech-Upgrade 1",
            "NAME_EN": "Tech upgrade 1",
            "NORMKURS": "71905756",
            "SMKURS": "76186370",
            "TS": "1602738841"
        },
        {
            "0": "45",
            "1": "Tech-Upgrade 2",
            "2": "Tech upgrade 2",
            "3": "200703253",
            "4": "263699955",
            "5": "1602738841",
            "ITEM_ID": "45",
            "NAME_DE": "Tech-Upgrade 2",
            "NAME_EN": "Tech upgrade 2",
            "NORMKURS": "200703253",
            "SMKURS": "263699955",
            "TS": "1602738841"
        },
        {
            "0": "46",
            "1": "Tech-Upgrade 3",
            "2": "Tech upgrade 3",
            "3": "253878259",
            "4": "345057980",
            "5": "1602738841",
            "ITEM_ID": "46",
            "NAME_DE": "Tech-Upgrade 3",
            "NAME_EN": "Tech upgrade 3",
            "NORMKURS": "253878259",
            "SMKURS": "345057980",
            "TS": "1602738841"
        },
        {
            "0": "48",
            "1": "Tech-Upgrade 4",
            "2": "Tech upgrade 4",
            "3": "102243959",
            "4": "0",
            "5": "1602738841",
            "ITEM_ID": "48",
            "NAME_DE": "Tech-Upgrade 4",
            "NAME_EN": "Tech upgrade 4",
            "NORMKURS": "102243959",
            "SMKURS": "0",
            "TS": "1602738841"
        },
        {
            "0": "51",
            "1": "Titan",
            "2": "Titanium",
            "3": "43465",
            "4": "48765",
            "5": "1602738841",
            "ITEM_ID": "51",
            "NAME_DE": "Titan",
            "NAME_EN": "Titanium",
            "NORMKURS": "43465",
            "SMKURS": "48765",
            "TS": "1602738841"
        },
        {
            "0": "159",
            "1": "\u00dcberstunden",
            "2": "Overtime",
            "3": "13662089545",
            "4": "15446797210",
            "5": "1602738841",
            "ITEM_ID": "159",
            "NAME_DE": "\u00dcberstunden",
            "NAME_EN": "Overtime",
            "NORMKURS": "13662089545",
            "SMKURS": "15446797210",
            "TS": "1602738841"
        },
        {
            "0": "96",
            "1": "Wachhunde",
            "2": "Watch dogs",
            "3": "620985",
            "4": "754630",
            "5": "1602738841",
            "ITEM_ID": "96",
            "NAME_DE": "Wachhunde",
            "NAME_EN": "Watch dogs",
            "NORMKURS": "620985",
            "SMKURS": "754630",
            "TS": "1602738841"
        },
        {
            "0": "98",
            "1": "Wachpersonal",
            "2": "Security staff",
            "3": "8336505",
            "4": "10042570",
            "5": "1602738841",
            "ITEM_ID": "98",
            "NAME_DE": "Wachpersonal",
            "NAME_EN": "Security staff",
            "NORMKURS": "8336505",
            "SMKURS": "10042570",
            "TS": "1602738841"
        },
        {
            "0": "87",
            "1": "Waffen",
            "2": "Weapons",
            "3": "283348",
            "4": "289950",
            "5": "1602738841",
            "ITEM_ID": "87",
            "NAME_DE": "Waffen",
            "NAME_EN": "Weapons",
            "NORMKURS": "283348",
            "SMKURS": "289950",
            "TS": "1602738841"
        },
        {
            "0": "43",
            "1": "Wartungskit",
            "2": "Maintenance kit",
            "3": "35856660",
            "4": "39543699",
            "5": "1602738841",
            "ITEM_ID": "43",
            "NAME_DE": "Wartungskit",
            "NAME_EN": "Maintenance kit",
            "NORMKURS": "35856660",
            "SMKURS": "39543699",
            "TS": "1602738841"
        },
        {
            "0": "24",
            "1": "Ziegel",
            "2": "Bricks",
            "3": "2740",
            "4": "2905",
            "5": "1602738841",
            "ITEM_ID": "24",
            "NAME_DE": "Ziegel",
            "NAME_EN": "Bricks",
            "NORMKURS": "2740",
            "SMKURS": "2905",
            "TS": "1602738841"
        }
    ]
