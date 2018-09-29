#-*-coding:utf8-*-
#
# Get config file
# xianwen.zhang
# 2018-09-20

import os,sys
import configparser

def get_config():
    if os.path.exists("thief.conf"):
        conf = configparser.ConfigParser()
        conf.read("thief.conf")
        return conf
    else:
        sys.exit(-1)