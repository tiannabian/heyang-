__author__ = '何旺彤'
import requests
'''
res = requests.get('https://github.com/')
print(res)
from selenium import  webdriver
driver = webdriver.Firefox()
driver.get('https://github.com/')
print("我爱南志姣")
'''

#selenium使用元素定位
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#1、通过id查找
ele = driver.find_element_by_id('kw')
print(ele)
#2、通过class
ele = driver.find_element_by_class_name('s_ipt')
print(ele)#打印出来是第一个对象
ele = driver.find_elements_by_class_name('s_ipt')
print(ele)#打印出来是一个列表
#3、通过name
ele = driver.find_element_by_name('wd')
#4、通过tagname
ele = driver.find_element_by_tag_name('input')
#5、通过text  ###
ele = driver.find_element_by_link_text('新闻')
#6、partial_link_text
ele = driver.find_element_by_partial_link_text('新')
#css选择器
ele = driver.find_element_by_css_selector('input#kw')
#xpath==>css选择器
#卸载selenium   pip uninstall selenium
#使用requests去访问selenium webdriver 暴露的接口地址，session_id
#怎么进行元素定位，id, name, class_name, tag_name
#link_test, partial_link_text, css_selector, Xpath

#id, name, class_name, tag_name==>find element()==>转成css选择器==>find element by_css_selector()


#selenium使用元素定位
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#1、通过id查找
ele = driver.find_element_by_id('kw')
print(ele)
#2、通过class
ele = driver.find_element_by_class_name('s_ipt')
print(ele)#打印出来是第一个对象
ele = driver.find_elements_by_class_name('s_ipt')
print(ele)#打印出来是一个列表
#3、通过name
ele = driver.find_element_by_name('wd')
#4、通过tagname
ele = driver.find_element_by_tag_name('input')
#5、通过text  ###
ele = driver.find_element_by_link_text('新闻')
#6、partial_link_text
ele = driver.find_element_by_partial_link_text('新')
#css选择器
ele = driver.find_element_by_css_selector('input#kw')
#xpath==>css选择器
#卸载selenium   pip uninstall selenium
#使用requests去访问selenium webdriver 暴露的接口地址，session_id
#怎么进行元素定位，id, name, class_name, tag_name
#link_test, partial_link_text, css_selector, Xpath

#id, name, class_name, tag_name==>find element()==>转成css选择器==>find element by_css_selector()

