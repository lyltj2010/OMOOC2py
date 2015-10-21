# -*- coding: utf-8 -*-

fr = open('diary.txt','r')
for line in fr:
	print line,
print
fr.close()

contents = raw_input("Anything want to share?\n")
fw = open('diary.txt','a+')
fw.write(contents+'\n')
fw.close()
