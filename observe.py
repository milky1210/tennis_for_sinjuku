import time  # スリープを使うために必要
import json
from selenium import webdriver  # Webブラウザを自動操作する（python -m pip install selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class Observer:
    def __init__(self, visible=True):
        json_open = open("pw_id.json", "r")
        json_load = json.load(json_open)
        self.ID = json_load["ID"]
        self.PW = json_load["PW"]
        if visible:
            self.driver = webdriver.Chrome()
        else:
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)

    def sclick(self, xpath, shift=False):

        time.sleep(0.2)
        if shift:
            element = self.driver.find_element(By.XPATH, xpath)
            actions = ActionChains(self.driver)  # ActionChainを作成
            actions.key_down(Keys.SHIFT)
            actions.click(element)
            actions.perform()
        else:
            self.driver.find_element(By.XPATH, xpath).click()

    def sclicks(self, xpaths, shift=False):
        for xpath in xpaths:
            self.sclick(xpath, shift)

    def observe(self, park=0, month=0, date_time=[[0, 5]]):
        # park: 0->落合中央公園, 1->西落合公園
        # month: 0->今月,1->来月
        # date: 取りたい日付のリスト
        # time: 取りたい時
        self.driver.get(
            "https://user.shinjuku-shisetsu-yoyaku.jp/regasu/reserve/gin_menu"
        )  # ここから始めないと不正な値とか言われるorz
        time.sleep(1)
        self.sclick(
            "/html/body/div/div[2]/ul[1]/li[2]/dl/dt/form/input[2]"
        )  # 高機能操作をクリック
        time.sleep(0.2)
        self.driver.find_element(
            By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[1]"
        ).send_keys(self.ID)
        time.sleep(0.2)
        self.driver.find_element(
            By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[2]"
        ).send_keys(self.PW)
        self.sclicks(
            [
                "/html/body/div/div[2]/div[1]/div/form/p/input",
                "/html/body/div/div[2]/div[1]/dl/dd/ul/li[1]/a",
                "/html/body/div/div[2]/div[2]/form[1]/div/div/div/div[1]/div/div[1]/select[1]/option[2]",
                "/html/body/div/div[2]/div[2]/form[1]/div/div/div/div[1]/div/div[1]/input[2]",
                "/html/body/div/div[2]/div[2]/form[4]/div/div/div/div[1]/div/div[1]/select",
                "/html/body/div/div[2]/div[2]/form[4]/div/div/div/div[1]/div/div[1]/select/option[2]",
                "/html/body/div/div[2]/div[2]/form[4]/div/div/div/div[1]/div/div[1]/input[2]",
            ]
        )
        # Ctr を押しながらクリックする
        self.sclicks(
            [
                "/html/body/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div[1]/select/option[3]",
                "/html/body/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div[1]/select/option[4]",
            ],
            shift=True,
        )
        self.sclick(
            "/html/body/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div[1]/input[2]"
        )
        self.sclicks(
            [
                "/html/body/div/div[2]/div[2]/form[5]/div/div/div/select/option[1]",
                "/html/body/div/div[2]/div[2]/form[5]/div/div/div/select/option[2]",
            ],
            shift=True,
        )
        self.sclicks(
            [
                "/html/body/div/div[2]/div[2]/form[5]/div/div/div/p[2]/input[2]",
                "/html/body/div/div[2]/div[2]/form[6]/p/input",
            ]
        )
        time.sleep(3)  # ページ遷移を挟むため少し待つ

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/div/ul[1]/li/a/img")
        if park == 1:  # 西落合公園なら遷移
            self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/ul/li[2]/a[1]")

        if month == 1:  # 来月なら遷移。
            self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/ul/li[2]/a[3]")
        selected = False
        # ボタン連打
        got_list = []
        for dt in date_time:
            xpath = "/html/body/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[{}]/tr/td[{}]/input".format(
                dt[0], dt[1]
            )
            if (
                len(self.driver.find_elements(By.XPATH, xpath)) > 0
            ):  # find_elementsの複数形に注意
                self.sclick(xpath)
                got_list.append(dt)
                selected = True
        self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/p/input")  # 予約リスト画面へ遷移
        time.sleep(1)
        xpath = "/html/body/div/div[2]/div[2]/p/a/img"
        if len(self.driver.find_elements(By.XPATH, xpath)) > 0 and selected:
            self.sclick(xpath)
        time.sleep(1)
        # 確定
        if True:
            xpath = "/html/body/div/div[2]/div[2]/p/a/input"
            if len(self.driver.find_elements(By.XPATH, xpath)) > 0 and selected:
                self.sclick(xpath)
                time.sleep(2)
                alert = self.driver.switch_to.alert
                alert.accept()
                print("get!")
        time.sleep(10)
        # gmail.send()
        self.driver.quit()
        return got_list


if __name__ == "__main__":
    # observerのテスト用スクリプト
    observer = Observer()
    observer.observe(park=1, month=1, date_time=[[2, 5]])
