from selenium.webdriver.common.by import By
from pom.base.BasePage import BasePage


class LoginPage(BasePage): #继承！！！Python 基础面向对象
    # 1、定义页面全部的元素
    sd_username = (By.NAME, "user-name") #登录文本框
    sd_password = (By.NAME, "password")  #密码框
    sd_login_button = (By.NAME, "login-button") #登录按钮
    sd_menu =  (By.ID,"react-burger-menu-btn") #菜单按钮
    sd_quit_button = (By.ID, "logout_sidebar_link") #退出按钮

    #告诉代码 我在做什么
    def do_login(self,username,password):
        self.send_keys(self.sd_username,username)
        self.send_keys(self.sd_password,password)
        self.click(self.sd_login_button)

    def quit_login(self):
        self.click(self.sd_menu)
        self.click(self.sd_quit_button)

"""if __name__ == '__main__':
    Lp = LoginPage()
    Lp.get_url("https://www.saucedemo.com/")

    Lp.do_login("standard_user", "secret_sauce")

    Lp.quit_login()
    sleep(5)"""

#POM 本质是把重复的操作独立的提取出去
#页面的操作 -- 会有很多种操作吗？
#页面操作都是固定的
#打开浏览器
#关闭浏览器
#输入文字
#点击。。。（可以把所有操作都提取出去）