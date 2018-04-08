__author__ = 'Xin'
# -*- coding: utf-8 -*-
import os
import shutil
import re

def pathWalk(rootDir):
    list_dirs = os.walk(rootDir)
    filelist = []
    for root, dirs, files in list_dirs:
        for f in files:
            filelist.append(os.path.join(root, f))
            #print f
        #print root, dirs
    return filelist

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

def pathFileMove(rootDir,pat):
    f = pathWalk(rootDir)
    saveDir = r'E:\UnionPayProject\randomForest\data\StatTestData\hubFolder\\'
    for i in f:
        if re.match(pat,i):
            shutil.move(i,saveDir)

if __name__ == '__main__':
    #'E:\\UnionPayProject\\randomForest\\trainTree\\'
    # pathFileMove(r'E:\UnionPayProject\randomForest\data\StatTestData\elkiData',r'.*norm.*txt\b')
    fs = pathWalk('/media/xinxin/文档/电脑原文件/bjsyq/')
    with open('fileTex.txt','w') as fw:
        for i in fs:
            fw.write(i+'\n')


    #print re.match(r".*norm.*txt\b",r"txthnormtxt")
    #f = pathWalk(r'E:\UnionPayProject\randomForest\data\StatTestData\elkiData')
    """

    for fname in f:
        stream = open(fname)
        while( not re.match(r'.*DATA',stream.readline())):
            continue
        fsave = open(fname.split('.')[0]+'.txt','w')
        line = stream.readline()
        while line:
            fsave.write(line)
            line = stream.readline()
        fsave.close()"""

