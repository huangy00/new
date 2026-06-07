from playwright.sync_api import Page
import allure
class LoginPage():
    def __init__(self,page:Page):
        self.page=page
        self.username_input=page.locator('#user-name')
        self.password_input=page.locator('#password')
        self.button_click=page.locator("#login-button")
        self.error_message=page.locator('[data-test="error"]')

    def goto(self):
        self.page.goto("https://www.saucedemo.com")
        allure.attach(self.page.screenshot(),name="login_page",attachment_type=allure.attachment_type.PNG)

    def login(self,username:str,password:str):
        with allure.step(f"输入账号{username}"):
            self.username_input.fill(username)
        with allure.step(f"输入密码{password}"):
            self.password_input.fill(password)
        with allure.step("点击登录按钮"):
            self.button_click.click()

    def get_error(self):
        return self.error_message.inner_text()