import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.MainWindow import Ui_MainWindow
from UI.forms_pack import Ui_Form


# 主窗体
class Main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.Button_pack_show.clicked.connect(self.forms_pack_show)

    def forms_pack_show(self):
        self.form_pack = Forms_pack()
        self.form_pack.show()


# 扫描窗体
class Forms_pack(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.returnPressed.connect(self.item_in)

    def item_in(self):
        text = self.lineEdit.text()

        print(text)

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, "提示", "退出后当前扫描明细将丢失\n确认继续吗？", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_ui = Main_ui()

    sys.exit(app.exec_())
