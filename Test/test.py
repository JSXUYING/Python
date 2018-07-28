#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#caculate value of BMI
name = input('Please enter your name:')
height = input('Please enter your height:')
weight = input('Please enter your weight:')
height = float(height)
weight = float(weight)
BMI = weight/(height*height)
if BMI < 18.5:
    print(name,'height=',height,'weight=',weight,'underweight')
elif 18.5 < BMI <25:
    print(name,'height=',height,'weight=',weight,'normal')
elif 25 < BMI <28:
    print(name,'height=',height,'weight=',weight,'overweight')
elif BMI>32:
    print(name,'height=',height,'weight=',weight,'fat')

