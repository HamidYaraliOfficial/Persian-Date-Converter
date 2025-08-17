# Persian Date Converter

This is a Python-based desktop application built with Tkinter for converting dates between Persian (Jalali), Gregorian, and Hijri calendars. It features a user-friendly interface with a dark/light theme toggle and a Jalali date picker for easy date selection.

## Features
- Convert dates between Persian (Jalali), Gregorian, and Hijri calendars.
- Input dates manually or select from a Jalali calendar popup.
- Validate date inputs for each calendar system (e.g., leap years, valid ranges).
- Support for both dark and light themes with a toggle button.
- Display converted dates in a clear, organized format.
- Persian-centric interface with support for Persian fonts (Sahel recommended).
- Error handling for invalid inputs and conversion issues.

## Requirements
- Python 3.7+
- `tkinter` (included with Python standard library)
- `jdatetime` library (`pip install jdatetime`)
- `hijri-converter` library (`pip install hijri-converter`)
- Optional: Sahel font for optimal Persian text rendering

## Setup
1. Install dependencies using `pip install -r requirements.txt` (create a `requirements.txt` with `jdatetime` and `hijri-converter`).
2. Optionally, ensure the Sahel font is installed on your system for proper Persian text display.
3. Run the application with `python app.py`.

## Usage
- Launch the application to open the main window.
- Select the date type (Persian, Gregorian, or Hijri) from the dropdown menu.
- Enter the day, month, and year in the provided fields or click the calendar button to select a date from the Jalali date picker.
- Click "Convert Date" to see the equivalent dates in all three calendar systems.
- Use the theme toggle button (🌙) to switch between dark and light modes.
- The application validates inputs and displays error messages for invalid dates.

## Code Structure
- `PersianDateConverter`: Main application class handling the UI, theme, and date conversion logic.
  - `apply_theme`: Configures dark/light theme styles.
  - `validate_date`: Ensures input dates are valid for the selected calendar.
  - `convert_date`: Performs date conversions using `jdatetime` and `hijri-converter`.
  - `update_results`: Displays converted dates in all three calendars.
  - `open_calendar`: Opens the Jalali date picker.
- `JalaliDatepicker`: Popup window for selecting dates in the Persian calendar.
  - `create_calendar`: Generates a dynamic calendar grid for the selected month.
  - `prev_month`, `next_month`: Navigate between months.
  - `update_month`, `update_year`: Update the calendar based on dropdown selections.
  - `select_date`: Sets the chosen date and updates the main window.

## Notes
- The application restricts Persian years to 1300–1500, Gregorian years to 1900–2100, and Hijri years to 1300–1500 for practical use.
- The Jalali calendar uses a 33-year cycle for leap year calculations.
- Ensure the Sahel font is installed for the best visual experience, though the app works with default fonts.

## License
MIT License

---

# مبدل تاریخ پارسی

این یک برنامه دسکتاپ مبتنی بر پایتون است که با استفاده از Tkinter ساخته شده و برای تبدیل تاریخ بین تقویم‌های پارسی (جلالی)، میلادی و قمری طراحی شده است. این برنامه دارای رابط کاربری ساده با قابلیت تغییر تم روشن/تاریک و انتخابگر تاریخ جلالی برای انتخاب آسان تاریخ است.

## ویژگی‌ها
- تبدیل تاریخ بین تقویم‌های پارسی (جلالی)، میلادی و قمری.
- ورود دستی تاریخ یا انتخاب از تقویم جلالی در پنجره پاپ‌آپ.
- اعتبارسنجی ورودی‌های تاریخ برای هر سیستم تقویمی (مانند سال‌های کبیسه و محدوده‌های معتبر).
- پشتیبانی از تم‌های روشن و تاریک با دکمه تغییر تم.
- نمایش تاریخ‌های تبدیل‌شده در قالبی منظم و واضح.
- رابط کاربری متمرکز بر پارسی با پشتیبانی از فونت پارسی (توصیه‌شده: فونت ساحل).
- مدیریت خطاها برای ورودی‌های نامعتبر و مشکلات تبدیل.

## پیش‌نیازها
- پایتون نسخه 3.7 یا بالاتر
- `tkinter` (موجود در کتابخانه استاندارد پایتون)
- کتابخانه `jdatetime` (نصب با `pip install jdatetime`)
- کتابخانه `hijri-converter` (نصب با `pip install hijri-converter`)
- اختیاری: فونت ساحل برای نمایش بهینه متن پارسی

## راه‌اندازی
1. وابستگی‌ها را با استفاده از `pip install -r requirements.txt` نصب کنید (فایل `requirements.txt` را با درج `jdatetime` و `hijri-converter` ایجاد کنید).
2. در صورت تمایل، فونت ساحل را روی سیستم خود نصب کنید تا نمایش متن پارسی بهینه باشد.
3. برنامه را با اجرای `python app.py` راه‌اندازی کنید.

