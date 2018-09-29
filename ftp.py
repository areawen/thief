#-*-coding:utf8-*-
#
# FTP 
# xianwen.zhang
# 2018-09-20

import os
import ftplib
import etc

def connect():
    try:
        conf     = etc.get_config()
        host     = conf.get("ftp","host") 
        post     = conf.get("ftp","post") 
        username = conf.get("ftp","username") 
        password = conf.get("ftp","password")
        timeout  = conf.get("ftp","timeout")
        ftp = ftplib.FTP() 
        ftp.set_debuglevel(2) 
        ftp.connect(host, post, timeout) 
        ftp.login(username, password) 
        return ftp
    except:
        pass

def upload(path,filename): 
    try:
        f = path + filename
        ftp = connect()
        bufsize = 1024
        file_handler = open(f, 'rb') 
        ftp.storbinary('STOR %s' % os.path.basename(f),file_handler,bufsize) 
        ftp.set_debuglevel(0) 
        file_handler.close() 
        ftp.quit()
    except:
        pass