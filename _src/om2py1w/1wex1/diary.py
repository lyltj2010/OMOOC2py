# -*- coding: utf-8 -*-

fr = open('diary.txt','r')
for line in fr:
	print line,
print
fr.close()

contents = raw_input("Anything want to share?\n")
fw = open('diary.txt','a+')
fw.write(contents+'\n')

while True:
	yn = raw_input('Do you wanna share more?(y/n)')
	if yn == 'n':
		break
	elif yn == 'y':
		contents = raw_input("Okay, let's share more!\n")
		fw.write(contents+'\n')
	else:
		print "Please type in 'y' or 'n'."

fw.close()
