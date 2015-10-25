# -*- coding: utf-8 -*-
#!/usr/bin/env python


def ReadDiary():
	f = open('MyDiary.txt','r')
	print 5*'='+'Diary begins'+5*'='

	for line in f:
		print line,
	print 6*'='+'Diary ends'+6*'='+'\n'

	f.close()

def WriteDiary():
	print "Anything want to share?"
	f = open('MyDiary.txt','a+')

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

#把独立的功能放在一个个函数里，思路清晰了不少。
ReadDiary()
WriteDiary()
