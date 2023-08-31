import tkinter

window = tkinter.Tk()
window.title("انبار داری یزدان بافت | yazdanbaft inventory")
l1 = tkinter.Label(window, text="یزدان بافت ایرانیان", font=("Aviny" ,50)).pack()

window.geometry("1280x720")

bt = tkinter.Button(window, text="Enter")
bt.grid(column=0, row=0)


window.mainloop()

