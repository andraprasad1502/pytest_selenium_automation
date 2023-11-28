import re
import time

from selenium import webdriver as wb
from selenium.webdriver.common.by import By


class ProfilePage:

    def get_username(self):
        user_name = self.driver.find_element(By.ID, "user_name").get_attribute("value")
        return user_name

    def edit_user_name(self, user_name):
        self.driver.find_element(By.ID, "user_name").clear()
        self.driver.find_element(By.ID, "user_name").send_keys(user_name)

    def save_profile_preferences(self):
        self.driver.find_element(By.XPATH, "//button[text()='Update Preferences']").click()
        time.sleep(2)
        text_note = self.driver.find_element(By.XPATH, "//div[@class='flash notice']//p").text
        if re.search("Profile updated", text_note, re.I):
            return True
        else:
            return False

