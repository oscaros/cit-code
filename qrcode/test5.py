import tkinter as tk
import tkinter.font as tkFont

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
        root.resizable(width=False, height=False)

        GLineEdit_726=tk.Entry(root)
        GLineEdit_726["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_726["font"] = ft
        GLineEdit_726["fg"] = "#333333"
        GLineEdit_726["justify"] = "center"
        GLineEdit_726["text"] = "Entry"
        GLineEdit_726.place(x=30,y=150,width=500,height=31)

        GLabel_97=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_97["font"] = ft
        GLabel_97["fg"] = "#333333"
        GLabel_97["justify"] = "center"
        GLabel_97["text"] = "Enter the data that you want to generate the QR code for"
        GLabel_97.place(x=10,y=120,width=350,height=30)

        GLabel_338=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_338["font"] = ft
        GLabel_338["fg"] = "#333333"
        GLabel_338["justify"] = "center"
        GLabel_338["text"] = "Mazda QR Code Generator "
        GLabel_338.place(x=230,y=20,width=259,height=51)

        GLabel_400=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_400["font"] = ft
        GLabel_400["fg"] = "#333333"
        GLabel_400["justify"] = "center"
        GLabel_400["text"] = "Enter the name of the QR code"
        GLabel_400.place(x=10,y=210,width=208,height=30)

        GLineEdit_28=tk.Entry(root)
        GLineEdit_28["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_28["font"] = ft
        GLineEdit_28["fg"] = "#333333"
        GLineEdit_28["justify"] = "center"
        GLineEdit_28["text"] = "Entry"
        GLineEdit_28.place(x=30,y=240,width=503,height=30)

        GLabel_42=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_42["font"] = ft
        GLabel_42["fg"] = "#333333"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = "Select the format in which you want the QR code"
        GLabel_42.place(x=20,y=300,width=283,height=30)

        GLabel_294=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_294["font"] = ft
        GLabel_294["fg"] = "#333333"
        GLabel_294["justify"] = "center"
        GLabel_294["text"] = "v1.0"
        GLabel_294.place(x=740,y=0,width=70,height=25)

        GLabel_953=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_953["font"] = ft
        GLabel_953["fg"] = "#333333"
        GLabel_953["justify"] = "center"
        GLabel_953["text"] = "...."
        GLabel_953.place(x=550,y=120,width=222,height=180)

        GLabel_984=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_984["font"] = ft
        GLabel_984["fg"] = "#333333"
        GLabel_984["justify"] = "center"
        GLabel_984["text"] = "Select the color of the QR code"
        GLabel_984.place(x=10,y=390,width=210,height=30)

        GLabel_629=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_629["font"] = ft
        GLabel_629["fg"] = "#333333"
        GLabel_629["justify"] = "center"
        GLabel_629["text"] = "Input the size of the QR code (Between 1 and 10)"
        GLabel_629.place(x=0,y=480,width=326,height=30)

        GLineEdit_861=tk.Entry(root)
        GLineEdit_861["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_861["font"] = ft
        GLineEdit_861["fg"] = "#333333"
        GLineEdit_861["justify"] = "center"
        GLineEdit_861["text"] = "Entry"
        GLineEdit_861.place(x=30,y=520,width=509,height=41)

        GButton_85=tk.Button(root)
        GButton_85["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=14)
        GButton_85["font"] = ft
        GButton_85["fg"] = "#000000"
        GButton_85["justify"] = "center"
        GButton_85["text"] = "Generate"
        GButton_85.place(x=190,y=590,width=228,height=30)
        GButton_85["command"] = self.GButton_85_command

        GMessage_608=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_608["font"] = ft
        GMessage_608["fg"] = "#333333"
        GMessage_608["justify"] = "center"
        GMessage_608["text"] = "......."
        GMessage_608.place(x=590,y=390,width=150,height=174)

        GListBox_589=tk.Listbox(root)
        GListBox_589["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_589["font"] = ft
        GListBox_589["fg"] = "#000000"
        GListBox_589["justify"] = "center"
        GListBox_589.place(x=30,y=330,width=504,height=48)
        GListBox_589["selectbackground"] = "#d7edd7"
        GListBox_589["selectmode"] = "single"

        GListBox_136=tk.Listbox(root)
        GListBox_136["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_136["font"] = ft
        GListBox_136["fg"] = "#333333"
        GListBox_136["justify"] = "center"
        GListBox_136.place(x=30,y=420,width=507,height=56)

        GButton_938=tk.Button(root)
        GButton_938["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        GButton_938["font"] = ft
        GButton_938["fg"] = "#000000"
        GButton_938["justify"] = "center"
        GButton_938["text"] = "Open Location"
        GButton_938.place(x=620,y=320,width=95,height=30)
        GButton_938["command"] = self.GButton_938_command

    def GButton_85_command(self):
        print("command")


    def FileLocationButton_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
