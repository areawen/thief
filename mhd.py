#-*-coding:utf8-*-
#
# Mobile hard disk
# xianwen.zhang
# 2018-09-21

import os
import psutil
import shutil

def get_drive_mhd():
    usb_drive_list = []
    drive_list = psutil.disk_partitions()
    for i in drive_list:
        if i.opts.find("removable") > 0:
            usb_drive_list.append(i.mountpoint)
    return usb_drive_list

def get_total_size(d):
    try:
        disk_info = psutil.disk_usage(d)
        return disk_info.total
    except:
        return 0
        
def get_free_size(d):
    try:
        disk_info = psutil.disk_usage(d)
        return disk_info.free
    except:
        return 0

def upload(path,filename):
    usb_drive_list = get_drive_mhd()
    for i in usb_drive_list:
        if os.path.getsize(path + filename) < get_free_size(i):
            print path + filename
            shutil.copyfile(path + filename,i + filename)