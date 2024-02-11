from tkinter import *
import pyautogui
import random
import pandas as pd

class Jenga:
    def __init__(self, root):
        self.root = root
        baseWidth = 1920
        baseHeight = 1080

        ratioWidth = self.root.winfo_screenwidth() / baseWidth
        ratioHeight = self.root.winfo_screenheight() / baseHeight

        self.ratioWidth = ratioWidth
        self.ratioHeight = ratioHeight

        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', True)
        self.root.geometry(f"{int(baseWidth * ratioWidth)}x{int(baseHeight * ratioHeight)}")
        self.root.bind('<Escape>', lambda e: self.root.destroy())


        self.CloseBtn_Image = PhotoImage(file="./Images/CloseBtn.png")
        self.MinimizeBtn_Image = PhotoImage(file="./Images/MinimizeBtn.png")
        self.AppIcon_Image = PhotoImage(file="./Images/AppIcon.png")

        Button(self.root, image=self.CloseBtn_Image, relief=RAISED, bg="white", bd=2, command=lambda: self.root.destroy()).place(x=int(1870 * ratioWidth), y=int(25 * ratioHeight), width=int(40 * ratioWidth), height=int(45 * ratioHeight))
        Button(self.root, image=self.MinimizeBtn_Image, relief=RAISED, bg="white", bd=2, command=lambda: self.root.iconify()).place(x=int(1820 * ratioWidth), y=int(25 * ratioHeight), width=int(40 * ratioWidth), height=int(45 * ratioHeight))

        Label(self.root.master, image=self.AppIcon_Image, bg="white", bd=2, relief=RAISED).place(x=int(7 * ratioWidth), y=int(25 * ratioHeight), width=int(45 * ratioWidth), height=int(45 * ratioHeight))
        Label(self.root.master, text="Oracle Blocks", font="Gabriola 40 bold", bg="white", bd=2, relief=RAISED).place(x=int(60 * ratioWidth), y=int(5 * ratioHeight), width=int(1755 * ratioWidth), height=int(85 * ratioHeight))

        self.MainStartButton = Button(self.root, text="Start Game", font="Gabriola 40 bold", bg="white", bd=2, relief=RAISED, command=self.StartGame)
        self.MainStartButton.place(x=int(700 * ratioWidth), y=int(500 * ratioHeight), width=int(500 * ratioWidth), height=int(100 * ratioHeight))

        self.PlayerName = StringVar()
        self.CurrentScore = IntVar()
        self.CurrRound = IntVar()
        self.Die1 = StringVar()
        self.Die2 = StringVar()
        self.Die3 = StringVar()
        self.Die1.set("")
        self.Die2.set("")
        self.Die3.set("")
    def StartGame(self):
        self.MainFrame = Frame(self.root, bd=4, relief=RIDGE)
        self.MainFrame.place(x=int(0 * self.ratioWidth), y=int(100 * self.ratioHeight), width=int(1920 * self.ratioWidth), height=int(980 * self.ratioHeight))

        NameLabel = Label(self.MainFrame, text="Instagram ID", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        NameLabel.place(x=int((1920 / 2 - 320)*self.ratioWidth), y=int(200 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))

        self.NameEntry = Entry(self.MainFrame, font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        self.NameEntry.place(x=int((1920 / 2 + 20)*self.ratioWidth), y=int(200 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))

        StartGameBtn = Button(self.MainFrame, text="Start Game", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.StartGame_Final)
        StartGameBtn.place(x=int((1920 / 2 - 150)*self.ratioWidth), y=int(300 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))

        # NewGameBtn = Button(self.MainFrame, text="New Game", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.NewGame)
        # NewGameBtn.place(x=int(10 * self.ratioWidth), y=int(900 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))
        #
        # FinishGameBtn = Button(self.MainFrame, text="Finish Game", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.FinishGame)
        # FinishGameBtn.place(x=int(1610 * self.ratioWidth), y=int(900 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))

    def StartGame_Final(self):
        self.QuestionSelection()
        self.PlayerName.set(self.NameEntry.get())
        self.Reset_Variables()
        self.CurrRound.set(1)

        if hasattr(self, "MainFrame"):
            self.MainFrame.destroy()

        self.MainFrame = Frame(self.root, bd=4, relief=RIDGE)
        self.MainFrame.place(x=int(0 * self.ratioWidth), y=int(100 * self.ratioHeight), width=int(1920 * self.ratioWidth), height=int(980 * self.ratioHeight))

        Label(self.MainFrame, text="Welcome: " + self.PlayerName.get(), font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED).place(x=int(20 * self.ratioWidth), y=int(20 * self.ratioHeight), width=int(1880 * self.ratioWidth), height=int(80 * self.ratioHeight))

        NewGameBtn = Button(self.MainFrame, text="New Game", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.NewGame)
        NewGameBtn.place(x=int(10 * self.ratioWidth), y=int(900 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))

        FinishGameBtn = Button(self.MainFrame, text="Finish Game", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.RemoveFail_Pressed)
        FinishGameBtn.place(x=int(1610 * self.ratioWidth), y=int(900 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(65 * self.ratioHeight))

        # self.CurrentRoundLabel = Label(self.MainFrame, textvariable=self.CurrRound, font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        # self.CurrentRoundLabel.place(x=int(20 * self.ratioWidth), y=int(120 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(50 * self.ratioHeight))
        #
        # self.CurrentScoreLabel = Label(self.MainFrame, textvariable=self.CurrentScore, font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        # self.CurrentScoreLabel.place(x=int(1600 * self.ratioWidth), y=int(120 * self.ratioHeight), width=int(300 * self.ratioWidth), height=int(50 * self.ratioHeight))

        CurrRound_Label = Label(self.MainFrame, text="Current Round:", font="Gabriola 20 bold")
        CurrRound_Label.place(x=int(20 * self.ratioWidth), y=int(120 * self.ratioHeight), width=int(200 * self.ratioWidth), height=int(50 * self.ratioHeight))
        CurrRound_Value = Label(self.MainFrame, textvariable=self.CurrRound, font="Gabriola 20 bold", anchor="w")
        CurrRound_Value.place(x=int(220 * self.ratioWidth), y=int(120 * self.ratioHeight), width=int(100 * self.ratioWidth), height=int(50 * self.ratioHeight))

        CurrentScore_Label = Label(self.MainFrame, text="Current Score:", font="Gabriola 20 bold")
        CurrentScore_Label.place(x=int(1600 * self.ratioWidth), y=int(120 * self.ratioHeight), width=int(200 * self.ratioWidth), height=int(50 * self.ratioHeight))
        CurrentScore_Value = Label(self.MainFrame, textvariable=self.CurrentScore, font="Gabriola 20 bold", anchor="w")
        CurrentScore_Value.place(x=int(1800 * self.ratioWidth), y=int(120 * self.ratioHeight), width=int(100 * self.ratioWidth), height=int(50 * self.ratioHeight))

        self.RollDie()
    def NewGame(self):
        if hasattr(self, "MainFrame"):
            self.MainFrame.destroy()
        if hasattr(self, "GameOverFrame"):
            self.GameOverFrame.destroy()

        self.MainStartButton.config(text="Start Game")


    def Reset_Variables(self):
        self.CurrentScore.set(0)
        self.CurrRound.set(0)
        self.Die1.set("")
        self.Die2.set("")
        self.Die3.set("")

    def RollDie(self):
        self.RollDie_Frame = Frame(self.MainFrame, bd=4, relief=RIDGE)
        self.RollDie_Frame.place(x=int(610 * self.ratioWidth), y=int(300 * self.ratioHeight), width=int(700 * self.ratioWidth), height=int(400 * self.ratioHeight))

        Die1 = Label(self.RollDie_Frame, textvariable=self.Die1, font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        Die1.place(x=int(50 * self.ratioWidth), y=int(50 * self.ratioHeight), width=int(100 * self.ratioWidth), height=int(100 * self.ratioHeight))

        Die2 = Label(self.RollDie_Frame, textvariable=self.Die2, font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        Die2.place(x=int(300 * self.ratioWidth), y=int(50 * self.ratioHeight), width=int(100 * self.ratioWidth), height=int(100 * self.ratioHeight))

        Die3 = Label(self.RollDie_Frame, textvariable=self.Die3, font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        Die3.place(x=int(550 * self.ratioWidth), y=int(50 * self.ratioHeight), width=int(100 * self.ratioWidth), height=int(100 * self.ratioHeight))

        self.RollButton = Button(self.RollDie_Frame, text="Roll The Die", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.RollDie_Button)
        self.RollButton.place(x=int(250 * self.ratioWidth), y=int(250 * self.ratioHeight), width=int(200 * self.ratioWidth), height=int(100 * self.ratioHeight))

    def RollDie_Button(self):
        Die1 = random.randint(1, 6)
        Die2 = random.randint(1, 6)
        Die3 = random.randint(1, 6)

        self.Die1.set(Die1)
        self.Die2.set(Die2)
        self.Die3.set(Die3)

        self.RollButton.destroy()

        self.RemoveTheBlock = Label(self.RollDie_Frame, text="Remove The Block", font="Gabriola 25 bold")
        self.RemoveSuccess = Button(self.RollDie_Frame, text="Removed", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.RemoveBlock_Pressed)
        self.RemoveFail = Button(self.RollDie_Frame, text="Failed", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.RemoveFail_Pressed)

        self.RemoveTheBlock.place(x=int(10 * self.ratioWidth), y=int(200 * self.ratioHeight), width=int(680 * self.ratioWidth), height=int(70 * self.ratioHeight))
        self.RemoveSuccess.place(x=int(50 * self.ratioWidth), y=int(300 * self.ratioHeight), width=int(280 * self.ratioWidth), height=int(70 * self.ratioHeight))
        self.RemoveFail.place(x=int(370 * self.ratioWidth), y=int(300 * self.ratioHeight), width=int(280 * self.ratioWidth), height=int(70 * self.ratioHeight))


    def RemoveFail_Pressed(self):
        # Game Over
        if hasattr(self, "QuestionFrame"):
            self.QuestionFrame.destroy()
        if hasattr(self, "RollDie_Frame"):
            self.RollDie_Frame.destroy()
        if hasattr(self, "MainFrame"):
            self.MainFrame.destroy()
        if hasattr(self, "GameOverFrame"):
            self.GameOverFrame.destroy()

        self.MainStartButton.config(text="New Game")

        self.GameOverFrame = Frame(self.root, bd=4, relief=RIDGE)
        self.GameOverFrame.place(x=int(400 * self.ratioWidth), y=int(220 * self.ratioHeight), width=int(1120 * self.ratioWidth), height=int(250 * self.ratioHeight))

        GameOverLabel = Label(self.GameOverFrame, text="Game Over", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        NameLabel = Label(self.GameOverFrame, text="Instagram ID: " + self.PlayerName.get(), font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        ScoreDisplay = Label(self.GameOverFrame, text="Score: " + str(self.CurrentScore.get()), font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)

        GameOverLabel.place(x=int(20 * self.ratioWidth), y=int(20 * self.ratioHeight), width=int(1080 * self.ratioWidth), height=int(50 * self.ratioHeight))
        NameLabel.place(x=int(120 * self.ratioWidth), y=int(80 * self.ratioHeight), width=int(880 * self.ratioWidth), height=int(50 * self.ratioHeight))
        ScoreDisplay.place(x=int(120 * self.ratioWidth), y=int(140 * self.ratioHeight), width=int(880 * self.ratioWidth), height=int(50 * self.ratioHeight))

        # NewGameBtn = Button(self.QuestionFrame, text="New Game", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        # NewGameBtn.place(x=int(460 * self.ratioWidth), y=int(210 * self.ratioHeight), width=int(200 * self.ratioWidth), height=int(70 * self.ratioHeight))



    def RemoveBlock_Pressed(self):
        self.CurrentScore.set(self.CurrentScore.get() + 5*self.CurrRound.get())
        DieTotal = int(self.Die1.get()) + int(self.Die2.get()) + int(self.Die3.get())
        CurrQuestion = self.data.iloc[DieTotal-1]

        if hasattr(self, "QuestionFrame"):
            self.QuestionFrame.destroy()
        if hasattr(self, "RollDie_Frame"):
            self.RollDie_Frame.destroy()

        self.QuestionFrame = Frame(self.MainFrame, bd=4, relief=RIDGE)
        self.QuestionFrame.place(x=int(100 * self.ratioWidth), y=int(220 * self.ratioHeight), width=int(1720 * self.ratioWidth), height=int(600 * self.ratioHeight))

        QuestionLabel = Label(self.QuestionFrame, text="Questiom", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        QuestionLabel.place(x=int(20 * self.ratioWidth), y=int(20 * self.ratioHeight), width=int(1680 * self.ratioWidth), height=int(50 * self.ratioHeight))

        Question = Label(self.QuestionFrame, text=CurrQuestion["Question"], font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED)
        Question.place(x=int(20 * self.ratioWidth), y=int(80 * self.ratioHeight), width=int(1680 * self.ratioWidth), height=int(400 * self.ratioHeight))

        GameOverButton = Button(self.QuestionFrame, text="Game Over", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.RemoveFail_Pressed)
        GameOverButton.place(x=int(10 * self.ratioWidth), y=int(500 * self.ratioHeight), width=int(200 * self.ratioWidth), height=int(70 * self.ratioHeight))

        QuestionSolvedButton = Button(self.QuestionFrame, text="Question Solved", font="Gabriola 20 bold", bg="white", bd=2, relief=RAISED, command=self.QuestionSolved_Final)
        QuestionSolvedButton.place(x=int(1510 * self.ratioWidth), y=int(500 * self.ratioHeight), width=int(200 * self.ratioWidth), height=int(70 * self.ratioHeight))

    def QuestionSolved_Final(self):
        self.CurrentScore.set(self.CurrentScore.get() + 10 * self.CurrRound.get())
        self.CurrRound.set(self.CurrRound.get() + 1)

        if hasattr(self, "QuestionFrame"):
            self.QuestionFrame.destroy()
        if hasattr(self, "RollDie_Frame"):
            self.RollDie_Frame.destroy()

        self.RollDie()

    def QuestionSelection(self):
        self.data = pd.read_csv("Questions.csv")
        self.data = self.data.sample(n=51)
        self.data = self.data.reset_index(drop=True)

if __name__ == "__main__":
    root = Tk()
    app = Jenga(root)
    root.mainloop()