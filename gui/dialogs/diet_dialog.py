from datetime import datetime

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from db.db_manager import DatabaseManager
from gui.transformed_ui.ui_dialog_diet import Ui_DialogDiet


class DietDialog(QDialog, Ui_DialogDiet):
    def __init__(self, db: DatabaseManager, diet_id=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = db
        self.diet_id = diet_id
        self.editDietId.setReadOnly(True)
        self.comboDietType.setEditable(True)

        self.btnSave.clicked.connect(self._on_save)
        self.btnCancel.clicked.connect(self.reject)

        self._load_data()

    def _load_data(self):
        types = self.db.get_distinct_diet_types()
        self.comboDietType.clear()
        default_types = ["Детский", "Диетический", "Усиленный", "Обычный"]
        for t in types:
            self.comboDietType.addItem(t)
        for dt in default_types:
            if dt not in types:
                self.comboDietType.addItem(dt)

        if self.diet_id:
            diet = self.db.get_diet_by_id(self.diet_id)
            if diet:
                d_id, d_name, d_type = diet
                self.editDietId.setText(str(d_id))
                self.editDietName.setText(d_name)
                self.comboDietType.setCurrentText(d_type)

    def _on_save(self):
        name = self.editDietName.text().strip()
        diet_type = self.comboDietType.currentText().strip()
        if not name or not diet_type:
            QMessageBox.warning(self, "Ошибка", "Укажите название и тип рациона.")
            return

        if self.diet_id:
            ok = self.db.update_diet(self.diet_id, name, diet_type)
        else:
            ok = self.db.add_diet(name, diet_type) is not None

        if ok:
            self.accept()
        else:
            QMessageBox.critical(
                self, "Ошибка",
                "Не удалось сохранить рацион (возможно, такое сочетание типа и названия уже существует)."
            )


class DietTypeDialog(QDialog):
    def __init__(self, db: DatabaseManager, old_type_name=None, parent=None):
        super().__init__(parent)
        self.db = db
        self.old_type_name = old_type_name
        self.setWindowTitle("Редактирование типа рациона" if old_type_name else "Добавление типа рациона")
        self.setMinimumWidth(420)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.editTypeName = QLineEdit(old_type_name or "")
        self.editTypeName.setPlaceholderText("Например: Детский, Диетический, Усиленный")
        form.addRow("Название типа рациона:", self.editTypeName)

        self.editFirstDietName = QLineEdit()
        self.editFirstDietName.setPlaceholderText("Например: Базовый рацион №1")
        if not self.old_type_name:
            form.addRow("Первый рацион этого типа:", self.editFirstDietName)
        else:
            info = QLabel("При изменении названия типа оно обновится у всех рационов этой группы.")
            info.setWordWrap(True)
            layout.addWidget(info)

        layout.addLayout(form)

        btns = QHBoxLayout()
        btn_cancel = QPushButton("Отмена")
        btn_save = QPushButton("Сохранить")
        btn_cancel.clicked.connect(self.reject)
        btn_save.clicked.connect(self._on_save)
        btns.addWidget(btn_cancel)
        btns.addWidget(btn_save)
        layout.addLayout(btns)

    def _on_save(self):
        new_type = self.editTypeName.text().strip()
        if not new_type:
            QMessageBox.warning(self, "Ошибка", "Введите название типа рациона.")
            return

        if self.old_type_name:
            ok = self.db.rename_diet_type(self.old_type_name, new_type)
        else:
            first_diet = self.editFirstDietName.text().strip()
            if not first_diet:
                QMessageBox.warning(
                    self, "Ошибка",
                    "Так как типы хранятся в таблице diets, укажите название первого рациона для этого типа."
                )
                return
            ok = self.db.add_diet_type_with_first_diet(new_type, first_diet) is not None

        if ok:
            self.accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить тип рациона.")


class AssignDietDialog(QDialog):
    def __init__(self, db: DatabaseManager, history_id=None, parent=None):
        super().__init__(parent)
        self.db = db
        self.history_id = history_id
        self.setWindowTitle("Редактирование назначения" if history_id else "Назначение рациона питомцу")
        self.setMinimumWidth(450)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.comboAnimal = QComboBox()
        for row in (self.db.get_all_animals() or []):
            self.comboAnimal.addItem(f"{row[1]} ({row[4]}, ID: {row[0]})", row[0])

        self.comboDiet = QComboBox()
        for row in (self.db.get_all_diets() or []):
            self.comboDiet.addItem(f"№{row[0]} — {row[1]} ({row[2]})", row[0])

        self.editStartDate = QLineEdit()
        self.editStartDate.setInputMask("99.99.9999;_")
        self.editStartDate.setText(datetime.now().strftime("%d.%m.%Y"))

        self.editEndDate = QLineEdit()
        self.editEndDate.setPlaceholderText("дд.мм.гггг (оставьте пустым, если активен)")

        form.addRow("Питомец:", self.comboAnimal)
        form.addRow("Рацион:", self.comboDiet)
        form.addRow("Дата начала (дд.мм.гггг):", self.editStartDate)
        form.addRow("Дата окончания:", self.editEndDate)
        layout.addLayout(form)

        btns = QHBoxLayout()
        btn_cancel = QPushButton("Отмена")
        btn_save = QPushButton("Сохранить")
        btn_cancel.clicked.connect(self.reject)
        btn_save.clicked.connect(self._on_save)
        btns.addWidget(btn_cancel)
        btns.addWidget(btn_save)
        layout.addLayout(btns)

        if self.history_id:
            self._load_existing()

    def _load_existing(self):
        rec = self.db.get_diet_history_by_id(self.history_id)
        if rec:
            _, animal_id, diet_id, start_date, end_date = rec
            for i in range(self.comboAnimal.count()):
                if self.comboAnimal.itemData(i) == animal_id:
                    self.comboAnimal.setCurrentIndex(i)
                    break
            for i in range(self.comboDiet.count()):
                if self.comboDiet.itemData(i) == diet_id:
                    self.comboDiet.setCurrentIndex(i)
                    break
            if start_date:
                self.editStartDate.setText(start_date.strftime("%d.%m.%Y"))
            if end_date:
                self.editEndDate.setText(end_date.strftime("%d.%m.%Y"))

    def _on_save(self):
        animal_id = self.comboAnimal.currentData()
        diet_id = self.comboDiet.currentData()
        start_str = self.editStartDate.text().strip()
        end_str = self.editEndDate.text().strip()

        if not animal_id or not diet_id:
            QMessageBox.warning(self, "Ошибка", "Выберите питомца и рацион.")
            return

        try:
            start_date = datetime.strptime(start_str, "%d.%m.%Y").date()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректную дату начала (дд.мм.гггг).")
            return

        end_date = None
        if end_str:
            try:
                end_date = datetime.strptime(end_str, "%d.%m.%Y").date()
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Введите корректную дату окончания (дд.мм.гггг) или оставьте пустой.")
                return

        if self.history_id:
            ok = self.db.update_diet_history(self.history_id, animal_id, diet_id, start_date, end_date)
        else:
            ok = self.db.assign_diet_to_animal(animal_id, diet_id, start_date, end_date)

        if ok:
            self.accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить запись о рационе питомца.")