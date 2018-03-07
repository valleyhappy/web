#!/usr/bin/env python 
#-*-coding:utf-8-*-

import  unittest
from page.login import *
from selenium import  webdriver

class LoginTest(unittest.TestCase,Login):
	def setUp(self,value='url'):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get(self.getXmlData(value))

	def tearDown(self):
		self.driver.quit()

	def test_login(self,parent='login',value='nick'):
		'''验证：登录成功'''
		self.login()
		self.assertEqual(self.getNick(),self.getXmlUser(parent,value))

if __name__ == '__main__':
    unittest.main(verbosity=2)


