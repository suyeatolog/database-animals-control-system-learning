from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QMessageBox

from db.db_manager import DatabaseManager
from gui.dialogs.employee_dialog import EmployeeDialog


class EmployeesController:
    def __init__(self, db: DatabaseManager, main_window):
        self.db = db
        self.main_window = main_window
        self.current_emp_id = None

        self.combo_role = main_window.comboEmployeeRole
        self.table = main_window.tableEmployees
        self.btn_add = main_window.btnAddEmployee
        self.btn_edit = main_window.btnSecondary3
        self.btn_delete = main_window.btnDelete4

        self.model = QStandardItemModel()
        self.table.setModel(self.model)

        self.combo_role.currentTextChanged.connect(self._filter_data)
        self.table.selectionModel().selectionChanged.connect(self._on_selection_changed)
        self.btn_add.clicked.connect(self._on_add)
        self.btn_edit.clicked.connect(self._on_edit)
        self.btn_delete.clicked.connect(self._on_delete)

        self.all_data = []
        self._load_data()

    def _load_data(self):
        self.all_data = self.db.get_employees_full() or []
        self._filter_data()

    def _filter_data(self):
        role_filter = self.combo_role.currentText()
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "ID", "ФИО", "Дата рождения", "Телефон", "Семейное положение", "Должность", "Супруг(а)"
        ])

        for row in self.all_data:
            emp_id, full_name, birth_date, phone, marital, role, spouse_id, spouse_name = row
            if role_filter != "Все" and role != role_filter:
                continue

            date_str = birth_date.strftime("%d.%m.%Y") if birth_date else ""
            items = [
                QStandardItem(str(emp_id)),
                QStandardItem(full_name),
                QStandardItem(date_str),
                QStandardItem(phone or ""),
                QStandardItem(marital or ""),
                QStandardItem(role),
                QStandardItem(spouse_name or "—")
            ]
            self.model.appendRow(items)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def _on_selection_changed(self):
        indexes = self.table.selectionModel().selectedRows()
        if indexes:
            self.current_emp_id = int(self.model.item(indexes[0].row(), 0).text())
        else:
            self.current_emp_id = None

    def _on_add(self):
        dialog = EmployeeDialog(self.db, parent=self.main_window)
        if dialog.exec():
            self._load_data()

    def _on_edit(self):
        if not self.current_emp_id:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите сотрудника для редактирования.")
            return
        dialog = EmployeeDialog(self.db, employee_id=self.current_emp_id, parent=self.main_window)
        if dialog.exec():
            self._load_data()

    def _on_delete(self):
        if not self.current_emp_id:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите сотрудника для удаления.")
            return
        reply = QMessageBox.question(
            self.main_window, "Подтверждение",
            "Удалить выбранного сотрудника? (Нельзя удалить сотрудника, за которым закреплены животные)",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            if self.db.delete_employee(self.current_emp_id):
                QMessageBox.information(self.main_window, "Успех", "Сотрудник удалён.")
                self._load_data()
            else:
                QMessageBox.critical(
                    self.main_window, "Ошибка",
                    "Не удалось удалить сотрудника. Сначала переназначьте его животных другому специалисту."
                )