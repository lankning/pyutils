# -*- coding:utf-8 -*-

'''
功能：将ins文件夹内的文件按照一定规则批量重命名
'''

import os

ins = "ins"
outs = 'outs'

files = os.listdir(ins)
for f in files:
    # print(os.path.join(ins,f))
    print(f[5:-16])
    newname = f[5:-16]+'.mp4'
    os.rename(os.path.join(ins,f),os.path.join(outs,newname))
