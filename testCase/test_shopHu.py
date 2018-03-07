#!/usr/bin/env python
#-*-coding:utf-8-*-

import  unittest
from selenium import  webdriver
from page.shopHu import *
from page.login import *


class LoginTest(unittest.TestCase,ShopHu,Login):
	def setUp(self,value='url'):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get(self.getXmlData(value))

	def tearDown(self):
		self.driver.quit()

	def test_addShop(self):
		'''验证：添加商户'''
		self.login()
		self.isAddShop()
		self.clickMnnage()
		shopName=self.getShopName()
		self.delShop()
		self.assertEqual(shopName, u'123456')

if __name__ == '__main__':
    unittest.main(verbosity=2)


