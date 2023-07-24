import selenium.webdriver.common.by
from common.BasePage import BasePage


class Cloud( BasePage ):
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
    input = (selenium.webdriver.common.by.By.XPATH, "//div[3]/div/div/input")
    submit = (selenium.webdriver.common.by.By.XPATH, "//button[contains(.,'登录')]")

    def user_name(self, text):
        self.wait( self.username, 5 )
        self.send_keys( self.username, text )

    def pass_word(self, text):
        self.wait( self.password, 5 )
        self.send_keys( self.password, text )

    def invert_input(self, text):
        self.wait( self.input, 5 )
        self.send_keys( self.input, text )
    def login_btn(self):
        self.click(self.submit)
        self.sleep( 2 )

