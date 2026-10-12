# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableView, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1483, 902)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.menuList = QListWidget(self.centralwidget)
        QListWidgetItem(self.menuList)
        QListWidgetItem(self.menuList)
        QListWidgetItem(self.menuList)
        QListWidgetItem(self.menuList)
        self.menuList.setObjectName(u"menuList")
        self.menuList.setMinimumSize(QSize(200, 0))
        self.menuList.setMaximumSize(QSize(200, 16777215))

        self.mainLayout.addWidget(self.menuList)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageAnimals = QWidget()
        self.pageAnimals.setObjectName(u"pageAnimals")
        self.layoutAnimals = QVBoxLayout(self.pageAnimals)
        self.layoutAnimals.setSpacing(16)
        self.layoutAnimals.setObjectName(u"layoutAnimals")
        self.layoutAnimals.setContentsMargins(32, 28, 32, 24)
        self.pageTitle = QLabel(self.pageAnimals)
        self.pageTitle.setObjectName(u"pageTitle")
        self.pageTitle.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.layoutAnimals.addWidget(self.pageTitle)

        self.layoutAnimalFilters = QHBoxLayout()
        self.layoutAnimalFilters.setSpacing(12)
        self.layoutAnimalFilters.setObjectName(u"layoutAnimalFilters")
        self.sectionLabel = QLabel(self.pageAnimals)
        self.sectionLabel.setObjectName(u"sectionLabel")
        self.sectionLabel.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.layoutAnimalFilters.addWidget(self.sectionLabel)

        self.comboAnimalType = QComboBox(self.pageAnimals)
        self.comboAnimalType.addItem("")
        self.comboAnimalType.addItem("")
        self.comboAnimalType.addItem("")
        self.comboAnimalType.addItem("")
        self.comboAnimalType.setObjectName(u"comboAnimalType")

        self.layoutAnimalFilters.addWidget(self.comboAnimalType)

        self.sectionLabel1 = QLabel(self.pageAnimals)
        self.sectionLabel1.setObjectName(u"sectionLabel1")
        self.sectionLabel1.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.layoutAnimalFilters.addWidget(self.sectionLabel1)

        self.editAnimalSearch = QLineEdit(self.pageAnimals)
        self.editAnimalSearch.setObjectName(u"editAnimalSearch")

        self.layoutAnimalFilters.addWidget(self.editAnimalSearch)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutAnimalFilters.addItem(self.spacerItem)

        self.btnAddAnimal = QPushButton(self.pageAnimals)
        self.btnAddAnimal.setObjectName(u"btnAddAnimal")

        self.layoutAnimalFilters.addWidget(self.btnAddAnimal)

        self.btnSecondary = QPushButton(self.pageAnimals)
        self.btnSecondary.setObjectName(u"btnSecondary")

        self.layoutAnimalFilters.addWidget(self.btnSecondary)

        self.btnDelete = QPushButton(self.pageAnimals)
        self.btnDelete.setObjectName(u"btnDelete")

        self.layoutAnimalFilters.addWidget(self.btnDelete)


        self.layoutAnimals.addLayout(self.layoutAnimalFilters)

        self.tableAnimals = QTableView(self.pageAnimals)
        self.tableAnimals.setObjectName(u"tableAnimals")
        self.tableAnimals.setMinimumSize(QSize(0, 650))
        self.tableAnimals.setAlternatingRowColors(True)
        self.tableAnimals.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableAnimals.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableAnimals.setShowGrid(False)

        self.layoutAnimals.addWidget(self.tableAnimals)

        self.stackedWidget.addWidget(self.pageAnimals)
        self.pageDiets = QWidget()
        self.pageDiets.setObjectName(u"pageDiets")
        self.layoutDiets = QVBoxLayout(self.pageDiets)
        self.layoutDiets.setSpacing(16)
        self.layoutDiets.setObjectName(u"layoutDiets")
        self.layoutDiets.setContentsMargins(32, 28, 32, 24)
        self.pageTitle1 = QLabel(self.pageDiets)
        self.pageTitle1.setObjectName(u"pageTitle1")
        self.pageTitle1.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.layoutDiets.addWidget(self.pageTitle1)

        self.tabDiets = QTabWidget(self.pageDiets)
        self.tabDiets.setObjectName(u"tabDiets")
        self.tabDietTypes = QWidget()
        self.tabDietTypes.setObjectName(u"tabDietTypes")
        self.vboxLayout = QVBoxLayout(self.tabDietTypes)
        self.vboxLayout.setSpacing(12)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout.addItem(self.spacerItem1)

        self.btnAddDietType = QPushButton(self.tabDietTypes)
        self.btnAddDietType.setObjectName(u"btnAddDietType")

        self.hboxLayout.addWidget(self.btnAddDietType)

        self.btnSecondary1 = QPushButton(self.tabDietTypes)
        self.btnSecondary1.setObjectName(u"btnSecondary1")

        self.hboxLayout.addWidget(self.btnSecondary1)

        self.btnDelete1 = QPushButton(self.tabDietTypes)
        self.btnDelete1.setObjectName(u"btnDelete1")

        self.hboxLayout.addWidget(self.btnDelete1)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.tableDietTypes = QTableView(self.tabDietTypes)
        self.tableDietTypes.setObjectName(u"tableDietTypes")
        self.tableDietTypes.setMinimumSize(QSize(0, 650))
        self.tableDietTypes.setAlternatingRowColors(True)
        self.tableDietTypes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDietTypes.setShowGrid(False)

        self.vboxLayout.addWidget(self.tableDietTypes)

        self.tabDiets.addTab(self.tabDietTypes, "")
        self.tabDietList = QWidget()
        self.tabDietList.setObjectName(u"tabDietList")
        self.vboxLayout1 = QVBoxLayout(self.tabDietList)
        self.vboxLayout1.setSpacing(12)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.horizontalSpacer_2)

        self.sectionLabel2 = QLabel(self.tabDietList)
        self.sectionLabel2.setObjectName(u"sectionLabel2")
        self.sectionLabel2.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.hboxLayout1.addWidget(self.sectionLabel2)

        self.comboDietTypeFilter = QComboBox(self.tabDietList)
        self.comboDietTypeFilter.setObjectName(u"comboDietTypeFilter")

        self.hboxLayout1.addWidget(self.comboDietTypeFilter)

        self.spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout1.addItem(self.spacerItem2)

        self.btnAddDiet = QPushButton(self.tabDietList)
        self.btnAddDiet.setObjectName(u"btnAddDiet")

        self.hboxLayout1.addWidget(self.btnAddDiet)

        self.btnSecondary2 = QPushButton(self.tabDietList)
        self.btnSecondary2.setObjectName(u"btnSecondary2")

        self.hboxLayout1.addWidget(self.btnSecondary2)

        self.btnDelete2 = QPushButton(self.tabDietList)
        self.btnDelete2.setObjectName(u"btnDelete2")

        self.hboxLayout1.addWidget(self.btnDelete2)


        self.vboxLayout1.addLayout(self.hboxLayout1)

        self.tableDiets = QTableView(self.tabDietList)
        self.tableDiets.setObjectName(u"tableDiets")
        self.tableDiets.setMinimumSize(QSize(0, 650))
        self.tableDiets.setAlternatingRowColors(True)
        self.tableDiets.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDiets.setShowGrid(False)

        self.vboxLayout1.addWidget(self.tableDiets)

        self.tabDiets.addTab(self.tabDietList, "")
        self.tabDietAssign = QWidget()
        self.tabDietAssign.setObjectName(u"tabDietAssign")
        self.vboxLayout2 = QVBoxLayout(self.tabDietAssign)
        self.vboxLayout2.setSpacing(12)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.spacerItem3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout2.addItem(self.spacerItem3)

        self.btnAssignDiet = QPushButton(self.tabDietAssign)
        self.btnAssignDiet.setObjectName(u"btnAssignDiet")

        self.hboxLayout2.addWidget(self.btnAssignDiet)

        self.btnDelete3 = QPushButton(self.tabDietAssign)
        self.btnDelete3.setObjectName(u"btnDelete3")

        self.hboxLayout2.addWidget(self.btnDelete3)


        self.vboxLayout2.addLayout(self.hboxLayout2)

        self.tableDietHistory = QTableView(self.tabDietAssign)
        self.tableDietHistory.setObjectName(u"tableDietHistory")
        self.tableDietHistory.setMinimumSize(QSize(0, 650))
        self.tableDietHistory.setAlternatingRowColors(True)
        self.tableDietHistory.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDietHistory.setShowGrid(False)

        self.vboxLayout2.addWidget(self.tableDietHistory)

        self.tabDiets.addTab(self.tabDietAssign, "")

        self.layoutDiets.addWidget(self.tabDiets)

        self.stackedWidget.addWidget(self.pageDiets)
        self.pageEmployees = QWidget()
        self.pageEmployees.setObjectName(u"pageEmployees")
        self.layoutEmployees = QVBoxLayout(self.pageEmployees)
        self.layoutEmployees.setSpacing(16)
        self.layoutEmployees.setObjectName(u"layoutEmployees")
        self.layoutEmployees.setContentsMargins(32, 28, 32, 24)
        self.pageTitle2 = QLabel(self.pageEmployees)
        self.pageTitle2.setObjectName(u"pageTitle2")
        self.pageTitle2.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.layoutEmployees.addWidget(self.pageTitle2)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setSpacing(12)
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.sectionLabel3 = QLabel(self.pageEmployees)
        self.sectionLabel3.setObjectName(u"sectionLabel3")
        self.sectionLabel3.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.hboxLayout3.addWidget(self.sectionLabel3)

        self.comboEmployeeRole = QComboBox(self.pageEmployees)
        self.comboEmployeeRole.addItem("")
        self.comboEmployeeRole.addItem("")
        self.comboEmployeeRole.addItem("")
        self.comboEmployeeRole.setObjectName(u"comboEmployeeRole")

        self.hboxLayout3.addWidget(self.comboEmployeeRole)

        self.spacerItem4 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout3.addItem(self.spacerItem4)

        self.btnAddEmployee = QPushButton(self.pageEmployees)
        self.btnAddEmployee.setObjectName(u"btnAddEmployee")

        self.hboxLayout3.addWidget(self.btnAddEmployee)

        self.btnSecondary3 = QPushButton(self.pageEmployees)
        self.btnSecondary3.setObjectName(u"btnSecondary3")

        self.hboxLayout3.addWidget(self.btnSecondary3)

        self.btnDelete4 = QPushButton(self.pageEmployees)
        self.btnDelete4.setObjectName(u"btnDelete4")

        self.hboxLayout3.addWidget(self.btnDelete4)


        self.layoutEmployees.addLayout(self.hboxLayout3)

        self.tableEmployees = QTableView(self.pageEmployees)
        self.tableEmployees.setObjectName(u"tableEmployees")
        self.tableEmployees.setMinimumSize(QSize(0, 650))
        self.tableEmployees.setAlternatingRowColors(True)
        self.tableEmployees.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableEmployees.setShowGrid(False)

        self.layoutEmployees.addWidget(self.tableEmployees)

        self.stackedWidget.addWidget(self.pageEmployees)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.layoutReports = QVBoxLayout(self.pageReports)
        self.layoutReports.setSpacing(16)
        self.layoutReports.setObjectName(u"layoutReports")
        self.layoutReports.setContentsMargins(32, 28, 32, 24)
        self.pageTitle3 = QLabel(self.pageReports)
        self.pageTitle3.setObjectName(u"pageTitle3")
        self.pageTitle3.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.layoutReports.addWidget(self.pageTitle3)

        self.tabReports = QTabWidget(self.pageReports)
        self.tabReports.setObjectName(u"tabReports")
        self.tabReport1 = QWidget()
        self.tabReport1.setObjectName(u"tabReport1")
        self.vboxLayout3 = QVBoxLayout(self.tabReport1)
        self.vboxLayout3.setSpacing(12)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setSpacing(12)
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.sectionLabel4 = QLabel(self.tabReport1)
        self.sectionLabel4.setObjectName(u"sectionLabel4")
        self.sectionLabel4.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.hboxLayout4.addWidget(self.sectionLabel4)

        self.comboReport1Type = QComboBox(self.tabReport1)
        self.comboReport1Type.addItem("")
        self.comboReport1Type.addItem("")
        self.comboReport1Type.addItem("")
        self.comboReport1Type.setObjectName(u"comboReport1Type")

        self.hboxLayout4.addWidget(self.comboReport1Type)

        self.sectionLabel5 = QLabel(self.tabReport1)
        self.sectionLabel5.setObjectName(u"sectionLabel5")
        self.sectionLabel5.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.hboxLayout4.addWidget(self.sectionLabel5)

        self.comboReport1Name = QComboBox(self.tabReport1)
        self.comboReport1Name.setObjectName(u"comboReport1Name")
        self.comboReport1Name.setEditable(True)

        self.hboxLayout4.addWidget(self.comboReport1Name)

        self.btnReport1Search = QPushButton(self.tabReport1)
        self.btnReport1Search.setObjectName(u"btnReport1Search")

        self.hboxLayout4.addWidget(self.btnReport1Search)

        self.spacerItem5 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout4.addItem(self.spacerItem5)


        self.vboxLayout3.addLayout(self.hboxLayout4)

        self.textReport1 = QTextBrowser(self.tabReport1)
        self.textReport1.setObjectName(u"textReport1")
        self.textReport1.setMinimumSize(QSize(0, 650))

        self.vboxLayout3.addWidget(self.textReport1)

        self.tabReports.addTab(self.tabReport1, "")
        self.tabReport2 = QWidget()
        self.tabReport2.setObjectName(u"tabReport2")
        self.vboxLayout4 = QVBoxLayout(self.tabReport2)
        self.vboxLayout4.setSpacing(12)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout5.addItem(self.horizontalSpacer)

        self.btnReport2Load = QPushButton(self.tabReport2)
        self.btnReport2Load.setObjectName(u"btnReport2Load")

        self.hboxLayout5.addWidget(self.btnReport2Load)


        self.vboxLayout4.addLayout(self.hboxLayout5)

        self.tableReport2 = QTableView(self.tabReport2)
        self.tableReport2.setObjectName(u"tableReport2")
        self.tableReport2.setMinimumSize(QSize(0, 650))
        self.tableReport2.setAlternatingRowColors(True)
        self.tableReport2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableReport2.setShowGrid(False)

        self.vboxLayout4.addWidget(self.tableReport2)

        self.tabReports.addTab(self.tabReport2, "")
        self.tabReport3 = QWidget()
        self.tabReport3.setObjectName(u"tabReport3")
        self.vboxLayout5 = QVBoxLayout(self.tabReport3)
        self.vboxLayout5.setSpacing(12)
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.hboxLayout6 = QHBoxLayout()
        self.hboxLayout6.setSpacing(12)
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.sectionLabel6 = QLabel(self.tabReport3)
        self.sectionLabel6.setObjectName(u"sectionLabel6")
        self.sectionLabel6.setStyleSheet(u"QLabel {\n"
"    color: #1A202C;\n"
"}")

        self.hboxLayout6.addWidget(self.sectionLabel6)

        self.editReport3Date = QLineEdit(self.tabReport3)
        self.editReport3Date.setObjectName(u"editReport3Date")

        self.hboxLayout6.addWidget(self.editReport3Date)

        self.btnReport3Load = QPushButton(self.tabReport3)
        self.btnReport3Load.setObjectName(u"btnReport3Load")

        self.hboxLayout6.addWidget(self.btnReport3Load)

        self.spacerItem6 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hboxLayout6.addItem(self.spacerItem6)


        self.vboxLayout5.addLayout(self.hboxLayout6)

        self.tableReport3 = QTableView(self.tabReport3)
        self.tableReport3.setObjectName(u"tableReport3")
        self.tableReport3.setMinimumSize(QSize(0, 650))
        self.tableReport3.setAlternatingRowColors(True)
        self.tableReport3.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableReport3.setShowGrid(False)

        self.vboxLayout5.addWidget(self.tableReport3)

        self.tabReports.addTab(self.tabReport3, "")

        self.layoutReports.addWidget(self.tabReports)

        self.stackedWidget.addWidget(self.pageReports)

        self.mainLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabDiets.setCurrentIndex(0)
        self.tabReports.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0417\u043e\u043e\u043f\u0430\u0440\u043a \u2014 \u0423\u0447\u0451\u0442 \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0445", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"    QMainWindow { background-color: #F4F6F8; }\n"
"    QWidget { font-family: \"Segoe UI\", \"Inter\", \"Roboto\", sans-serif; }\n"
"\n"
"    QListWidget#menuList {\n"
"        background-color: #FFFFFF;\n"
"        color: #1A202C;\n"
"        font-size: 14px;\n"
"        font-weight: 500;\n"
"        border: none;\n"
"        border-right: 1px solid #E2E8F0;\n"
"        outline: none;\n"
"    }\n"
"    QListWidget#menuList::item {\n"
"        padding: 14px 24px;\n"
"        border-left: 3px solid transparent;\n"
"        color: #4A5568;\n"
"    }\n"
"    QListWidget#menuList::item:selected {\n"
"        background-color: #EBF4FF;\n"
"        color: #2C5282;\n"
"        border-left: 3px solid #2C5282;\n"
"        font-weight: 600;\n"
"    }\n"
"    QListWidget#menuList::item:hover:!selected {\n"
"        background-color: #F7FAFC;\n"
"        color: #2D3748;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #2C5282;\n"
"        color: #FFFFFF;\n"
"        border: none;\n"
"        border-"
                        "radius: 6px;\n"
"        padding: 9px 18px;\n"
"        font-size: 13px;\n"
"        font-weight: 500;\n"
"    }\n"
"    QPushButton:hover { background-color: #2B6CB0; }\n"
"    QPushButton:pressed { background-color: #1E40AF; }\n"
"\n"
"    QPushButton#btnDelete { background-color: #C53030; }\n"
"    QPushButton#btnDelete:hover { background-color: #E53E3E; }\n"
"\n"
"    QPushButton#btnSecondary {\n"
"        background-color: #FFFFFF;\n"
"        color: #2D3748;\n"
"        border: 1px solid #E2E8F0;\n"
"    }\n"
"    QPushButton#btnSecondary:hover { background-color: #F7FAFC; border-color: #CBD5E0; }\n"
"\n"
"    QTableView {\n"
"        background-color: #FFFFFF;\n"
"        alternate-background-color: #FAFBFC;\n"
"        color: #1A202C;\n"
"        gridline-color: #EDF2F7;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 8px;\n"
"        font-size: 13px;\n"
"        selection-background-color: #EBF4FF;\n"
"        selection-color: #2C5282;\n"
"    }\n"
"    QTableView::item { padding: 8p"
                        "x 12px; }\n"
"    QTableView::item:hover { background-color: #F7FAFC; }\n"
"    QHeaderView::section {\n"
"        background-color: #F7FAFC;\n"
"        color: #4A5568;\n"
"        padding: 10px 12px;\n"
"        border: none;\n"
"        border-bottom: 1px solid #E2E8F0;\n"
"        border-right: 1px solid #EDF2F7;\n"
"        font-size: 12px;\n"
"        font-weight: 600;\n"
"    }\n"
"\n"
"    QLineEdit, QComboBox, QDateEdit, QDoubleSpinBox, QSpinBox {\n"
"        background-color: #FFFFFF;\n"
"        color: #1A202C;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 6px;\n"
"        padding: 8px 12px;\n"
"        font-size: 13px;\n"
"    }\n"
"    QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QDoubleSpinBox:focus {\n"
"        border: 1px solid #2C5282;\n"
"    }\n"
"    QComboBox::drop-down {\n"
"        border: none;\n"
"        width: 24px;\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        background-color: #FFFFFF;\n"
"        border: 1px solid #E2E8F0;\n"
"        selec"
                        "tion-background-color: #EBF4FF;\n"
"        selection-color: #2C5282;\n"
"        outline: none;\n"
"    }\n"
"\n"
"    QLabel#pageTitle {\n"
"        font-size: 24px;\n"
"        font-weight: 600;\n"
"        color: #1A202C;\n"
"        padding-bottom: 4px;\n"
"    }\n"
"    QLabel#sectionLabel {\n"
"        font-size: 13px;\n"
"        font-weight: 500;\n"
"        color: #4A5568;\n"
"    }\n"
"\n"
"    QGroupBox {\n"
"        background-color: #FFFFFF;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 8px;\n"
"        margin-top: 12px;\n"
"        padding: 20px 16px 16px 16px;\n"
"        font-size: 14px;\n"
"        font-weight: 600;\n"
"        color: #1A202C;\n"
"    }\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        subcontrol-position: top left;\n"
"        padding: 0 8px;\n"
"        color: #2C5282;\n"
"    }\n"
"\n"
"    QTabWidget::pane {\n"
"        border: 1px solid #E2E8F0;\n"
"        background-color: #FFFFFF;\n"
"        border-radius: 8px;\n"
"    "
                        "    padding: 16px;\n"
"    }\n"
"    QTabBar::tab {\n"
"        background-color: transparent;\n"
"        color: #4A5568;\n"
"        padding: 10px 20px;\n"
"        border: none;\n"
"        border-bottom: 2px solid transparent;\n"
"        font-size: 13px;\n"
"        font-weight: 500;\n"
"        margin-right: 4px;\n"
"    }\n"
"    QTabBar::tab:selected {\n"
"        color: #2C5282;\n"
"        border-bottom: 2px solid #2C5282;\n"
"        font-weight: 600;\n"
"    }\n"
"    QTabBar::tab:hover:!selected {\n"
"        color: #2D3748;\n"
"        background-color: #F7FAFC;\n"
"    }\n"
"\n"
"    QTextBrowser {\n"
"        background-color: #FFFFFF;\n"
"        border: 1px solid #E2E8F0;\n"
"        border-radius: 8px;\n"
"        padding: 16px;\n"
"        font-size: 14px;\n"
"        color: #1A202C;\n"
"    }\n"
"\n"
"    QStatusBar {\n"
"        background-color: #FFFFFF;\n"
"        border-top: 1px solid #E2E8F0;\n"
"        color: #4A5568;\n"
"        font-size: 12px;\n"
"    }\n"
"\n"
"    QScrollBar:v"
                        "ertical {\n"
"        background: transparent;\n"
"        width: 10px;\n"
"        margin: 0;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background: #CBD5E0;\n"
"        border-radius: 5px;\n"
"        min-height: 20px;\n"
"    }\n"
"    QScrollBar::handle:vertical:hover { background: #A0AEC0; }\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }\n"
"   ", None))

        __sortingEnabled = self.menuList.isSortingEnabled()
        self.menuList.setSortingEnabled(False)
        ___qlistwidgetitem = self.menuList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u0442\u043e\u043c\u0446\u044b", None))
        ___qlistwidgetitem1 = self.menuList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0446\u0438\u043e\u043d\u044b", None))
        ___qlistwidgetitem2 = self.menuList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        ___qlistwidgetitem3 = self.menuList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442\u044b", None))
        self.menuList.setSortingEnabled(__sortingEnabled)

        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u0442\u043e\u043c\u0446\u044b \u0437\u043e\u043e\u043f\u0430\u0440\u043a\u0430", None))
        self.sectionLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.comboAnimalType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))
        self.comboAnimalType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0442\u0438\u0446\u044b", None))
        self.comboAnimalType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043f\u0442\u0438\u043b\u0438\u0438", None))
        self.comboAnimalType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041c\u043b\u0435\u043a\u043e\u043f\u0438\u0442\u0430\u044e\u0449\u0438\u0435", None))

        self.sectionLabel1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.editAnimalSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.btnAddAnimal.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnSecondary.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pageTitle1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0446\u0438\u043e\u043d\u044b \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.btnAddDietType.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0438\u043f", None))
        self.btnSecondary1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnDelete1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabDiets.setTabText(self.tabDiets.indexOf(self.tabDietTypes), QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f\u044b \u0440\u0430\u0446\u0438\u043e\u043d\u043e\u0432", None))
        self.sectionLabel2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.btnAddDiet.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0446\u0438\u043e\u043d", None))
        self.btnSecondary2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnDelete2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabDiets.setTabText(self.tabDiets.indexOf(self.tabDietList), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0446\u0438\u043e\u043d\u044b", None))
        self.btnAssignDiet.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0438\u0442\u044c \u0440\u0430\u0446\u0438\u043e\u043d", None))
        self.btnDelete3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0439", None))
        self.tabDiets.setTabText(self.tabDiets.indexOf(self.tabDietAssign), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0440\u0430\u0446\u0438\u043e\u043d\u0430", None))
        self.pageTitle2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.sectionLabel3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.comboEmployeeRole.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))
        self.comboEmployeeRole.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043c\u043e\u0442\u0440\u0438\u0442\u0435\u043b\u044c", None))
        self.comboEmployeeRole.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0442\u0435\u0440\u0438\u043d\u0430\u0440", None))

        self.btnAddEmployee.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnSecondary3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnDelete4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pageTitle3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442\u044b", None))
        self.sectionLabel4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.comboReport1Type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0442\u0438\u0446\u044b", None))
        self.comboReport1Type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043f\u0442\u0438\u043b\u0438\u0438", None))
        self.comboReport1Type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u043b\u0435\u043a\u043e\u043f\u0438\u0442\u0430\u044e\u0449\u0438\u0435", None))

        self.sectionLabel5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.btnReport1Search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.textReport1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0438 \u0438\u043c\u044f \u043f\u0438\u0442\u043e\u043c\u0446\u0430, \u0437\u0430\u0442\u0435\u043c \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u00ab\u041d\u0430\u0439\u0442\u0438\u00bb.", None))
        self.tabReports.setTabText(self.tabReports.indexOf(self.tabReport1), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u043f\u0438\u0442\u043e\u043c\u0446\u0443", None))
        self.btnReport2Load.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.tabReports.setTabText(self.tabReports.indexOf(self.tabReport2), QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043c\u0435\u0439\u043d\u044b\u0435 \u043f\u0430\u0440\u044b", None))
        self.sectionLabel6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 (\u0434\u0434.\u043c\u043c.\u0433\u0433\u0433\u0433):", None))
        self.editReport3Date.setInputMask(QCoreApplication.translate("MainWindow", u"99.99.9999;_", None))
        self.editReport3Date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0434\u0434.\u043c\u043c.\u0433\u0433\u0433\u0433", None))
        self.btnReport3Load.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabReports.setTabText(self.tabReports.indexOf(self.tabReport3), QCoreApplication.translate("MainWindow", u"\u0416\u0438\u0432\u043e\u0442\u043d\u044b\u0435 \u0438 \u0440\u0430\u0446\u0438\u043e\u043d\u044b", None))
    # retranslateUi

