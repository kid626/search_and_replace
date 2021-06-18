#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Copyright Copyright © 2021 fanzh . All rights reserved.
@Desc  查找并替换
@Author: fzh
@ProjectName: search_and_replace.py
@time: 2021-06-18 14:24
"""
import os
import sys
import getopt


# 文件查找 find . -name file_name -type f
# 查找函数：search_path 查找根路径 file_name 需要查找的文件名
def search(search_path, search_file_name, search_result):
    # 获取当前路径下地所有文件
    all_file = os.listdir(search_path)
    # 对于每一个文件
    for each_file in all_file:
        # 若文件为一个文件夹
        if os.path.isdir(search_path + os.sep + each_file):
            # 递归查找
            search(search_path + os.sep + each_file, search_file_name, search_result)
        # 如果是需要被查找的文件
        elif each_file == search_file_name:
            # 输出路径
            search_result.append(search_path + os.sep + search_file_name)


# 替换 sed -i 's/old_str/new_str/'
# 文本替换 replace_file_name 需要替换的文件路径，replace_old_str 要替换的字符，replace_new_str 替换的字符
def replace(replace_file_name, replace_old_str, replace_new_str):
    f1 = open(replace_file_name, "r")
    content = f1.read()
    f1.close()
    t = content.replace(replace_old_str, replace_new_str)
    with open(replace_file_name, "w") as f2:
        f2.write(t)
    f2.close()


if __name__ == '__main__':
    result = []
    # 默认当前目录
    path = os.getcwd()
    file_name = "test"
    old_str = "old_str"
    new_str = "new_str"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:f:o:n:", ["help", "path=", "file=", "old=", "new="])
    except getopt.GetoptError:
        print('usage: search_and_replace.py -p <path> -f <file_name> -o <old_str> -n <new_str>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('usage: search_and_replace.py -p <path> -f <file_name> -o <old_str> -n <new_str>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-f", "--file"):
            file_name = arg
        elif opt in ("-o", "--old"):
            old_str = arg
        elif opt in ("-n", "--new"):
            new_str = arg
    search(path, file_name, result)
    for file_name in result:
        replace(file_name, old_str, new_str)
        print("replace {} to {} in file {} successfully".format(old_str, new_str, file_name))
