# -*- coding: utf-8 -*-
#!/usr/bin/env python
import Tkinter as tk

class Windows():

	def __init__(self,master):
		self.master = master
		self.master.title('少年，吐槽时间到了！')

		self.top_frame = tk.Frame(self.master)
		self.name_label = tk.Label(self.top_frame,text='日记名称')
		self.name_entry = tk.Entry(self.top_frame)
		self.top_frame.pack()
		self.name_label.grid(row=0,column=0)
		self.name_entry.grid(row=0,column=1)


		self.middle_frame = tk.Frame(self.master)
		self.content_label = tk.Label(self.middle_frame,text="内容")
		self.content_text = tk.Text(self.middle_frame)
		self.middle_frame.pack()
		self.content_label.grid(row=0,column=0)
		self.content_text.grid(row=0,column=1)

		self.bottom_frame = tk.Frame(self.master)
		self.menu_label_1 = tk.Button(self.bottom_frame,text="Save",bg='grey')
		self.menu_label_2 = tk.Button(self.bottom_frame,text="Discard",bg='red')
		self.menu_label_3 = tk.Button(self.bottom_frame,text="About",bg='grey')
		self.bottom_frame.pack()
		self.menu_label_1.grid(row=0,column=0)
		self.menu_label_2.grid(row=0,column=1)
		self.menu_label_3.grid(row=0,column=2)

	def foo():
		pass
		

def main():
	root = tk.Tk()
	app = Windows(root)
	root.mainloop()

if __name__ == "__main__":
	main()