import pandas as pd
import tkinter as tk
import pd_val_def as val

def Excel_data():
    """Writes current data in Excel"""
    df = pd.DataFrame({
        "واحد اندازه گیری" : [val.value1, val.value2, val.value3, ],
        "تعداد" : [val.Number1],
        "دسته بندی" : [val.category1],
        "نام کالا" : [val.name1]
    })
    df.to_excel("data.xlsx", sheet_name="data", index=False)


# niazi be fujnc zir nist
def Excel():
    Excel_data()
    print("Data Saved In Computer")
