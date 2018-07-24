#/usr/bin/env python3
#-*- coding:utf-8 -*-
def findMinAndMax(L):
    if not L:
       return (None,None)
    elif len(L)==1:
       return (L[0],L[0])
    else:
       min = max = L[0]
       for i in L:
          if i < min:
               min = i
          elif i > max:
               max = i
       return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
