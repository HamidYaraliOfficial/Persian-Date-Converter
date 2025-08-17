import tkinter as tk
from tkinter import ttk, messagebox
import jdatetime
from hijri_converter import convert
from datetime import datetime

class PersianDateConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("مبدل تاریخ پارسی")
        self.geometry("400x600")
        self.resizable(False, False)
        
        self.selected_date = jdatetime.date.today()
        self.is_dark_theme = False
        self.create_widgets()
        self.apply_theme()

    def is_persian_leap_year(self, year):
        cycle_position = year % 33
        return cycle_position in [1, 5, 9, 13, 17, 22, 26, 30]

    def apply_theme(self):
        bg_color = "#1e1e1e" if self.is_dark_theme else "#ffffff"
        fg_color = "#ffffff" if self.is_dark_theme else "#212121"
        entry_bg = "#2c2c2c" if self.is_dark_theme else "#f5f5f5"
        button_bg = "#3f51b5" if self.is_dark_theme else "#6200ea"
        button_fg = "#ffffff"
        frame_bg = "#2a2a2a" if self.is_dark_theme else "#fafafa"
        
        self.configure(bg=bg_color)
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("TFrame", background=frame_bg)
        style.configure("TLabel", background=frame_bg, foreground=fg_color, font=("Sahel", 12))
        style.configure("TButton", background=button_bg, foreground=button_fg, 
                       font=("Sahel", 12, "bold"), padding=8, borderwidth=0)
        style.configure("TCombobox", fieldbackground=entry_bg, foreground=fg_color, 
                       font=("Sahel", 12), arrowsize=14)
        style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color, 
                       font=("Sahel", 12), padding=5)
        style.map("TButton", background=[('active', '#5c6bc0' if self.is_dark_theme else '#7c4dff')])
        style.map("TCombobox", fieldbackground=[('readonly', entry_bg)])

    def toggle_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme()
        for widget in self.winfo_children():
            widget.configure(style="TFrame")
            for child in widget.winfo_children():
                child.configure(style=child.winfo_class())

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        
        # Theme toggle button
        theme_button = ttk.Button(main_frame, text="🌙 روشن/تاریک", command=self.toggle_theme, width=12)
        theme_button.grid(row=0, column=0, pady=10)
        
        # Date input frame
        input_frame = ttk.LabelFrame(main_frame, text="ورود تاریخ", padding="15")
        input_frame.grid(row=1, column=0, pady=15, sticky=(tk.E, tk.W))
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.columnconfigure(3, weight=1)
        
        # Date type selection
        ttk.Label(input_frame, text="نوع تاریخ:").grid(row=0, column=3, padx=10, pady=8)
        self.date_type = tk.StringVar(value="شمسی")
        date_types = ["شمسی", "میلادی", "قمری"]
        self.date_type_combo = ttk.Combobox(input_frame, textvariable=self.date_type, 
                                          values=date_types, state="readonly", width=12)
        self.date_type_combo.grid(row=0, column=2, padx=10, pady=8)
        self.date_type_combo.bind("<<ComboboxSelected>>", self.update_date_fields)
        
        # Date fields
        ttk.Label(input_frame, text="روز:").grid(row=0, column=1, padx=10, pady=8)
        self.day_var = tk.StringVar(value=str(self.selected_date.day))
        self.day_entry = ttk.Entry(input_frame, textvariable=self.day_var, width=6)
        self.day_entry.grid(row=0, column=0, padx=10, pady=8)
        
        ttk.Label(input_frame, text="ماه:").grid(row=1, column=1, padx=10, pady=8)
        self.month_var = tk.StringVar(value=str(self.selected_date.month))
        self.month_entry = ttk.Entry(input_frame, textvariable=self.month_var, width=6)
        self.month_entry.grid(row=1, column=0, padx=10, pady=8)
        
        ttk.Label(input_frame, text="سال:").grid(row=2, column=1, padx=10, pady=8)
        self.year_var = tk.StringVar(value=str(self.selected_date.year))
        self.year_entry = ttk.Entry(input_frame, textvariable=self.year_var, width=8)
        self.year_entry.grid(row=2, column=0, padx=10, pady=8)
        
        # Calendar button
        ttk.Button(input_frame, text="📅 تقویم", command=self.open_calendar, width=12).grid(
            row=1, column=2, columnspan=2, padx=10, pady=8)
        
        # Conversion frame
        convert_frame = ttk.LabelFrame(main_frame, text="نتایج تبدیل", padding="15")
        convert_frame.grid(row=2, column=0, pady=15, sticky=(tk.E, tk.W))
        convert_frame.columnconfigure(0, weight=1)
        
        # Result labels
        self.result_jalali = ttk.Label(convert_frame, text="شمسی: ", font=("Sahel", 12))
        self.result_jalali.grid(row=0, column=0, padx=10, pady=8)
        
        self.result_gregorian = ttk.Label(convert_frame, text="میلادی: ", font=("Sahel", 12))
        self.result_gregorian.grid(row=1, column=0, padx=10, pady=8)
        
        self.result_hijri = ttk.Label(convert_frame, text="قمری: ", font=("Sahel", 12))
        self.result_hijri.grid(row=2, column=0, padx=10, pady=8)
        
        # Convert button
        ttk.Button(main_frame, text="تبدیل تاریخ", command=self.convert_date, width=15).grid(
            row=3, column=0, pady=20)
        
        self.update_results()

    def open_calendar(self):
        datepicker = JalaliDatepicker(self, self.day_var, self.month_var, self.year_var)
        datepicker.grab_set()

    def validate_date(self, year, month, day, date_type):
        try:
            year = int(year)
            month = int(month)
            day = int(day)
            
            if date_type == "شمسی":
                max_days = 30 if month > 6 else 31
                if month == 12:
                    max_days = 30 if self.is_persian_leap_year(year) else 29
                if not (1 <= month <= 12):
                    return False, "ماه باید بین ۱ تا ۱۲ باشد"
                if not (1 <= day <= max_days):
                    return False, f"روز باید بین ۱ تا {max_days} باشد"
                if not (1300 <= year <= 1500):
                    return False, "سال باید بین ۱۳۰۰ تا ۱۵۰۰ باشد"
            elif date_type == "میلادی":
                if not (1 <= month <= 12):
                    return False, "ماه باید بین ۱ تا ۱۲ باشد"
                max_days = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30
                if month == 2:
                    max_days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
                if not (1 <= day <= max_days):
                    return False, f"روز باید بین ۱ تا {max_days} باشد"
                if not (1900 <= year <= 2100):
                    return False, "سال باید بین ۱۹۰۰ تا ۲۱۰۰ باشد"
            else:  # قمری
                if not (1 <= month <= 12):
                    return False, "ماه باید بین ۱ تا ۱۲ باشد"
                max_days = 30 if month in [2, 4, 6, 8, 10, 12] else 29
                if not (1 <= day <= max_days):
                    return False, f"روز باید بین ۱ تا {max_days} باشد"
                if not (1300 <= year <= 1500):
                    return False, "سال باید بین ۱۳۰۰ تا ۱۵۰۰ باشد"
            return True, ""
        except ValueError:
            return False, "لطفاً مقادیر عددی معتبر وارد کنید"

    def update_date_fields(self, event=None):
        date_type = self.date_type.get()
        try:
            if date_type == "شمسی":
                self.day_var.set(str(self.selected_date.day))
                self.month_var.set(str(self.selected_date.month))
                self.year_var.set(str(self.selected_date.year))
            elif date_type == "میلادی":
                gregorian = self.selected_date.togregorian()
                self.day_var.set(str(gregorian.day))
                self.month_var.set(str(gregorian.month))
                self.year_var.set(str(gregorian.year))
            else:  # قمری
                hijri = convert.Gregorian(self.selected_date.togregorian().year,
                                      self.selected_date.togregorian().month,
                                      self.selected_date.togregorian().day).to_hijri()
                self.day_var.set(str(hijri.day))
                self.month_var.set(str(hijri.month))
                self.year_var.set(str(hijri.year))
            self.update_results()
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در به‌روزرسانی تاریخ: {str(e)}")

    def convert_date(self):
        year = self.year_var.get()
        month = self.month_var.get()
        day = self.day_var.get()
        date_type = self.date_type.get()
        
        valid, error_message = self.validate_date(year, month, day, date_type)
        if not valid:
            messagebox.showerror("خطا", error_message)
            return
            
        try:
            year = int(year)
            month = int(month)
            day = int(day)
            
            if date_type == "شمسی":
                self.selected_date = jdatetime.date(year, month, day)
            elif date_type == "میلادی":
                self.selected_date = jdatetime.date.fromgregorian(
                    year=year, month=month, day=day)
            else:  # قمری
                gregorian = convert.Hijri(year, month, day).to_gregorian()
                self.selected_date = jdatetime.date.fromgregorian(
                    year=gregorian.year, month=gregorian.month, day=gregorian.day)
            
            self.update_results()
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در تبدیل تاریخ: {str(e)}")

    def update_results(self):
        try:
            # Jalali date
            jalali_str = self.selected_date.strftime("%Y/%m/%d")
            self.result_jalali.config(text=f"شمسی: {jalali_str}")
            
            # Gregorian date
            gregorian = self.selected_date.togregorian()
            gregorian_str = gregorian.strftime("%Y/%m/%d")
            self.result_gregorian.config(text=f"میلادی: {gregorian_str}")
            
            # Hijri date
            hijri = convert.Gregorian(gregorian.year, gregorian.month, 
                                   gregorian.day).to_hijri()
            hijri_str = f"{hijri.year}/{hijri.month:02d}/{hijri.day:02d}"
            self.result_hijri.config(text=f"قمری: {hijri_str}")
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در نمایش نتایج: {str(e)}")

