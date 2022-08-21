# %%
import tkinter,requests
import pytube
from pytube import YouTube
from tkinter import *
from PIL import ImageTk, Image

# %%

def getYoutubeobject(url):
    yt=YouTube(url)
    return yt
def submit():
    url=txt.get()
    ytobject=getYoutubeobject(url)
    label2.configure(text=ytobject.title)
    img=ImageTk.PhotoImage(Image.open(requests.get(ytobject.thumbnail_url, stream=True).raw))
    labelimg=tkinter.Label(frame1,image=img,height=300,width=400)
    labelimg.image=img
    labelimg.grid(row=5,column=0)
    downbtn.grid(row=6,column=0)
def download():
    url=txt.get()
    ytobject=getYoutubeobject(url)
    stream = ytobject.streams.get_by_itag(22)
    stream.download()


# %%

window=tkinter.Tk()
frame1=Frame(window)
window.title("YouTube Video Downloader")
window.geometry("500x500")
frame1=Frame(window)
frame1.pack()
title=tkinter.Label(frame1,text="YouTube Video Downloader",font=("Arial Bold",22))
title.grid(row=0,pady=30)
label1=tkinter.Label(frame1,text="Enter url of Video:",font=("Arial",15))
label1.grid(row = 1, column = 0, sticky = W, pady = 2)
txt=tkinter.Entry(frame1,width=70)
txt.grid(row=2,column=0,padx=10)
submitbtn=tkinter.Button(frame1,text="Enter",command=submit)
submitbtn.grid(row=2,column=1,sticky='w')
label1=tkinter.Label(frame1,text="Video Title:",font=("Arial",15))
label1.grid(row=3,column=0,sticky="w")
label2=tkinter.Label(frame1,text="",font=("Arial",10))
label2.grid(row=4)
downbtn=tkinter.Button(frame1,text="Click to Download",command=download)


window.mainloop()


