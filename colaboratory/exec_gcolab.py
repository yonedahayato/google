from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import chromedriver_binary

from setting import (
    COLAB_URL,
    GOOGLE_PASS,
    GOOGLE_ID,
)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--remote-debugging-port=9222")
chromeOptions.add_argument("--headless")

chromeOptions.add_argument('--no-sandbox')

driver = webdriver.Chrome(chrome_options=chromeOptions)
url = COLAB_URL

login_id = GOOGLE_ID
pas = GOOGLE_PASS

# ページを開く
driver.get(url)

time.sleep(5)
# ログイン画面:userid
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(login_id)
driver.find_element_by_class_name('CwaK9').click()
time.sleep(2)

# ログイン画面:pwd
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(pas)
driver.find_element_by_xpath("//*[@id='passwordNext']").click()
time.sleep(10)

# Google Colab
print(driver.current_url)
driver.find_element_by_class_name('cell-execution').click() #セルの実行
