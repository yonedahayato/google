import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

userdata_dir = 'UserData'  # カレントディレクトリの直下にUser Profile 作る場合
os.makedirs(userdata_dir, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')

# User Profile のpath設定
options.add_argument('--user-data-dir=' + userdata_dir)

driver_path = os.getcwd() + "/chromedriver"
driver = webdriver.Chrome(driver_path, options=options)
try:
    driver.get("https://google.com")
except:
    driver.quit()
finally:
    driver.quit()
