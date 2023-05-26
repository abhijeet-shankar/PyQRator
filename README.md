# PyQRator

PyQRator is a Python project that provides functionalities to scan and generate QR codes. It can scan QR codes using images or the camera of a device, and can generate QR codes with or without images in the center of the code. The frontend of the project is a web-based application by using the generating capabilities of Flask's web framework, while the Pyzbar and qrcode libraries are used for QR code applications.


## Run Locally

Clone the project

```bash
  git clone https://github.com/abhijeet-shankar/PyQRator.git
```

Go to the project directory

```bash
  cd PyQRator
```

Install dependencies

```bash
    pip install Flask
    pip install Pyzbar
    pip install qrcode
    pip install Pillow
    pip install webbrowser
    pip install sys
    pip install cv2
    pip install tkinter
```

Run the QRator.py for flask interface
```bash
  python QRator.py
```
Run the MeowScan.py for tkinter interface(scanner only). 
```bash
  python MeowScan.py
```



## Usage

To use PyQRator, you need to install all dependencies. 

1. You can then run the Flask application by running the QRator.py file. This will start the server, and you can access the application by opening a web browser and navigating to http://localhost:8080/.

2. Select the option to proceed with.

3. If QR scan is the option follow the steps and proceed.

4. Else for QR generator select the color,image,text to be encoded.
Choose the file location where you want to save the generated file and provide a filename.


## License

PyQRator is licensed under MIT license. Click [MIT](https://choosealicense.com/licenses/mit/) for more information.


## Contributing

Contributions to PyQRator are welcome. Whether you want to fix a bug, add a new feature, or improve the documentation, please fork the repository and create a pull request.
