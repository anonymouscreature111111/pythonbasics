from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title("My photo album")
window.geometry("400x200")

title  = Label(window, text="My Photo album", fg="white", bg="purple", width=40)
title.pack(pady=10)
img_file = Image.open('lisa.jpg')
img_file = img_file.resize((300,180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo("Great", "You clicked the photo!")
msg_btn = Button(window, text="Click to react", bg="blue", fg="white", command=show_message)
msg_btn.pack(pady=5)

def show_details():
    top = Toplevel()
    top.title("Photo Details")
    top.geometry("200x120")
    info = Label(top, text="Taken on: 1 Jume 2025")
    info.pack(pady=10)
    place = Label(top, text="Location: My garden")
    place.pack()
    top.mainloop()
details_btn = Button(window, text="See details", bg="green", fg="white", command=show_details)
details_btn.pack(pady=5)
window.mainloop()