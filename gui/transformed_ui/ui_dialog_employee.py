# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_employee.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from gui.transformed_ui.dialog_geometry import set_dialog_height

class Ui_DialogEmployee(object):
    def setupUi(self, DialogEmployee):
        if not DialogEmployee.objectName():
            DialogEmployee.setObjectName(u"DialogEmployee")
        DialogEmployee.resize(540, 560)
        set_dialog_height(DialogEmployee)
        self.mainLayout = QVBoxLayout(DialogEmployee)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 24, 28, 24)
        self.labelTitle = QLabel(DialogEmployee)
        self.labelTitle.setObjectName(u"labelTitle")

        self.mainLayout.addWidget(self.labelTitle)

        self.groupBox = QGroupBox(DialogEmployee)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.editEmpId = QLineEdit(self.groupBox)
        self.editEmpId.setObjectName(u"editEmpId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editEmpId)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.editEmpName = QLineEdit(self.groupBox)
        self.editEmpName.setObjectName(u"editEmpName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editEmpName)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label2)

        self.dateEmpBirth = QDateEdit(self.groupBox)
        self.dateEmpBirth.setObjectName(u"dateEmpBirth")
        self.dateEmpBirth.setCalendarPopup(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEmpBirth)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label3)

        self.editEmpPhone = QLineEdit(self.groupBox)
        self.editEmpPhone.setObjectName(u"editEmpPhone")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editEmpPhone)

        self.label4 = QLabel(self.groupBox)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label4)

        self.comboMarital = QComboBox(self.groupBox)
        self.comboMarital.addItem("")
        self.comboMarital.addItem("")
        self.comboMarital.addItem("")
        self.comboMarital.setObjectName(u"comboMarital")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboMarital)

        self.label5 = QLabel(self.groupBox)
        self.label5.setObjectName(u"label5")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label5)

        self.comboRole = QComboBox(self.groupBox)
        self.comboRole.addItem("")
        self.comboRole.addItem("")
        self.comboRole.setObjectName(u"comboRole")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboRole)


        self.mainLayout.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(DialogEmployee)
        self.groupBox1.setObjectName(u"groupBox1")
        self.vboxLayout = QVBoxLayout(self.groupBox1)
        self.vboxLayout.setSpacing(12)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.checkHasSpouse = QCheckBox(self.groupBox1)
        self.checkHasSpouse.setObjectName(u"checkHasSpouse")

        self.vboxLayout.addWidget(self.checkHasSpouse)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(12)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label6 = QLabel(self.groupBox1)
        self.label6.setObjectName(u"label6")

        self.hboxLayout.addWidget(self.label6)

        self.comboSpouse = QComboBox(self.groupBox1)
        self.comboSpouse.setObjectName(u"comboSpouse")
        self.comboSpouse.setEnabled(False)

        self.hboxLayout.addWidget(self.comboSpouse)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.mainLayout.addWidget(self.groupBox1)

        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mainLayout.addItem(self.spacerItem1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(12)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.spacerItem2)

        self.btnCancel = QPushButton(DialogEmployee)
        self.btnCancel.setObjectName(u"btnCancel")

        self.hboxLayout1.addWidget(self.btnCancel)

        self.btnSave = QPushButton(DialogEmployee)
        self.btnSave.setObjectName(u"btnSave")

        self.hboxLayout1.addWidget(self.btnSave)


        self.mainLayout.addLayout(self.hboxLayout1)


        self.retranslateUi(DialogEmployee)
        self.checkHasSpouse.toggled.connect(self.comboSpouse.setEnabled)

        QMetaObject.connectSlotsByName(DialogEmployee)
    # setupUi

    def retranslateUi(self, DialogEmployee):
        DialogEmployee.setWindowTitle(QCoreApplication.translate("DialogEmployee", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        DialogEmployee.setStyleSheet(QCoreApplication.translate("DialogEmployee", u"\n"
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
"    QLineEdit, QComboBox, QDateEdit {\n"
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
"        background-col"
                        "or: #FFFFFF;\n"
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
"    QCheckBox {\n"
"        font-size: 13px;\n"
"        color: #2D3748;\n"
"        spacing: 8px;\n"
"    }\n"
"    QCheckBox::indicator {\n"
"        width: 16px;\n"
"        height: 16px;\n"
"        border: 1px solid #CBD5E0;\n"
"        border-radius: 3px;\n"
"        background-color: #FFFFFF;\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"        background-color: #2C5282;\n"
"        border-color: #2C5282;\n"
"    }\n"
"    QPushButton#btnSave {\n"
"        background-color: #38A169;\n"
"        color: #FFFFFF;\n"
"        border: none;\n"
"        border-radius: 6px;\n"
""
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
"        font-weight: 500;\n"
"    }\n"
"    QPushButton#btnCancel:hover { background-color: #F7FAFC; border-color: #CBD5E0; }\n"
"   ", None))
        self.labelTitle.setText(QCoreApplication.translate("DialogEmployee", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.labelTitle.setObjectName(QCoreApplication.translate("DialogEmployee", u"dialogTitle", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogEmployee", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label.setText(QCoreApplication.translate("DialogEmployee", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.editEmpId.setPlaceholderText(QCoreApplication.translate("DialogEmployee", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.label1.setText(QCoreApplication.translate("DialogEmployee", u"\u0424\u0418\u041e", None))
        self.label2.setText(QCoreApplication.translate("DialogEmployee", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.dateEmpBirth.setDisplayFormat(QCoreApplication.translate("DialogEmployee", u"dd.MM.yyyy", None))
        self.label3.setText(QCoreApplication.translate("DialogEmployee", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.editEmpPhone.setPlaceholderText(QCoreApplication.translate("DialogEmployee", u"+7 (___) ___-__-__", None))
        self.label4.setText(QCoreApplication.translate("DialogEmployee", u"\u0421\u0435\u043c\u0435\u0439\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.comboMarital.setItemText(0, QCoreApplication.translate("DialogEmployee", u"\u041d\u0435 \u0432 \u0431\u0440\u0430\u043a\u0435", None))
        self.comboMarital.setItemText(1, QCoreApplication.translate("DialogEmployee", u"\u0412 \u0431\u0440\u0430\u043a\u0435", None))
        self.comboMarital.setItemText(2, QCoreApplication.translate("DialogEmployee", u"\u0420\u0430\u0437\u0432\u0435\u0434\u0451\u043d(\u0430)", None))

        self.label5.setText(QCoreApplication.translate("DialogEmployee", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.comboRole.setItemText(0, QCoreApplication.translate("DialogEmployee", u"\u0421\u043c\u043e\u0442\u0440\u0438\u0442\u0435\u043b\u044c", None))
        self.comboRole.setItemText(1, QCoreApplication.translate("DialogEmployee", u"\u0412\u0435\u0442\u0435\u0440\u0438\u043d\u0430\u0440", None))

        self.groupBox1.setTitle(QCoreApplication.translate("DialogEmployee", u"\u0421\u0443\u043f\u0440\u0443\u0433(\u0430) \u0432 \u0437\u043e\u043e\u043f\u0430\u0440\u043a\u0435", None))
        self.checkHasSpouse.setText(QCoreApplication.translate("DialogEmployee", u"\u0421\u0443\u043f\u0440\u0443\u0433(\u0430) \u0442\u0430\u043a\u0436\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0432 \u0437\u043e\u043e\u043f\u0430\u0440\u043a\u0435", None))
        self.label6.setText(QCoreApplication.translate("DialogEmployee", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogEmployee", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btnCancel.setObjectName(QCoreApplication.translate("DialogEmployee", u"btnCancel", None))
        self.btnSave.setText(QCoreApplication.translate("DialogEmployee", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btnSave.setObjectName(QCoreApplication.translate("DialogEmployee", u"btnSave", None))
    # retranslateUi
