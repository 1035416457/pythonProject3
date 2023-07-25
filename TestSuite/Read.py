import unittest

from TestSuite.Test01.Case_01_login import lzoslogin

test=unittest.TestLoader().loadTestsFromTestCase(lzoslogin)
# #创建一个测试套件
suite=unittest.TestSuite([test])
# #运行测试套件
runner=unittest.TextTestRunner()
runner.run(suite)




