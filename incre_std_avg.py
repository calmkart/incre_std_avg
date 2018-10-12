# -*- coding: utf-8 -*-
from __future__ import division
import numpy


class incre_std_avg():
    '''
    增量计算海量数据平均值和标准差,方差
    1.数据
    obj.avg为平均值
    obj.std为标准差
    obj.n为数据个数
    对象初始化时需要指定历史平均值,历史标准差和历史数据个数(初始数据集为空则可不填写)
    2.方法
    obj.incre_in_list()方法传入一个待计算的数据list,进行增量计算,获得新的avg,std和n(海量数据请循环使用该方法)
    obj.incre_in_value()方法传入一个待计算的新数据,进行增量计算,获得新的avg,std和n(海量数据请将每个新参数循环带入该方法)
    '''

    def __init__(self, h_avg=0, h_std=0, n=0):
        self.avg = h_avg
        self.std = h_std
        self.n = n

    def incre_in_list(self, new_list):
        avg_new = numpy.mean(new_list)
        incre_avg = (self.n*self.avg+len(new_list)*avg_new) / \
            (self.n+len(new_list))
        std_new = numpy.std(new_list)
        incre_std = numpy.sqrt((self.n*(self.std**2+(incre_avg-self.avg)**2)+len(new_list)
                                * (std_new**2+(incre_avg-avg_new)**2))/(self.n+len(new_list)))
        self.avg = incre_avg
        self.std = incre_std
        self.n += len(new_list)

    def incre_in_value(self, value):
        incre_avg = (self.n*self.avg+value)/(self.n+1)
        incre_std = numpy.sqrt((self.n*(self.std**2+(incre_avg-self.avg)
                                        ** 2)+(incre_avg-value)**2)/(self.n+1))
        self.avg = incre_avg
        self.std = incre_std
        self.n += 1


if __name__ == "__main__":
    c = incre_std_avg()
    c.incre_in_value(0.05)
    print c.avg
    print c.std
    print c.n
    c.incre_in_value(0.02)
    c.incre_in_list([0.5, 0.2, 0.3])
    print c.avg
    print c.std
    print c.n
