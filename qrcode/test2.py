import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_592=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_592["font"] = ft
        GLabel_592["fg"] = "#333333"
        GLabel_592["justify"] = "center"
        GLabel_592["text"] = "Please enter the name of the QR code"
        GLabel_592.place(x=10,y=50,width=220,height=30)

        GLineEdit_235=tk.Entry(root)
        GLineEdit_235["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_235["font"] = ft
        GLineEdit_235["fg"] = "#333333"
        GLineEdit_235["justify"] = "center"
        GLineEdit_235["text"] = "Entry"
        GLineEdit_235.place(x=10,y=90,width=75,height=30)

        GButton_840=tk.Button(root)
        GButton_840["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_840["font"] = ft
        GButton_840["fg"] = "#000000"
        GButton_840["justify"] = "center"
        GButton_840["text"] = "Generate"
        GButton_840.place(x=10,y=140,width=70,height=25)
        GButton_840["command"] = self.GButton_840_command

    def GButton_840_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
