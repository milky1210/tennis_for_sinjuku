import time                            # スリープを使うために必要
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import gmail
from selenium.webdriver.common.action_chains import ActionChains



class Observer:
	ID = "00016732"
	PW = "19971210"
	driver = webdriver.Chrome()
	def sclick(self,xpath,shift=False):
		time.sleep(0.2)
		if(shift):
			element = self.driver.find_element(By.XPATH,xpath)
			actions = ActionChains(self.driver)  # ActionChainを作成
			actions.key_down(Keys.SHIFT)
			actions.click(element)
			actions.perform()
		else:
			self.driver.find_element(By.XPATH,xpath).click()
	def sclicks(self,xpaths,shift = False):
		for xpath in xpaths:
			self.sclick(xpath,shift)

	def observe(self):
		self.driver.get('https://user.shinjuku-shisetsu-yoyaku.jp/regasu/reserve/gin_menu')   # ここから始めないと不正な値とか言われるorz
		self.sclick("/html/body/div/div[2]/ul[1]/li[2]/dl/dt/form/input[2]")  # 高機能操作をクリック
		time.sleep(1)
		self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/form/div/input[1]").send_keys(self.ID)
		time.sleep(1)
		self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/form/div/input[2]").send_keys(self.PW)
		self.sclicks([
		"/html/body/div/div[2]/div[1]/div/form/p/input",
		"/html/body/div/div[2]/div[1]/dl/dd/ul/li[1]/a",
		"/html/body/div/div[2]/div[2]/form[1]/div/div/div/div[1]/div/div[1]/select[1]/option[2]",
		"/html/body/div/div[2]/div[2]/form[1]/div/div/div/div[1]/div/div[1]/input[2]",
		"/html/body/div/div[2]/div[2]/form[4]/div/div/div/div[1]/div/div[1]/select",
		"/html/body/div/div[2]/div[2]/form[4]/div/div/div/div[1]/div/div[1]/select/option[2]",
		"/html/body/div/div[2]/div[2]/form[4]/div/div/div/div[1]/div/div[1]/input[2]"])
		# Ctr を押しながらクリックする
		self.sclicks([
		"/html/body/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div[1]/select/option[3]",
		"/html/body/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div[1]/select/option[4]"],shift=True)
		self.sclick("/html/body/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div[1]/input[2]")
		self.sclicks([
		"/html/body/div/div[2]/div[2]/form[5]/div/div/div/select/option[1]",
		"/html/body/div/div[2]/div[2]/form[5]/div/div/div/select/option[2]"],shift=True)
		self.sclicks([
		"/html/body/div/div[2]/div[2]/form[5]/div/div/div/p[2]/input[2]",
		"/html/body/div/div[2]/div[2]/form[6]/p/input"])
		time.sleep(3)  # ページ遷移を挟むため少し待つ
		self.driver.switch_to.window(self.driver.window_handles[1])
		self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/div/ul[1]/li/a/img")
		
		# ボタン連打
		self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[3]/tr/td[5]/input")
		self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[10]/tr/td[5]/input")
		self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[10]/tr/td[6]/input")
		self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/p/input")  # 予約リスト画面へ遷移
		time.sleep(3)
		self.sclick("/html/body/div/div[2]/div[2]/p/a/img")
		time.sleep(3)
		#確定
		time.sleep(10)
		#gmail.send() 
		self.driver.quit()



if __name__ == '__main__':
	observer = Observer()
	observer.observe()
