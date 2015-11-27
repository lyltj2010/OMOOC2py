doc =  \
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
count = {}
for word in doc.split():
	count[word] = count.get(word,0)+1
print count