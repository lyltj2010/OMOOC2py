# -*- coding: utf-8 -*-
#!/usr/bin/env python
import time
import os

def GetTime():
	'''记录日志时间www.tutorialspoint.com/python/time_strftime.htm'''

	formatter = '%A %b %d %Y %H:%M:%S'
	return time.strftime(formatter)

def Create():
	'''为每篇日记创建单独的文件'''

	name = raw_input('Enter diary name: ')+'.txt'
	f = open(name,'a+')
	f.close()
	return name #返回日记名字，便于WriteDiary()使用

def ReadDiary(name):
	'''打印指定日记'''

	f = open(name+'.txt','r')
	print 5*'='+'Diary begins'+5*'='+'\n'
	print f.read()
	print 6*'='+'Diary ends'+6*'='+'\n'
	f.close()

def WriteDiary():
	'''写日记'''

	name = Create()
	print "少年，今天想吐槽什么？".decode('utf-8')
	f = open(name,'a+')
	t = GetTime()
	f.write(t+'\n')

	while True:
		contents = raw_input(">>")

		if contents.upper() in ['?','HELP']:
			# use \ 换行
			helpdoc = "Press ENTER to continue writing.\n"\
			+"Enter EXIT, QUIT or Q to quit.\n"\
			+"Enter HELP or '?' for help" 
			print helpdoc
		
		if contents.upper() in ['Q','QUIT','EXIT']:
			# str.lower() or str.upper() to convert
			break
		f.write(contents+'\n')
	
	f.close()

def PrintDiary():
	'''Print all files ending with .txt'''

	cwd = os.getcwd()
	file_name = os.listdir(cwd)
	name = []
	for item in file_name:
		#任性的循环
		if item.endswith('.txt'):
			temp = item.split('.txt')[0]
			# split()www.jb51.net/article/63592.htm
			name.append(temp)

	for item in name:
		ReadDiary(item)

#把独立的功能放在一个个函数里，思路清晰了不少。
PrintDiary()
WriteDiary()