from page.ApComUsrBase import ApComUsr
from common.Cloud import TestBase

class ApComUsrCase(TestBase):
    def test_Application_List(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        input = ApComUsr(self.driver)

        #input.item_btn()
        #input.get_windows_img()  # 调用基类截图方法
        # try:
        #     assert 'selenium' in 'selenium'
        #     print( 'Test Pass.' )
        # except Exception as e:
        #     print( 'Test Fail.', format( e ) )
