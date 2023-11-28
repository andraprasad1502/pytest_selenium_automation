import pytest
from baseClass import BaseClass
from testConfig import settings
from datetime import datetime


class TestCases(BaseClass):

    def test_edit_user_name(self, launch_browser):
        try:
            new_user_name = "Test User2"
            self.click_papertrail()
            self.enter_user_name(settings.user_name)
            self.enter_password(settings.password)
            self.submit_login()
            self.click_settings()
            self.click_profile()
            self.edit_user_name(new_user_name)
            assert self.save_profile_preferences()

            user_name = self.get_username()
            assert user_name == new_user_name

        except Exception as e:

            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
            self.driver.save_screenshot("Logs/screenshot_"+dt_string+".png")
            assert False



