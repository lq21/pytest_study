from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#谷歌浏览器管理
from webdriver_manager.chrome import ChromeDriverManager
#火狐浏览器
#from webdriver_manager.firefox import firefoxDriverManager

#将Web页面功能定义封装，例如获取url、点击按钮、文本框输入
class BasePage(object):
    def __init__(self,browser):
        self.driver = browser
        self.wait = WebDriverWait(self.driver, 10)

    def get_url(self,url):
        self.driver.get(url)

    def quit_brower(self):
        self.driver.quit()

    #输入（元素，文本）
    def send_keys(self,selector,context):
        #self.driver.find_element(*selector).send_keys(context)
        element = self.wait.until(EC.element_to_be_clickable(selector))
        element.send_keys(context)

    def click(self,selector):
        #self.driver.find_element(*selector).click()
        element = self.wait.until(EC.element_to_be_clickable(selector))
        element.click()


