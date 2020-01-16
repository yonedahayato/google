# set options to be headless, ..
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import subprocess as sp
from datetime import datetime, timedelta, timezone
import urllib3
import time
import os

class SeleniumColaboratory():
    def __init__(self, mode="2"):
        userdata_dir = "/root/user-agent"
        # カレントディレクトリをpathに設定
        self.path = os.getcwd()
        # 検証用のテキストファイル
        self.store_path = self.path + "/elapsed_time.txt"

        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=" + userdata_dir)
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("window-size=1500,1000")
        # open it, go to a website, and get results
        self.driver = webdriver.Chrome("chromedriver",options=options)

        # FIleB path
        self.access_path = "https://colab.research.google.com/drive/1rNgIBr3EK9BWNl5aJwfUSjJm2w8VRoAE"
        # FilleA path for auto-access
        self.access_path_2 = "https://colab.research.google.com/drive/1EpNSDGGiScLhSmDqxvdidP2CzjJFWmhQ"

        # インスタンスのタイプを設定するための変数
        self.mode = str(mode)

        # 検証用ファイルに日時を追記
        jtime = self.get_japan_time()
        initial_text = "------------------ " + jtime.strftime("%Y-%m-%d") +  " ------------------\n"
        self.append_time_file(initial_text)

        from datetime import datetime
        self.time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # self.limit_time_hour = 11
        self.limit_time_hour = 0.5

    def click_runall(self):
        """
        「すべてのセルを実行」をクリックする関数
        """
        select_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID,"runtime-menu-button")))
        select_dropdown.click()
        time.sleep(1)
        select_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID,":1u")))
        select_dropdown.click()

    def click_change_runtime(self):
        """
        ランタイムのタイプを変更する関数
        """
        # ランタイムクリック
        select_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID,"runtime-menu-button")))
        select_dropdown.click()
        # ランタイムのタイプ変更クリック
        select_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID,":25")))
        select_dropdown.click()
        # ドロップダウンクリック
        self.driver.save_screenshot("/content/colab_test/screenshot_{}.png".format(self.time_stamp))
        select_dropdown = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID,"input-4")))
        select_dropdown.click()

        # 待たずにクリックしてしまうことがあるので
        time.sleep(1)

        # XPATH避けたい
        # ランタイム選択
        select_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='accelerator']/paper-item[" + self.mode + "]")))
        select_dropdown.click()

        # 保存ボタンクリック
        select_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID,"ok")))
        select_dropdown.click()

    def check_time(self):
        """
        インスタンス起動時間[Hour]を返す関数
        """
        # インスタンスを起動してからの時間を返す
        res = sp.Popen(["cat", "/proc/uptime"], stdout=sp.PIPE)
        # 単位はHour
        use_time = float(sp.check_output(["awk", "{print $1 /60 /60 }"], stdin=res.stdout).decode().replace("\n",""))
        return use_time

    def append_time_file(self, txt):
        """
        検証用に用意。テキストファイルにtxtを追記する関数
        """
        with open(self.store_path, mode='a') as f:
            f.write(txt)

    def access_another_colabo(self, path):
        """
        引数のpathに設定されたページを取得し, (Colaboratory前提なので)実行する関数
        """
        #新規タブを開く
        self.driver.execute_script("window.open()") #make new tab
        self.driver.switch_to.window(self.driver.window_handles[-1]) #switch new tab
        self.driver.get(path)
        # ページの要素が全て読み込まれるまで待機
        WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located)

        # 指定のURLにアクセスできているか確認(認証ページに飛ばされていないか確認)
        cur_url = self.driver.current_url
        print(cur_url)

        #ランタイムのタイプを変更する
        self.click_change_runtime()

        # 全てのセルを実行する
        self.click_runall()

    def auto_access(self, path):
        print("start auto access")
        """
        引数のpathに設定されたページを取得するだけの関数
        """
        try:
            #新規タブを開いて更新処理
            self.driver.execute_script("window.open()") #make new tab
            self.driver.switch_to.window(self.driver.window_handles[-1]) #switch new tab
            self.driver.get(path)
            # ページの要素が全て読み込まれるまで待機
            WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located)
            # 指定のURLにアクセスできているか確認(認証ページに飛ばされていないか確認)
            cur_url = self.driver.current_url
            print(cur_url)
            self.click_change_runtime()
            time.sleep(30)

        except urllib3.exceptions.NewConnectionError as e:
            print(str(e))
            print("********Portal New connection timed out***********")
            time.sleep(30)

        except urllib3.exceptions.MaxRetryError as e:
            print(str(e))
            time.sleep(30)
            print("*********Portal Max tries exceeded************")
        else:
            print("success to auto access")

    def set_mode(self, mode):
        print("set_mode")
        """
        ランタイムのタイプを設定する関数
        """
        if mode == "None":
            self.mode = "1"
        elif mode == "GPU":
            self.mode = "2"
        elif mode == "TPU":
            self.mode == "3"
        else:
            self.mode = "1"

    def git_push(self):
        print("git push")
        """
        addしてcommitしてpushする関数
        """
        try:
            repo = git.Repo.init()
            repo.index.add(self.store_path)
            repo.index.commit("add elapsed_time.txt")
            origin = repo.remote(name="origin")
            origin.push()
            return "Success"

        except:
            return "Error"
    def get_japan_time(self):
        """
        日本時間を返す関数
        """
        # タイムゾーンの生成
        JST = timezone(timedelta(hours=+9), 'JST')

        return datetime.now(JST)

    def main(self):

        while True:
            elapsed_time = self.check_time()
            print(elapsed_time)

            # 検証用の処理
            jtime = self.get_japan_time()
            append_text = "File A : " + str(elapsed_time) + " Hour (" +str(jtime.strftime("%H:%M:%S")) + ")\n"
            print(append_text)
            self.append_time_file(append_text)

            # 11時間越えたら
            if elapsed_time > self.limit_time_hour:
                # GitHubにプッシュ
                result = self.git_push()
                self.set_mode("None")
                # ColaboratoryファイルBを開く
                self.access_another_colabo(self.access_path)

                self.set_mode("GPU")
                self.auto_access(self.access_path_2)
                break

            else:
                self.set_mode("GPU")
                self.auto_access(self.access_path_2)
                # 60分ごとにチェック
                # time.sleep(3600)
                print("sleep 5s")
                time.sleep(5)

    def start(self):
        self.set_mode("GPU")
        self.auto_access(self.access_path_2)
        self.click_runall()

if __name__ == "__main__":
    sc = SeleniumColaboratory()
    sc.start()
