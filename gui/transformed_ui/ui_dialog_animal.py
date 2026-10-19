# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_animal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QDoubleSpinBox, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from gui.transformed_ui.dialog_geometry import set_dialog_height

class Ui_DialogAnimal(object):
    def setupUi(self, DialogAnimal):
        if not DialogAnimal.objectName():
            DialogAnimal.setObjectName(u"DialogAnimal")
        DialogAnimal.resize(680, 880)
        DialogAnimal.setMinimumSize(QSize(680, 880))
        set_dialog_height(DialogAnimal)
        self.mainLayout = QVBoxLayout(DialogAnimal)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 24, 28, 24)
        self.groupGeneral = QGroupBox(DialogAnimal)
        self.groupGeneral.setObjectName(u"groupGeneral")
        self.groupGeneral.setMinimumSize(QSize(0, 450))
        self.formGeneral = QFormLayout(self.groupGeneral)
        self.formGeneral.setObjectName(u"formGeneral")
        self.formGeneral.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formGeneral.setHorizontalSpacing(16)
        self.formGeneral.setVerticalSpacing(12)
        self.label = QLabel(self.groupGeneral)
        self.label.setObjectName(u"label")

        self.formGeneral.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.editAnimalId = QLineEdit(self.groupGeneral)
        self.editAnimalId.setObjectName(u"editAnimalId")

        self.formGeneral.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editAnimalId)

        self.label1 = QLabel(self.groupGeneral)
        self.label1.setObjectName(u"label1")

        self.formGeneral.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.editAnimalName = QLineEdit(self.groupGeneral)
        self.editAnimalName.setObjectName(u"editAnimalName")

        self.formGeneral.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editAnimalName)

        self.label2 = QLabel(self.groupGeneral)
        self.label2.setObjectName(u"label2")

        self.formGeneral.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label2)

        self.dateBirth = QDateEdit(self.groupGeneral)
        self.dateBirth.setObjectName(u"dateBirth")
        self.dateBirth.setCalendarPopup(False)

        self.formGeneral.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateBirth)

        self.label3 = QLabel(self.groupGeneral)
        self.label3.setObjectName(u"label3")

        self.formGeneral.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label3)

        self.comboGender = QComboBox(self.groupGeneral)
        self.comboGender.addItem("")
        self.comboGender.addItem("")
        self.comboGender.setObjectName(u"comboGender")

        self.formGeneral.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboGender)

        self.label4 = QLabel(self.groupGeneral)
        self.label4.setObjectName(u"label4")

        self.formGeneral.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label4)

        self.comboAnimalType = QComboBox(self.groupGeneral)
        self.comboAnimalType.addItem("")
        self.comboAnimalType.addItem("")
        self.comboAnimalType.addItem("")
        self.comboAnimalType.setObjectName(u"comboAnimalType")

        self.formGeneral.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboAnimalType)

        self.label5 = QLabel(self.groupGeneral)
        self.label5.setObjectName(u"label5")

        self.formGeneral.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label5)

        self.comboZone = QComboBox(self.groupGeneral)
        self.comboZone.setObjectName(u"comboZone")

        self.formGeneral.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboZone)

        self.label6 = QLabel(self.groupGeneral)
        self.label6.setObjectName(u"label6")

        self.formGeneral.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label6)

        self.comboKeeper = QComboBox(self.groupGeneral)
        self.comboKeeper.setObjectName(u"comboKeeper")

        self.formGeneral.setWidget(6, QFormLayout.ItemRole.FieldRole, self.comboKeeper)

        self.label7 = QLabel(self.groupGeneral)
        self.label7.setObjectName(u"label7")

        self.formGeneral.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label7)

        self.comboVet = QComboBox(self.groupGeneral)
        self.comboVet.setObjectName(u"comboVet")

        self.formGeneral.setWidget(7, QFormLayout.ItemRole.FieldRole, self.comboVet)


        self.mainLayout.addWidget(self.groupGeneral)

        self.stackDetails = QStackedWidget(DialogAnimal)
        self.stackDetails.setObjectName(u"stackDetails")
        self.pageBird = QWidget()
        self.pageBird.setObjectName(u"pageBird")
        self.vboxLayout = QVBoxLayout(self.pageBird)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.pageBird)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setVerticalSpacing(12)
        self.label8 = QLabel(self.groupBox)
        self.label8.setObjectName(u"label8")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label8)

        self.editBirdCountryCode = QLineEdit(self.groupBox)
        self.editBirdCountryCode.setObjectName(u"editBirdCountryCode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editBirdCountryCode)

        self.label9 = QLabel(self.groupBox)
        self.label9.setObjectName(u"label9")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label9)

        self.editBirdCountryName = QLineEdit(self.groupBox)
        self.editBirdCountryName.setObjectName(u"editBirdCountryName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editBirdCountryName)

        self.label10 = QLabel(self.groupBox)
        self.label10.setObjectName(u"label10")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label10)

        self.dateBirdDeparture = QDateEdit(self.groupBox)
        self.dateBirdDeparture.setObjectName(u"dateBirdDeparture")
        self.dateBirdDeparture.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateBirdDeparture)

        self.label11 = QLabel(self.groupBox)
        self.label11.setObjectName(u"label11")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label11)

        self.dateBirdArrival = QDateEdit(self.groupBox)
        self.dateBirdArrival.setObjectName(u"dateBirdArrival")
        self.dateBirdArrival.setCalendarPopup(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateBirdArrival)


        self.vboxLayout.addWidget(self.groupBox)

        self.stackDetails.addWidget(self.pageBird)
        self.pageReptile = QWidget()
        self.pageReptile.setObjectName(u"pageReptile")
        self.vboxLayout1 = QVBoxLayout(self.pageReptile)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.vboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.groupBox1 = QGroupBox(self.pageReptile)
        self.groupBox1.setObjectName(u"groupBox1")
        self.formLayout1 = QFormLayout(self.groupBox1)
        self.formLayout1.setObjectName(u"formLayout1")
        self.formLayout1.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout1.setHorizontalSpacing(16)
        self.formLayout1.setVerticalSpacing(12)
        self.label12 = QLabel(self.groupBox1)
        self.label12.setObjectName(u"label12")

        self.formLayout1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label12)

        self.spinReptileTemp = QDoubleSpinBox(self.groupBox1)
        self.spinReptileTemp.setObjectName(u"spinReptileTemp")
        self.spinReptileTemp.setMinimum(10.000000000000000)
        self.spinReptileTemp.setMaximum(50.000000000000000)
        self.spinReptileTemp.setSingleStep(0.500000000000000)
        self.spinReptileTemp.setValue(28.000000000000000)

        self.formLayout1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinReptileTemp)

        self.label13 = QLabel(self.groupBox1)
        self.label13.setObjectName(u"label13")

        self.formLayout1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label13)

        self.dateReptileHibernStart = QDateEdit(self.groupBox1)
        self.dateReptileHibernStart.setObjectName(u"dateReptileHibernStart")
        self.dateReptileHibernStart.setCalendarPopup(False)

        self.formLayout1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateReptileHibernStart)

        self.label14 = QLabel(self.groupBox1)
        self.label14.setObjectName(u"label14")

        self.formLayout1.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label14)

        self.dateReptileHibernEnd = QDateEdit(self.groupBox1)
        self.dateReptileHibernEnd.setObjectName(u"dateReptileHibernEnd")
        self.dateReptileHibernEnd.setCalendarPopup(False)

        self.formLayout1.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateReptileHibernEnd)


        self.vboxLayout1.addWidget(self.groupBox1)

        self.stackDetails.addWidget(self.pageReptile)
        self.pageEmpty = QWidget()
        self.pageEmpty.setObjectName(u"pageEmpty")
        self.vboxLayout2 = QVBoxLayout(self.pageEmpty)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.label15 = QLabel(self.pageEmpty)
        self.label15.setObjectName(u"label15")
        self.label15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.label15)

        self.stackDetails.addWidget(self.pageEmpty)

        self.mainLayout.addWidget(self.stackDetails)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.spacerItem)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(12)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout.addItem(self.spacerItem1)

        self.btnCancel = QPushButton(DialogAnimal)
        self.btnCancel.setObjectName(u"btnCancel")

        self.hboxLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(DialogAnimal)
        self.btnSave.setObjectName(u"btnSave")

        self.hboxLayout.addWidget(self.btnSave)


        self.mainLayout.addLayout(self.hboxLayout)


        self.retranslateUi(DialogAnimal)

        QMetaObject.connectSlotsByName(DialogAnimal)
    # setupUi

    def retranslateUi(self, DialogAnimal):
        DialogAnimal.setWindowTitle(QCoreApplication.translate("DialogAnimal", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0438\u0442\u043e\u043c\u0446\u0430", None))
        DialogAnimal.setStyleSheet(QCoreApplication.translate("DialogAnimal", u"\n"
"    QDialog {\n"
"        background-color: #F4F6F8;\n"
"        font-family: \"Segoe UI\", \"Inter\", \"Roboto\", sans-serif;\n"
"    }\n"
"    QLabel { font-size: 13px; color: #2D3748; }\n"
"    QLabel#dialogTitle {\n"
"        font-size: 22px;\n"
"        font-weight: 600;\n"
"        color: #1A202C;\n"
"    }\n"
"    QLineEdit, QComboBox, QDateEdit, QDoubleSpinBox {\n"
"        background-color: #FFFFFF;\n"
"        color: #1A202C;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 6px;\n"
"        padding: 8px 12px;\n"
"        font-size: 13px;\n"
"    }\n"
"    QLineEdit:focus, QComboBox:focus, QDateEdit:focus {\n"
"        border: 1px solid #2C5282;\n"
"    }\n"
"    QComboBox::drop-down { border: none; width: 24px; }\n"
"    QComboBox QAbstractItemView {\n"
"        background-color: #FFFFFF;\n"
"        border: 1px solid #E2E8F0;\n"
"        selection-background-color: #EBF4FF;\n"
"        selection-color: #2C5282;\n"
"        outline: none;\n"
"    }\n"
"    QGroupBox {\n"
"      "
                        "  background-color: #FFFFFF;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 8px;\n"
"        margin-top: 14px;\n"
"        padding: 22px 18px 18px 18px;\n"
"        font-size: 14px;\n"
"        font-weight: 600;\n"
"        color: #1A202C;\n"
"    }\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        subcontrol-position: top left;\n"
"        padding: 0 10px;\n"
"        color: #2C5282;\n"
"    }\n"
"    QPushButton#btnSave {\n"
"        background-color: #38A169;\n"
"        color: #FFFFFF;\n"
"        border: none;\n"
"        border-radius: 6px;\n"
"        padding: 10px 28px;\n"
"        font-size: 13px;\n"
"        font-weight: 500;\n"
"    }\n"
"    QPushButton#btnSave:hover { background-color: #48BB78; }\n"
"    QPushButton#btnCancel {\n"
"        background-color: #FFFFFF;\n"
"        color: #2D3748;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 6px;\n"
"        padding: 10px 28px;\n"
"        font-size: 13px;\n"
"        font-weight: 500"
                        ";\n"
"    }\n"
"    QPushButton#btnCancel:hover { background-color: #F7FAFC; border-color: #CBD5E0; }\n"
"   ", None))
        self.groupGeneral.setTitle(QCoreApplication.translate("DialogAnimal", u"\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("DialogAnimal", u"\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.editAnimalId.setPlaceholderText(QCoreApplication.translate("DialogAnimal", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.label1.setText(QCoreApplication.translate("DialogAnimal", u"\u0418\u043c\u044f", None))
        self.label2.setText(QCoreApplication.translate("DialogAnimal", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.dateBirth.setDisplayFormat(QCoreApplication.translate("DialogAnimal", u"dd.MM.yyyy", None))
        self.label3.setText(QCoreApplication.translate("DialogAnimal", u"\u041f\u043e\u043b", None))
        self.comboGender.setItemText(0, QCoreApplication.translate("DialogAnimal", u"\u0421\u0430\u043c\u0435\u0446", None))
        self.comboGender.setItemText(1, QCoreApplication.translate("DialogAnimal", u"\u0421\u0430\u043c\u043a\u0430", None))

        self.label4.setText(QCoreApplication.translate("DialogAnimal", u"\u0422\u0438\u043f \u0436\u0438\u0432\u043e\u0442\u043d\u043e\u0433\u043e", None))
        self.comboAnimalType.setItemText(0, QCoreApplication.translate("DialogAnimal", u"\u041f\u0442\u0438\u0446\u0430", None))
        self.comboAnimalType.setItemText(1, QCoreApplication.translate("DialogAnimal", u"\u0420\u0435\u043f\u0442\u0438\u043b\u0438\u044f", None))
        self.comboAnimalType.setItemText(2, QCoreApplication.translate("DialogAnimal", u"\u041c\u043b\u0435\u043a\u043e\u043f\u0438\u0442\u0430\u044e\u0449\u0435\u0435", None))

        self.label5.setText(QCoreApplication.translate("DialogAnimal", u"\u0417\u043e\u043d\u0430 \u043e\u0431\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.label6.setText(QCoreApplication.translate("DialogAnimal", u"\u0421\u043c\u043e\u0442\u0440\u0438\u0442\u0435\u043b\u044c", None))
        self.label7.setText(QCoreApplication.translate("DialogAnimal", u"\u0412\u0435\u0442\u0435\u0440\u0438\u043d\u0430\u0440", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogAnimal", u"\u0421\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0437\u0438\u043c\u043e\u0432\u043a\u0435", None))
        self.label8.setText(QCoreApplication.translate("DialogAnimal", u"\u041a\u043e\u0434 \u0441\u0442\u0440\u0430\u043d\u044b", None))
        self.editBirdCountryCode.setPlaceholderText(QCoreApplication.translate("DialogAnimal", u"RU, DE...", None))
        self.label9.setText(QCoreApplication.translate("DialogAnimal", u"\u0421\u0442\u0440\u0430\u043d\u0430 \u0437\u0438\u043c\u043e\u0432\u043a\u0438", None))
        self.label10.setText(QCoreApplication.translate("DialogAnimal", u"\u0414\u0430\u0442\u0430 \u0443\u043b\u0451\u0442\u0430", None))
        self.dateBirdDeparture.setDisplayFormat(QCoreApplication.translate("DialogAnimal", u"dd.MM.yyyy", None))
        self.label11.setText(QCoreApplication.translate("DialogAnimal", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u043b\u0451\u0442\u0430", None))
        self.dateBirdArrival.setDisplayFormat(QCoreApplication.translate("DialogAnimal", u"dd.MM.yyyy", None))
        self.groupBox1.setTitle(QCoreApplication.translate("DialogAnimal", u"\u041e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u043f\u0442\u0438\u043b\u0438\u0438", None))
        self.label12.setText(QCoreApplication.translate("DialogAnimal", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430, \u00b0C", None))
        self.label13.setText(QCoreApplication.translate("DialogAnimal", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0437\u0438\u043c\u043d\u0435\u0439 \u0441\u043f\u044f\u0447\u043a\u0438", None))
        self.dateReptileHibernStart.setDisplayFormat(QCoreApplication.translate("DialogAnimal", u"dd.MM.yyyy", None))
        self.label14.setText(QCoreApplication.translate("DialogAnimal", u"\u041a\u043e\u043d\u0435\u0446 \u0437\u0438\u043c\u043d\u0435\u0439 \u0441\u043f\u044f\u0447\u043a\u0438", None))
        self.dateReptileHibernEnd.setDisplayFormat(QCoreApplication.translate("DialogAnimal", u"dd.MM.yyyy", None))
        self.label15.setStyleSheet(QCoreApplication.translate("DialogAnimal", u"color: #718096; font-style: italic; font-size: 13px; padding: 24px;", None))
        self.label15.setText(QCoreApplication.translate("DialogAnimal", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u044e\u0442\u0441\u044f", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogAnimal", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btnSave.setText(QCoreApplication.translate("DialogAnimal", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi
