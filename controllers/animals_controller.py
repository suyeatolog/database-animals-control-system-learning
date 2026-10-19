from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QMainWindow, QMessageBox

from db.db_manager import DatabaseManager
from gui.dialogs.animal_dialog import AnimalDialog


class AnimalsController:
    def __init__(self, db: DatabaseManager, main_window: 'QMainWindow'):
        self.db = db
        self.main_window = main_window
        self.current_animal_id = None
        
        # Берём виджеты из главного окна (они уже созданы через setupUi)
        self.combo_type = main_window.comboAnimalType
        self.edit_search = main_window.editAnimalSearch
        self.table = main_window.tableAnimals
        self.btn_add = main_window.btnAddAnimal
        self.btn_edit = main_window.btnSecondary  # ← в .ui файле это "Редактировать"
        self.btn_delete = main_window.btnDelete
        
        # Создаём модель для таблицы
        self.model = QStandardItemModel()
        self.table.setModel(self.model)
        
        # Подключаем сигналы
        self.combo_type.currentTextChanged.connect(self._filter_data)
        self.edit_search.textChanged.connect(self._filter_data)
        self.table.selectionModel().selectionChanged.connect(self._on_selection_changed)
        self.btn_add.clicked.connect(self._on_add)
        self.btn_edit.clicked.connect(self._on_edit)
        self.btn_delete.clicked.connect(self._on_delete)
        
        # Загружаем данные
        self.all_data = []
        self._load_data()
    
    def _load_data(self):
        self.all_data = self.db.get_all_animals()
        self._filter_data()
    
    def _filter_data(self):
        type_filter = self.combo_type.currentText()
        name_filter = self.edit_search.text().lower()
        
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "ID", "Имя", "Дата рождения", "Пол", "Тип", "Зона", "Смотритель", "Ветеринар"
        ])
        
        for row in self.all_data:
            animal_id, name, birth_date, gender, animal_type, zone, keeper, vet = row
            
            # Фильтр по типу
            if type_filter != "Все":
                type_map = {"Птицы": "Птица", "Рептилии": "Рептилия", "Млекопитающие": "Млекопитающее"}
                if animal_type != type_map.get(type_filter):
                    continue
            
            # Фильтр по имени
            if name_filter and name_filter not in name.lower():
                continue
            
            date_str = birth_date.strftime("%d.%m.%Y") if birth_date else ""
            
            items = [
                QStandardItem(str(animal_id)),
                QStandardItem(name),
                QStandardItem(date_str),
                QStandardItem(gender),
                QStandardItem(animal_type),
                QStandardItem(zone),
                QStandardItem(keeper),
                QStandardItem(vet)
            ]
            self.model.appendRow(items)
        
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    
    def _on_selection_changed(self):
        indexes = self.table.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            self.current_animal_id = int(self.model.item(row, 0).text())
        else:
            self.current_animal_id = None
    
    def _on_add(self):
        dialog = AnimalDialog(self.db, parent=self.main_window)
        if dialog.exec():
            self._load_data()
    
    def _on_edit(self):
        if not self.current_animal_id:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите животное для редактирования.")
            return
        dialog = AnimalDialog(self.db, animal_id=self.current_animal_id, parent=self.main_window)
        if dialog.exec():
            self._load_data()
    
    def _on_delete(self):
        if not self.current_animal_id:
            QMessageBox.warning(self.main_window, "Внимание", "Выберите животное для удаления.")
            return
        
        reply = QMessageBox.question(
            self.main_window, "Подтверждение",
            "Вы уверены, что хотите удалить это животное?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if self.db.delete_animal(self.current_animal_id):
                QMessageBox.information(self.main_window, "Успех", "Животное удалено.")
                self._load_data()
            else:
                QMessageBox.critical(self.main_window, "Ошибка", "Не удалось удалить животное.")