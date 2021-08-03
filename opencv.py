import cv2 as cv
#For reading an image 
img=cv.imread('D:\ABHIR\Pictures(Snip)\whiplash.jpg')#Path of the image
cv.imshow('Nethan',img)#Show the image
cv.waitKey(0)
#for reaing a video and displaying it
c=cv.VideoCapture('D:\Python\Squirrel On A Wood.mp4')#0 web cam 1 the first cam connected to the computer 2 the 2nd and so on. Or else the path of the video.
while True:
    isTrue, frame = c.read()#For reading each fram while true and then displaying the image with a time delay of 0. 
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'): #If the letter d is pressed then break out of the loop and then end this video by releasing it. 
        break
c.release()
cv.destroyAllWindows()
#-215 assertion error means that the path of the file was not found.

#Resizing and rescaling
img = cv.imread('D:\ABHIR\Pictures(Snip)\whiplash.jpg')#Path of the image.
def rescale(frame, t,m):
    #This method will work forimage, video and live videos
    width=int(frame.shape[1]*t)#Width of thbe image is resized to 0.75 of its original value
    height=int(frame.shape[0]* m)#Height of the scale is resized to the 0.75 of its original value
    dim =(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
cv.imshow('Whilplash',rescale(img,0.5,0.5))
c=cv.VideoCapture('D:\Python\Squirrel On A Wood.mp4')#0 web cam 1 the first cam connected to the computer 2 the 2nd and so on
t=float(input("Enter the width resolution of the video you want : "))
m=float(input("Enter the height resolution of the video you want : "))
while True:
    isTrue, frame = c.read()#For reading each fram while true and then displaying the image with a time delay of 0. 
    frame_resized=rescale(frame,t,m)
    cv.imshow('video',frame)
    cv.imshow('Video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #If the letter d is pressed then break out of the loop and then end this video by releasing it. 
        break
c.release()
#In case of live video. Like the webcam.
cv.destroyAllWindows()
def res(width,height):
    #The live video only
    c.set(3,width)
    c.set(4,height)
    #3 and 4 represent the width and height of the video resp.
#For creating a solid border images.
import numpy as np
img = cv.imread('D:\ABHIR\Pictures(Snip)\whiplash.jpg')
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
cv.imshow('Whiplash',img)
blank[2:30,300:400]=0,225,0
cv.rectangle(blank,(0,0),(250,250),(0,225,0),thickness=2)
cv.imshow('Green',blank)
cv.waitKey(0)
