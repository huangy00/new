import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger
@allure.feature("购物流程")
class TestCheckout:
    @allure.story("添加商品到购物车")
    @allure.step("购买第一个商品")
    def test_add_cart(self,page:Page):
        login_page=LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")
        inventory_page=InventoryPage(page)
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        assert page.locator('.cart_item').count() == 1
        logger.info("商品已添加到购物车")