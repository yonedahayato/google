!pip install schedule

import time
import schedule
from datetime import datetime

def job():
    #現在日時の表示
    dt = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(dt)
    print('ほげ')


##2分毎にjobを実行
schedule.every(2).minutes.do(job)

##毎時間ごとにjobを実行
#schedule.every().hour.do(job)

##PM15:10にjobを実行
#schedule.every().day.at("15:10").do(job)

##月曜日にjobを実行
#schedule.every().monday.do(job)

##水曜日の13:15にjobを実行
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
