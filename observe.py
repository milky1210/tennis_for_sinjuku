import time                            # スリープを使うために必要
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import gmail

ID = "00016732"
PW = "19971210"

def observe():
	driver = webdriver.Chrome()            # Chromeを準備
	driver.get('https://user.shinjuku-shisetsu-yoyaku.jp/regasu/reserve/gin_menu')   # ここから始めないと不正な値とか言われるorz
	time.sleep(5)  # ページ遷移まち
	driver.find_element(By.XPATH,"/html/body/div/div[2]/ul[1]/li[2]/dl/dt/form/input[2]").click()  # 高機能操作をクリック
	time.sleep(5)  # ページ遷移待ち
	driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/form/div/input[1]").send_keys(ID)
	time.sleep(1)
	driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/form/div/input[2]").send_keys(PW)
	time.sleep(1)
	driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/form/p/input").click()
	time.sleep(5)
	gmail.send()
	driver.quit()



if __name__ == '__main__':
	observe()
