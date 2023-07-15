import tkinter as tk
from tkinter import messagebox
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text='Your message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arail', 15))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text='Show Messagebox', font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text='Show message', font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        #on pressing window close 'X' button
        self.root.protocol('WM_DELETE__WINDOW', self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))
    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Do you want to quit?'):
            self.root.destroy()        
MyGUI()
