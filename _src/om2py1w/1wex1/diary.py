# -*- coding: utf-8 -*-
import sys

fr = open('diary.txt','r')
for line in fr:
	print line,
fr.close()

script, contents = sys.argv
fw = open('diary.txt','a+')
fw.write(contents+'\n')
fw.close()
