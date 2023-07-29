#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# File       : relion_star_class_sum.py
# Time       ：2023/7/29 11:04
# Author     ：Jago
# Email      ：huwl2022@shanghaitech.edu.cn
# version    ：python 3.10.11
# Description：
"""
from multiprocessing import Pool


def save_included(line):
    linelist = line.split()
    if (len(linelist) == 32) and (not int(linelist[26]) == 1):
        with open("data/run336_it025_data_2&3class.star", 'a', encoding='utf-8', newline='') as f:
            f.write(line)


if __name__ == "__main__":
    pool = Pool(16)
    with open("data/run336_it025_data.star", "r") as f:
        line = f.readline()
        while line:
            pool.apply(func=save_included, args=(line,))
            line = f.readline()
    pool.close()
    pool.join()
    print("done")

