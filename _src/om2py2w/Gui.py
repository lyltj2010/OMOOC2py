# -*- coding: utf-8 -*-
#!/usr/bin/env python
from Tkinter import *
root = Tk()
root.title('少年，吐槽时间到了！')

top_frame = Frame(root)
top_frame.pack()
middle_frame = Frame(root)
middle_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

mood_label = Label(top_frame,text='心情:')
a = Checkbutton(top_frame,text='好')
b = Checkbutton(top_frame,text='中')
c = Checkbutton(top_frame,text='差')
mood_label.grid(row=0,column=0)
a.grid(row=0,column=1)
b.grid(row=0,column=2)
c.grid(row=0,column=3)
blank_label = Label(top_frame,text=40*' ')
blank_label.grid(row=0,column=4)
weather_label = Label(top_frame,text='天气:')
a_1 = Checkbutton(top_frame,text='晴')
b_1 = Checkbutton(top_frame,text='阴天')
c_1 = Checkbutton(top_frame,text='雨雪')
weather_label.grid(row=0,column=5)
a_1.grid(row=0,column=6)
b_1.grid(row=0,column=7)
c_1.grid(row=0,column=8)

name_label = Label(middle_frame,text='日记名称')
name_entry = Entry(middle_frame)
name_label.grid(row=0,column=0,sticky=E)
name_entry.grid(row=0,column=1)

content_label = Label(bottom_frame,text="内容")
content_text = Text(bottom_frame)
content_label.grid(row=0,column=0)
content_text.grid(row=0,column=1)

root.mainloop()