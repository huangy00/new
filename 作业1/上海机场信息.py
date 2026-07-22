from playwright.sync_api import sync_playwright
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. 获取股价
    page.goto("https://quote.eastmoney.com/sh600009.html")
    # 定位价格元素
    price_elem = page.locator("span.price_down.blinkgreen, span.price_up.blinkred").first
    price = price_elem.inner_text().strip()
    print(f"价格: {price}")

    # 2. 获取公司简介（直接定位你找到的 class）
    page.goto("https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SH600009&color=b#/gsgk")
    # 等待简介元素出现
    intro_elem = page.locator(".desc-detail")
    intro_text = intro_elem.inner_text().strip()
    print(f"简介长度: {len(intro_text)} 字符")

    browser.close()

# 3. 写入 MD 文件
md_content = f"""上海机场（600009）

最新股价: {price} 元

公司简介

{intro_text}
"""

file_path = os.path.join(desktop, "上海机场.md")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"已保存到 {file_path}")