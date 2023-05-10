from flask import Flask, jsonify, render_template, request
app = Flask(__name__, template_folder='meow')

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import cv2
import sys
from pyzbar import pyzbar
import webbrowser
from PIL import ImageTk,Image




@app.route('/')
def index():
   return render_template('index.html')


@app.route('/home')
def home():
   return render_template('iindex.html')






def read_barcodes(frame,str1):
   barcodes = pyzbar.decode(frame)
   for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        for i in barcode_info:
               str1+= i
               font = cv2.FONT_HERSHEY_DUPLEX
               cv2.putText(frame, barcode_info, (x + 3, y - 1), font, 1.0, (255, 255, 255), 1)   
   return frame,str1
 






@app.route('/camqr',methods=["POST","GET"])
def camqr():
    meow=Tk()
    meow.attributes("-topmost", True)
    messagebox.showinfo('NOTE','IF THE QR TAKES TOO LONG TO SEARCH, KINDLY CHECK YOUR QR CODE AND PRESS SPACE TO EXIT')
    meow.destroy()
    meow.mainloop()
    str1=""
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
      ret, frame = camera.read()
      frame,str1 = read_barcodes(frame,str1)
      cv2.imshow('Barcode/QR code reader', frame)
      if str1:
        #hehe.destroy()
        #print(str1)
        #meow.destroy()
        cv2.destroyAllWindows()
        break   
      if cv2.waitKey(1) & 0xFF ==ord(" "):
         cv2.destroyAllWindows()
         #meow.destroy()
         break
    if str1:  
      b=webbrowser.open(str1)
      cv2.destroyAllWindows()
      #meow.destroy()
      str1=""
   # meow.destroy()   
##    else:
##      messagebox.showerror('ERROR','Sorry the given image had no QR, Please retry with another QR code')
##      cv2.destroyAllWindows()
   # meow.mainloop()
    return  render_template('index.html')





@app.route('/imgqr',methods=["POST","GET"])      
def imgqr():
    try:
       str1=""
       heh=Tk()
       heh.attributes("-topmost",True)
       img=filedialog.askopenfilename()
       img = cv2.imread(img, 0)
       while True:
        img,str1 = read_barcodes(img,str1)
        if str1:
           heh.destroy()
           print(str1)
           #cv2.imshow('Barcode/QR code reader', img)
           b=webbrowser.open(str1)
           cv2.destroyAllWindows()
           str1=""
           break
        elif cv2.waitKey(1) & 0xFF ==ord(" "):
           break
        else:
           goo=Tk()
           goo.attributes("-topmost",True)
           messagebox.showerror('ERROR','Sorry the given image had no QR, Please  retry with another QR code')
           goo.destroy()
           heh.destroy()
           goo.mainloop()
           break
       heh.mainloop()
    except:
       heh.destroy()
       goo=Tk()
       goo.attributes("-topmost",True)
       messagebox.showerror('ERROR',' Please  enter an image with QR code')
       goo.after(200,goo.destroy())
       goo.mainloop()
    return  render_template('index.html')





if __name__ == '__main__':
   app.run(debug=True,port=6969)