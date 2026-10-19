import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from controllers.animals_controller import AnimalsController
from controllers.diets_controller import DietsController
from controllers.employees_controller import EmployeesController
from controllers.reports_controller import ReportsController
from db.db_manager import DatabaseManager
from gui.transformed_ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.db = DatabaseManager()
        if not self.db.connect():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к БД.")
            sys.exit(1)
        
        self.animals_ctrl = AnimalsController(self.db, self)
        self.employees_ctrl = EmployeesController(self.db, self)
        self.diets_ctrl = DietsController(self.db, self)
        self.reports_ctrl = ReportsController(self.db, self)

        self.menuList.currentRowChanged.connect(self._on_menu_changed)
        self.menuList.setCurrentRow(0)
    
    def _on_menu_changed(self, index):
        self.stackedWidget.setCurrentIndex(index)
    
    def closeEvent(self, event):
        self.db.disconnect()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())