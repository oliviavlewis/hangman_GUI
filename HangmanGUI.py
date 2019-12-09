# Olivia Lewis
# Lecture 26
# Hangman Graphical User Interface (GUI)

# GUI programming is called event driven programming.
# this means that after main is done running, the program waits for user to interact with it
# Auto Py to Exe will allow the code to execute on another computer without pycharm

from tkinter import *  # the star means import all the classes that are inside this file
import random

class HangmanGUI:
    def __init__(self):
        root = Tk()  # root get you the entire window
        root.title("Hangman GUI")  # this sets the title at the top of the pop up window
        root.geometry("400x575")  # this sets the dimensions that the window starts out as
        self.myFrame = Frame(root)  # myFrame on that root is what is inside the box you cant set the title on the frame
        self.myFrame.grid()
        # create a label (does not change)
        self.label1 = Label(self.myFrame, text="Enter a letter")  # we want it to go in myFrame, and say Enter a Letter
        self.label1.config(font="Arial 14 bold")
        self.label1.grid(row=0, column=0, sticky=E)  # this allows us to choose where in the grid we will put the label
        # grid method being called on a Label object means that it is a method in this class
        # implement a textfield
        self.textfield = Entry(self.myFrame)  # this creates an entry field variable
        self.textfield.grid(row=0, column=1, sticky=W)  # puts it in the first row, middle column, stick it to the west(left)
        self.textfield.focus()  # set the cursor in the textfield
        self.textfield.config(bg="red", fg="yellow")
        # create a button
        root.update()  # this allows the button to depress, it will still work without this, but it looks better
        # this has to do with the way Python communicates with the OS to render the GUI
        self.button = Button(self.myFrame, text="Guess Letter", command=self.buttonClicked)
        # add the button to myFrame and set the text, also call the method buttonClicked, which is defined below
        # command= sets the event and tells python what we want to have happen
        self.button.grid(row=1, column=0, columnspan=2)  # merge the columns
        root.bind('<Return>', self.buttonClicked)  # on the root, bind the enter key to call buttonClicked method

        self.guessedLetters = []
        self.lettersToGuessLabel = Label(self.myFrame, text=self.getLettersDisplayed())
        self.lettersToGuessLabel.grid(row=2, column=0, columnspan=2)
        self.secretWord = self.getSecretWord()
        self.displayedWordLabel = Label(self.myFrame, text=self.getDisplayedWord())
        self.displayedWordLabel.grid(row=3, column=0, columnspan=2)
        self.displayedWordLabel.config(fg="blue", font="Courier 14 bold")
        self.statusMessageLabel = Label(self.myFrame)
        self.statusMessageLabel.grid(row=4, column=0, columnspan=2)
        self.statusMessageLabel.config(font="Courier 14 bold")

        self.imageList = []
        # this is going to be a list of photo image objects
        self.imageList.append(PhotoImage(file="hangman0.png"))
        # PhotoImage is a class inside the tkinter file
        self.imageList.append(PhotoImage(file="hangman1.png"))
        self.imageList.append(PhotoImage(file="hangman2.png"))
        self.imageList.append(PhotoImage(file="hangman3.png"))
        self.imageList.append(PhotoImage(file="hangman4.png"))
        self.imageList.append(PhotoImage(file="hangman5.png"))
        self.imageList.append(PhotoImage(file="hangman6.png"))
        self.imageList.append(PhotoImage(file="hangman7.png"))
        # add the first image to the frame so that it comes up immediately when you run the GUI
        # we are going to make it a label that has this image in it
        self.imageLabel = Label(self.myFrame, image=self.imageList[0])
        self.imageLabel.grid(row=5, column=0, columnspan=2)  # this puts the image label in the grid
        self.imageCounter = 0

    def getLettersDisplayed(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        stringToReturn = ""
        for ch in alphabet:
            if ch in self.guessedLetters:
                stringToReturn += "- "
            else:
                stringToReturn += ch + " "
        return stringToReturn

    def getSecretWord(self):
        inputFile = open("hangmanwords.txt", "r")
        secretList = []
        for word in inputFile:
            secretList.append(word.strip())
        inputFile.close()
        return random.choice(secretList)

    def getDisplayedWord(self):
        display = []
        for ch in self.secretWord:
            if ch.upper() in self.guessedLetters:
                display.append(ch.upper())
            else:
                display.append("_")
        return " ".join(display)

    def buttonClicked(self, event=None):
        if self.imageCounter != 7:
            textvalue = self.textfield.get()  # this gets us teh value of what they type
            print("User typed " + textvalue)
            self.textfield.delete(0, len(textvalue))  # this allows us to clear the textfield after enter is hit
            if len(textvalue) == 1:  # this is how we make sure that the user does not enter more than one letter
                self.guessedLetters.append(textvalue.upper())
                self.lettersToGuessLabel.config(text=self.getLettersDisplayed())
                if textvalue.upper() in self.secretWord.upper():  # check to see if the guessed letter in word
                    self.statusMessageLabel.config(text=textvalue.upper() + " IS in the secret word!")
                    self.displayedWordLabel.config(text=self.getDisplayedWord())
                    # check to see if there are any more underscores in the display
                    if "_" not in self.getDisplayedWord():  # the user has guessed all the letters
                        self.statusMessageLabel.config(text="You won! You guessed the secret word!")
                        self.button.config(state=DISABLED)
                        self.imageCounter = 7
                else:  # this will add a body part to our hangman only if we don't guess a letter correct
                    self.statusMessageLabel.config(text=textvalue.upper() + " is NOT in the secret word.")
                    print("Button clicked!")  # this will print into the command line, not the GUI
                    self.imageCounter += 1  # each time the user clicks the button, increment the image counter by one
                    # we use the config method to change the image that is displayed on image label to the next index in imageList
                    self.imageLabel.config(image=self.imageList[self.imageCounter])
                    if self.imageCounter == 7:
                        self.statusMessageLabel.config(text="You lost! The secret word was " + self.secretWord.upper() + ".")
                        # this changes the variable of the button (the state of the component) to not allow more guesses
                        self.button.config(state=DISABLED)


def main():
    hg = HangmanGUI()
    hg.myFrame.mainloop()  # this line of code indicates that it should not terminate until the user does something to
    # make it terminate


main()