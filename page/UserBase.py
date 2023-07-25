import selenium.webdriver.common.by
from common.BasePage import BasePage


class UserBase( BasePage ):
    #定位器
    background = (selenium.webdriver.common.by.By.XPATH, "//footer/div/div/div/div[15]")
    menu = (selenium.webdriver.common.by.By.XPATH, "//li[2]/div/span/span[2]")
    user = (selenium.webdriver.common.by.By.XPATH, "//span[contains(., '用户管理')]")
    Dynamic  = (selenium.webdriver.common.by.By.XPATH, "//span[contains(.,'动态参与者')]")
    user_add = (selenium.webdriver.common.by.By.XPATH, "/html/body/div[1]/div/div/div/div/section/section/section/main/div/div/div[1]/div[2]/div[1]/div/div/span/button[1]/span")
    # password = (selenium.webdriver.common.by.By.XPATH, "//input[@type='password']")
    # input = (selenium.webdriver.common.by.By.CLASS_NAME, "verification-code > input")#"//div[3]/div/div/input #(//input[@type='text'])[Test03]
    # contains = (selenium.webdriver.common.by.By.XPATH, "//p[contains(.,'换一张')]")
    # submit = (selenium.webdriver.common.by.By.XPATH, "//button[contains(.,'登录')]")
    # item = (selenium.webdriver.common.by.By.XPATH, "//div[9]")
    # def user_name(self, text):
    #     self.wait( self.username, 1 )
    #     self.send_keys( self.username, text )
    # def pass_word(self, text):
    #     self.wait( self.password, 1 )
    #     self.send_keys( self.password, text )
    # def invert_input(self, text):
    #     self.wait( self.input, 1 )
    #     self.send_keys( self.input, text )
    # def login_btn(self):
    #     self.click(self.submit)
    #     self.sleep( 1 )
    def click_BackGround(self):
        self.click(self.background)
        self.sleep( 3 )
    def click_Ant_Menu(self):
        self.click(self.menu)
        self.sleep( 3 )
    def click_User(self):
        self.click(self.user)
        self.sleep( 3 )
    def click_user_add(self):
        self.click(self.user_add)
        self.sleep( 3 )
    # def clear_input(self):#清除验证码
    #     self.clear(self.input)
    # def clear_user_name(self):
    #     self.clear(self.username)
    # def clear_pass_word(self):
    #     self.clear(self.password)
    # def contains_btn(self): #换一张验证码
    #     self.click(self.contains)
    #     self.sleep( 1 )