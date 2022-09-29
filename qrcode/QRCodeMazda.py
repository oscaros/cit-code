# pip install qrcode
# Importing libraries
import qrcode
import os

#Algorithm

#ask user to input the text/data they would like to encode
#create a folder using os module that will save our QR codes if not exists (use a try except )
#display the contents of the folder showing the codes generated so far --def displayContents():  
#allow the user to name the qr code. 
# But we will 1st check if name exists in folder --def nameQr():
#ability of user to determine the output size and color of the generated image--def createQR(userInput, color, length, height)

#functions, modules, venv, loops, control flow, lists, input validation, OOP, Classes, Tkinter for UI
#comparison ops, exceptions, handle files, handle exceptions, break, pass, continue


path = os.getcwd()+"/myqrcodes/"  #stores our folder path in variable path

#create our qr folder if not exists
def createFolder():
    try:
        os.mkdir(path) #create our folder
        return path       
    except FileExistsError as err:
        return err
    finally:
        return path   

#returns everything in path so far
def getPath(path):
    try:
        listedfiles =os.listdir(path) #return all files in a list
        return listedfiles
    except FileNotFoundError as fnf_err:
        return fnf_err

#used to return all QR codes in our QR code folder
def displayAllQr():
    path2 = createFolder()
    try:
        QRlist = os.listdir(path2)
        for qr in QRlist:
          print(qr)
    except FileNotFoundError as fnf_err:
        return fnf_err

#check if name of Qr already exists
def nameQR(listedFiles, userInputName): 
   for file in listedFiles:
        if userInputName+".png" in listedFiles:
            print("Oops! File already exists. choose another name")
            return True    
        else:
            pass

def createQR(userInput, path, name,color, size):
    data = userInput
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=size,
    border=4,
    )
    qr.add_data(data)

    img = qr.make_image(fill_color=color, back_color="white") 
    img.save(path+name+'.png')
    #print("code has been been created and saved ")
    return path+name+'.png'
    

def main():
    
    while True:
        menu = input("Input 1 to generate a new QR code,  Input 2 to list all QR codes Or input x to exit ")
        if menu == "1":
            path = createFolder() #create folder if it doesnot exist
            listedfiles = getPath(path) #return the folder contents

            #get user input -->data, name, color and size
            userInputdata = input("Enter data or contents of QR code: ")
            userInputName = input("Enter name of QR code: ")
            userInputColor = input("Enter color of QR code: ")
            userInputSize = input("Enter size of QR code (from size 1 to 10): ")
            
            #validate user input incase they dont put integers
            if not userInputSize.isdigit():
                print("please input digits for size")
                break

            #validate user input incase they dont put letters
            if userInputColor.isdigit():
                print("Color should not be a number")
                break

            #check if name to be given to QR already exists
            nameQR(listedfiles, userInputName)

            #create QR code
            createQR(userInputdata, path, userInputName, userInputColor, userInputSize)

        elif menu =="2":
            displayAllQr()
            

        elif menu =="x":
            break

        else:
            print("You have entered an uknown menu item")
            break
    
if __name__ == '__main__':
    main()
