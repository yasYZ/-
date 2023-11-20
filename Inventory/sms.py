from persiantools.jdatetime import JalaliDate

# تبدیل تاریخ میلادی به شمسی
date_gregorian = JalaliDate.to_jalali(2023, 11, 18)

# دریافت سال، ماه و روز شمسی
year = date_gregorian.year
month = date_gregorian.month
day = date_gregorian.day