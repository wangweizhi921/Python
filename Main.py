# _*_ coding:utf-8 _*_
import ClassMain as CMain
from Windows import *
import time



class main:
    def __init__(self):
        self.tt=CMain.ConfigInfo['HwndName']
        HwndList = []
        HwndList=CMain.GetHwnd(self.tt)
        if not HwndList:
            print('没有运行程序')
        else:
            print(HwndList)
      




if __name__ == '__main__':	
    main()