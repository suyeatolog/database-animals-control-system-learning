from datetime import datetime

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QMessageBox

from db.db_manager import DatabaseManager


class ReportsController:
    def __init__(self, db: DatabaseManager, main_window):
        self.db = db
        self.main_window = main_window

        self.combo_r1_type = main_window.comboReport1Type
        self.combo_r1_name = main_window.comboReport1Name
        self.btn_r1_search = main_window.btnReport1Search
        self.text_r1 = main_window.textReport1

        self.combo_r1_type.currentTextChanged.connect(self._update_r1_names)
        self.btn_r1_search.clicked.connect(self._load_report1)

        self.btn_r2_load = main_window.btnReport2Load
        self.table_r2 = main_window.tableReport2
        self.model_r2 = QStandardItemModel()
        self.table_r2.setModel(self.model_r2)
        self.btn_r2_load.clicked.connect(self._load_report2)

        self.edit_r3_date = main_window.editReport3Date
        self.btn_r3_load = main_window.btnReport3Load
        self.table_r3 = main_window.tableReport3
        self.model_r3 = QStandardItemModel()
        self.table_r3.setModel(self.model_r3)

        self.edit_r3_date.setText(datetime.now().strftime("%d.%m.%Y"))
        self.btn_r3_load.clicked.connect(self._load_report3)

        self._update_r1_names()
        self._load_report2()
        self._load_report3()

    def _map_type(self, ui_type_text):
        return {
            "Птицы": "Птица",
            "Рептилии": "Рептилия",
            "Млекопитающие": "Млекопитающее"
        }.get(ui_type_text, ui_type_text)

    def _update_r1_names(self):
        target_type = self._map_type(self.combo_r1_type.currentText())
        animals = self.db.get_all_animals() or []
        self.combo_r1_name.clear()
        for row in animals:
            if row[4] == target_type:
                self.combo_r1_name.addItem(row[1])

    def _load_report1(self):
        animal_type = self._map_type(self.combo_r1_type.currentText())
        name = self.combo_r1_name.currentText().strip()
        if not name:
            QMessageBox.warning(self.main_window, "Внимание", "Укажите имя питомца.")
            return

        rows = self.db.get_full_animal_report(animal_type, name)
        if not rows:
            self.text_r1.setHtml("<h3>Питомец с таким типом и именем не найден.</h3>")
            return

        html_parts = []
        for r in rows:
            (anim_id, a_name, b_date, gender, a_type,
             z_name, z_desc, k_name, k_phone, v_name, v_phone,
             d_id, d_name, d_type) = r

            extra_html = ""
            if a_type == "Птица":
                b = self.db.get_bird_details(anim_id)
                if b:
                    extra_html = f"""
                    <h4>Сведения о зимовке (Птица):</h4>
                    <ul>
                        <li><b>Страна зимовки:</b> {b[1] or '—'} (Код: {b[0] or '—'})</li>
                        <li><b>Дата улёта:</b> {b[2].strftime('%d.%m.%Y') if b[2] else '—'}</li>
                        <li><b>Дата прилёта:</b> {b[3].strftime('%d.%m.%Y') if b[3] else '—'}</li>
                    </ul>
                    """
            elif a_type == "Рептилия":
                rep = self.db.get_reptile_details(anim_id)
                if rep:
                    extra_html = f"""
                    <h4>Особенности рептилии:</h4>
                    <ul>
                        <li><b>Нормальная температура:</b> {rep[0]} °C</li>
                        <li><b>Сроки зимней спячки:</b> с {rep[1].strftime('%d.%m.%Y') if rep[1] else '—'} по {rep[2].strftime('%d.%m.%Y') if rep[2] else '—'}</li>
                    </ul>
                    """

            diet_hist = self.db.get_animal_diet_history_list(anim_id) or []
            if diet_hist:
                hist_items = "".join([
                    f"<li>№{dh[0]} «{dh[1]}» ({dh[2]}) — с {dh[3].strftime('%d.%m.%Y')} "
                    f"по {dh[4].strftime('%d.%m.%Y') if dh[4] else 'наст. время'}</li>"
                    for dh in diet_hist
                ])
                hist_html = f"<h4>История рационов питания:</h4><ul>{hist_items}</ul>"
            else:
                hist_html = "<p><i>История рационов отсутствует.</i></p>"

            diet_str = f"№{d_id} «{d_name}» ({d_type})" if d_id else "Не назначен"
            html_parts.append(f"""
                <h2>Карточка питомца: {a_name} (Уникальный №: {anim_id})</h2>
                <p><b>Тип:</b> {a_type} | <b>Пол:</b> {gender} | <b>Дата рождения:</b> {b_date.strftime('%d.%m.%Y') if b_date else '—'}</p>
                <p><b>Зона обитания:</b> {z_name} <i>({z_desc or 'без описания'})</i></p>
                <p><b>Текущий рацион:</b> {diet_str}</p>
                <p><b>Смотритель:</b> {k_name} (тел: {k_phone or '—'})</p>
                <p><b>Ветеринар:</b> {v_name} (тел: {v_phone or '—'})</p>
                {extra_html}
                {hist_html}
                <hr>
            """)

        self.text_r1.setHtml("".join(html_parts))

    def _load_report2(self):
        rows = self.db.get_married_couples_report() or []
        self.model_r2.clear()
        self.model_r2.setHorizontalHeaderLabels([
            "Супруг 1 (ФИО)", "Дата рожд. 1", "Телефон 1", "Должность 1",
            "Супруг 2 (ФИО)", "Дата рожд. 2", "Телефон 2", "Должность 2"
        ])
        for r in rows:
            n1, b1, p1, r1, n2, b2, p2, r2 = r
            self.model_r2.appendRow([
                QStandardItem(n1),
                QStandardItem(b1.strftime("%d.%m.%Y") if b1 else ""),
                QStandardItem(p1 or ""),
                QStandardItem(r1),
                QStandardItem(n2),
                QStandardItem(b2.strftime("%d.%m.%Y") if b2 else ""),
                QStandardItem(p2 or ""),
                QStandardItem(r2),
            ])
        self.table_r2.resizeColumnsToContents()
        self.table_r2.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_r2.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

    def _load_report3(self):
        date_str = self.edit_r3_date.text().strip()
        try:
            target_date = datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            QMessageBox.warning(self.main_window, "Ошибка", "Введите корректную дату в формате дд.мм.гггг")
            return

        rows = self.db.get_animals_diets_on_date(target_date) or []
        self.model_r3.clear()
        self.model_r3.setHorizontalHeaderLabels([
            "ID питомца", "Имя питомца", "Тип", "Номер рациона", "Название рациона", "Тип рациона"
        ])
        for r in rows:
            anim_id, name, a_type, d_id, d_name, dt_name, _, _ = r
            self.model_r3.appendRow([
                QStandardItem(str(anim_id)),
                QStandardItem(name),
                QStandardItem(a_type),
                QStandardItem(str(d_id) if d_id else "Не назначен"),
                QStandardItem(d_name or "—"),
                QStandardItem(dt_name or "—"),
            ])
        self.table_r3.resizeColumnsToContents()
        self.table_r3.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)