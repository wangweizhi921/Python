""" # _*_ coding:utf-8 _*_"""
import win32gui
import win32con
import win32api
import time


#获取当前主机上的所有句柄id
def get_all_windows():
    all_window_handles = []
    # 枚举所有窗口句柄，添加到列表中
    def enum_windows_proc(hwnd, param):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            param.append((hwnd, win32gui.GetWindowText(hwnd),win32gui.GetClassName(hwnd)))
        return True
 
    # 调用枚举窗口API
    win32gui.EnumWindows(enum_windows_proc, all_window_handles)
 
    return all_window_handles  #返回的是一个句柄id的列表
 
 
 
#遍历窗口句柄的所有子窗口
def get_child_windows(parent_window_handle):
    child_window_handles = []
    def enum_windows_proc(hwnd,param):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            param.append((hwnd, win32gui.GetWindowText(hwnd),win32gui.GetClassName(hwnd)))
        return True
    #win32gui.EnumChildWindows    遍历窗口句柄的所有子窗口
    win32gui.EnumChildWindows(parent_window_handle, enum_windows_proc, child_window_handles)
    return child_window_handles




title_list = []
title_list = get_all_windows()
# print(title_list)

hwnd=(133752)

win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, 87, 0)
time.sleep(0.1)
win32gui.PostMessage(hwnd, win32con.WM_KEYUP, 87, 0)

time.sleep(2)

win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, 87, 0)
time.sleep(0.1)
win32gui.PostMessage(hwnd, win32con.WM_KEYUP, 87, 0)


""" 

mystring=['北国风光，千里冰封，万里雪飘。',
'望长城内外，惟余莽莽；大河上下，顿失滔滔。',
'山舞银蛇，原驰蜡象，欲与天公试比高。',
'须晴日，看红装素裹，分外妖娆。',
'江山如此多娇，引无数英雄竞折腰。',
'惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。',
'一代天骄，成吉思汗，只识弯弓射大雕。',
'俱往矣，数风流人物，还看今朝。','《沁园春·雪》']


for index, i in enumerate(mystring):
    for ch in i:
        print(ch,end='')
        win32gui.SendMessage(handleEdit, win32con.WM_CHAR, ord(ch), 0)
        time.sleep(0.05)
    win32gui.PostMessage(handleEdit, win32con.WM_KEYDOWN, 13, 0)
    time.sleep(0.1)
    win32gui.PostMessage(handleEdit, win32con.WM_KEYUP, 13, 0)
    
    

#获取保存按钮
cmdId=win32gui.GetMenuItemID(subMenu, 3)
#点击保存
win32gui.PostMessage(handle, win32con.WM_COMMAND, cmdId, 0)


position = win32api.MAKELONG(400,100) #x,y为点击点相对于该窗口的坐标
win32api.SendMessage(handleEdit,win32con.WM_RBUTTONDOWN,win32con.MK_RBUTTON,position)#向窗口发送模拟鼠标点击
win32api.SendMessage(handleEdit,win32con.WM_RBUTTONUP,win32con.MK_RBUTTON,position)#模拟释放鼠标左键


 """