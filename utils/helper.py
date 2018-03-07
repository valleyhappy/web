#!/usr/bin/env python
#-*-coding:utf-8-*-


import  os
import  xml.dom.minidom

class DataHelper(object):

	def base_dir(self,path1,path2):
		'''第一个次参数是文件夹，第二个参数指文件'''
		return os.path.join(os.path.dirname(os.path.dirname(__file__)), path1, path2)

	def getXmlData(self,value):
		#parse--生成一个Document对象
		dom = xml.dom.minidom.parse(self.base_dir('data','system.xml'))
		#获取根元素节点
		db = dom.documentElement
		#实现对节点数据的查询
		name = db.getElementsByTagName(value)
		#节点中查找节点元素
		nameValue = name[0]
		#节点中的第一个元素属性的值
		return nameValue.firstChild.data

	def getXmlUser(self,parent, child):
		dom = xml.dom.minidom.parse(self.base_dir('data','system.xml'))
		db = dom.documentElement
		itemlist = db.getElementsByTagName(parent)
		item = itemlist[0]
		return item.getAttribute(child)




