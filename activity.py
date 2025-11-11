from tkinter import *
from tkinter import ttk

def calculate():
    try:
        c = float(celsius.get())
        f_result = (c * (9/5)) + 32
        far.set(f_result) 
        
    except ValueError:
        pass
        

root = Tk()
root.title("Temperature Converter")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

celsius = StringVar()
far = StringVar() 

celsius_entry = ttk.Entry(mainframe, width=7, textvariable=celsius)
celsius_entry.grid(column=1, row=1, sticky=(W, E))

far_label = ttk.Label(mainframe, textvariable=far)
far_label.grid(column=1, row=2, sticky=(W, E))

calc_button = ttk.Button(mainframe, text="Total", command=calculate)
calc_button.grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, text="°C").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="=").grid(column=0, row=2, sticky=E)
ttk.Label(mainframe, text="F").grid(column=2, row=2, sticky=W)

root.mainloop()
