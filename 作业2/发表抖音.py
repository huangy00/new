from playwright.sync_api import sync_playwright
import time
import json


def publish_image_text():
    with sync_playwright() as p:
        # 1. 加载登录状态
        with open("douyin_cookie.json", "r") as f:
            storage = json.load(f)
        
        # 2. 启动浏览器
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(storage_state=storage,
        geolocation={"latitude": 30, "longitude": 120},
        permissions=["geolocation"]
        )
        page = context.new_page()
        
        # 3. 打开创作者中心
        page.goto("https://creator.douyin.com/")
        print("已打开创作者中心")
        time.sleep(2)
        
        # 4. 点击发布按钮
        try:
            page.get_by_text("高清发布").click()
            #page.locator("#douyin-creator-master-side-upload")
            print("点击了'高清发布'")
        except:
            page.goto("https://creator.douyin.com/content/publish")
            print("直接进入发布页面")
        time.sleep(2)
        
        # 5. 选择图文
        try:
            #page.get_by_text('发布图文').click()
            page.click("text=图文")
            print("点击了'发布图文'")
        except:
            pass
        time.sleep(2)
        
        # 6. 上传图片
        image_path = r"C:\Users\34068\Pictures\Screenshots\屏幕截图 2026-07-18 160850.png"
        file_input = page.locator("input[type='file'][accept*='image']")
        file_input.set_input_files(image_path)
        print("图片已上传")
        time.sleep(3)
        
        # 7. 填写标题与作品描述
        title_input = page.get_by_placeholder('添加作品标题')
        #title_input = page.locator('input[placeholder*="添加作品标题"]')
        title_input.fill('软件自动化测试')
        time.sleep(1)
        
        
        desc_input = page.locator('div[data-placeholder*="添加作品描述"]')
        #等待元素可见
        desc_input.wait_for(timeout=10000)
        #填充文字
        desc_input.fill("这里是自动化发抖音的UI测试")
        
        
        # 8.点击自己可见
        privacy_btn=page.get_by_label("仅自己可见")
        try:
            privacy_btn.scroll_into_view_if_needed()
            time.sleep(0.5)
            privacy_btn.click()
            print("点击自己可见成功")

        except Exception as e:
            print(f"点击失败{e}")
        
        # 定位发布按钮 精确匹配"发布"
        publish_btn = page.get_by_role("button", name="发布", exact=True)
        print("已定位发布按钮")
        
        # 9. 点击发布
        try:
            #publish_btn.scroll_into_view_if_needed()
            time.sleep(0.5)
            publish_btn.click()
            print("点击发布成功")
        except Exception as e:
            print(f"点击失败: {e}")
            
        
        #处理可能的弹窗
        #page.on("dialog", lambda dialog: dialog.accept())
        
        # 10. 等待发布成功提示
        try:
            page.wait_for_selector("text=发布成功", timeout=15000)
            print("发布成功")
        except:
            print("未检测到发布成功提示")
        
        # 11 等待几秒后关闭
        time.sleep(5)
        browser.close()
        print("结束")


def publish_video():
    """自动发布视频到抖音（仅自己可见）"""
    with sync_playwright() as p:
        with open("douyin_cookie.json", "r") as f:
            storage = json.load(f)
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(storage_state=storage,
            geolocation={"latitude": 30, "longitude": 120},
            permissions=["geolocation"])
        page = context.new_page()
        page.goto("https://creator.douyin.com/creator-micro/home")
        print("已打开创作者中心")
        time.sleep(3)
        page.get_by_text("高清发布").click()
        print("点击了高清发布")
        page.wait_for_url("**/content/upload", timeout=15000)
        time.sleep(2)
        video_path = r"C:\Users\34068\Desktop\f524732d45a194a9bd46c0d908f56df6.mp4"
        page.locator("input[type='file']").first.set_input_files(video_path)
        print("视频文件已上传，等待处理...")
        time.sleep(8)
        try:
            desc_input = page.locator('div[contenteditable="true"]').first
            desc_input.wait_for(timeout=15000)
            desc_input.fill("自动化测试视频 - 由AI Agent自动发布")
            print("已填写描述")
        except Exception as e:
            print(f"填写描述失败: {e}")
        time.sleep(1)
        try:
            page.get_by_label("仅自己可见").scroll_into_view_if_needed()
            time.sleep(0.5)
            page.get_by_label("仅自己可见").click()
            print("已设置为仅自己可见")
        except Exception as e:
            print(f"设置可见性失败: {e}")
        try:
            btn = page.get_by_role("button", name="发布", exact=True)
            btn.scroll_into_view_if_needed()
            time.sleep(1)
            btn.click()
            print("已点击发布")
        except Exception as e:
            print(f"点击发布失败: {e}")
        try:
            page.wait_for_selector("text=发布成功", timeout=30000)
            print("视频发布成功!")
        except:
            print("未检测到发布成功提示")
        time.sleep(5)
        browser.close()


def delete_latest_video():
    """删除最新发布的私密作品"""
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
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "image":
            publish_image_text()
        elif sys.argv[1] == "video":
            publish_video()
        elif sys.argv[1] == "delete":
            delete_latest_video()
        elif sys.argv[1] == "all":
            print("=== 开始发布视频 ===")
            publish_video()
            print("=== 开始发布图文 ===")
            try:
                publish_image_text()
            except Exception as e:
                print(f"图文发布失败: {e}")
    else:
        print("无参数，默认全部执行")
        print("=== 开始发布视频 ===")
        publish_video()
        print("=== 开始发布图文 ===")
        try:
            publish_image_text()
        except Exception as e:
            print(f"图文发布失败: {e}")
