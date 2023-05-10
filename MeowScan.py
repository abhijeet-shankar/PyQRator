from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import cv2
import sys
from pyzbar import pyzbar
import webbrowser
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode('black')
customtkinter.set_default_color_theme('dark-blue')

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
 
def camqr():
    messagebox.showinfo('NOTE','IF THE QR TAKES TOO LONG TO SEARCH, KINDLY CHECK YOUR QR CODE AND PRESS SPACE TO EXIT')
    str1=""
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
      ret, frame = camera.read()
      frame,str1 = read_barcodes(frame,str1)
      cv2.imshow('Barcode/QR code reader', frame)
      if str1:
        print(str1)
        break   
      if cv2.waitKey(1) & 0xFF ==ord(" "):
         cv2.destroyAllWindows()
         break
    if str1:  
      b=webbrowser.open(str1)
      cv2.destroyAllWindows()

      
def imgqr():
    try:
       str1=""
       img=filedialog.askopenfilename()
       img = cv2.imread(img, 0)
       while True:
        img,str1 = read_barcodes(img,str1)
        if str1:
           print(str1)
           #cv2.imshow('Barcode/QR code reader', img)
           b=webbrowser.open(str1)
           cv2.destroyAllWindows()
           break
        elif cv2.waitKey(1) & 0xFF ==ord(" "):
           break
        else:
           messagebox.showerror('ERROR','Sorry the given image had no QR, Please  retry with another QR code')
           break
    except:
       img== None
       messagebox.showerror('ERROR','Please enter an image containing a QR code')
       #sys.exit()
            
def choices():
  app1=customtkinter.CTk()
  app.withdraw()
  app1.geometry("200x180")
  app1.resizable(0,0)
  app1.title('Choices')
  app1['background']='#000000'
  button1 = customtkinter.CTkButton(app1, text="CameraQR search",height=30, width=45, command=camqr,border_width=2,border_color='white')
  button1.place(x=40, y=10)
  button2 = customtkinter.CTkButton(app1, text="ImageQR search",height=30, width=45, command=imgqr,border_width=2,border_color='white')
  button2.place(x=44, y=50)
  button3 = customtkinter.CTkButton(app1, text="EXIT!!",height=30, width=45, command=app1.destroy,border_width=2,border_color='white')
  button3.place(x=70, y=90)
  app1.mainloop()


app=customtkinter.CTk()
app.geometry("350x300")
app.resizable(0,0)
app.title('QR CODE SCANNER')
app['background']='#205072'

photu = ImageTk.PhotoImage(Image.open(r"meowscan.jpg"))


button = customtkinter.CTkButton(app,command=choices,height=7,border_width=4,border_color='white',image=photu)
button.pack()



label = Label(app, text='Press the above image',width=350,height=300,font= ('Helvetica',20, 'italic'),bg='black',fg='yellow')
label.pack()



app.mainloop()


