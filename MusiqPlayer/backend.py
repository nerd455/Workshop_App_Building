import glob
import os
from tkinter import *
from pygame import mixer

songList = [""]
song = 0
playing = False


def init_ui():
    global status, btn_next, btn_play, btn_prev, btn_add, song, songList, playing, txt
    playing = False
    songList = [""]
    song = 0
    status.configure(text="Nothing to play !!!")
    txt.configure(state="normal")
    txt.delete(0, END)
    txt.insert(0, "Enter directory:")
    btn_add.configure(state="normal")
    btn_prev.configure(state="disabled")
    btn_next.configure(state="disabled")
    btn_play.configure(state="disabled")
    mixer.init()
    mixer.music.stop()


def on_add_click():
    global txt, status, btn_play, btn_next, btn_prev, song, songList, playing
    path = txt.get()
    for filename in glob.glob(os.path.join(path, '*.mp3')):
        songList.append(filename)
    if len(songList) != 1:
        print(songList)
        txt.configure(state="disabled")
        btn_add.configure(state="disabled")
        btn_prev.configure(state="normal")
        btn_next.configure(state="normal")
        btn_play.configure(state="normal", text="pause")
        song += 1
        current_song = songList[song].split('/')
        status.configure(text="Playing: "+current_song[len(current_song)-1])
        mixer.init()
        mixer.music.load(songList[song])
        mixer.music.play()
        playing = True


def on_reset_click():
    init_ui()
    print("reset")


def on_play_click():
    global txt, status, btn_play, btn_next, btn_prev, song, songList, playing
    if playing:
        mixer.music.pause()
        playing = False
        btn_next.configure(state="disabled")
        btn_prev.configure(state="disabled")
        btn_play.configure(text="play")
        status.configure(text="Paused")
    else:
        mixer.music.unpause()
        playing = True
        btn_next.configure(state="normal")
        btn_prev.configure(state="normal")
        btn_play.configure(text="pause")
        current_song = songList[song].split('/')
        status.configure(text="Playing: " + current_song[len(current_song) - 1])
    print("play")


def on_next_click():
    global txt, status, btn_play, btn_next, btn_prev, song, songList
    print("next")
    if song == len(songList)-1:
        song = 0
    song += 1
    current_song = songList[song].split('/')
    status.configure(text="Playing: " + current_song[len(current_song) - 1])
    mixer.init()
    mixer.music.load(songList[song])
    mixer.music.play()


def on_prev_click():
    global txt, status, btn_play, btn_next, btn_prev, song, songList
    print("prev")
    if song == 1:
        song = len(songList)
    song -= 1
    current_song = songList[song].split('/')
    status.configure(text="Playing: " + current_song[len(current_song) - 1])
    mixer.init()
    mixer.music.load(songList[song])
    mixer.music.play()


window = Tk()
window.title("Musiq Player")
window.resizable(False, False)

t_frame = Frame(window, borderwidth=5, relief=FLAT)
b_frame = Frame(window, borderwidth=5, relief=FLAT)
status = Label(window, text="Nothing to play !!!", borderwidth=5, relief=FLAT)

txt = Entry(t_frame, width=30, borderwidth=5, relief=FLAT)
btn_add = Button(t_frame, text="Add", command=on_add_click)
btn_re = Button(t_frame, text="Reset", command=on_reset_click)
btn_prev = Button(b_frame, text="prev", command=on_prev_click)
btn_play = Button(b_frame, text="play", command=on_play_click)
btn_next = Button(b_frame, text="next", command=on_next_click)

t_frame.pack()
b_frame.pack()
status.pack(side=LEFT)
txt.pack(side=LEFT)
btn_add.pack(side=LEFT)
btn_re.pack(side=LEFT)
btn_prev.pack(side=LEFT)
btn_play.pack(side=LEFT)
btn_next.pack(side=RIGHT)

init_ui()
window.mainloop()
