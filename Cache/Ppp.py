# _*_ coding:utf-8 _*_
import win32con
import win32gui
import time









handle = win32gui.FindWindow('Notepad','新建文本文档.txt - 记事本')
handleEdit = win32gui.FindWindowEx(handle, None, 'EDIT', None)


menu = win32gui.GetMenu(handle)
subMenu = win32gui.GetSubMenu(menu, 0)



mystring=['北国风光，千里冰封，万里雪飘。','望长城内外，惟余莽莽；大河上下，顿失滔滔','《沁园春·雪》']




for index, i in enumerate(mystring):
    for ch in i:
        print(ch)
        win32gui.SendMessage(handleEdit, win32con.WM_CHAR, ord(ch), 0)
        time.sleep(0.1)
    win32gui.PostMessage(handleEdit, win32con.WM_KEYDOWN, 13, 0)
    time.sleep(1)
    win32gui.SendMessage(handleEdit, win32con.WM_KEYUP, 13, 0)
    
    
    
win32gui.PostMessage(handleEdit, win32con.WM_KEYDOWN, 13, 0)
win32gui.SendMessage(handleEdit, win32con.WM_KEYUP, 13, 0)
#获取保存按钮
cmdId=win32gui.GetMenuItemID(subMenu, 3)
#点击保存
win32gui.PostMessage(handle, win32con.WM_COMMAND, cmdId, 0)

