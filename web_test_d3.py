from selenium.webdriver.support.select import Select

__author__ = '何旺彤'
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome

driver = Chrome()
driver.implicitly_wait(20)

#函数注解
def wait_find_element(loactor) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(ec.presence_of_all_elements_located(loactor))
    return input_ele

driver.get('http://baidu.com')

#定位设置
ele = wait_find_element((By.XPATH,"//a[text()='设置']"))
ele.click()

#定位高级设置
gj = wait_find_element((By.XPATH, "//a[text()='高级搜索' ]"))
gj.click()

# #第一种方法，定位select
# select = wait_find_element((By.XPATH, "//select[@name='ft']"))
# select.click()
# select.find_element_by_xpath('//option[@value="pdf"]').click()


#第二种方法：使用Select类
select = wait_find_element((By.XPATH, "//select[@name='ft']"))
sel_new = Select(select)
#选项1、value  2、index  3、text
sel_new.select_by_value('pdf')
#取消选择，意义对应+all
sel_new.deselect_all()


#三大切换
#windows 切换：1、拿到window的句柄
#name 2、print(window_handles, current_windows_handle)

#窗口等待， ec.new_window_is_open(current_handles)

# iframe:1、frame  2、name  3、索引  4、WebElement
# 等待：frame_to_be_available_and_switch_to_it()
# ec.frame_to_be_available_and_switch_to_it

# 弹窗切换：alert， Alert类：text，accept(),dismiss()
# Select:告诉了我们；如果你觉得click不好用，你自己封装
# find_element()  不仅可以在driver对象上用，还可以在WebElent对象用==》下属标签
# 函数注解

'''



#鼠标操作
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome, ActionChains

driver = Chrome()
driver.implicitly_wait(20)

def wait_find_element(loactor) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(ec.presence_of_all_elements_located(loactor))
    return input_ele

driver.get('http://baidu.com')

# #ActionChains  动作链条
# ac = ActionChains(driver)
# #第一步：鼠标悬停
# ac.move_to_element()
# #第二步：点击动作
# ac.click()
# #第三步：右击
# ac.context_click()
# #以perform结束
# ac.perform()
# #或者以整体去运行
# ac = ActionChains(driver)
# ac.move_to_element().click().context_click().perform()

#举例子：百度首页，悬停到设置
ac = ActionChains(driver)
ele = wait_find_element((By.XPATH,"//a[text()='设置']"))
ac.move_to_element(ele).perform()
ac.click(wait_find_element((By.XPATH, "//a[text()='高级搜索' ]"))).perform()

'''
链式调用  actionChains
1、每次都是return self
2、perform()  run()
作用：用在连续调用，一次运行不同的程序或者函数
：数据库，ORM模型==》链式调用

函数：
1、click()
2、double-click()
3、context_click()
4、click_and_hold()
5、drag_and_drop()
move_to_element
'''



