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
