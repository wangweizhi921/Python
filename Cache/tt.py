
import win32con
import win32gui
import time
import ProConfig
from  FunHwnd import Get_All_Windows as Gaw




# 查找标题为“HwndName”的窗口
HwndName='King GEngine'
HwndList = []
HwndList=Gaw(HwndName)

print(HwndList)