import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.nytimes.com/")
sleep(5)

today_date = datetime.today().strftime("%Y-%m-%d")

driver.maximize_window()
sleep(2)

elements = driver.find_elements(By.CSS_SELECTOR, ".indicate-hover")

data_list = []

for element in elements:
    article_title = element.text

    if article_title:
        data_list.append({
            "Date": today_date,
            "Title": article_title
        })

df = pd.DataFrame(data_list)

csv_file = "nyt_article.csv"
df.to_csv(csv_file, index=False)

print(f"Data Saved to {csv_file}")

driver.quit()