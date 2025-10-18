from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time


def get_page_elements(url):
    # 设置Edge浏览器选项
    edge_options = Options()
    edge_options.add_argument('--disable-blink-features=AutomationControlled')  # 避免被检测为自动化工具
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)
    edge_options.add_experimental_option("detach", True)  # 关键设置：浏览器不自动关闭

    try:
        # 创建浏览器驱动
        driver = webdriver.Edge(options=edge_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        print("正在访问页面...")
        driver.get(url)

        # 等待页面加载
        time.sleep(3)

        # 获取页面基本信息
        print(f"页面标题: {driver.title}")
        print(f"当前URL: {driver.current_url}")
        print(f"页面源代码长度: {len(driver.page_source)} 字符")



        # 保存页面源代码到文件便于分析
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print(f"\n页面源代码已保存到: page_source.html")

        return driver.page_source

    except Exception as e:
        print(f"发生错误: {e}")
        return None





# 使用示例
if __name__ == "__main__":
    url = "http://wx.m.ddxq.mobi/#/"
    page_source = get_page_elements(url)

    if page_source:
        print("\n页面已成功加载，您现在可以:")
        print("1. 查看保存的HTML文件分析结构")
        print("2. 使用浏览器开发者工具检查元素")
        print("3. 编写XPath定位所需元素")