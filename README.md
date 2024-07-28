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
   
