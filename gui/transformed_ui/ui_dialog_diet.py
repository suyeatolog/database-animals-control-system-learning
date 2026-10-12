# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_diet.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_DialogDiet(object):
    def setupUi(self, DialogDiet):
        if not DialogDiet.objectName():
            DialogDiet.setObjectName(u"DialogDiet")
        DialogDiet.resize(480, 380)
        self.mainLayout = QVBoxLayout(DialogDiet)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 24, 28, 24)
        self.labelTitle = QLabel(DialogDiet)
        self.labelTitle.setObjectName(u"labelTitle")

        self.mainLayout.addWidget(self.labelTitle)

        self.groupBox = QGroupBox(DialogDiet)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.editDietId = QLineEdit(self.groupBox)
        self.editDietId.setObjectName(u"editDietId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editDietId)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.editDietName = QLineEdit(self.groupBox)
        self.editDietName.setObjectName(u"editDietName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editDietName)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label2)

        self.comboDietType = QComboBox(self.groupBox)
        self.comboDietType.setObjectName(u"comboDietType")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboDietType)


        self.mainLayout.addWidget(self.groupBox)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mainLayout.addItem(self.spacerItem)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(12)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem1)

        self.btnCancel = QPushButton(DialogDiet)
        self.btnCancel.setObjectName(u"btnCancel")

        self.hboxLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(DialogDiet)
        self.btnSave.setObjectName(u"btnSave")

        self.hboxLayout.addWidget(self.btnSave)


        self.mainLayout.addLayout(self.hboxLayout)


        self.retranslateUi(DialogDiet)

        QMetaObject.connectSlotsByName(DialogDiet)
    # setupUi

    def retranslateUi(self, DialogDiet):
        DialogDiet.setWindowTitle(QCoreApplication.translate("DialogDiet", u"\u0420\u0430\u0446\u0438\u043e\u043d \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        DialogDiet.setStyleSheet(QCoreApplication.translate("DialogDiet", u"\n"
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
"    QLineEdit, QComboBox {\n"
"        background-color: #FFFFFF;\n"
"        color: #1A202C;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 6px;\n"
"        padding: 8px 12px;\n"
"        font-size: 13px;\n"
"    }\n"
"    QLineEdit:focus, QComboBox:focus {\n"
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
"        background-color: #FFFFFF;\n"
"        bor"
                        "der: 1px solid #E2E8F0;\n"
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
"        font-weight: 500;\n"
"    }\n"
"    QPushButton#btnCancel:ho"
                        "ver { background-color: #F7FAFC; border-color: #CBD5E0; }\n"
"   ", None))
        self.labelTitle.setText(QCoreApplication.translate("DialogDiet", u"\u0420\u0430\u0446\u0438\u043e\u043d \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.labelTitle.setObjectName(QCoreApplication.translate("DialogDiet", u"dialogTitle", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogDiet", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0440\u0430\u0446\u0438\u043e\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("DialogDiet", u"\u041d\u043e\u043c\u0435\u0440 \u0440\u0430\u0446\u0438\u043e\u043d\u0430", None))
        self.editDietId.setPlaceholderText(QCoreApplication.translate("DialogDiet", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.label1.setText(QCoreApplication.translate("DialogDiet", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.editDietName.setPlaceholderText(QCoreApplication.translate("DialogDiet", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \u0420\u0430\u0446\u0438\u043e\u043d \u21165", None))
        self.label2.setText(QCoreApplication.translate("DialogDiet", u"\u0422\u0438\u043f \u0440\u0430\u0446\u0438\u043e\u043d\u0430", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogDiet", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btnCancel.setObjectName(QCoreApplication.translate("DialogDiet", u"btnCancel", None))
        self.btnSave.setText(QCoreApplication.translate("DialogDiet", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btnSave.setObjectName(QCoreApplication.translate("DialogDiet", u"btnSave", None))
    # retranslateUi

