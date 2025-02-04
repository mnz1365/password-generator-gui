import tkinter
import random
import string
import pyperclip

resultList = list()
finalResult = None
passwordLength = 0
numbersList = [1,2,3,4,5,6,7,8,9,0]
uppercaseList = list(string.ascii_uppercase)
lowercaseList = list(string.ascii_lowercase)
symbolsList = list(string.punctuation)
options = list()



root = tkinter.Tk()
root.geometry("700x400")
root.title('password generator')
root.resizable(False, False)

# first label for custom password
firstLabel = tkinter.Label(root, text="please configure you password:")
firstLabel.place(x=20,y=10)

frame = tkinter.Frame(root, highlightbackground="black", highlightthickness=1)
frame.place(x=20, y=50, width=200, height=280)

# checkboxs
number_checked = tkinter.IntVar()
numberCheckbox = tkinter.Checkbutton(root, text="include number", variable=number_checked)
numberCheckbox.place(x=30,y=70)

letters_checked = tkinter.IntVar()
lettersCheckbox = tkinter.Checkbutton(root, text="include letters", variable=letters_checked)
lettersCheckbox.place(x=30,y=105)

uppercase_checked = tkinter.IntVar()
uppercaseCheckbox = tkinter.Checkbutton(root, text="include uppercase", variable=uppercase_checked)
uppercaseCheckbox.place(x=30,y=140)

lowercase_checked = tkinter.IntVar()
lowercaseCheckbox = tkinter.Checkbutton(root, text="include lowercase", variable=lowercase_checked)
lowercaseCheckbox.place(x=30,y=175)

symbols_checked = tkinter.IntVar()
symbolsCheckbox = tkinter.Checkbutton(root, text="include symbols", variable=symbols_checked)
symbolsCheckbox.place(x=30,y=210)

passLengthLabel = tkinter.Label(root, text="password length")
passLengthLabel.place(x=32,y=245)

passLengthEntry = tkinter.Entry(root, width=5)
passLengthEntry.place(x=130,y=245)

# generate password button
def passwordCreate():
    global resultList, finalResult, passwordLength, resultEntry
    resultList = []
    
    if passLengthEntry.get() == "":
        passwordLength = 8
    if passLengthEntry.get() != "":
        passwordLength = int(passLengthEntry.get())
        
    
    
    if number_checked.get() == 0 and letters_checked.get() == 0 and uppercase_checked.get() == 0 and lowercase_checked.get() == 0 and symbols_checked.get() == 0:
        passwordLength = passwordLength / 4
        passwordLength = int(passwordLength)
        
        for i in range(passwordLength):
            resultList.append(str(numbersList[random.randint(0, len(numbersList)-1)]))
            resultList.append(uppercaseList[random.randint(0, len(uppercaseList)-1)])
            resultList.append(lowercaseList[random.randint(0, len(lowercaseList)-1)])
            resultList.append(symbolsList[random.randint(0, len(symbolsList)-1)])

            
        for i in range(int(passwordLength/2)):
            firstRandomNumber = random.randint(0, 7)
            secondRandomNumber = firstRandomNumber
            while secondRandomNumber == firstRandomNumber:
                secondRandomNumber = random.randint(0, 7)
                
            temporaryNumber = resultList[firstRandomNumber]
            resultList[firstRandomNumber] = resultList[secondRandomNumber]
            resultList[secondRandomNumber] = temporaryNumber
    else:
            
        options = []
        if number_checked.get() == 1:
            options.append("numbers")
        if uppercase_checked.get() == 1:
            options.append("uppercase")
        if lowercase_checked.get() == 1:
            options.append("lowercase")
        if symbols_checked.get() == 1:
            options.append("symbols")
        
        count = 0
        resultList = []
        for i in range(passwordLength):
            if options[count] == "numbers":
                resultList.append(str(numbersList[random.randint(0, len(numbersList)-1)]))
            if options[count] == "uppercase":
                resultList.append(uppercaseList[random.randint(0, len(uppercaseList)-1)])
            if options[count] == "lowercase":
                resultList.append(lowercaseList[random.randint(0, len(lowercaseList)-1)])
            if options[count] == "symbols":
                resultList.append(symbolsList[random.randint(0, len(symbolsList)-1)])
            count = count + 1
            if count == len(options) :
                count = 0
            
        # mixing option items
        for i in range(passwordLength):
            firstRandomNumber = random.randint(0, passwordLength-1)
            secondRandomNumber = firstRandomNumber
            while secondRandomNumber == firstRandomNumber:
                secondRandomNumber = random.randint(0, passwordLength-1)
                
            temporaryNumber = resultList[firstRandomNumber]
            resultList[firstRandomNumber] = resultList[secondRandomNumber]
            resultList[secondRandomNumber] = temporaryNumber
    #  list of result to string  
    finalResult = ""
    for i in resultList:
        finalResult += i
    resultList = []
    resultEntry.delete(0, tkinter.END)
    resultEntry.insert(0, finalResult)
            
    
    

generatePassButton = tkinter.Button(root, text ="generate password", command = passwordCreate)
generatePassButton.place(x=60,y=280)

# result in text box
resultEntry = tkinter.Entry(root, width=30)
resultEntry.place(x=330,y=100)


# generate password button
def passwordCopy():
    pyperclip.copy(resultEntry.get())

copyPassButton = tkinter.Button(root, text ="copy", command = passwordCopy)
copyPassButton.place(x=530,y=97)



root.mainloop()