# library
import logzero
from logzero import logger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# library setting
import chromedriver_binary

from setting import (
    COLAB_URL,
    GOOGLE_PASS,
    GOOGLE_ID,
)

logzero.logfile('./log/exec_gcolab.log')

# setting
userdata_dir = "./userdata"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--remote-debugging-port=9222")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--lang=ja')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--user-data-dir=' + userdata_dir)

driver = webdriver.Chrome(chrome_options=chromeOptions)
url = COLAB_URL

login_id = GOOGLE_ID
pas = GOOGLE_PASS

def main():
    # ページを開く
    driver.get(url)
    logger.info("ページを開きました。: {}".format(url))
    time.sleep(2)

    try:
        logger.info("手順1を試みます。")
        # ログイン画面:userid
        driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(login_id)
        driver.find_element_by_class_name('CwaK9').click()
        time.sleep(2)
        # ログイン画面:pwd
        driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(pas)
        driver.find_element_by_xpath("//*[@id='passwordNext']").click()
    except:
        logger.info("手順1が失敗しました。")
        try:
            logger.info("手順2を試みます。")
            # ログイン画面:userid
            driver.find_element_by_xpath("//*[@id='Email']").send_keys(login_id)
            driver.find_element_by_xpath("//*[@id='next']").click()
            time.sleep(2)
            # ログイン画面:pwd
            driver.find_element_by_xpath("//*[@id='Passwd']").send_keys(pas)
            driver.find_element_by_xpath("//*[@id='signIn']").click()
        except:
            logger.info("手順2が失敗しました。")
            save_file_for_debug(driver)
        else:
            logger.info("手順2が成功しました。")
    else:
        logger.info("手順1が成功しました。")

    time.sleep(10)

    try:
        logger.info("Colabの実行を試みます。")
        # Google Colab
        logger.info(driver.current_url)
        driver.find_element_by_class_name('cell-execution').click() #セルの実行
    except Exception as e:
        logger.error("Colabの実行が失敗しました。")
        logger.exception(e)
        save_file_for_debug(driver)
    else:
        logger.info("Colabの実行が成功しました。")
        time.sleep(60)
        save_file_for_debug(driver)

    driver.close()
    driver.quit()

def save_file_for_debug(driver):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    driver.save_screenshot('./log/screenshot_{}.png'.format(now))
    html = driver.page_source
    with open('./log/page_{}.html'.format(now), 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == "__main__":
    main()
