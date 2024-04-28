
#获取当前所有句柄Id,Title,ClassName
def Get_All_Windows(HwndClassName=None):
    All_Window_Handles = []
    # 枚举所有窗口句柄，添加到列表中
    def Enum_Windows_Hwnd(HwndIndex, Hwnd_Param):
        if win32gui.IsWindow(HwndIndex) and win32gui.IsWindowEnabled(HwndIndex) and win32gui.IsWindowVisible(HwndIndex):
            if HwndClassName != None :
                if win32gui.GetClassName(HwndIndex) == HwndClassName:
                    Hwnd_Param.append((HwndIndex, win32gui.GetWindowText(HwndIndex),win32gui.GetClassName(HwndIndex)))  
            else:
                Hwnd_Param.append((HwndIndex, win32gui.GetWindowText(HwndIndex),win32gui.GetClassName(HwndIndex)))               
        return True
 
    # 调用枚举窗口API
    win32gui.EnumWindows(Enum_Windows_Hwnd, All_Window_Handles)
 
    return All_Window_Handles  #返回的是一个句柄id的列表

