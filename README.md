# Cafebazaar Scraper Manual

This script scrapes the Cafebazaar.ir application page for comments using Python and Selenium. The input is the URL of your application's page, and the output is an `.xlsx` file containing the comments.

## Prerequisites
1. **Install Google Chrome:**
   [Google Chrome Download](https://www.google.com/chrome/)
2. **Install ChromeDriver:**
   [ChromeDriver Download](https://sites.google.com/chromium.org/driver/downloads)
3. **Install Python:**
   [Python Download](https://www.python.org/downloads/)
4. **Install Pip:**
   [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/)

## Setup
1. **Install Required Python Packages:**
   Open your command prompt or terminal and run the following commands to install Selenium, BeautifulSoup4, and Pandas:
   
   ```sh
   pip install selenium
   pip install beautifulsoup4
   pip install pandas
   ```

3. **Edit the Script:**
   Open the script file and change the `url` variable (line 10) to your application's page address on Cafebazaar.ir. Save the file after making this change.

   ```python
   url = 'https://cafebazaar.ir/app/com.farsitel.bazaar'  # Change this to your app page URL
   ```

4. **Run the Script:**
   Run the script using Python with the following command:

   ```sh
   python Cafebazaar_Scraper.py
   ```

   Wait until the script finishes execution. It will create an output file named `comments.xlsx` containing the scraped comments.





# راهنمای استفاده از اسکریپت Cafebazaar Scraper

این اسکریپت با استفاده از پایتون و Selenium، نظرات یک اپلیکیشن را از سایت کافه بازار Cafebazaar.ir استخراج می‌کند. ورودی این اسکریپت آدرس صفحه اپلیکیشن شما و خروجی آن یک فایل اکسل حاوی نظرات می‌باشد.

## پیش‌نیازها

1. **نصب Google Chrome:**
   [دانلود Google Chrome](https://www.google.com/chrome/)

2. **نصب ChromeDriver:**
   [دانلود ChromeDriver](https://sites.google.com/chromium.org/driver/downloads)

3. **نصب Python:**
   [دانلود Python](https://www.python.org/downloads/)

4. **نصب Pip:**
   [راهنمای نصب Pip](https://pip.pypa.io/en/stable/installation/)

## راه‌اندازی

1. **نصب پکیج‌های مورد نیاز پایتون:**
   ترمینال یا خط فرمان را باز کنید و دستورات زیر را برای نصب Selenium، BeautifulSoup4 و Pandas اجرا کنید:

   ```sh
   pip install selenium
   pip install beautifulsoup4
   pip install pandas
   ```

2. **ویرایش اسکریپت:**
   فایل اسکریپت را باز کرده و مقدار متغیر `url` (در خط 10) را به آدرس صفحه اپلیکیشن خود در سایت Cafebazaar.ir تغییر دهید. پس از انجام این تغییر، فایل را ذخیره کنید.

   ```python
   url = 'https://cafebazaar.ir/app/com.farsitel.bazaar'  # این را به آدرس صفحه اپلیکیشن خود تغییر دهید
   ```

3. **اجرای اسکریپت:**
   اسکریپت را با استفاده از پایتون با دستور زیر اجرا کنید:

   ```sh
   python Cafebazaar_Scraper.py
   ```

   صبر کنید تا اجرای اسکریپت به پایان برسد. این اسکریپت یک فایل خروجی با نام `comments.xlsx` حاوی نظرات استخراج شده ایجاد خواهد کرد.
