# -*- coding: utf-8 -*-
#!/usr/bin/env python
import Tkinter as tk
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Windows():

	def __init__(self,master):
		self.master = master
		self.master.title('少年，吐槽时间到了！')
		self.CreateWidget(self.master)

	def CreateWidget(self,master):

        #创建菜单
		self.menu = tk.Menu(master)
		self.master.config(menu=self.menu)

		self.file_menu = tk.Menu(master)
		self.menu.add_cascade(label='File',menu=self.file_menu)
		self.file_menu.add_command(label='New',command=self.foo)
		self.file_menu.add_command(label='Open',command=self.foo)
		self.file_menu.add_command(label='Save',command=self.foo)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Exit',command=self.foo)

		self.help_menu = tk.Menu(master)
		self.menu.add_cascade(label='Help',menu=self.help_menu)
		self.help_menu.add_command(label='Guide',command=self.foo)

		self.top_frame = tk.Frame(master)
		self.top_frame.pack()
		self.welcome_label = tk.Label(self.top_frame,text='Welcome to Diary World!')
		self.welcome_label.pack()

		#创建内容text窗口
		self.bottom_frame = tk.Frame(master)
		self.bottom_frame.pack()

		self.content_label = tk.Label(self.bottom_frame,text="内容")
		self.content_label.pack(side='left')

		self.scrollbar = tk.Scrollbar(self.bottom_frame)
		self.scrollbar.pack(side='right',fill='y')
		self.content = tk.Text(self.bottom_frame,yscrollcommand=self.scrollbar.set)
		self.content.pack()
		self.scrollbar.config(command=self.content.yview)

	def foo():
		pass
		return None


def main():
	root = tk.Tk()
	app = Windows(root)
	root.mainloop()

if __name__ == "__main__":
	main()