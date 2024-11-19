# """imported tkinter module"""
# import tkinter
#
# """creating window object"""
# window = tkinter.Tk()
# window.minsize(width=500, height=500)
# window.config(padx=100, pady=100)
#
# """setting up label"""
# label1 = tkinter.Label(text="I am a label", font=("Courier", 20, "bold"))
# # label1.pack(expand=True)
# label1.grid(row=1, column=1)
# label1.config(padx=50, pady=50)
#
# # """changing and configuring label"""
# # label1["text"] = "I'm a new label"
# # label1.config(text="I'm a new label")
#
# """function to print on button click"""
# def buttonClicked():
#     inputText = input.get()
#     label1.config(text=inputText)
#
# """creating button object"""
# button = tkinter.Button(text="Click me", command=buttonClicked)
# # button.pack(expand=True)
# button.grid(row=2, column=2)
#
# """creating button2 object"""
# button2 = tkinter.Button(text="Click me again", command=buttonClicked)
# button2.grid(row=1, column=3)
#
# """creating input object"""
# input = tkinter.Entry(width=10)
# # input.pack(expand=True)
# input.grid(row=3, column=4)
#
# """main loop to keep window open"""
# window.mainloop()

#####

# day27: Mile to Kilometer converter
"""imported tkinter module"""
import tkinter

"""constant"""
FONT = ("Courier", 20, "bold")

"""variable to hold the value of 1 mile in km"""
mileKm = 1.60934

"""function to convert miles to kilometer"""
def convert():
    miles = int(input1.get())
    milesToKm = round(miles * mileKm, 2)
    label4.config(text=milesToKm)

# window

"""creating the window object"""
window = tkinter.Tk()
window.minsize(width=500, height=500)
window.title("Mile to Km converter")
window.config(padx=100, pady=100)


# label

"""creating the label1 object"""
label1 = tkinter.Label(text="Is equal to", font=FONT)
label1.grid(row=2, column=1)
label1.config(padx=20, pady=20)

"""creating the label2 object"""
label2 = tkinter.Label(text="Miles", font=FONT)
label2.grid(row=1, column=3)
label2.config(padx=20, pady=20)

"""creating the label3 object"""
label3 = tkinter.Label(text="Km", font=FONT)
label3.grid(row=2, column=3)
label3.config(padx=20, pady=20)

"""creating the label4 object"""
label4 = tkinter.Label(text="0", font=FONT)
label4.grid(row=2, column=2)
label4.config(padx=20, pady=20)


# input

"""creating the input1 object"""
input1 = tkinter.Entry(width=10)
input1.grid(row=1, column=2)


# button

"""creating the button object"""
button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=3, column=2)
button.config(padx=20, pady=20)


"""keeps the window open"""
window.mainloop()