# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:59:16 2018

@author: bharg
"""

import zipfile
import optparse
from threading import Thread

def extractFile(zfile,password):
    try:
        zfile.extractall(pwd=password)
        print " The password found for the zip file is %s"%(password)
    except:
        pass
def main():
    #opening a zip file
    parser = optparse.OptionParser("Usage: %s" %("-f <zipfile> -d <dictionary>"))
    parser.add_option('-f', dest='zname', type='string', help = 'specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname==None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        zfile = zipfile.ZipFile(zname)
        passfile = open(dname, 'r')
        for line in passfile.readlines():
          password = line.strip("\n")
          t=Thread(target=extractFile, args=(zfile,password))
          t.start()
        
if __name__ == '__main__':
    main()