import sys
from PyQt5.QtWidgets import *





# 每一个步骤,都可以进行拦截

# 所以先建立一个主窗口的class类,然后再去创建,为了重构函数
############################### 接收事件第一步,notify ######################### 
    # 接收事件第一步,notify
############################### 函数开始 ######################################
class CheckEvent(QApplication):
    def notify(self,QObject,QEvent): # notify
        #判断obj的继承类是否为QPushButton 并且 类型是否为,鼠标点击MouseButtonPress
        if QObject.inherits("QPushButton") and QEvent.type() == QEvent.MouseButtonPress: 
            print('notify-mouse-pressed')
        return super().notify(QObject,QEvent) #发送事件 
############################### 函数结束 ######################################
    
############################### 接收事件第二步,event ######################### 
    # 接收事件第二步,event 
    # 注意,这里是重写按钮,所以需要重新写一个类,并且调用时使用类名称而不是原来的QPushButton
############################### 函数开始 ######################################
class Buttons(QPushButton):
    def event(self, QEvent):
        if QEvent.type() == QEvent.MouseButtonPress:
            print('event-mouse-pressed')
        return super().event(QEvent) #发送事件

############################### 接收事件第三步,mousePressEvent ######################### 
    def mousePressEvent(self,QMouseEvent) -> None:
        print('mousePressEvent-mouse-pressed')
        return super().mousePressEvent(QMouseEvent)
############################### 函数结束 ######################################
    
    




class MainWindow(QMainWindow):#创建一个应用程序窗口
    def __init__(self):
        super().__init__()
        self.Set_UI()
    def Set_UI(self):
        self.Set_Window()
        self.SetUiButton() # 创建按钮 
        self.SetUiLable()  # 创建文本
    def Set_Window(self):       # 创建测试窗口
        self.setWindowTitle("这个是窗口标题")
        self.resize(800,500)      
    def SetUiButton(self):      # 创建测试按钮
        self.btn = Buttons(self)
        self.btn.setText("这个是按钮")
        self.btn.move(100,50) 
        pass
    def SetUiLable(self):       # 创建测试Lable
        # self.label = QLabel(self)
        # self.label.setText("这个是文本")
        # self.label.move(100,100)
        pass
      


if __name__ == "__main__":
    
    app = CheckEvent(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



