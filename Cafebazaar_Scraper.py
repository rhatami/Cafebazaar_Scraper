from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

### Put your app page URL here ###
url = 'https://cafebazaar.ir/app/com.farsitel.bazaar'
### Put your app page URL here ###

print("Starting the Scraping process ...")

# Initialize the WebDriver and getting the URL
driver = webdriver.Chrome()
driver.get(url)

# Function to scroll and load more comments until there is no load more button
def load_more_comments(driver):
    print("Loading all comments. Please wait ...")
    
    while True:
        try:
            # Wait for the load more button to be clickable and click it
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'AppCommentsList__loadmore'))
            )
            load_more_button.click()
            time.sleep(2)  # Wait for new comments to load
        except:
            break

#1 Load all the comments
load_more_comments(driver)

print("All comments loaded. Extracting the information. Please wait ...")

#2 Parse the page source
soup = BeautifulSoup(driver.page_source, 'html.parser')

#3 Extract all the comments blocks
comments = soup.find_all(class_='AppCommentsList__item')

#4 Extract comment details
comment_list = []
for comment in comments:
    # Extracting Username
    user = comment.find(class_='AppComment__profile').get_text(strip=True)
    # Extracting Comment Text
    comment_text = comment.find(class_='AppComment__body').get_text(strip=True)
    # Extract and conver the star rating to numeric scale
    meta = comment.find(class_='AppComment__meta')
    rating_fill = meta.find(class_='rating__fill')['style']
    rating_percentage = float(rating_fill.split('width:')[1].split('%')[0].strip())
    rating = round(rating_percentage / 20)  # Convert percentage to a 5-star scale
    # Extracting Date
    date = meta.find_all('div')[-1].get_text(strip=True)
    # Adding comment to the comment_list
    comment_list.append({
        'User': user,
        'Date': date,
        'Comment': comment_text,
        'Rating': rating
    })

# Close the WebDriver
driver.quit()

print("Data extraction completed. Writing data to file. Please wait ...")

#5 Save the data to an Excel file
output_file = 'comments.xlsx'
df = pd.DataFrame(comment_list)
df.to_excel(output_file, index=False)

print("Scraping complete. Data saved to " + output_file)
