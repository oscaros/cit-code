import os

def CreateFile():
    try:
        open(os.getcwd() +'/answers2.txt', "w")
    except FileNotFoundError:
        print("The file does not exist")

def WriteAnswers(answers: dict):
    try:
        with open(os.getcwd() +'/answers2.txt', 'w') as file:
            file.write("Answers to week8 quiz questions \n")
            for key, value in answers.items():
                file.write(f"Qn. {key} : Answer is {value} \n")

    except FileNotFoundError:
        print("The file does not exist")

def ReadFile():
    try:
        with open(os.getcwd() +'/answers2.txt', 'r+') as file:
            mytext = file.readlines()
            for i in mytext:
                print(i)
    except FileNotFoundError:
        print("The file does not exist")

def main():
    CreateFile()
    answers = {
        "1": "d",
        "2": "c",
    }
    WriteAnswers(answers)
    ReadFile()

if __name__ == "__main__":
    main()

        
        


