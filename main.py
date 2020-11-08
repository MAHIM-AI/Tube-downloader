from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo, showwarning
from PIL import Image, ImageTk
from pytube import YouTube
from threading import *
#
root = Tk()
root.title("Tube Download")
root.iconbitmap("icon.ico")
root.geometry("500x600")
root.minsize(500, 600)
root.maxsize(500, 600)
img = Image.open("bg.jfif")
photo = ImageTk.PhotoImage(img)
im = Label(image=photo).pack()
Label(text="URL of the vedio", font=20).pack(padx=10)
url = StringVar()
urlE = Entry(textvariable=url, font=(None, 20))
urlE.pack(ipady=10, ipadx=120)
urlE.focus()
file_size = 0

def complete(stream=None, file_path=None):
    print("Downloaded")
    showinfo("Downloaded", "Downloading successful")
    db['text'] = '<Download>'
    db['state'] = "active"
def on_progress(stream=None,chunk=None,bytesRemaning=None):
    percent=(100*(file_size-bytesRemaning)/file_size)
    db['text'] = '{:00.0f}% downloaded'.format(percent)
def download():
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    try:
        yt = YouTube(url.get())
        st = yt.streams.first()
        yt.register_on_complete_callback(complete)
        yt.register_on_progress_callback(on_progress)
        file_size = st.filesize
        st.download(path_to_save)

        url.set("")
    except EXCEPTION as e:
        showwarning("Error", "Error in downloading")

def clicked():
    try:
        db['text'] = "Please wait"
        db['state'] = "disabled"
        if url.get() == '':
            showwarning("Error", 'Please give a url')
            db['text'] = '<Download>'
            db['state'] = "active"

        thread = Thread(target=download)
        thread.start()


    except EXCEPTION as e:
        showwarning("Error", "Error in downloading")
        db['text'] = '<Download>'
        db['state'] = "active"


db = Button(text="<Download>", font=('Bauhaus 93', 30), command=clicked)
db.pack(pady=60)

root.mainloop()
