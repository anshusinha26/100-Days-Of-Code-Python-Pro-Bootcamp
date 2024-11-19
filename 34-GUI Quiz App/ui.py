THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

"""imported every class from the tkinter module"""
from tkinter import *

"""imported QuizBrain from the quiz_brain module"""
from quiz_brain import QuizBrain

"""created QuizInterface class"""
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window

        """created the window object"""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label

        """created the labelScore object"""
        self.labelScore = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "normal"))
        self.labelScore.grid(row=1, column=2)


        # canvas

        """created the canvas object"""
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.questionText = self.canvas.create_text(150, 125, width=280, text="Hello", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        # button

        """created the buttonTrue object"""
        self.trueImg = PhotoImage(file="images/true.png")
        self.buttonTrue = Button(image=self.trueImg, highlightthickness=0, bd=0, command=self.pressTrue)
        self.buttonTrue.grid(row=3, column=1)

        """created the buttonFalse object"""
        self.falseImg = PhotoImage(file="images/false.png")
        self.buttonFalse = Button(image=self.falseImg, highlightthickness=0, bd=0, command=self.pressFalse)
        self.buttonFalse.grid(row=3, column=2)

        """calling getNextQuestion method"""
        self.getNextQuestion()

        """loop to keep the window open"""
        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=q_text)
        else:
            self.canvas.itemconfig(self.questionText, text="You've reached to end of the quiz.")
            self.buttonTrue.config(state="disabled")
            self.buttonFalse.config(state="disabled")

    def pressTrue(self):
        is_right = self.quiz.check_answer("True")
        self.giveFeedback(is_right)

    def pressFalse(self):
        is_right = self.quiz.check_answer("False")
        self.giveFeedback(is_right)

    def giveFeedback(self, is_right):
        if is_right:
            self.labelScore.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.getNextQuestion)
