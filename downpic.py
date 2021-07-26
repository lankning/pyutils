# -*- coding:utf-8 -*-

'''
功能：去除与图片本身无关的数据以降低图片的大小，批量处理
'''

import os
from PIL import Image 
import numpy as np

ins = './pics'
outs = './outs'

if bool(1-os.path.exists(outs)):
    os.mkdir(outs)

imgs = os.listdir(ins)
for i in imgs:
    image = Image.open(os.path.join(ins,i)) # 用PIL中的Image.open打开图像
    img = np.array(image) # 转化成numpy数组
    img = Image.fromarray(np.uint8(img),"RGB")
    img.save(os.path.join(outs,i))