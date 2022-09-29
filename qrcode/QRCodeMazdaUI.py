import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
import tkinter.font as tkFont
import QRCodeMazda as logic
import os

class App:
    def __init__(self, root):
        #setting title
        root.title("Mazda!!!")
        #setting window size
        width=800
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        DataToEncodeTextBox=tk.Entry(root) #textbox
        DataToEncodeTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        DataToEncodeTextBox["font"] = ft
        DataToEncodeTextBox["fg"] = "#333333"
        DataToEncodeTextBox["justify"] = "center"
        DataToEncodeTextBox.place(x=30,y=150,width=500,height=31)

        DataToEncodeLabel=tk.Label(root) #label
        ft = tkFont.Font(family='Times',size=10)
        DataToEncodeLabel["font"] = ft
        DataToEncodeLabel["fg"] = "#333333"
        DataToEncodeLabel["justify"] = "center"
        DataToEncodeLabel["text"] = "Enter the data that you want to generate the QR code for"
        DataToEncodeLabel.place(x=10,y=120,width=350,height=30)

        MazdaLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        MazdaLabel["font"] = ft
        MazdaLabel["fg"] = "#333333"
        MazdaLabel["justify"] = "center"
        MazdaLabel["text"] = "Mazda QR Code Generator "
        MazdaLabel.place(x=230,y=20,width=259,height=51)

        NameOfQRLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        NameOfQRLabel["font"] = ft
        NameOfQRLabel["fg"] = "#333333"
        NameOfQRLabel["justify"] = "center"
        NameOfQRLabel["text"] = "Enter the name of the QR code"
        NameOfQRLabel.place(x=10,y=210,width=208,height=30)

        NameOfQRTextBox=tk.Entry(root)
        NameOfQRTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        NameOfQRTextBox["font"] = ft
        NameOfQRTextBox["fg"] = "#333333"
        NameOfQRTextBox["justify"] = "center"
        NameOfQRTextBox.place(x=30,y=240,width=503,height=30)

        FormatOfQRLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        FormatOfQRLabel["font"] = ft
        FormatOfQRLabel["fg"] = "#333333"
        FormatOfQRLabel["justify"] = "center"
        FormatOfQRLabel["text"] = "Select the format in which you want the QR code"
        FormatOfQRLabel.place(x=20,y=300,width=283,height=30)

        VersionLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        VersionLabel["font"] = ft
        VersionLabel["fg"] = "#333333"
        VersionLabel["justify"] = "center"
        VersionLabel["text"] = "v1.0"
        VersionLabel.place(x=730,y=0,width=70,height=25)

        StatusLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        StatusLabel["font"] = ft
        StatusLabel["fg"] = "#333333"
        StatusLabel["justify"] = "center"
        StatusLabel["text"] = "...."
        StatusLabel.place(x=560,y=120,width=222,height=222)

        ColorOfQRLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        ColorOfQRLabel["font"] = ft
        ColorOfQRLabel["fg"] = "#333333"
        ColorOfQRLabel["justify"] = "center"
        ColorOfQRLabel["text"] = "Select the color of the QR code"
        ColorOfQRLabel.place(x=10,y=390,width=210,height=30)

        SizeOfQRLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        SizeOfQRLabel["font"] = ft
        SizeOfQRLabel["fg"] = "#333333"
        SizeOfQRLabel["justify"] = "center"
        SizeOfQRLabel["text"] = "Input the size of the QR code (Between 1 and 10)"
        SizeOfQRLabel.place(x=0,y=480,width=326,height=30)

        SizeOfQRTextBox=tk.Entry(root)
        SizeOfQRTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        SizeOfQRTextBox["font"] = ft
        SizeOfQRTextBox["fg"] = "#333333"
        SizeOfQRTextBox["justify"] = "center"
        SizeOfQRTextBox.place(x=30,y=520,width=509,height=41)

        GenerateButton=tk.Button(root)
        GenerateButton["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=14)
        GenerateButton["font"] = ft
        GenerateButton["fg"] = "#000000"
        GenerateButton["justify"] = "center"
        GenerateButton["text"] = "Generate"
        GenerateButton.place(x=190,y=590,width=228,height=30)
        GenerateButton["command"] = self.GenerateButton_command

        GMessage_608=tk.Message(root)  
        ft = tkFont.Font(family='Times',size=10)
        GMessage_608["font"] = ft
        GMessage_608["fg"] = "#333333"
        GMessage_608["justify"] = "center"
        GMessage_608["text"] = "......."
        GMessage_608.place(x=590,y=390,width=150,height=174)

        QRImageFormatListBox=tk.Listbox(root) #select box
        QRImageFormatListBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        QRImageFormatListBox["font"] = ft
        QRImageFormatListBox["fg"] = "#000000"
        QRImageFormatListBox["justify"] = "center"
        QRImageFormatListBox.place(x=30,y=330,width=504,height=48)
        QRImageFormatListBox["selectbackground"] = "#d7edd7"
        QRImageFormatListBox["selectmode"] = "single"
        QRImageFormatListBox.insert(1, ".png")
        QRImageFormatListBox.insert(2, ".jpg")

        ColorChooserButton=tk.Button(root)
        ColorChooserButton["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        ColorChooserButton["font"] = ft
        ColorChooserButton["fg"] = "#000000"
        ColorChooserButton["justify"] = "center"
        ColorChooserButton["text"] = "Choose Color"
        ColorChooserButton.place(x=30,y=420,width=507,height=56)
        ColorChooserButton["command"] = self.ColorChooserButton_command

        FileLocationButton=tk.Button(root)
        FileLocationButton["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        FileLocationButton["font"] = ft
        FileLocationButton["fg"] = "#000000"
        FileLocationButton["justify"] = "center"
        FileLocationButton["text"] = "Open Location"
        FileLocationButton.place(x=620,y=320,width=95,height=30)
        FileLocationButton["command"] = self.FileLocationButton_command
    
        #refence objs so that they are callable in another sub function
        self.DataToEncodeTextBox = DataToEncodeTextBox 
        self.NameOfQRTextBox = NameOfQRTextBox
        self.SizeOfQRTextBox = SizeOfQRTextBox
        self.QRImageFormatListBox = QRImageFormatListBox
        self.StatusLabel = StatusLabel
        self.ColorChooserButton = ColorChooserButton

    def ColorChooserButton_command(self):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        colorr = color_code[1]


    def GenerateButton_command(self):
        dataToEncode = self.DataToEncodeTextBox.get()
        nameofQR = self.NameOfQRTextBox.get()
        SizeOfQRTextBox = self.SizeOfQRTextBox.get()
        #imageFormat = self.QRImageFormatListBox.get(self.QRImageFormatListBox.curselection())
        QRColor = colorchooser.askcolor(title ="Choose color of QR Code")[1]
        #print(type(QRColor))

        #do some validation
        if dataToEncode == '' or nameofQR == '' or SizeOfQRTextBox == '': #or SizeOfQRTextBox ==''
            messagebox.showerror("showerror", "Make sure all fields are filled out")

        elif int(SizeOfQRTextBox) < 1 or int(SizeOfQRTextBox) > 10:
            messagebox.showerror("showerror", "Size of QR code should be between 1 and 11")

        else:
            #generating QR
            logicFile = logic
            #1st generate a folder if it doesnot exist
            logicFile.createFolder()
            existingFiles = logicFile.path
            #print(existingFiles)
            doesFileExist = logicFile.nameQR(existingFiles, nameofQR)
            #print(doesFileExist)

            if doesFileExist != True: 
                logicFile.createQR(dataToEncode, logicFile.path , nameofQR, QRColor, SizeOfQRTextBox )
                statuslabel = self.StatusLabel
                image = tk.PhotoImage(file = logicFile.createQR(dataToEncode, logicFile.path , nameofQR, QRColor, SizeOfQRTextBox))
                statuslabel.configure(image = image)
                statuslabel.image = image
            else:
                messagebox.showerror("showerror", "Name is already used choose a diffrent name")


    def FileLocationButton_command(self):
        logicFile = logic
        os.system("start " + logicFile.path)


        #print(logicFile.createQR(dataToEncode, logicFile.path , nameofQR, QRColor, SizeOfQRTextBox ))
        #subLabel.config(text="QR of " + Subject.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
