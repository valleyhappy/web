#!/usr/bin/env python 
#-*-coding:utf-8-*-

from base.base import *
from selenium.webdriver.common.by import By
from utils.helper import *

class Login(WebDriver,DataHelper):
	login_loc=(By.XPATH,'//*[@id="app"]/div/section[1]/div/div[2]/button')
	username_loc=(By.NAME,'username')
	password_loc=(By.NAME,'password')
	loginButton_loc=(By.XPATH,'//*[@id="app"]/div/div/div[2]/form/div[4]/button')
	nick_loc=(By.XPATH,'//*[@id="app"]/div/nav/div/div/ul[2]/li/a/div')

	@property
	def clickLogin(self):
		self.findElement(*self.login_loc).click()

	def typeUsername(self,username):
		self.findElement(*self.username_loc).send_keys(username)

	def typePassword(self,password):
		self.findElement(*self.password_loc).send_keys(password)

	@property
	def clickLoginButton(self):
		self.findElement(*self.loginButton_loc).click()

	def login(self,parent='login',username='username',password='password'):
		self.clickLogin
		self.wait()
		self.typeUsername(self.getXmlUser(parent,username))
		self.typePassword(self.getXmlUser(parent,password))
		self.clickLoginButton
		self.wait()

	def getNick(self):
		'''获取昵称'''
		return self.findElement(*self.nick_loc).text

	u'创建商户逻辑'
	add_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/a')
	account_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[1]/div/input')
	name_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[2]/div/input')
	passwd_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div/input')
	save_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[9]/div/button')

	def clickAdd(self):
		self.wait()
		self.findElement(*self.add_loc).click()

	def typeAaccount(self, account):
		self.wait()
		self.findElement(*self.account_loc).send_keys(account)

	def typeName(self, username):
		self.wait()
		self.findElement(*self.name_loc).send_keys(username)

	def typePasswd(self, password):
		self.wait()
		self.findElement(*self.passwd_loc).send_keys(password)

	def clickSave(self):
		self.findElement(*self.save_loc).click()
		self.wait()

	def addShop(self, account='123456', name='123456', passwd='123456'):
		self.clickAdd()
		self.typeAaccount(account)
		self.typeName(name)
		self.typePasswd(passwd)
		self.clickSave()

	u'查询'
	so_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[2]/input')
	soButton_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[3]/button')
	shopName_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[1]/div/a')

	def typeSo(self, name):
		self.wait()
		self.findElement(*self.so_loc).send_keys(name)

	def clickSo(self):
		self.findElement(*self.soButton_loc).click()

	def getShopName(self):
		self.wait()
		return self.findElement(*self.shopName_loc).text


	def so(self, name='123456'):
		self.typeSo(name)
		self.clickSo()

	u'删除'
	sel_loc=(By.XPATH,".//*[@id='app']/div/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div/i")
	del_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/div/ul/li[2]')
	delOk_loc=(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div/div[2]/button[1]')

	def clickSel(self):
		self.wait()
		self.findElement(*self.sel_loc).click()

	def clickDel(self):
		self.wait()
		self.findElement(*self.del_loc).click()

	def clickDelOk(self):
		self.wait()
		self.findElement(*self.delOk_loc).click()

	def  delShop(self):
		self.refersh()
		self.clickSel()
		self.clickDel()
		self.clickDelOk()

	u'商户管理'
	manage_loc=(By.LINK_TEXT,'商户管理')

	def clickMnnage(self):
		self.wait()
		self.findElement(*self.manage_loc).click()


	def isAddShop(self):
		try:
			self.so()
			assert self.getShopName() in u'123456'
			self.delShop()
		except:
			self.addShop()
		else:
			self.addShop()
		finally:
			pass









