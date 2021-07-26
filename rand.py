# -*- coding:utf-8 -*-

'''
功能：斗地主玩癞子的时候生成癞子
'''

import random
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
index = random.randint(0,12)
print("癞子：",cards[index])