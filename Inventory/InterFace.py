import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import data
import email_center

windows = tk.Tk()

windows.title("انبار داری یزدان بافت | pxc")

# add source tab

Tab_control = ttk.Notebook(windows, width=5, height=1)
adding_resource_tab1 = ttk.Frame(Tab_control)
Tab_control.add(adding_resource_tab1, text="اضافه کردن کالا")
Tab_control.pack(expand=1, fill="both")

lbl = ttk.Label(text="انبار داری یزدان بافت | PXC app")
lbl1 = ttk.Label(text=".  .  .")
lbl2 = ttk.Label(text="Support in telegram @yasYZ_Dev")
lbl3 = ttk.Label(text="CopyRight CC by @TopUP")
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


spin_box = ttk.Spinbox(adding_resource_tab1, from_=0, to=1000000000000, textvariable=spin_value, wrap=True)
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

lbl4_upper = ttk.Label(adding_resource_tab1, text="مشخصات کالا")
lbl4_upper.pack()
txt1 = ttk.Entry(adding_resource_tab1)
txt1.pack()


def Find_Value_func3_Entry():
    """show Entry var"""
    Entry = txt1.get()
    data.in_Name.append(Entry)


lbl5_upper = ttk.Label(adding_resource_tab1, text="فرستنده")
lbl5_upper.pack()
txt2 = ttk.Entry(adding_resource_tab1)
txt2.pack()


def find_sender():
    """show Entry var"""
    entry = txt2.get()
    data.in_sender.append(entry)


# def situation():
#     if selected_var2.get() == "انبار کالای تولید شده":
#         data.in_Situation.append(f" تولید شده{txt1.get()}+{spin_value.get()}")
#     elif selected_var2.get() == "انبار مواد اولیه":
#         data.in_Situation.append(f"مواد اولیه (مواد مصرفی){txt1.get()}+{spin_value.get()}")
#     elif selected_var2.get() == "انبار درجریان ساخت":
#         data.in_Situation.append(f"قطعه وارد انبار شد{txt1.get()}+{spin_value.get()}")
#     else:
#         return


def caller_func():
    """check and import data to database"""
    Find_Value_func3_Entry()
    value_changed_spin()
    find_sender()
    if not (data.in_val or data.in_cat):
        file = open('log/ui_log.txt', 'a')
        file.write(f'data is not correct(user dont select option)\n')
        file.close()
        showinfo(
            title="Result",
            message="Try again Error101"
        )
        return
    elif data.in_Num == [0]:
        file = open('log/ui_log.txt', 'a')
        file.write(f'data is not correct(user dont input number)\n')
        file.close()
        showinfo(
            title="Result",
            message="Try again Error102"
        )
        return
    elif data.in_Name == [0]:
        file = open('log/ui_log.txt', 'a')
        file.write(f'data is not correct(user dont input product name)\n')
        file.close()
        showinfo(
            title="Result",
            message="Try again Error103"
        )
        return
    elif data.in_sender == [0]:
        file = open('log/ui_log.txt', 'a')
        file.write(f'data is not correct(user dont input sender name)\n')
        file.close()
        showinfo(
            title="Result",
            message="Try again Error104"
        )
        return
    else:
        file = open('log/ui_log.txt', 'a')
        file.write(f'data save in db\n')
        file.close()
        combo.set("")
        combo2.set("")
        spin_box.delete(0, tk.END)
        txt1.delete(0, tk.END)
        txt2.delete(0, tk.END)
        email_center.email_sender()
        data.data_saving()
        showinfo(
            title="Result",
            message="completed"
        )


btn2 = tk.Button(adding_resource_tab1, height=2, width=10, text="Submit", bg="blue", fg="white", command=caller_func)
btn2.pack()

# export source tab

export_resource_tab2 = ttk.Frame(Tab_control)
Tab_control.add(export_resource_tab2, text="ترخیص کالا")
Tab_control.pack(expand=1, fill="both")


selected_var4 = tk.StringVar()
lbl6 = tk.Label
combo3 = ttk.Combobox(export_resource_tab2, width=17, height=1, textvariable=selected_var4)
combo3["values"] = "همه"
combo3.set("همه")
combo3.pack()


def show_value(event):
    """show value data"""
    selected_value4 = selected_var4.get()
    showinfo(
        title='Result',
        message=f'You selected {selected_value4}!'
    )


data.show_all_values()


def value():
    for item in data.show_all_val:
        show_item = tk.Entry(export_resource_tab2, width=25)
        show_item.insert(tk.END, f"{item[0]}")
        show_item.configure(state="readonly")
        show_item.pack()


btn3 = tk.Button(export_resource_tab2, height=2, width=10, text="Submit", bg="blue", fg="white", command=value)
btn3.pack()
combo3.bind("<<ComboboxSelected>>", show_value)

# change source tab

change_resource_tab2 = ttk.Frame(Tab_control)
Tab_control.add(change_resource_tab2, text="تغییرات")
Tab_control.pack(expand=1, fill="both")

# show result

show_result_tab2 = ttk.Frame(Tab_control)
Tab_control.add(show_result_tab2, text="نمایش نتایج")
Tab_control.pack(expand=1, fill="both")

windows.geometry("500x500")
icon = tk.PhotoImage(file="../yazdan30x30.png")
windows.iconphoto(False, icon)

windows.mainloop()
