from playwright.sync_api import Page
import allure

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('.title')
        self.add_car_buttons = page.locator('.btn_inventory')
        self.shopping_cart_link = page.locator('.shopping_cart_link')

    def get_title_text(self):
        return self.title.inner_text()
    
    def add_item_to_cart_by_index(self, index: int = 0):
        with allure.step(f"添加第 {index+1} 个商品"):
            self.add_car_buttons.nth(index).click()

    def go_to_cart(self):
        with allure.step("前往购物车"):
            self.shopping_cart_link.click()
