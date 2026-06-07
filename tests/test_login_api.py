import allure
import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from utils.logger import logger

@allure.feature("请求登录")
class Testlogin:
    @allure.story("正确登录")
    @allure.title("使用标准用户登录成功")
    def test_login(self,page:Page):
        login_page=LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")
        inventory_page=InventoryPage(page)
        assert inventory_page.get_title_text()=="Products"
        logger.info("登录成功，进入商品页面")