import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import data

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
    """show value data"""
    selected_value1 = selected_var1.get()
    data.in_val.append(selected_value1)
    showinfo(
        title='Result',
        message=f'You selected {selected_value1}!'
    )


combo.bind("<<ComboboxSelected>>", Find_Value_func1)

lbl2_upper = ttk.Label(adding_resource_tab1, text="مقدار")
lbl2_upper.pack()
spin_value = tk.StringVar(value=0)


def value_changed_spin():
    """show Number data"""
    spin = spin_value.get()
    data.in_Num.append(spin)


spin_box = ttk.Spinbox(adding_resource_tab1, from_=0, to=1000000000000, textvariable=spin_value, wrap=True, command=value_changed_spin)
spin_box.pack()

lbl3_upper = ttk.Label(adding_resource_tab1, text="دسته بندی")
lbl3_upper.pack()

selected_var2 = tk.StringVar()
combo2 = ttk.Combobox(adding_resource_tab1, width=17, height=1, textvariable=selected_var2)
combo2["values"] = ("انبار درجریان ساخت", "انبار مواد اولیه", "انبار کالای تولید شده")
combo2["state"] = "readonly"
combo2.pack()


def Find_cat_func2(event):
    """show categories"""
    selected_value2 = selected_var2.get()
    data.in_cat.append(selected_value2)
    showinfo(
        title='Result',
        message=f'You selected {selected_value2}!'
    )


combo2.bind("<<ComboboxSelected>>", Find_cat_func2)

lbl4_upper = ttk.Label(adding_resource_tab1, text="نام کالا")
lbl4_upper.pack()
txt1 = ttk.Entry(adding_resource_tab1)
txt1.pack()


def Find_Value_func3_Entry():
    """show Entry var"""
    Entry = txt1.get()
    data.in_Name.append(Entry)


def caller_func():
    Find_Value_func3_Entry()
    value_changed_spin()
    if (data.in_val or data.in_cat) == []:
        print(f"data is not correct(user dont select option)")
        showinfo(
        title="Result",
        message="Try again Error101"
        )
        return
    elif data.in_Num == ['0']:
        print(f"data is not correct(user dont input number)")
        showinfo(
        title="Result",
        message="Try again Error101"
        )
        return
    elif data.in_Name == [0]:
        print(f"data is not correct(user dont input product name)")
        showinfo(
        title="Result",
        message="Try again Error101"
        )
        return
    else:
        print("data save in computer")
        data.data_saving()
        showinfo(
            title="Result",
            message="completed"
        )


btn2 = tk.Button(adding_resource_tab1, height=2, width=10, text="Submit", bg="blue", fg="red", command=caller_func)
btn2.pack()

windows.geometry("500x500")
windows.mainloop()
