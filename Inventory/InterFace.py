import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import data
import export_source
import email_center

windows = tk.Tk()

windows.title("انبار داری یزدان بافت | pxc")

# add source tab

data.organization()

Tab_control = ttk.Notebook(windows, width=5, height=1)
adding_resource_tab1 = ttk.Frame(Tab_control)
Tab_control.add(adding_resource_tab1, text="اضافه کردن کالا")
Tab_control.pack(expand=1, fill="both")

lbl = ttk.Label(text="انبار داری یزدان بافت | PXC app")
lbl1 = ttk.Label(text=".  .  .")
lbl2 = ttk.Label(text="Support in telegram @yasYZ_Dev")
lbl3 = ttk.Label(text="CopyRight CC by @TopUP")
lbl4 = ttk.Label(text="V1.0.0.83")
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
        email_center.email_input_sender(name=data.in_Name, number=data.in_Num, category=data.in_cat)
        data.data_saving()
        showinfo(
            title="Result",
            message="completed"
        )


btn2 = tk.Button(adding_resource_tab1, height=2, width=10, text="Submit", bg="blue", fg="white", command=caller_func)
btn2.pack()

# export source tab

export_resource_tab2 = ttk.Frame(Tab_control)
Tab_control.add(export_resource_tab2, text="ترخیص کالا/نمایش نتایج")
Tab_control.pack(expand=1, fill="both")


selected_var4 = tk.StringVar()
lbl6 = tk.Label
combo3 = ttk.Combobox(export_resource_tab2, width=17, height=1, textvariable=selected_var4)
combo3["values"] = "همه", "جستجو"
combo3.set("همه")
combo3.pack()

index1 = [0]


def find_search_box_val():
    """show Entry var"""
    lbl10 = tk.Label(export_resource_tab2, text="search")
    lbl10.pack()
    search_box = tk.Entry(export_resource_tab2)
    search_box.pack()

    def search():
        entry = search_box.get()
        data.show_data.append(entry)
        data.data_show()
        if index1 == [0]:
            for i, row in enumerate(data.data_show_var):
                _, name, *_ = row
                create_button_search(i + 1, name)
            index1.remove(0)
            index1.append(1)
        else:
            file = open('log/ui_log.txt', 'a')
            file.write(f'**user dont change topic()!\n')
            file.close()
    btn4 = tk.Button(export_resource_tab2, text="جستجو", bg="blue", fg="white", command=search)
    btn4.pack()


def show_value(event):
    """show value data"""
    selected_value4 = selected_var4.get()
    data.del_all_showed_data()

    if selected_value4 == 'جستجو':
        try:
            data.__search_del__()
            find_search_box_val()
            index1.remove(1)
            index1.append(0)
        except ValueError as ex:
            print(f"selected {selected_value4}")
    elif selected_value4 == 'همه':
        try:
            submit()
            index1.remove(1)
            index1.append(0)
        except ValueError as ex:
            print(f"selected {selected_value4}")

    showinfo(
        title='Result',
        message=f'You selected {selected_value4}!'
    )


combo3.bind("<<ComboboxSelected>>", show_value)


def value():
    """write export source data on ui page"""
    data.del_all_showed_data()
    if index1 == [0]:
        data.select_row()
        for i, row in enumerate(data.row_data):
            _, name, *_ = row
            create_button(i + 1, name)
        index1.remove(0)
        index1.append(1)
    else:
        file = open('log/ui_log.txt', 'a')
        file.write(f'**user dont change topic()!\n')
        file.close()


def create_button(index, name):
    detail_button = tk.Button(export_resource_tab2, width=55, text=f" ترخیص کالا/نمایش نتایج/ {name} (ردیف کالا{index})", fg="blue", bg="white", command=lambda: export_source.export_tab(index-1, name))
    detail_button.pack()


def create_button_search(index, name):
    detail_button = tk.Button(export_resource_tab2, width=55, text=f" ترخیص کالا/نمایش نتایج/ {name} (ردیف کالا{index})", fg="blue", bg="white", command=lambda: export_source.export_tab_search(index-1, name))
    detail_button.pack()


def submit():
    btn3 = tk.Button(export_resource_tab2, height=2, width=10, text="Submit", bg="blue", fg="white", command=value)
    btn3.pack()

# coming soon for 2.0V...
# change source tab

# change_resource_tab2 = ttk.Frame(Tab_control)
# Tab_control.add(change_resource_tab2, text="تغییرات")
# Tab_control.pack(expand=1, fill="both")

# show result

# show_result_tab2 = ttk.Frame(Tab_control)
# Tab_control.add(show_result_tab2, text="نمایش نتایج")
# Tab_control.pack(expand=1, fill="both")

windows.geometry("500x500")

photo = tk.PhotoImage(file="../logoyazdan_32x32.ico")
windows.iconphoto(False, photo)

windows.mainloop()
