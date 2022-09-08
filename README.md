#cropping an image in the photoeditor
import cv2
#read input image
img = cv2.imread(input('enter your picture file name: '))
#check the type of read image
print(type(img))
#shape of the image
print('Shape of the image',img.shape)
#[rows,columns]
crop = img[50:180 , 100:300]
#Display the image
cv2.imshow('original',img)
cv2.imshow('cropped',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

# Create a Tkinter window
root = Tk()  # Create a window
root.title("Photo Editor App")  # Set the title of the window
root.geometry("640x640")  # Set the size of the window


def select():  # Load images from the computer
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1
