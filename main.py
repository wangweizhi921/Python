from PyQt6.QtWidgets import *
import sys
import Ui_Main

class QApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
    #----------------------------------------------------------------如果有重定义函数

class MainWindows(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Set_Ui()

    def Set_Ui(self):
        self.Set_Windows()
        self.Set_Button()
        
        
    def Set_Button(self):
        self.buttom = QPushButton(self)
        self.buttom.setText("按钮")
        self.buttom.clicked.connect(self.Button_Click)
        self.buttom.move(100,100)
        
    def Set_Windows(self):
        self.setWindowTitle("这个是窗口标题")
        self.resize(800,500) 
        self.status = self.statusBar()
        self.status.showMessage('我是状态栏',5000) 
    
    def Button_Click(self,):
        print("按钮被点击了")
    

if __name__ == "__main__":
    
    App = QApp(sys.argv)
    Window = MainWindows()
    ui = Ui_Main.Ui_MainWindow()
    ui.setupUi(Window)
    Window.show()
    print(dir(Window.buttom))
    sys.exit(App.exec())
    
    
    
    