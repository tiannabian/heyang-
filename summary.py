__author__ = '123456'
# coding=utf-8

"""
import pytest

@pytest.mark.error
    pass#表示标签
1、为什么要使用pytest?
pytest -m 标签,冒烟测试；
可以放到方法上面也可以放到类上面；
一个方法和类上面可以有多个标签
注意1：mark表达式一定要用双引号
注意2：



缓存文件： .pyc .pyd  .pyo
缓存文件夹：   cache

2、跳过函数
3、可以自动发现测试用例(怎么知道的呢？——符合命名规则test_*.py或者 *_test.py 的文件；以test_开头的函数名； 以Test开头的测试类（没有__init__函数）当中，以test_开头的函数)
4、断言很方便assert
5、非常非常多的插件  重运行  allure测试报告
    pytest -m "demon" --resultlog=report\test.log
    pytest -m demo --junitxml=report\test.xml
    装插件 pip install pytest-html   pytest -m demo --html=report\test.html
6、兼容unittest

7、fixture环境管理非常灵活
yield和return类似，但是函数遇到return停止，遇到yield不停止
作用域 函数、类、模块、会话


pytest的参数化  @pytest.mark.parametrize('data', user_info_error)
不能和unittest同时使用


pytest-allure
1、安装allure,   官网下载  解压到本地， 配置环境变量
2、 查看测试报告allure serve report\allure

jenkins
分布式配置：高并发、高性能  Master-slave;master就是jenkins的一个服务，一个网站；slave就是我们现在运行的电脑

"""

"""
web自动化测试内容
web自动化测试概论
前端页面：html,DOM对象
Seleniumd的使用
selenium自动化测试框架原理、xpath  CSS对比
pytest另一个单元测试框架
jenkins集成和allure
一、web自动化测试概论
什么是web测试，为什么还要web测试？
二、前端页面：html、DOM对象、js
1、HTML
元素定位，依据？？HTML购成（标签对  属性）。。。
2、DOM
只有js可以操作DOM吗？不是
DOM文档对象模型 为什么要用？方便
独立于平台和编程语言，可以被python java  js 等，只要支持对象，基本就ok
节点：（12个节点）文档节点（根节点，document,HTML）、元素节点（标签）、属性节点（id=""）、文本节点(text)、注释节点(注释)、指令节点(事件)

getElement
修改属性
alert
节点之间的关系：子孙关系、父子关系、同胞关系，只有根节点没有父节点

DOM事件：键盘、鼠标、windows、表单、拖动、event js
少部分情况，显示等待，强制1

三、selenium的使用
元素定位
xpath
css选择器
css vs xpath面试题
复杂操作：
等待：三大等待的区别,python 线程等待
显示等待 while finded==False
隐式等待，直接发送等待命令
三大切换，窗口，frame、alert    window_handlers,切换==>(current_handlers)
actionchains  链式  return obj[列表]， perform()
select 1、点击  2、select类  3、option,index,value,text
如果修改HTML, JS
窗口拖动，懒加载，拖动到可视范围
富文本，HTML，编辑器send_keys()
文件上传和下载操作

四、selenium自动化测试框架搭建
测试用例设计
带版本信息，一步一步封装优化
PageObject， MVC model, 会问到什么是，为什么会用到
ddt和用例数据分组
basepage
locator
效率问题和环境依赖

五、pytest另一个单元测试框架
冒烟用例smoke  打标记 @pytest.mark.smoke  方法和类都可以用
自动收集用例，用例执行顺序和unittest不一样，pytest-order
环境管理更加灵活  fixture
超多的插件，测试报告allure,重运行机制

六、jenkins
分布式  master-slave
jenkins alluer 插件








"""

