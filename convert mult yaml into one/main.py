# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/18 14:26
@Author  : jackyLiu
@Address : https://github.com/Onedragon424
@Reference:
    how to merge two yaml: https://stackoverflow.com/questions/47424865/merge-two-yaml-files-in-python
"""
# dependence: hiyapyco
from codecs import unicode_escape_encode
from decimal import localcontext
import hiyapyco
import yaml
import io
import sys
import os

if __name__ == "__main__":

    # read file information
    argc = len(sys.argv)
    if argc != 3:
        print("file run, target file, import yaml file")
        sys.exit(-1)
        
    local_config = sys.argv[1]
    tmp_config = sys.argv[2]

    print(f"merge {tmp_config} into {local_config}")

    # check if file exists
    if not os.path.isfile(tmp_config):
        print(f"import file is not exists")
        sys.exit(-1)
    if not os.path.isfile(local_config):
        print(f"target file is not exists")
        sys.exit(-1)

    # read str from file 
    local = ""
    tmp = ""
    with open(tmp_config, 'r', encoding='utf-8') as File:
        tmp = File.read()
    with open(local_config, 'r', encoding='utf-8') as File:
        local = File.read()

    # reference : https://stackoverflow.com/questions/47424865/merge-two-yaml-files-in-python
    merged_yaml = hiyapyco.load([local, tmp], method=hiyapyco.METHOD_MERGE)
    with open(local_config, 'w', encoding='utf-8-sig') as File:
        print(type(merged_yaml))
        File.write(hiyapyco.dump(merged_yaml))
        # File.write(hiyapyco.dump(merged_yaml))
        
    #write result to local_config
    # yaml_file = open(local_config, 'w')
    # yaml.dump(merged_yaml,yaml_file,encoding='utf-8',allow_unicode=True)
    # yaml_file.close() 