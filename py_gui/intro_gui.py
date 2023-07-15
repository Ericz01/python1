import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('GUI program')
#adding hello world! to the window
label = tk.Label(root, text='Hello World!', font=('Arial', 18))
#re-positioning 'Hello world!'
label.pack(padx=20, pady=20)
#setting a text box for user of 3 lines and font 15 with a 10 point indent
textbox = tk.Text(root, height=3, font=('Arial', 15))
textbox.pack(padx=10)
#setting a text box that's unscrollable ie with definite size
#myentry = tk.Entry(root)
#myentry.pack(padx=10, pady=10)
#setting up a button
#mybutton = tk.Button(root, text='Click here', font=('arial', 15))
#mybutton.pack(padx=10, pady=10)

#setting up a grid of buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')#strech the columns to fill x-axis

root.mainloop()