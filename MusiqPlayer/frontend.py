from tkinter import *

window = Tk()

window.title("Musiq Player")
window.resizable(False, False)

t_frame = Frame(window, borderwidth=5, relief=FLAT)
b_frame = Frame(window, borderwidth=5, relief=FLAT)
status = Label(window, text="Nothing to play !!!", borderwidth=5, relief=FLAT)

txt = Entry(t_frame, width=30, borderwidth=5, relief=FLAT)
btn_add = Button(t_frame, text="Add")
btn_re = Button(t_frame, text="Reset")
btn_prev = Button(b_frame, text="prev")
btn_play = Button(b_frame, text="play")
btn_next = Button(b_frame, text="next")

t_frame.pack()
b_frame.pack()
status.pack(side=LEFT)
txt.pack(side=LEFT)
btn_add.pack(side=LEFT)
btn_re.pack(side=LEFT)
btn_prev.pack(side=LEFT)
btn_play.pack(side=LEFT)
btn_next.pack(side=RIGHT)

window.mainloop()
