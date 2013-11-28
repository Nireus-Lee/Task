#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os,urllib
path = '/home/lijc/neunn.jpg'
url = "http://www.cnscn.com.cn/company/skin/default/banner.jpg"
data = urllib.urlopen(url).read()
f = file(path,"wb")
f.write(data)
f.close()
