#!/usr/bin/python
#-*- coding:utf-8 -*-
List=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
#可以使用list中的sort排序的方法来实现最大的两个值的筛选。
#首先使用sort拍一下序，排序是有小到大排列的。
List.sort()
#然后再通过索引，取出来最后的两个值。
print '第一个最大值是:',List[-1]
print '第二个最大值是:',List[-2]