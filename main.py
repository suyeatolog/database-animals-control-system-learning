from PySide6.QtWidgets import QApplication, QMainWindow

from gui.transformed_ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuList.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex
        )
        self.menuList.setCurrentRow(0)

if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()