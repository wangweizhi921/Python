
import win32gui
import win32api
import win32con
import time
import keyboard
import threading
import pyautogui as pg






# title_list=pg.getAllTitles() 获取所有句柄标题,列表
# print(pg.position()) # 获取当前鼠标位置

# point = win32api.GetCursorPos()  #win32api.GetCursorPos 获取鼠标当前的坐标(x,y)
# hwnd = win32gui.WindowFromPoint(point)  #查看坐标位置窗口的句柄


 
""" time.sleep(2)

 
print(hwnd)  #输出句柄 """

 
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
 
 
#查询传入的句柄id、类名
def get_title(window_handle, class_name):
    #查询句柄的类名
    window_class = win32gui.GetClassName(window_handle)
 
    #判断窗口类名是否和指定的类名相同，如果相同则返回该窗口句柄，否则返回空值
    if window_class == class_name:
        return window_handle
 
#遍历窗口句柄的所有子窗口
def get_child_windows(parent_window_handle):
    child_window_handles = []
    def enum_windows_proc(hwnd, param):
        param.append(hwnd)
        return True
    #win32gui.EnumChildWindows    遍历窗口句柄的所有子窗口
    win32gui.EnumChildWindows(parent_window_handle, enum_windows_proc, child_window_handles)
    return child_window_handles
 
 
# 根据标题查找窗口句柄
def find_hwnd_by_title(title):
    all_windows = get_all_windows()  #查询所有句柄
    matched_windows = []      #存放所有匹配类名的句柄id
 
    # 在所有窗口中查找标题匹配的窗口句柄
    for window_handle in all_windows:
        #get_title方法  检查传入句柄对应的类名和我们实际的类名是否对应
        window_title = get_title(window_handle, title)
        if window_title:
            matched_windows.append(window_title) #如果对应就写入列表
 
    # 如果没有匹配到，则在所有子窗口中查找标题匹配的窗口句柄
    if matched_windows:
        return matched_windows
    else:
        child_window_handles = []
        for parent_window_handle in all_windows:
            #不论子窗口是否有数据都追加到列表
            child_window_handles.extend(get_child_windows(parent_window_handle))
        for child_window_handle in child_window_handles:
            if get_title(child_window_handle, title):
                matched_windows.append(get_title(child_window_handle, title))
    return matched_windows
 

    
def on_key_press(event):
    print(f"Key {event.name} pressed")
 

    
def task(n):
    print(f"Thread {n} starting")
    # 这个位置,输出一个按键
    
""" def main():
    threads = []        # 绑定线程
    for i in range(5):  # 创建5个线程
        t = threading.Thread(target=task, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
            t.join()  # 等待所有线程完成 """
    


# hwnd=(67238)       
# key_code=1
# win32gui.SetForegroundWindow(hwnd)
# time.sleep(2)  
# win32gui.SendMessage(hwnd , win32gui.WM_KEYDOWN , key_code ,0)  
# time.sleep(0.1)
# win32gui.SendMessage(hwnd , win32gui.WM_KEYUP , key_code ,0) 

    # print(t)
    
    # keyboard.hook(on_key_press)
    # keyboard.wait('ctrl')
    
    
    
title_list=get_all_windows()
    # window_class = get_title(67238,'King GEngine')
print(title_list)
    
    
    
    
    # print(title_list)
    # 传奇 Class_Name=KING GEngine
    
"""     all_windows = get_all_windows()
    for hwnd, window_title in all_windows:
        print(f'Handle: {hwnd}, Title: {window_title}')
    # print(titls) """
    
    
    
    # multiprocessing