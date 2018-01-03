#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
sdir = set()
sdirlen = set()
sname = set()
def get_name(line):
    return line.split(',')[0].split('/')[-1].split('.mp4')[0]

def get_dir_list(filename):
    '''
    通过文件解析出所有url涉及的目录路径，
    并将路径存放在列表中返回
    '''
    f = open(filename,'r')
    for line in f:
        url = line.split(',')[0]
        url_dir = re.match(r'http://.*/',url).group()
        sdir.add(url_dir)
    f.close()
    return list(sdir)

def get_easy_list():
    l1 = get_dir_list(filename)

if __name__ == '__main__':
    filename = 'list5.csv'
    l1 = get_dir_list(filename)
    for i in l1:
        f = open(filename,'r')
        list_i = re.findall(i+'.*',f.read())
        print i,len(list_i)


#f = open('list5.csv','r')
#for line in f:
#    url = line.split(',')[0]
#    url_dir = re.match(r'http://.*/',url).group()
#    sdir.add(url_dir)
#    name = get_name(line)
#    sdirlen.add(len(line.split(',')[0].split('/')))
#    sname.add(len(name))
#    if len(name) <= 4:
#        print line
#f.close()
#print sdir
#print len(sdir)
#print sdirlen
#print sname

