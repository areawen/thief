#-*-coding:utf8-*-
#
# Main program entry
# xianwen.zhang
# 2018-09-20

import os,string
import hashlib
import ftp
import etc

def is_exists_suffix(suffix):
    conf = etc.get_config()
    suffix_list = conf.get("default","suffix").strip().split(",")
    if suffix in suffix_list:
        return True
    else:
        return False

def get_drive():
    drive_list = []
    for i in range(65,91):  
        vol = chr(i) + ':'
        if os.path.isdir(vol):
            drive_list.append(vol)
    return drive_list

def get_file(path):
    try:
        if os.path.isdir(path):
            files = os.listdir(path)
            for i in files:
                if os.name == "posix":
                    f = path + "/" + i
                else:
                    f = path + "\\" + i
                if os.path.isfile(f):
                    index = i.rfind(".")
                    if index > 0:
                        suffix = i[index + 1:]
                        if is_exists_suffix(suffix):
                            upload_file(f)
            else:
                get_file(f)
    except:
        pass

def upload_file(f):
    print f

def main():
    if os.name == "nt":
        drive_list = get_drive()
        for i in drive_list:
            get_file(i)
    else:
        get_file("/Users/shiye/Desktop/test")

if __name__ == "__main__":
    main()