# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Files_UI\untitled_apagar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela_apagar(object):
    def setupUi(self, Janela_apagar):
        Janela_apagar.setObjectName("Janela_apagar")
        Janela_apagar.resize(196, 94)
        Janela_apagar.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(Janela_apagar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, -20, 311, 161))
        self.label.setStyleSheet("background-color:black")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_sim = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sim.setGeometry(QtCore.QRect(20, 35, 48, 48))
        self.btn_sim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sim.setStyleSheet("border-radius:1px")
        self.btn_sim.setText("")
        self.btn_sim.setIconSize(QtCore.QSize(48, 48))
        self.btn_sim.setObjectName("btn_sim")
        self.btn_nao = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nao.setGeometry(QtCore.QRect(120, 35, 48, 48))
        self.btn_nao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_nao.setStyleSheet("border-radius:1px")
        self.btn_nao.setText("")
        self.btn_nao.setIconSize(QtCore.QSize(48, 48))
        self.btn_nao.setObjectName("btn_nao")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 9, 180, 10))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        Janela_apagar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_apagar)
        QtCore.QMetaObject.connectSlotsByName(Janela_apagar)

    def retranslateUi(self, Janela_apagar):
        _translate = QtCore.QCoreApplication.translate
        Janela_apagar.setWindowTitle(_translate("Janela_apagar", "  "))
        self.label_2.setText(_translate("Janela_apagar", "CERTEZA QUE DESEJA EXCLUIR?"))