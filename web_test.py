import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

__author__ = '何旺彤'

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

#ipt<s_ipt       //input[@id='kw']/../..     //a[text()='新闻']
'''
#import time
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.implicitly_wait()
# driver.get('http://www.baidu.com')
#+等待
'''
time.sleep(3)

#最小化
driver.minimize_window()
#最大化
driver.maximize_window()

#访问豆瓣
driver.get('http://www.douban.com')

#后退
driver.back()
#前进
driver.forward()

#刷新
driver.refresh()

#获取网页标题
print(driver.title)

#获取url地址
print(driver.current_url)

#截屏
driver.save_screenshot('test_png')

#获取当前窗口句柄
print(driver.current_window_handle)

#关闭标签页,当只有一个标签页的时候，执行close相当于关闭浏览器
driver.close()
#关闭浏览器
driver.quit()
'''



'''
#显示等待用法：
#初始化计时器
wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
#if
ele = wait.until(ec.presence_of_element_located((By.ID, 'kw')))
#ele = driver.find_element_by_id('kw')

#获取属性
#ele_name = ele.get_attribute('name')
#print(ele_name)
#修改属性:为什么python  selenium没有set_attribute方法
#无法直接通过python执行修改动作
#python = = webdriver = =(JS= = 浏览器)
ele.send_keys('柠柠檬班')

#提交
submit_ele = driver.find_element_by_id('su')
submit_ele.click()
time.sleep(3)

#动态等待的思路
# continued = True
# timeout = 10
# while continued:
#     try:
#         ele = driver.find_element_by_id('su')
#         continued = False
#     except Exception as e:
#         continue
#如果页面加载中，你却在执行find_element（）,会报错
#当找元素的时候，你会发现报错：No Such Element   Element can not located
#1、表达式有问题  2、没有等待  3、元素不可用（隐藏，不能用）

#3、等待方式  1、强制的  2、隐式  3、显性等待
#find_element  强制等待（休息）
#演唱会 摄像头,隐式等待只能用一次   driver.implicitly_wait()
#显性等待，特别行动小组，门卡
driver.quit()
'''




from selenium.webdriver import Chrome

driver = Chrome()
driver.implicitly_wait(20)

driver.get('http://www.baidu.com')

#计时器1、第一个参数driver  第二个参数是过期时间，第三个参数频率
# wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
# wait.until(ec.presence_of_all_elements_located((By.ID,'kw')))
#练习定位柠檬拌图片
#定位input输入框

#函数注解
def wait_find_element(loactor) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(ec.presence_of_all_elements_located(loactor))
    return input_ele

input_ele = wait_find_element((By.ID, 'kw'))
input_ele.send_keys('柠檬班')

# sub_ele = wait_find_element((By.ID, 'su'))
# sub_ele.click()#快捷方式，当输入的内容在一个form表单里面的时候，可以使用ele.submit()  来进行提交；使用方式是
input_ele.submit()

#定位柠檬班腾讯课堂
nm_ke = wait_find_element((By.XPATH, "//a[contains(text(),'lemon.ke.qq.com/')]"))
nm_ke.click()

time.sleep(2)
#窗口切换的等待
current_handles = driver.window_handles
wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
wait.until(ec.new_window_is_opened(current_handles))

#iframe切换

#窗口切换，首先要去取到每一个窗口的id
#窗口的句柄也就是窗口的名字
#print(driver.current_window_handle)#获取当前窗口
print(driver.window_handles)#获取所有句柄信息，返回是一个列表
driver.switch_to.window(driver.window_handles[1])


#点击定位图片
img = wait_find_element((By.TAG_NAME,'img'))
print(img)
















