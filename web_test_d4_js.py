

__author__ = '何旺彤'
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import  Keys

driver = Chrome()
driver.implicitly_wait(20)

#函数注解
def wait_find_element(loactor) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(ec.presence_of_all_elements_located(loactor))
    return input_ele

#driver.get('http://baidu.com')

########################################################################

#键盘操作使用keys
#ele = driver.find_element_by_id('kw')
#ele.send_keys('admin',Keys.CONTROL, Keys.CANCEL)

########################################################################
"""
js脚本
python  - webdriver  -   js桥梁  -  浏览器
1、find_element_by_id(id)==>{"by":"id", "value":"kw"} js命令:getElementById(id)
2、python 发送js代码  ==>{"by":"script","value":"document.getElementById('kw')"}

readonly表示只读
python能直接修改html属性吗？    python不能直接修改html属性 ，没有现成的命令去修改HTML,只能传输js去运行
"""
#ele = driver.find_element_by_id("kw")
#ele.get_attribute('name')

#访问12306
driver.get("https://www.12306.cn/index/")
#
date_ele = wait_find_element((By.ID,"train_date"))
print(date_ele)

#修改    readonly属性，   病并把value修改成 value = 2019-08-30  TODO:一定要记得休眠，否则修改不成功，原因：js反应不过来
js_code = "a = document.getElementById('train_date')"
driver.execute_script("js_code")
time.sleep(2)
js_code_1 = "a.readOnly=false"
driver.execute_script("js_code_1")
time.sleep(2)
js_code_2 = "a.value = 2019-08-30"
driver.execute_script("js_code_2")
time.sleep(2)

'''
#第二种方法
date_ele = wait_find_element((By.ID,"train_date"))
print(date_ele)
js_code = 'arguments[0].readOnly=false'
driver.execute_script(js_code, date_ele)

js_code_1 = 'arguments[0].value="2019-09-09"'
driver.execute_script(js_code_1, date_ele)
'''


'''
总结
1、鼠标操作 ActionChains  链式调用，存储动作，函数的动态调用
单击
双击
右击context_click
鼠标悬停
拖拽：drag_and_drop

perform()
2、Key，键盘发送  send_keys()

3、js脚本发送

'''

