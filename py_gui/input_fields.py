import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('Input_fields')

e = tk.Entry(root)
e.pack()
e.insert(0, 'Enter your name')

def myClick():
    my_label = tk.Label(root, text=e.get())
    my_label.pack()

my_button = tk.Button(root, text='Submit name', command=myClick)
my_button.pack()


root.mainloop()