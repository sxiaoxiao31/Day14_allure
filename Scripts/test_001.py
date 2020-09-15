import allure
from selenium import webdriver


class Test01:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

    @allure.step('第二步')
    def method(self):
        print('\n-----allure')

    @allure.step('第一步')
    def test_01(self):
        self.method()
        # 添加截图
        allure.attach(self.driver.get_screenshot_as_png(),'截图',allure.attachment_type.PNG)
        print('\n-----Python')
