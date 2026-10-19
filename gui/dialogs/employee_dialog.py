from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

from db.db_manager import DatabaseManager
from gui.transformed_ui.ui_dialog_employee import Ui_DialogEmployee


class EmployeeDialog(QDialog, Ui_DialogEmployee):
    def __init__(self, db: DatabaseManager, employee_id=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dateEmpBirth.setCalendarPopup(False)

        self.db = db
        self.employee_id = employee_id
        self.editEmpId.setReadOnly(True)

        self.btnSave.clicked.connect(self._on_save)
        self.btnCancel.clicked.connect(self.reject)

        self._load_data()

    def _load_data(self):
        employees = self.db.get_all_employees() or []
        self.comboSpouse.clear()
        for emp_id, full_name, role in employees:
            if emp_id != self.employee_id:
                self.comboSpouse.addItem(f"{full_name} ({role})", emp_id)

        if self.employee_id:
            emp = self.db.get_employee_by_id(self.employee_id)
            if emp:
                emp_id, full_name, birth_date, phone, marital, role, spouse_id = emp
                self.editEmpId.setText(str(emp_id))
                self.editEmpName.setText(full_name)
                if birth_date:
                    self.dateEmpBirth.setDate(QDate(birth_date.year, birth_date.month, birth_date.day))
                self.editEmpPhone.setText(phone or "")
                self.comboMarital.setCurrentText(marital or "Не в браке")
                self.comboRole.setCurrentText(role)

                if spouse_id:
                    self.checkHasSpouse.setChecked(True)
                    for i in range(self.comboSpouse.count()):
                        if self.comboSpouse.itemData(i) == spouse_id:
                            self.comboSpouse.setCurrentIndex(i)
                            break

    def _on_save(self):
        full_name = self.editEmpName.text().strip()
        phone = self.editEmpPhone.text().strip()
        if not full_name:
            QMessageBox.warning(self, "Ошибка", "Введите ФИО сотрудника.")
            return

        birth_date = self.dateEmpBirth.date().toPython()
        marital = self.comboMarital.currentText()
        role = self.comboRole.currentText()
        spouse_id = self.comboSpouse.currentData() if self.checkHasSpouse.isChecked() else None

        if self.checkHasSpouse.isChecked() and spouse_id:
            marital = "В браке"

        if self.employee_id:
            ok = self.db.update_employee(
                self.employee_id, full_name, birth_date, phone, marital, role, spouse_id
            )
            if ok:
                QMessageBox.information(self, "Успех", "Данные сотрудника обновлены.")
                self.accept()
            else:
                QMessageBox.critical(self, "Ошибка", "Не удалось обновить сотрудника.")
        else:
            new_id = self.db.add_employee(full_name, birth_date, phone, marital, role, spouse_id)
            if new_id:
                QMessageBox.information(self, "Успех", "Сотрудник добавлен.")
                self.accept()
            else:
                QMessageBox.critical(self, "Ошибка", "Не удалось добавить сотрудника.")