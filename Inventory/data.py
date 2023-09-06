import pandas as pd


def Excel_data():
    """Writes current data in Excel"""
    df = pd.DataFrame([[f"value", f"Number", f"category"],
                       [f"12", f"22", f"32"],
                       [f"31", f"32", f"33"],
                       [f"31", f"32", f"33"],
                       [f"31", f"32", f"33"],
                       [f"31", f"32", f"1000"]],
                  index=["1", "2", "3", "4", "5", "6"], columns=["واحد اندازه گیری", "تعداد", "دسته بندی"])

    df.to_excel('data.xlsx', sheet_name='data')

Excel_data()