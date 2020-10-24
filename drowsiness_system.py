import numpy
from pygame import mixer
import time
import cv2
from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry('400x600')
frame=Frame(root,relief=RIDGE,border=5)
frame.pack(fill=BOTH,expand=1)
label=Label(frame,text="DRIVER CAM",bg="black",fg="white",font=("times new roman",35,"bold"))
label.pack(fill=X)
frame.config(background="black")
def hel():
    help(cv2)
def anotherWin():
    messagebox.showinfo("Information","This is a 2.10 edition made by Microsoft Comapany Limited \n providing people the software \n For more information please remain up to date.")

menu=Menu(root)
root.config(menu=menu)

sub=Menu(menu)
menu.add_cascade(label="Tools",menu=sub)
sub.add_command(label="open cv docs",command=hel)

sub1=Menu(menu)
menu.add_cascade(label="About",menu=sub1)
sub1.add_command(label="Driver cam",command=anotherWin)

def exitt():
    exit()
def web(): # just do recording 
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",gray)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
    cap.release()
    cv2.destroyAllWindows()
    
def webrec():#do a recording and save it
    cap=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter("sample.avi",fourcc,11.0,(640,480))
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame1",frame)
        out.write(frame)
        if cv2.waitKey(1)==ord('q'):
           break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
def webdet():
    cap=cv2.VideoCapture(0)
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    while(cap.isOpened()):
      _,img=cap.read()
      gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      faces=face_cascade.detectMultiScale(gray,1.1,8)

      for(x,y,w,h) in faces:
          font=cv2.FONT_HERSHEY_COMPLEX
          cv2.putText(img,"Face",(x+w,y+h),font,1,(250,250,250),2)
          cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
          roi_gray=gray[y:y+h,x:x+w]
          roi_color=img[y:y+h,x:x+w]
        
          eyes=eye_cascade.detectMultiScale(roi_gray,1.1,8)
          for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
     #output displayed       
      cv2.imshow('img',img)
      if (cv2.waitKey(1)== ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

def webdetRec():
    cap=cv2.VideoCapture(0)
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter("sample2.avi",fourcc,11.0,(640,480))
    while(cap.isOpened()):
     _,img=cap.read()
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces=face_cascade.detectMultiScale(gray,1.1,8)
     for(x,y,w,h) in faces:
       font=cv2.FONT_HERSHEY_COMPLEX
       cv2.putText(img,"Face",(x+w,y+h),font,1,(250,250,250),2)  
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
       roi_gray=gray[y:y+h,x:x+w]
       roi_color=img[y:y+h,x:x+w]
       eyes=eye_cascade.detectMultiScale(roi_gray,1.1,8)
       for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
           out.write(img)
     #output displayed       
     cv2.imshow('img',img)
     if cv2.waitKey(1)== ord('q'):
         break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def alert():
    mixer.init()
    alert=mixer.Sound('beep-07.wav')
    alert.play()
    time.sleep(0.01)
    alert.play()
def blink():
    cap=cv2.VideoCapture(0)
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    blink_cascade=cv2.CascadeClassifier('CustomBlinkCascade.xml')
    while(cap.isOpened()):
     _,img=cap.read()
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces=face_cascade.detectMultiScale(gray,1.1,8)
     for(x,y,w,h) in faces:
       font=cv2.FONT_HERSHEY_COMPLEX
       cv2.putText(img,"Face",(x+w,y+h),font,1,(250,250,250),2)
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
       roi_gray=gray[y:y+h,x:x+w]
       roi_color=img[y:y+h,x:x+w]
       
       eyes=eye_cascade.detectMultiScale(roi_gray,1.1,15)
       for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)
           
       blink=blink_cascade.detectMultiScale(roi_gray,1.1,15)
       for(eyx,eyy,eyw,eyh) in blink:
          cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(0,255,0),3)
          alert()
     #output displayed       
     cv2.imshow('img',img)
     if cv2.waitKey(1)== ord('q'):
         break
    cap.release()
    cv2.destroyAllWindows()


b1=Button(frame,padx=5,pady=5,width=39,bg="white",fg="black",relief=GROOVE,command=web,text="OPEN CAM",font=("times new roman",20))
b1.pack(fill=BOTH,pady=10)

b2=Button(frame,padx=5,pady=5,width=39,bg="white",fg="black",relief=GROOVE,command=webrec,text="OPEN CAM AND RECORD",font=("times new roman",20))
b2.pack(fill=BOTH,pady=10)

b3=Button(frame,padx=5,pady=5,width=39,bg="white",fg="black",relief=GROOVE,command=webdet,text="OPEN CAM AND DETECT",font=("times new roman",20))
b3.pack(fill=BOTH,pady=10)

b4=Button(frame,padx=5,pady=5,width=39,bg="white",fg="black",relief=GROOVE,command=webdetRec,text="DETECT AND RECORD ",font=("times new roman",20))
b4.pack(fill=BOTH,pady=10)

b4=Button(frame,padx=5,pady=5,width=39,bg="white",fg="black",relief=GROOVE,command=blink,text="DETECT EYE BLINK AND RECORD ",font=("times new roman",15))
b4.pack(fill=BOTH,pady=10)

b4=Button(frame,padx=5,pady=5,width=39,bg="white",fg="black",relief=GROOVE,command=exitt,text="EXIT",font=("times new roman",20))
b4.pack(fill=BOTH,pady=10)
    
root.mainloop()