## استفاده
- برنامه را اجرا کنید تا پنجره اصلی باز شود.
- نوع تاریخ (شمسی، میلادی یا قمری) را از منوی کشویی انتخاب کنید.
- روز، ماه و سال را در فیلدهای مربوطه وارد کنید یا با کلیک بر روی دکمه تقویم، تاریخ را از انتخابگر تاریخ جلالی انتخاب کنید.
- روی دکمه "تبدیل تاریخ" کلیک کنید تا معادل تاریخ در هر سه سیستم تقویمی نمایش داده شود.
- از دکمه تغییر تم (🌙) برای جابه‌جایی بین حالت‌های روشن و تاریک استفاده کنید.
- برنامه ورودی‌ها را اعتبارسنجی کرده و در صورت وجود تاریخ نامعتبر، پیام خطا نمایش می‌دهد.

## ساختار کد
- `PersianDateConverter`: کلاس اصلی برنامه که رابط کاربری، تم و منطق تبدیل تاریخ را مدیریت می‌کند.
  - `apply_theme`: تنظیم استایل‌های تم روشن/تاریک.
  - `validate_date`: اطمینان از معتبر بودن تاریخ‌های ورودی برای تقویم انتخاب‌شده.
  - `convert_date`: انجام تبدیل تاریخ با استفاده از `jdatetime` و `hijri-converter`.
  - `update_results`: نمایش تاریخ‌های تبدیل‌شده در هر سه تقویم.
  - `open_calendar`: باز کردن انتخابگر تاریخ جلالی.
- `JalaliDatepicker`: پنجره پاپ‌آپ برای انتخاب تاریخ در تقویم جلالی.
  - `create_calendar`: تولید شبکه تقویمی پویا برای ماه انتخاب‌شده.
  - `prev_month`، `next_month`: جابه‌جایی بین ماه‌ها.
  - `update_month`، `update_year`: به‌روزرسانی تقویم بر اساس انتخاب‌های منوی کشویی.
  - `select_date`: تنظیم تاریخ انتخاب‌شده و به‌روزرسانی پنجره اصلی.

## نکات
- برنامه سال‌های پارسی را به ۱۳۰۰–۱۵۰۰، سال‌های میلادی را به ۱۹۰۰–۲۱۰۰ و سال‌های قمری را به ۱۳۰۰–۱۵۰۰ محدود کرده است.
- تقویم جلالی از چرخه ۳۳ ساله برای محاسبه سال‌های کبیسه استفاده می‌کند.
- برای بهترین تجربه بصری، نصب فونت ساحل توصیه می‌شود، هرچند برنامه با فونت‌های پیش‌فرض نیز کار می‌کند.

## مجوز
مجوز MIT

---

# 波斯日期转换器

这是一个基于Python的桌面应用程序，使用Tkinter构建，用于在波斯（贾利利）、公历和回历之间进行日期转换。它具有用户友好的界面，支持深色/浅色主题切换，并提供贾利利日期选择器以便于日期选择。

## 功能
- 在波斯（贾利利）、公历和回历之间转换日期。
- 手动输入日期或从贾利利日期选择器中选择。
- 验证每个日历系统的输入日期（例如闰年、有效范围）。
- 支持深色和浅色主题，通过按钮切换。
- 以清晰、组织化的格式显示转换后的日期。
- 以波斯语为中心，支持波斯字体（推荐使用Sahel字体）。
- 处理无效输入和转换问题的错误。

## 要求
- Python 3.7或更高版本
- `tkinter`（Python标准库中包含）
- `jdatetime`库（使用`pip install jdatetime`安装）
- `hijri-converter`库（使用`pip install hijri-converter`安装）
- 可选：Sahel字体，用于最佳波斯文本渲染

## 设置
1. 使用`pip install -r requirements.txt`安装依赖项（创建一个包含`jdatetime`和`hijri-converter`的`requirements.txt`文件）。
2. 可选：确保系统上安装了Sahel字体以优化波斯文本显示。
3. 使用`python app.py`运行应用程序。

## 使用
- 启动应用程序以打开主窗口。
- 从下拉菜单中选择日期类型（波斯、公历或回历）。
- 在提供的字段中输入日、月、年，或点击日历按钮从贾利利日期选择器中选择日期。
- 点击“转换日期”按钮查看所有三种日历系统的等效日期。
- 使用主题切换按钮（🌙）在深色和浅色模式之间切换。
- 应用程序验证输入，并在日期无效时显示错误消息。

## 代码结构
- `PersianDateConverter`：主应用程序类，处理用户界面、主题和日期转换逻辑。
  - `apply_theme`：配置深色/浅色主题样式。
  - `validate_date`：确保所选日历的输入日期有效。
  - `convert_date`：使用`jdatetime`和`hijri-converter`执行日期转换。
  - `update_results`：显示所有三种日历的转换日期。
  - `open_calendar`：打开贾利利日期选择器。
- `JalaliDatepicker`：用于在波斯日历中选择日期的弹出窗口。
  - `create_calendar`：为所选月份生成动态日历网格。
  - `prev_month`、`next_month`：在月份之间导航。
  - `update_month`、`update_year`：根据下拉菜单选择更新日历。
  - `select_date`：设置所选日期并更新主窗口。

## 注意事项
- 应用程序将波斯年份限制在1300–1500，公历年份限制在1900–2100，回历年份限制在1300–1500，以适应实际使用。
- 贾利利日历使用33年周期计算闰年。
- 为获得最佳视觉体验，建议安装Sahel字体，尽管应用程序也支持默认字体。

## 许可证
MIT许可证