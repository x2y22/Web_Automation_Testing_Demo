import json
import os
import page

def read_json(filename):
    '''
    :param filename: JSON文件的位置
    :return: 测试用例组成的字典
    '''
    with open(filename,"r",encoding="utf-8") as f:
        return json.load(f)