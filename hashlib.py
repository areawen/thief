#-*-coding:utf8-*-
#
# Hashlib model
# xianwen.zhang
# 2018-09-21

import os
import hashlib

def get_sha1(f):
    xd = open(f,"rb").read() 
    gys = xd
    sha1 = hashlib.sha1(gys) 
    osv = sha1.hexdigest() 
    print(osv)
    bx = bytes(osv,encoding='utf-8') 
    with open(f,'wb') as f:
        f.write(bx)