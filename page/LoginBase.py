import selenium.webdriver.common.by
from common.BasePage import BasePage


class LoginBase( BasePage ):
    # # 定位器
    # input_box = (selenium.webdriver.common.by.By.ID, 'kw')
    # search_submit = (selenium.webdriver.common.by.By.XPATH, '//*[@id="su"]')
    #
    # def value_input(self, text):
    #     self.wait( self.input_box, 5 )
    #     self.send_keys( self.input_box, text )
    #
    # def submit_btn(self):
    #     self.click( self.search_submit )
    #     self.sleep( Test03 )

    username = (selenium.webdriver.common.by.By.CLASS_NAME, "user-name > .w-full")
    password = (selenium.webdriver.common.by.By.XPATH, "//input[@type='password']")
    input = (selenium.webdriver.common.by.By.CLASS_NAME, "verification-code > input")#"//div[3]/div/div/input #(//input[@type='text'])[Test03]
    contains = (selenium.webdriver.common.by.By.XPATH, "//p[contains(.,'换一张')]")
    submit = (selenium.webdriver.common.by.By.XPATH, "//button[contains(.,'登录')]")
    item = (selenium.webdriver.common.by.By.XPATH, "//div[9]")
    def user_name(self, text):
        self.wait( self.username, 1 )
        self.send_keys( self.username, text )
    def pass_word(self, text):
        self.wait( self.password, 1 )
        self.send_keys( self.password, text )
    def invert_input(self, text):
        self.wait( self.input, 1 )
        self.send_keys( self.input, text )
    def login_btn(self):
        self.click(self.submit)
        self.sleep( 1 )
    def item_btn(self):
        self.click( self.item )
        self.sleep( 3 )
    def click_input(self):   #双击击验证码输入框
        self.double_click(self.input)
    def clear_input(self):#清除验证码
        self.clear(self.input)
    def clear_user_name(self):
        self.clear(self.username)
    def clear_pass_word(self):
        self.clear(self.password)
    def contains_btn(self): #换一张验证码
        self.click(self.contains)
        self.sleep( 1 )

