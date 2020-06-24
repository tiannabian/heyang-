# 解析小程序的trace，获取以下内容：
# 1系统信息
# 2小程序启动时间
# 3内存，cpu，fps
# 4渲染，页面打开时间

import json
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
import pyecharts.options as opts


wx_api_info = []        # 保存所有API信息（对应wx的api）
app_api_info = []       # 保存所有的app信息
page_api_info = []      # 保存所有的page信息

hardware_cpu = []       # 保存cpu信息
hardware_fps = []       # 保存fps信息
hardware_mem = []       # 保存内存信息


def judge_content_save(item_dict, judge_equal_tuple, judge_contain_tuple=None):
    """
    【判断item_dict的内容是否保存】
    item_dict: 待比较的字典字段
    judge_equal_tuple: 一个元组，第一个元素保存的是key值，第二个元素保存的是比较值， 判断是否==关系
    judge_contain_tuple: 一个元组，第一个元素保存的是key值，第二个元素保存的是判断值， 判断in关系
    如果条件满足，返回true 否则返回false
    """
    # judge_equal_tuple一定会存在
    key, value = judge_equal_tuple
    judge_first = (key in item_dict) and (item_dict[key] == value)
    # 第二次判断
    if judge_contain_tuple:
        key, value = judge_contain_tuple
        judge_sencod = (key in item_dict) and (value in item_dict[key])
        return judge_first and judge_sencod
    else:
        return judge_first

def get_api_wx_app_data(result_list, item_dict, judge_equal_tuple):
    """
    【api的信息，通过一个字段的==比较即可判断】
    如果api（wx,app两类信息）的信息存在，则把他添加到外部的result_list中
    item_dict: 待比较的字典字段
    judge_equal_tuple: 一个元组，第一个元素保存的是key值，第二个元素保存的是比较值
    返回函数，持续时间，打点时间
    """
    if judge_content_save(item_dict, judge_equal_tuple):
        # 有的信息item_dict 不存在dur，这些是参数类型信息，过滤掉
        if 'dur' in item_dict:
            result_list.append((item_dict['name'], item_dict['dur'], item_dict['ts']))

def get_api_page_data(result_list, item_dict, judge_equal_tuple):
    """
    【api的信息，通过一个字段的==比较即可判断】【因为page类判断特殊，所以，单独拎出来】
    如果api（page类信息）的信息存在，则把他添加到外部的result_list中
    item_dict: 传入的当前数据
    judge_equal_tuple: 传入的判断数据
    page页面类型， 页面函数，持续时间，打点时间
    """
    key, value = judge_equal_tuple
    if value in str(item_dict[key]):
        result_list.append((item_dict['cat'], item_dict['name'], item_dict['dur'], item_dict['ts']))

def get_hardware_info(result_list, item_dict, judge_equal_tuple, judge_contain_tuple):
    """
    抽象的，判断hardware的信息是否存在（mem，fps，cpu三类信息）
    item_dict: 待比较的字典字段
    judge_equal_tuple: 一个元组，第一个元素保存的是key值，第二个元素保存的是比较值
    judge_contain_tuple: 一个元组，第一个元素保存的是key值，第二个元素保存的是判断值
    返回对应类型的值，打点时间
    """
    if judge_content_save(item_dict, judge_equal_tuple, judge_contain_tuple):
        contain_key, contain_value = judge_contain_tuple
        result_list.append((item_dict[contain_key][contain_value], item_dict['ts']))

def get_all_init_data(path_f):
    """
    获取所有的初始待计算信息
    pf: 原始数据的路径
    """
    with open(path_f, mode="r", encoding="utf-8") as pf:

        json_data = json.load(pf)  # json格式字符串转化为dict
        # print(json_data)
        for tmp_item in json_data['traceEvents']:
            # 保存获取的api信息
            get_api_wx_app_data(wx_api_info, tmp_item, ('cat', 'API'))
            get_api_wx_app_data(app_api_info, tmp_item, ('cat', 'App'))
            get_api_page_data(page_api_info, tmp_item, ('cat', '/'))
            # 保存硬件hardware信息
            get_hardware_info(hardware_cpu, tmp_item, ('cat', 'Hardware'), ("args", "CPU"))
            get_hardware_info(hardware_mem, tmp_item, ('cat', 'Hardware'), ("args", "MEMORY"))
            get_hardware_info(hardware_fps, tmp_item, ('cat', 'Hardware'), ("args", "FPS"))

if __name__ == '__main__':

    get_all_init_data(r".\trace_wx17ea87763491620f_1588906219658_1588907320966.txt")
    print("wx-API: ", wx_api_info)
    print("app-API: ", app_api_info)
    print("page-API: ", page_api_info)
    print("cpu: ", hardware_cpu)
    print("fps: ", hardware_fps)
    print("mem: ", hardware_mem)
