from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

from db.db_manager import DatabaseManager
from gui.transformed_ui.ui_dialog_animal import Ui_DialogAnimal


class AnimalDialog(QDialog, Ui_DialogAnimal):
    def __init__(self, db: DatabaseManager, animal_id=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        for date_widget in (
            self.dateBirth,
            self.dateBirdDeparture,
            self.dateBirdArrival,
            self.dateReptileHibernStart,
            self.dateReptileHibernEnd,
        ):
            date_widget.setCalendarPopup(False)
            date_widget.setDisplayFormat("dd.MM.yyyy")

        self.editAnimalId.setReadOnly(True)
        self.db = db
        self.animal_id = animal_id

        self.comboAnimalType.currentTextChanged.connect(self._on_type_changed)
        self.btnSave.clicked.connect(self._on_save)
        self.btnCancel.clicked.connect(self.reject)

        self._load_data()

        self._on_type_changed(self.comboAnimalType.currentText())

    def _load_data(self):
        zones = self.db.get_all_zones() or []
        self.comboZone.clear()
        for zone_id, zone_name in zones:
            self.comboZone.addItem(zone_name, zone_id)

        keepers = self.db.get_keepers() or []
        self.comboKeeper.clear()
        for keeper_id, keeper_name in keepers:
            self.comboKeeper.addItem(keeper_name, keeper_id)

        vets = self.db.get_vets() or []
        self.comboVet.clear()
        for vet_id, vet_name in vets:
            self.comboVet.addItem(vet_name, vet_id)

        if self.animal_id:
            animal = self.db.get_animal_by_id(self.animal_id)
            if animal:
                self.editAnimalId.setText(str(animal[0]))
                self.editAnimalName.setText(animal[1])
                if animal[2]:
                    self.dateBirth.setDate(QDate(animal[2].year, animal[2].month, animal[2].day))
                self.comboGender.setCurrentText(animal[3])
                self.comboAnimalType.setCurrentText(animal[4])

                for i in range(self.comboZone.count()):
                    if self.comboZone.itemData(i) == animal[5]:
                        self.comboZone.setCurrentIndex(i)
                        break

                for i in range(self.comboKeeper.count()):
                    if self.comboKeeper.itemData(i) == animal[6]:
                        self.comboKeeper.setCurrentIndex(i)
                        break

                for i in range(self.comboVet.count()):
                    if self.comboVet.itemData(i) == animal[7]:
                        self.comboVet.setCurrentIndex(i)
                        break

                if animal[4] == "Птица":
                    bird = self.db.get_bird_details(self.animal_id)
                    if bird:
                        self.editBirdCountryCode.setText(bird[0] or "")
                        self.editBirdCountryName.setText(bird[1] or "")
                        if bird[2]:
                            self.dateBirdDeparture.setDate(QDate(bird[2].year, bird[2].month, bird[2].day))
                        if bird[3]:
                            self.dateBirdArrival.setDate(QDate(bird[3].year, bird[3].month, bird[3].day))
                elif animal[4] == "Рептилия":
                    reptile = self.db.get_reptile_details(self.animal_id)
                    if reptile:
                        self.spinReptileTemp.setValue(float(reptile[0]))
                        if reptile[1]:
                            self.dateReptileHibernStart.setDate(QDate(reptile[1].year, reptile[1].month, reptile[1].day))
                        if reptile[2]:
                            self.dateReptileHibernEnd.setDate(QDate(reptile[2].year, reptile[2].month, reptile[2].day))

    def _on_type_changed(self, type_name):
        if type_name == "Птица":
            self.stackDetails.setCurrentIndex(0)
        elif type_name == "Рептилия":
            self.stackDetails.setCurrentIndex(1)
        else:
            self.stackDetails.setCurrentIndex(2)

    def _on_save(self):
        name = self.editAnimalName.text().strip()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите имя питомца.")
            return

        zone_id = self.comboZone.currentData()
        keeper_id = self.comboKeeper.currentData()
        vet_id = self.comboVet.currentData()

        if not zone_id or not keeper_id or not vet_id:
            QMessageBox.warning(self, "Ошибка", "Заполните все обязательные поля.")
            return

        birth_date = self.dateBirth.date().toPython()
        animal_type = self.comboAnimalType.currentText()
        gender = self.comboGender.currentText()

        if self.animal_id:
            self.db.update_animal(
                self.animal_id, name, birth_date, gender, animal_type,
                zone_id, keeper_id, vet_id
            )
            if animal_type == "Птица":
                country_code = self.editBirdCountryCode.text().strip() or None
                country_name = self.editBirdCountryName.text().strip() or None
                departure = self.dateBirdDeparture.date().toPython() if self.dateBirdDeparture.date().isValid() else None
                arrival = self.dateBirdArrival.date().toPython() if self.dateBirdArrival.date().isValid() else None
                self.db.update_bird_details(self.animal_id, country_code, country_name, departure, arrival)
            elif animal_type == "Рептилия":
                temp = self.spinReptileTemp.value()
                hibern_start = self.dateReptileHibernStart.date().toPython() if self.dateReptileHibernStart.date().isValid() else None
                hibern_end = self.dateReptileHibernEnd.date().toPython() if self.dateReptileHibernEnd.date().isValid() else None
                self.db.update_reptile_details(self.animal_id, temp, hibern_start, hibern_end)
            else:
                self.db.clear_special_details(self.animal_id)

            QMessageBox.information(self, "Успех", "Данные обновлены.")
        else:
            new_id = self.db.add_animal(name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id)
            if new_id:
                if animal_type == "Птица":
                    country_code = self.editBirdCountryCode.text().strip() or None
                    country_name = self.editBirdCountryName.text().strip() or None
                    departure = self.dateBirdDeparture.date().toPython() if self.dateBirdDeparture.date().isValid() else None
                    arrival = self.dateBirdArrival.date().toPython() if self.dateBirdArrival.date().isValid() else None
                    self.db.add_bird_details(new_id, country_code, country_name, departure, arrival)
                elif animal_type == "Рептилия":
                    temp = self.spinReptileTemp.value()
                    hibern_start = self.dateReptileHibernStart.date().toPython() if self.dateReptileHibernStart.date().isValid() else None
                    hibern_end = self.dateReptileHibernEnd.date().toPython() if self.dateReptileHibernEnd.date().isValid() else None
                    self.db.add_reptile_details(new_id, temp, hibern_start, hibern_end)

                QMessageBox.information(self, "Успех", "Животное добавлено.")
            else:
                QMessageBox.critical(self, "Ошибка", "Не удалось добавить животное.")
                return

        self.accept()