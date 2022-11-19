"""
在两个模板文件中取最多的
reference from https://blog.csdn.net/zengyaowu1988/article/details/111316009
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import yaml
import os
import io
import sys
 
 
argc = len(sys.argv)
#print(argc)
if argc != 3 :
	print("check_config.py template_config local_config")
	sys.exit(1)
 
 
template_config = sys.argv[1]
local_config = sys.argv[2]
 
print(template_config)
print(local_config)
 
if not os.path.isfile(template_config):
    print(template_config + " is not exists!")
    sys.exit(1)
    
if not os.path.isfile(local_config):
    print(local_config + " is not exists!")
    sys.exit(1)    
    
#open template_config
old = io.open(template_config, 'r', encoding="utf-8")
cfg_old = old.read()
dict_old = yaml.load(cfg_old,Loader=yaml.FullLoader)
 
#open local_config
new = io.open(local_config, 'r',encoding="utf-8")
cfg_new = new.read()
dict_new = yaml.load(cfg_new,Loader=yaml.FullLoader)
 
 
def merge_data(data_1, data_2):
    """
    使用 data_2 和 data_1 合成一个新的字典。
    对于 data_2 和 data_1 都有的 key，如果data_2为None，则用data_1，否则用data_2。
    :param data_1:
    :param data_2:
    :return:
    """
    if isinstance(data_1, dict) and isinstance(data_2, dict):
        new_dict = {}
        d2_keys = list(data_2.keys())
        for d1k in data_1.keys():
            if d1k in d2_keys:  # d1,d2都有。去往深层比对
                d2_keys.remove(d1k)
                new_dict[d1k] = merge_data(data_1.get(d1k), data_2.get(d1k))
            else:
                new_dict[d1k] = data_1.get(d1k)  # d1有d2没有的key
        for d2k in d2_keys:  # d2有d1没有的key
            new_dict[d2k] = data_2.get(d2k)
        return new_dict
    else:
        if data_2 == None:#d2为空使用d1
            return data_1
        else:             #d2不为空使用d2
            return data_2
 
 
result = merge_data(dict_old, dict_new)
#print(result)
 
old.close()
new.close()
 
#write result to local_config
yaml_file = open(local_config, 'w+')
yaml.dump(result,yaml_file,default_flow_style=False,encoding='utf-8',allow_unicode=True)
yaml_file.close() 