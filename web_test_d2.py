__author__ = '何旺彤'
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome

driver = Chrome()
driver.implicitly_wait(20)

driver.get('file:///D:/Users/%E4%BD%95%E6%97%BA%E5%BD%A4/PycharmProjects/heyang-/index.html')


'''
#iframe切换  1、name  2、索引  3、WebElement
driver.switch_to.frame('myiframe')#第一种方法
#先拿到WebElement
frame = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(frame)

#等待新的iframe可以用在进行切换
ec.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'frame'))

#怎么切换回去初始的HTML内容
driver.switch_to.default_content()

#多个iframe，多个嵌套。切到父级
driver.switch_to.parent_frame()
'''



#alert切换
driver.find_element_by_name('click').click()   #先定位元素
alert = driver.switch_to.alert    #获取alert对象
alert.text    #获取文本内容
alert.accept()    #确认，返回原来的页面
alert.dismiss()    #取消，返回原来的页面

#扩展知识@property

driver.add_cookie()    #添加cookie
driver.get_cookie()    #获取cookie















