from selenium.webdriver.support.select import Select

__author__ = '何旺彤'

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