class JalaliDatepicker(tk.Toplevel):
    def __init__(self, master, day_var, month_var, year_var):
        super().__init__(master)
        self.day_var = day_var
        self.month_var = month_var
        self.year_var = year_var
        self.title("تقویم پارسی")
        self.geometry("400x450")
        self.resizable(False, False)
        
        self.selected_date = jdatetime.date.today()
        self.min_year = 1300
        self.max_year = 1500
        self.apply_theme()
        self.create_widgets()

    def is_persian_leap_year(self, year):
        cycle_position = year % 33
        return cycle_position in [1, 5, 9, 13, 17, 22, 26, 30]

    def apply_theme(self):
        bg_color = "#1e1e1e" if self.master.is_dark_theme else "#ffffff"
        fg_color = "#ffffff" if self.master.is_dark_theme else "#212121"
        button_bg = "#3f51b5" if self.master.is_dark_theme else "#6200ea"
        button_fg = "#ffffff"
        frame_bg = "#2a2a2a" if self.master.is_dark_theme else "#fafafa"
        
        self.configure(bg=bg_color)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background=frame_bg)
        style.configure("TLabel", background=frame_bg, foreground=fg_color, font=("Sahel", 12))
        style.configure("TButton", background=button_bg, foreground=button_fg, 
                       font=("Sahel", 12, "bold"), padding=6, borderwidth=0)
        style.configure("TCombobox", fieldbackground=frame_bg, foreground=fg_color, 
                       font=("Sahel", 12), arrowsize=14)
        style.map("TButton", background=[('active', '#5c6bc0' if self.master.is_dark_theme else '#7c4dff')])

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="15")
        main_frame.pack(fill="both", expand=True)
        main_frame.columnconfigure(0, weight=1)
        
        self.date_label = ttk.Label(main_frame, text=self.selected_date.strftime("%Y/%m/%d"), font=("Sahel", 14))
        self.date_label.pack(pady=15)
        
        # Navigation frame
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(fill="x")
        nav_frame.columnconfigure(0, weight=1)
        nav_frame.columnconfigure(1, weight=1)
        nav_frame.columnconfigure(2, weight=1)
        
        ttk.Button(nav_frame, text="◄", command=self.prev_month, width=3).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(nav_frame, text="►", command=self.next_month, width=3).grid(row=0, column=2, padx=5, pady=5)
        
        self.month_var = tk.StringVar()
        self.month_dropdown = ttk.Combobox(
            nav_frame, textvariable=self.month_var, state="readonly", width=12)
        self.month_dropdown['values'] = (
            'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
            'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند')
        self.month_dropdown.set(self.month_dropdown['values'][self.selected_date.month-1])
        self.month_dropdown.bind("<<ComboboxSelected>>", self.update_month)
        self.month_dropdown.grid(row=0, column=1, padx=5, pady=5)
        
        self.year_var = tk.StringVar(value=str(self.selected_date.year))
        self.year_dropdown = ttk.Combobox(
            nav_frame, textvariable=self.year_var, state="readonly", width=8)
        self.year_dropdown['values'] = list(range(self.min_year, self.max_year + 1))
        self.year_dropdown.bind("<<ComboboxSelected>>", self.update_year)
        self.year_dropdown.grid(row=1, column=1, padx=5, pady=5)
        
        self.calendar_frame = ttk.Frame(main_frame)
        self.calendar_frame.pack(fill="both", expand=True, pady=10)
        
        self.create_calendar()

    def create_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
            
        day_names = ["ش", "ی", "د", "س", "چ", "پ", "ج"]
        for i, day_name in enumerate(day_names):
            label = ttk.Label(self.calendar_frame, text=day_name, anchor="center", font=("Sahel", 12, "bold"))
            label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            
        year = self.selected_date.year
        month = self.selected_date.month
        num_days = 30 if month > 6 else 31
        if month == 12:
            num_days = 30 if self.is_persian_leap_year(year) else 29
            
        first_day = jdatetime.date(year, month, 1).weekday()
        
        for day in range(1, num_days + 1):
            row = (first_day + day - 1) // 7 + 1
            col = (first_day + day - 1) % 7
            button = ttk.Button(self.calendar_frame, text=str(day), 
                              command=lambda d=day: self.select_date(d), width=4)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
        for i in range(7):
            self.calendar_frame.columnconfigure(i, weight=1)
        for i in range(7):
            self.calendar_frame.rowconfigure(i, weight=1)

    def prev_month(self):
        month = self.selected_date.month - 1
        year = self.selected_date.year
        if month == 0:
            month = 12
            year -= 1
        if year >= self.min_year:
            self.selected_date = jdatetime.date(year, month, min(self.selected_date.day, 30))
            self.month_dropdown.set(self.month_dropdown['values'][month-1])
            self.year_var.set(str(year))
            self.create_calendar()
            self.date_label.config(text=self.selected_date.strftime("%Y/%m/%d"))

    def next_month(self):
        month = self.selected_date.month + 1
        year = self.selected_date.year
        if month == 13:
            month = 1
            year += 1
        if year <= self.max_year:
            self.selected_date = jdatetime.date(year, month, min(self.selected_date.day, 30))
            self.month_dropdown.set(self.month_dropdown['values'][month-1])
            self.year_var.set(str(year))
            self.create_calendar()
            self.date_label.config(text=self.selected_date.strftime("%Y/%m/%d"))

    def update_month(self, event):
        month_index = self.month_dropdown['values'].index(self.month_var.get()) + 1
        self.selected_date = jdatetime.date(
            self.selected_date.year, month_index, min(self.selected_date.day, 30))
        self.create_calendar()
        self.date_label.config(text=self.selected_date.strftime("%Y/%m/%d"))

    def update_year(self, event):
        selected_year = int(self.year_var.get())
        self.selected_date = jdatetime.date(
            selected_year, self.selected_date.month, min(self.selected_date.day, 30))
        self.create_calendar()
        self.date_label.config(text=self.selected_date.strftime("%Y/%m/%d"))

    def select_date(self, day):
        self.selected_date = jdatetime.date(
            self.selected_date.year, self.selected_date.month, day)
        self.day_var.set(str(self.selected_date.day))
        self.month_var.set(str(self.selected_date.month))
        self.year_var.set(str(self.selected_date.year))
        self.master.date_type.set("شمسی")  # Set date type to Jalali when selecting from calendar
        self.master.convert_date()  # Trigger conversion to update results
        self.destroy()

if __name__ == "__main__":
    app = PersianDateConverter()
    app.mainloop()