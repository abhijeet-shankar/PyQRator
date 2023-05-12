import qrcode
from PIL import ImageTk, Image
import webbrowser
from pyzbar import pyzbar
import sys
import cv2
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from flask import Flask, jsonify, render_template, request, send_file
app = Flask(__name__, template_folder='meow')


global basewidth
basewidth = 100


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


def read_barcodes(frame, str1):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        for i in barcode_info:
            str1 += i
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 3, y - 1),
                        font, 1.0, (255, 255, 255), 1)
    return frame, str1


@app.route('/camqr', methods=["POST", "GET"])
def camqr():
    meow = Tk()
    meow.attributes("-topmost", True)
    messagebox.showinfo(
        'NOTE', 'IF THE QR TAKES TOO LONG TO SEARCH, KINDLY CHECK YOUR QR CODE AND PRESS SPACE TO EXIT')
    meow.destroy()
    meow.mainloop()
    str1 = ""
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame, str1 = read_barcodes(frame, str1)
        cv2.imshow('Barcode/QR code reader', frame)
        if str1:
            # hehe.destroy()
            # print(str1)
            # meow.destroy()
            cv2.destroyAllWindows()
            break
        if cv2.waitKey(1) & 0xFF == ord(" "):
            cv2.destroyAllWindows()
            # meow.destroy()
            break
    if str1:
        b = webbrowser.open(str1)
        cv2.destroyAllWindows()
        # meow.destroy()
        str1 = ""
    # meow.destroy()
# else:
# messagebox.showerror('ERROR','Sorry the given image had no QR, Please retry with another QR code')
# cv2.destroyAllWindows()
    # meow.mainloop()
    return render_template('index.html')


@app.route('/imgqr', methods=["POST", "GET"])
def imgqr():
    try:
        str1 = ""
        heh = Tk()
        heh.attributes("-topmost", True)
        img = filedialog.askopenfilename()
        img = cv2.imread(img, 0)
        while True:
            img, str1 = read_barcodes(img, str1)
            if str1:
                heh.destroy()
                print(str1)
                # cv2.imshow('Barcode/QR code reader', img)
                b = webbrowser.open(str1)
                cv2.destroyAllWindows()
                str1 = ""
                break
            elif cv2.waitKey(1) & 0xFF == ord(" "):
                break
            else:
                goo = Tk()
                goo.attributes("-topmost", True)
                messagebox.showerror(
                    'ERROR', 'Sorry the given image had no QR, Please  retry with another QR code')
                goo.destroy()
                heh.destroy()
                goo.mainloop()
                break
        heh.mainloop()
    except:
        heh.destroy()
        goo = Tk()
        goo.attributes("-topmost", True)
        messagebox.showerror('ERROR', ' Please  enter an image with QR code')
        goo.after(200, goo.destroy())
        goo.mainloop()
    return render_template('index.html')


@app.route('/generate_qr')
def generate_qr():
    return render_template("qr.html")


@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    # Get the text to encode from the form data
    text_to_encode = request.form['text_to_encode']
    color = request.form['color-picker']
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H)
    QRcode.add_data(text_to_encode)
    QRcode.make()
    QRimg = QRcode.make_image(
        fill_color=color, back_color="white").convert('RGB')

    img = request.files['image']
    # Save the image to a temporary file
    # temp_file = 'temp_image.jpg'

    if (img):
        logo = Image.open(img)
        # adjust image size
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
               (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        # Save the image to a temporary file
        temp_file = 'temp_qr_code.png'
        QRimg.save(temp_file)
        return send_file(temp_file, mimetype='image/png', as_attachment=True)
    else:
        # Save the image to a temporary file
        temp_file = 'temp_qr_code.png'
        QRimg.save(temp_file)
        return send_file(temp_file, mimetype='image/png', as_attachment=True)
    # Return the image file to the user
    return render_template('qr.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
