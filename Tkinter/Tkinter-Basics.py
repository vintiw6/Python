from tkinter import *
from PIL import ImageTk, Image
# A library used import image 


root = Tk()
# root is the variable which is an object of Tk class

root.title("Login Form")
# To change title

# root.iconbitmap('whatever')
# to change the logo in the window

root.minsize(400,400)
# this help in limiting the size till a minimum amount

root.maxsize(1920,1080)
# similar to minsize this is max version

# To create a particular size window we use geomerty function
root.geometry('1280x720')

# To change the background colours we use configure function then background atrribute
root.configure(background='#000096')

# This line below inserts an image into the page
img = (Image.open('Screenshot 2024-05-30 003732.png'))
resized_image = img.resize((480,720))
# .resize functions help in resizing the image
img = ImageTk.PhotoImage(resized_image)

# Label function helps in dislpaying the image on the page
img_label = Label(root,image=img)
# pack fucntion is used as geometry manager
img_label.pack(pady=(10,10))

text_label = Label(root,text="PARTH")
text_label.pack()







root.mainloop()
# this makes the screen appear contsantly as it is a loop

