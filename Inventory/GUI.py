import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk


windows = tk.Tk()

windows.title("انبار داری یزدان بافت | pxc")
windows.geometry("1280x720")

Tab_control = ttk.Notebook(windows, width=5, height=1)
adding_resource_tab1 = ttk.Frame(Tab_control)
Tab_control.add(adding_resource_tab1, text="adding resources")
Tab_control.pack(expand=1, fill="both")

lbl = ttk.Label(text="انبار داری یزدان بافت | PXC app")
lbl1 = ttk.Label(text=".  .  .")
lbl2 = ttk.Label(text="Support in telegram @yasYZ_YZ")
lbl3 = ttk.Label(text="CopyRight CC by @yasYZ")
lbl.pack(ipadx=10, ipady=10)
lbl1.pack(ipadx=10, ipady=10)
lbl2.pack(side="right")
lbl3.pack(side="left")
lbl_upper = ttk.Label(adding_resource_tab1, text="واحد اندازه گیری")
lbl_upper.pack()

selected_var1 = tk.StringVar()
combo = ttk.Combobox(adding_resource_tab1, width=10, height=1, textvariable=selected_var1)
combo["values"] = ("KG", "Liter", "Number")
combo["state"] = "readonly"
combo.pack()


def Find_Value_func1(event):
    selected_value1 = selected_var1.get()
    showinfo(
        title='Result',
        message=f'You selected {selected_value1}!'
    )


combo.bind("<<ComboboxSelected>>", Find_Value_func1)

lbl2_upper = ttk.Label(adding_resource_tab1, text="مقدار")
lbl2_upper.pack()

def value_changed():
    print(spin_value.get())


spin_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(adding_resource_tab1, from_=0, to=1000000000000, textvariable=spin_value, wrap=True, command=value_changed)

spin_box.pack()

lbl3_upper = ttk.Label(adding_resource_tab1, text="دسته بندی")
lbl3_upper.pack()

selected_var2 = tk.StringVar()
combo2 = ttk.Combobox(adding_resource_tab1, width=17, height=1, textvariable=selected_var2)
combo2["values"] = ("انبار درجریان ساخت", "انبار مواد اولیه", "انبار کالای تولید شده")
combo2["state"] = "readonly"
combo2.pack()


def Find_Value_func2(event):
    selected_value2 = selected_var2.get()
    showinfo(
        title='Result',
        message=f'You selected {selected_value2}!'
    )


combo2.bind("<<ComboboxSelected>>", Find_Value_func2)

lbl4_upper = ttk.Label(adding_resource_tab1, text="نام کالا")
lbl4_upper.pack()


def Find_Value_func3():
    Entry = txt1.get()
    showinfo(
        title='Result',
        message=f'You selected {Entry}!'
    )


txt1 = ttk.Entry(adding_resource_tab1)
txt1.pack()

btn1 = tk.Button(adding_resource_tab1, height=3, width=15, text="Submit", bg="blue", fg="white", command=Find_Value_func3)
btn1.pack()


windows.geometry("500x500")
windows.mainloop()
