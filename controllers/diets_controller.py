from datetime import datetime

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QMessageBox

from db.db_manager import DatabaseManager
from gui.dialogs.diet_dialog import AssignDietDialog, DietDialog, DietTypeDialog


class DietsController:
    def __init__(self, db: DatabaseManager, main_window):
        self.db = db
        self.main_window = main_window

        self.table_types = main_window.tableDietTypes
        self.btn_add_type = main_window.btnAddDietType
        self.btn_edit_type = main_window.btnSecondary1
        self.btn_del_type = main_window.btnDelete1
        self.model_types = QStandardItemModel()
        self.table_types.setModel(self.model_types)

        self.btn_add_type.clicked.connect(self._add_diet_type)
        self.btn_edit_type.clicked.connect(self._edit_diet_type)
        self.btn_del_type.clicked.connect(self._delete_diet_type)

        self.combo_type_filter = main_window.comboDietTypeFilter
        self.table_diets = main_window.tableDiets
        self.btn_add_diet = main_window.btnAddDiet
        self.btn_edit_diet = main_window.btnSecondary2
        self.btn_del_diet = main_window.btnDelete2
        self.model_diets = QStandardItemModel()
        self.table_diets.setModel(self.model_diets)

        self.combo_type_filter.currentTextChanged.connect(self._filter_diets)
        self.btn_add_diet.clicked.connect(self._add_diet)
        self.btn_edit_diet.clicked.connect(self._edit_diet)
        self.btn_del_diet.clicked.connect(self._delete_diet)

        self.table_history = main_window.tableDietHistory
        self.btn_assign = main_window.btnAssignDiet
        self.btn_finish = main_window.btnDelete3
        self.model_history = QStandardItemModel()
        self.table_history.setModel(self.model_history)

        self.btn_assign.clicked.connect(self._assign_diet)
        self.btn_finish.clicked.connect(self._finish_or_delete_diet_history)
        self.table_history.doubleClicked.connect(self._edit_diet_history)

        self.all_diets = []
        self._load_all()

    def _load_all(self):
        self._load_diet_types()
        self._load_diets()
        self._load_history()

    def _load_diet_types(self):
        types_summary = self.db.get_diet_types_summary() or []
        self.model_types.clear()
        self.model_types.setHorizontalHeaderLabels([
            "Тип рациона", "Кол-во рационов", "Входящие рационы"
        ])

        current_filter = self.combo_type_filter.currentText()
        self.combo_type_filter.blockSignals(True)
        self.combo_type_filter.clear()
        self.combo_type_filter.addItem("Все")

        for diet_type, count, diet_names in types_summary:
            self.model_types.appendRow([
                QStandardItem(diet_type),
                QStandardItem(str(count)),
                QStandardItem(diet_names or "")
            ])
            self.combo_type_filter.addItem(diet_type)

        if current_filter:
            idx = self.combo_type_filter.findText(current_filter)
            if idx >= 0:
                self.combo_type_filter.setCurrentIndex(idx)
        self.combo_type_filter.blockSignals(False)

        self.table_types.resizeColumnsToContents()
        self.table_types.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    def _add_diet_type(self):
        dlg = DietTypeDialog(self.db, parent=self.main_window)
        if dlg.exec():
            self._load_all()

    def _edit_diet_type(self):
        indexes = self.table_types.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите тип рациона в таблице.")
            return
        old_type = self.model_types.item(indexes[0].row(), 0).text()
        dlg = DietTypeDialog(self.db, old_type_name=old_type, parent=self.main_window)
        if dlg.exec():
            self._load_all()

    def _delete_diet_type(self):
        indexes = self.table_types.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите тип рациона для удаления.")
            return
        diet_type = self.model_types.item(indexes[0].row(), 0).text()
        reply = QMessageBox.question(
            self.main_window, "Подтверждение",
            f"Удалить тип «{diet_type}» и все входящие в него рационы?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            if self.db.delete_diet_type(diet_type):
                self._load_all()
            else:
                QMessageBox.critical(
                    self.main_window, "Ошибка",
                    "Нельзя удалить этот тип рациона, так как его рационы уже назначены животным в истории."
                )

    def _load_diets(self):
        self.all_diets = self.db.get_all_diets() or []
        self._filter_diets()

    def _filter_diets(self):
        type_filter = self.combo_type_filter.currentText()
        self.model_diets.clear()
        self.model_diets.setHorizontalHeaderLabels(["Номер рациона", "Название рациона", "Тип рациона"])

        for diet_id, diet_name, diet_type in self.all_diets:
            if type_filter and type_filter != "Все" and diet_type != type_filter:
                continue
            self.model_diets.appendRow([
                QStandardItem(str(diet_id)),
                QStandardItem(diet_name),
                QStandardItem(diet_type)
            ])

        self.table_diets.resizeColumnsToContents()
        self.table_diets.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def _add_diet(self):
        dlg = DietDialog(self.db, parent=self.main_window)
        if dlg.exec():
            self._load_all()

    def _edit_diet(self):
        indexes = self.table_diets.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите рацион для редактирования.")
            return
        diet_id = int(self.model_diets.item(indexes[0].row(), 0).text())
        dlg = DietDialog(self.db, diet_id=diet_id, parent=self.main_window)
        if dlg.exec():
            self._load_all()

    def _delete_diet(self):
        indexes = self.table_diets.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите рацион для удаления.")
            return
        diet_id = int(self.model_diets.item(indexes[0].row(), 0).text())
        if QMessageBox.question(self.main_window, "Удаление", "Удалить выбранный рацион?") == QMessageBox.Yes:
            if self.db.delete_diet(diet_id):
                self._load_all()
            else:
                QMessageBox.critical(
                    self.main_window, "Ошибка",
                    "Не удалось удалить рацион (он используется в истории кормления животных)."
                )

    def _load_history(self):
        rows = self.db.get_diet_history() or []
        self.model_history.clear()
        self.model_history.setHorizontalHeaderLabels([
            "ID записи", "ID питомца", "Питомец", "№ рациона", "Рацион", "Тип", "Дата начала", "Дата окончания"
        ])
        for r in rows:
            history_id, anim_id, anim_name, diet_id, diet_name, diet_type, start_d, end_d = r
            self.model_history.appendRow([
                QStandardItem(str(history_id)),
                QStandardItem(str(anim_id)),
                QStandardItem(anim_name),
                QStandardItem(str(diet_id)),
                QStandardItem(diet_name),
                QStandardItem(diet_type),
                QStandardItem(start_d.strftime("%d.%m.%Y") if start_d else ""),
                QStandardItem(end_d.strftime("%d.%m.%Y") if end_d else "Активен")
            ])
        self.table_history.resizeColumnsToContents()
        self.table_history.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

    def _assign_diet(self):
        dlg = AssignDietDialog(self.db, parent=self.main_window)
        if dlg.exec():
            self._load_history()

    def _edit_diet_history(self):
        indexes = self.table_history.selectionModel().selectedRows()
        if not indexes:
            return
        history_id = int(self.model_history.item(indexes[0].row(), 0).text())
        dlg = AssignDietDialog(self.db, history_id=history_id, parent=self.main_window)
        if dlg.exec():
            self._load_history()

    def _finish_or_delete_diet_history(self):
        indexes = self.table_history.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите запись в таблице.")
            return
        row = indexes[0].row()
        history_id = int(self.model_history.item(row, 0).text())
        status = self.model_history.item(row, 7).text()

        msg = QMessageBox(self.main_window)
        msg.setWindowTitle("Действие с назначением")
        msg.setText("Что вы хотите сделать с выбранной записью о рационе питомца?")
        btn_finish = msg.addButton("Завершить сегодняшней датой", QMessageBox.AcceptRole)
        btn_edit = msg.addButton("Редактировать", QMessageBox.ActionRole)
        btn_delete = msg.addButton("Удалить запись совсем", QMessageBox.DestructiveRole)
        msg.addButton("Отмена", QMessageBox.RejectRole)
        msg.exec()

        clicked = msg.clickedButton()
        if clicked == btn_finish:
            if status != "Активен":
                QMessageBox.information(self.main_window, "Информация", "Этот рацион уже завершён.")
                return
            if self.db.finish_current_diet(history_id, datetime.now().date()):
                self._load_history()
        elif clicked == btn_edit:
            dlg = AssignDietDialog(self.db, history_id=history_id, parent=self.main_window)
            if dlg.exec():
                self._load_history()
        elif clicked == btn_delete:
            if self.db.delete_diet_history(history_id):
                self._load_history()