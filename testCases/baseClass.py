import pytest
from pageObjects.mainPage import MainPage
from pageObjects.loginPage import LoginPage
from pageObjects.profilePage import ProfilePage
from pageObjects.paperTrailHeader import PaperTrailHeader


@pytest.mark.usefixtures("launch_browser")
class BaseClass(MainPage, LoginPage, ProfilePage, PaperTrailHeader):
    pass
