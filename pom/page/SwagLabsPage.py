from selenium.webdriver.common.by import By
from pom.page.LoginPage import LoginPage


class SwagLabsPage(LoginPage):
    sd_menu =  (By.ID,"react-burger-menu-btn") #菜单按钮
    sd_shopping = (By.ID,"shopping_cart_container") #购物车按钮

    def click_cartname(self,cartname):
        self.click((By.LINK_TEXT,cartname))

    def click_cartimg(self,cartname):
        self.click((By.XPATH, f"//img[@alt='{cartname}']"))

    def click_menu(self):
        self.click(self.sd_menu)

    def click_shopping(self):
        self.click(self.sd_shopping)

    def click_add_to_cart(self,cartname):
        self.click((By.XPATH,f"//div[text()='{cartname}']/ancestor::div[@class='inventory_item_description']//button[text()='Add to cart']"))
