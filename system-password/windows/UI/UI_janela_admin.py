# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Files_UI\untitled_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela_admin(object):
    def setupUi(self, Janela_admin):
        Janela_admin.setObjectName("Janela_admin")
        Janela_admin.setWindowModality(QtCore.Qt.NonModal)
        Janela_admin.resize(216, 105)
        Janela_admin.setBaseSize(QtCore.QSize(0, 0))
        Janela_admin.setWindowOpacity(1.0)
        Janela_admin.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(Janela_admin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-51, -31, 311, 161))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(9, 9, 293, 181))
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setText("")
        self.label.setObjectName("label")
        self.input_senha = QtWidgets.QLineEdit(self.widget)
        self.input_senha.setGeometry(QtCore.QRect(90, 70, 161, 20))
        self.input_senha.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_senha.setMaxLength(100)
        self.input_senha.setClearButtonEnabled(False)
        self.input_senha.setObjectName("input_senha")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 185, 21))
        self.label_3.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.label_3.setObjectName("label_3")
        self.cadastrar = QtWidgets.QPushButton(self.widget)
        self.cadastrar.setGeometry(QtCore.QRect(203, 89, 48, 48))
        self.cadastrar.setStyleSheet("border-radius:1px;\n"
"background-size:cover;")
        self.cadastrar.setText("")
        self.cadastrar.setIconSize(QtCore.QSize(48, 48))
        self.cadastrar.setObjectName("cadastrar")
        self.mostrarS = QtWidgets.QPushButton(self.widget)
        self.mostrarS.setGeometry(QtCore.QRect(230, 70, 21, 20))
        self.mostrarS.setStyleSheet("border-radius:1px;\n"
"background-size:cover;")
        self.mostrarS.setText("")
        self.mostrarS.setObjectName("mostrarS")
        self.imgS = QtWidgets.QLabel(self.widget)
        self.imgS.setGeometry(QtCore.QRect(60, 63, 32, 32))
        self.imgS.setText("")
        self.imgS.setObjectName("imgS")
        Janela_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_admin)
        QtCore.QMetaObject.connectSlotsByName(Janela_admin)

    def retranslateUi(self, Janela_admin):
        _translate = QtCore.QCoreApplication.translate
        Janela_admin.setWindowTitle(_translate("Janela_admin", "Admin"))
        self.input_senha.setPlaceholderText(_translate("Janela_admin", "Senha"))
        self.label_3.setText(_translate("Janela_admin", "Registre uma senha de admin"))
