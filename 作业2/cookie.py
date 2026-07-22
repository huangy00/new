from playwright.sync_api import sync_playwright


def login_douyin():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://creator.douyin.com/")
        input("请登录，登录完成后继续")
        storage= context.storage_state(path="douyin_cookie.json" )
        print("登录状态已保存")
        browser.close()

if __name__ == "__main__":
    login_douyin()