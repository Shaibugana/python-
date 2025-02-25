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
    # create canvas to display image
canvas2 = Canvas(root,width="600",height="420",relief=RIDGE,bd=2)
canvas2.place(x=15,y=150)

# create buttons
btn1 = Button(root,text="Select Image",bg='black',fg='gold',font=('ariel 15 bold'),relief=GROOVE,command=select)
btn1.place(x=100,y=595)
btn2 = Button(root,text="Save",width=12,bg='black',fg='gold',font=('ariel 15 bold'),relief=GROOVE,command=save)
btn2.place(x=280,y=595)
btn3 = Button(root,text="Exit",width=12,bg='black',fg='gold',font=('ariel 15 bold'),relief=GROOVE,command=root.destroy)
btn3.place(x=460,y=595)

# Execute Tkinter
root.mainloop()
file=input('file')
image=cv2.imread(file)
cv2.imshow(file,image)

def resize():
    w_image =int(input('width'))
    h_image = int(input('height'))
    height,width = h_image,w_image
    imgresive = cv2.resize(image,(height,width))
    print(imgresive)
    cv2.imshow('image resized',imgressive)
def bright():
    image.cropped = image[int(input()),int(input())]
    print('work')
    cv2.imshow('crop',image.cropped)

list = [resize,bright]
for i in list:
    print(i)

option = input('choose')

if option =='resize':
    resize()
elif option == 'bright':
    bright()

cv2.waitkey(0)
cv2.destroyAllWindows()
# importing module from PIL import ImageColor

# using getrgb for red img2 = ImageColor.getcolor("red",'L')
print(img2)

# code that turns it to black and white
img = cv2.imread(pic)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
status = cv2.imwrite(pic,gray_img)

cv2.imshow("Original",img)
cv2.imshow("Gray Scaled",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    canvas2.image = img1
def blur(event):  # The Blur effect
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1


def brightness(event):  # The brightness effect
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        canvas2.create_image(300, 210, image=img3)
        canvas2.image = img3
 def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        canvas2.create_image(300, 210, image=img5)
        canvas2.image = img5


def rotate(event):
    global img_path, img6, img7
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img6 = img.rotate(int(rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    canvas2.create_image(300, 210, image=img7)
    canvas2.image = img7


def flip(event):
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
        img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
        img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img9 = ImageTk.PhotoImage(img8)
    canvas2.create_image(300, 210, image=img9)
    canvas2.image = img9


def border(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image = img11
