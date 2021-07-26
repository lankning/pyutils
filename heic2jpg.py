# -*- coding:utf-8 -*-

'''
功能：将.HEIC文件转为.JPG文件，批量处理
'''

import os, pyheif
from PIL import Image 
import numpy as np

ins = './heics'
outs = './outs'

if bool(1-os.path.exists(outs)):
    os.mkdir(outs)

imgs = os.listdir(ins)
for i in imgs:
    try:
        heif_file = pyheif.read(os.path.join(ins,i))
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )
        # 如果需要去除元数据，降低图片大小，开启下方2行注释
        # img = np.array(image) # 转化成numpy数组
        # img = Image.fromarray(np.uint8(img),"RGB")
        img.save(os.path.join(outs,i.split(".")[0]+'.jpg'))
        print("Success: %s" % i,"shape: ",np.shape(img))
    except:
        print("Fail: %s" % i)