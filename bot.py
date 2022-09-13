from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class InstagramBot:
    def __init__(self):
        self.service = Service("/Users/bryce/Desktop/Development/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        self.SIMILAR_ACCOUNT = "Similar instagram handle"
        self.INSTAGRAM_USER = "Your Instagram User"
        self.INSTAGRAM_PASS = "Your Instagram PASS"

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        insta_user = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        insta_user.send_keys(self.INSTAGRAM_USER)
        insta_pass = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        insta_pass.send_keys(self.INSTAGRAM_PASS)
        insta_pass.send_keys(Keys.ENTER)
        time.sleep(5)
        turn_off_notifications = self.driver.find_element(By.XPATH, "/html/body")
        turn_off_notifications.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.SIMILAR_ACCOUNT}/followers")
        time.sleep(5)
        follower_list = []
        div_index = 1
        for _ in range(25):
            follow_buttons = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div[2]/div/div/div["
                                                                f"1]/div/div[2]/div/div/div/div/div[2]/div/div/div["
                                                                f"2]/div[2]/div/div[{str(div_index)}]/div[3]/button")
            follower_list.append(follow_buttons)
            div_index += 1

        for button in follower_list:
            try:
                if button.text == "Following" or button.text == "Requested":
                    pass
                else:
                    button.click()
                    time.sleep(3)
            except ElementClickInterceptedException:
                continue

