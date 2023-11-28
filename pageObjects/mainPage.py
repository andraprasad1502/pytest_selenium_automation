from selenium import webdriver as wb
from selenium.webdriver.common.by import By


class MainPage:

    def click_papertrail(self):
        self.driver.find_element(By.ID, "product-3").click()

