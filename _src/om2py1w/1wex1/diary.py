# -*- coding: utf-8 -*-
import sys
script, contents = sys.argv
f = open('diary.txt','a')
f.write(contents+'\n')
f.close()
