import time  # スリープを使うために必要
import json
from selenium import webdriver  # Webブラウザを自動操作する（python -m pip install selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Observer:
    json_open = open("pw_id.json", "r")
    json_load = json.load(json_open)
    ID = json_load["ID"]
    PW = json_load["PW"]
    driver = webdriver.Chrome()

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

    def observe(self, month=0, date_time=[[0, 5]]):
        # month: 0->今月,1->来月
        # date: 取りたい日付のリスト
        # time: 取りたい時
        self.driver.get(
            "https://user.shinjuku-shisetsu-yoyaku.jp/regasu/reserve/gin_menu"
        )  # ここから始めないと不正な値とか言われるorz
        self.sclick(
            "/html/body/div/div[2]/ul[1]/li[2]/dl/dt/form/input[2]"
        )  # 高機能操作をクリック
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[1]"
        ).send_keys(self.ID)
        time.sleep(1)
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

        if month == 1:  # 来月なら遷移。
            self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/ul/li[2]/a[3]")
        # ボタン連打
        for i in range(31):
            xpath = "/html/body/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[{}]/tr/td[5]/input".format(
                i
            )
            if (
                len(self.driver.find_elements(By.XPATH, xpath)) > 0
            ):  # find_elementsの複数形に注意
                self.sclick(xpath)
            else:
                print(xpath + "はとれねぇよい")
        self.sclick("/html/body/div/div[2]/div[2]/div[2]/div/p/input")  # 予約リスト画面へ遷移
        time.sleep(3)
        xpath = "/html/body/div/div[2]/div[2]/p/a/img"
        if len(self.driver.find_elements(By.Xpath, xpath)) > 0:
            self.sclick(xpath)
        time.sleep(3)
        # 確定
        if False:
            xpath = "/html/body/div/div[2]/div[2]/p/a/img"
            if len(self.driver.find_elements(By.Xpath, xpath)) > 0:
                self.sclick(xpath)

        time.sleep(10)
        # gmail.send()
        self.driver.quit()


if __name__ == "__main__":
    observer = Observer()
    observer.observe(month=1)
