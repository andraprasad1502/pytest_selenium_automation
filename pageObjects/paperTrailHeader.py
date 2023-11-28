from selenium import webdriver as wb
from selenium.webdriver.common.by import By


class PaperTrailHeader:

    def click_settings(self):
        self.driver.find_element(By.XPATH, "//div[text()='Settings']").click()

    def click_profile(self):
        self.driver.find_element(By.XPATH, "//a[@href='/account/profile']").click()

