from playwright.sync_api import sync_playwright
import time
import json

def delete_latest_video():
    with sync_playwright() as p:
        with open("douyin_cookie.json", "r") as f:
            storage = json.load(f)
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(storage_state=storage)
        page = context.new_page()
        page.goto("https://creator.douyin.com/creator-micro/content/manage")
        print("已打开内容管理")
        time.sleep(3)
        page.get_by_text("删除作品").first.click()
        print("已点击删除作品")
        time.sleep(2)
        page.get_by_role("button", name="确定").click()
        print("已点击确定删除")
        time.sleep(3)
        print("删除操作已完成!")
        browser.close()

if __name__ == "__main__":
    delete_latest_video()