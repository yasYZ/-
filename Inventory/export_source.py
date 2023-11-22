import tkinter as tk
import datetime
from tkinter import ttk
from tkinter.messagebox import showinfo
import data
import email_center


def export_tab(row_index):
    export_page = tk.Tk()
    export_page.title("ترخیص کالا | PXC")

    lbl_detail = tk.Label(export_page, text="جزییات و ترخبص کالا")
    lbl_detail.pack()
    data.select_row()

    labels = ["شماره محصول", "مشخصات", "انبار", "واحد اندازه گیری", "مقدار", "وضعیت", "تاریخ", "فرستنده"]

    for index, item in enumerate(data.row_data[row_index]):
        label = labels[index]
        lbl_detail = tk.Label(export_page, text=f"{label}")
        lbl_detail.pack()

        show_item = tk.Entry(export_page, width=25)
        show_item.pack()
        show_item.insert(tk.END, item)
        show_item.configure(state="readonly")

    lbl1 = tk.Label(export_page, text="____________________________________")
    lbl1.pack()
    lbl2 = tk.Label(export_page, text="مقدار ترخیص")
    lbl2.pack()

    spin_box = tk.StringVar(value=0)
    spin_box = ttk.Spinbox(export_page, from_=0, to=1000000000000, textvariable=spin_box, wrap=True)
    spin_box.pack()

    def value_changed_spin():
        """show Number data"""
        data.select_exporter()
        spin = [spin_box.get()]
        showinfo(title='Result', message=f'You selected{spin[0]}!')
        for x, y in zip(data.selected_number, spin):
            data.out_number.append(int(x[0]) - int(y))
            print((int(x[0]) - int(y)))
            for item in spin:
                spin.remove(item)

    def exporter_activate():
        value_changed_spin()
        data.find_number_val()
        if spin_box.get() is None:
            file0 = open('log/ui_log.txt', 'a')
            file0.write(f'**data does not exist. error in {datetime.datetime.today()}!\n')
            file0.close()
        elif data.zero_number == [0]:
            data.change_situation(row_index)
            data.update_query(row_index)
            showinfo(
                title="با موفقیت انجام شد",
                message="""کالا با موفقبت از سیستم انبارداری خارج شد اپ به طور خودکار بسته میشود در صورت استفاده دوباره اپ را دوباره باز کنین"""
            )
            exit(0)
        else:
            # __index__ = row_index + 1
            data.update_query(row_index)
            showinfo(
                title="با موفقیت انجام شد",
                message="""کالا با موفقبت از سیستم انبارداری خارج شد اپ به طور خودکار بسته میشود در صورت استفاده دوباره اپ را دوباره باز کنین"""
            )
            exit(0)

    btn = tk.Button(export_page, text="Submit", width=10, height=2, bg="blue", fg="white", command=exporter_activate)
    btn.pack()
    data.del_all_showed_data()
    export_page.geometry("300x500")
    # icon = tk.PhotoImage(file="../yazdan30x30.png")
    # export_page.iconphoto(False, icon)
    export_page.mainloop()


def export_tab_search(row_index, name):
    export_page = tk.Tk()
    export_page.title("ترخیص کالا | PXC")

    lbl_detail = tk.Label(export_page, text="جزییات و ترخبص کالا")
    lbl_detail.pack()
    data.data_show()

    labels = ["شماره محصول", "مشخصات", "انبار", "واحد اندازه گیری", "مقدار", "وضعیت", "تاریخ", "فرستنده"]

    for index, item in enumerate(data.data_show_var[row_index]):
        label = labels[index]
        lbl_detail = tk.Label(export_page, text=f"{label}")
        lbl_detail.pack()

        show_item = tk.Entry(export_page, width=25)
        show_item.pack()
        show_item.insert(tk.END, item)
        show_item.configure(state="readonly")

    lbl1 = tk.Label(export_page, text="____________________________________")
    lbl1.pack()
    lbl2 = tk.Label(export_page, text="مقدار ترخیص")
    lbl2.pack()

    spin_box = tk.StringVar(value=0)
    spin_box = ttk.Spinbox(export_page, from_=0, to=1000000000000, textvariable=spin_box, wrap=True)
    spin_box.pack()

    def value_changed_spin():
        """show Number data"""
        data.select_exporter()
        data.insert_number.append(row_index+1)
        spin = [spin_box.get()]
        showinfo(title='Result', message=f'You selected{spin[0]}!')
        for x, y in zip(data.selected_number, spin):
            data.out_number.append(int(x[0]) - int(y))
            for item in spin:
                spin.remove(item)

    def exporter_activate():
        value_changed_spin()
        data.find_number_val()
        if spin_box.get() is None:
            file0 = open('log/ui_log.txt', 'a')
            file0.write(f'**data does not exist. error in {datetime.datetime.today()}!\n')
            file0.close()
        elif data.zero_number == '0':
            data.change_situation(row_index)
            data.update_query(row_index)
            showinfo(
                title="با موفقیت انجام شد",
                message="""کالا با موفقبت از سیستم انبارداری خارج شد اپ به طور خودکار بسته میشود در صورت استفاده دوباره اپ را دوباره باز کنین"""
            )
            email_center.email_export_sender(name=row_index, number=spin_box.get())
            exit(0)
        else:
            data.update_query(row_index)
            showinfo(
                title="با موفقیت انجام شد",
                message="""کالا با موفقبت از سیستم انبارداری خارج شد اپ به طور خودکار بسته میشود در صورت استفاده دوباره اپ را دوباره باز کنین"""
            )
            email_center.email_export_sender(name=name, number=spin_box.get())
            exit(0)
    btn = tk.Button(export_page, text="Submit", width=10, height=2, bg="blue", fg="white", command=exporter_activate)
    btn.pack()
    data.del_all_showed_data()
    export_page.geometry("300x500")
    # icon = tk.PhotoImage(file="../yazdan30x30.png")
    # export_page.iconphoto(False, icon)
    export_page.mainloop()
