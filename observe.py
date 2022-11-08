import time                            # スリープを使うために必要
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)


ID = "00016732"
PW = "19971210"

def observe():
	driver = webdriver.Chrome()            # Chromeを準備
	driver.get('https://user.shinjuku-shisetsu-yoyaku.jp/regasu/reserve/gin_menu')   # ここから始めないと不正な値とか言われるorz
	time.sleep(5)                          # 5秒間待機
	driver.quit()



if __name__ == '__main__':
	observe()
