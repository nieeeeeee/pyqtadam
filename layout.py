# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 347)
        Dialog.setStyleSheet("background-color: #B0C4DE")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 271, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.EditImie = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.EditImie.setObjectName("EditImie")
        self.gridLayout.addWidget(self.EditImie, 1, 1, 1, 1)
        self.EditNazwisko = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.EditNazwisko.setObjectName("EditNazwisko")
        self.gridLayout.addWidget(self.EditNazwisko, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(330, 20, 271, 281))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkUperLower = QtWidgets.QCheckBox(parent=self.gridLayoutWidget_2)
        self.checkUperLower.setObjectName("checkUperLower")
        self.gridLayout_2.addWidget(self.checkUperLower, 1, 0, 1, 2)
        self.checkCyfry = QtWidgets.QCheckBox(parent=self.gridLayoutWidget_2)
        self.checkCyfry.setObjectName("checkCyfry")
        self.gridLayout_2.addWidget(self.checkCyfry, 2, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_2)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.checkSpecialCharacters = QtWidgets.QCheckBox(parent=self.gridLayoutWidget_2)
        self.checkSpecialCharacters.setObjectName("checkSpecialCharacters")
        self.gridLayout_2.addWidget(self.checkSpecialCharacters, 3, 0, 1, 2)
        self.buttonGenerate = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonGenerate.setStyleSheet("background-color: #4682B4")
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.gridLayout_2.addWidget(self.buttonGenerate, 4, 0, 1, 2)
        self.checkCyfry.raise_()
        self.label_5.raise_()
        self.spinBox.raise_()
        self.checkSpecialCharacters.raise_()
        self.checkUperLower.raise_()
        self.buttonGenerate.raise_()
        self.zatwierdz = QtWidgets.QPushButton(parent=Dialog)
        self.zatwierdz.setGeometry(QtCore.QRect(190, 310, 251, 32))
        self.zatwierdz.setStyleSheet("background-color: #4682B4")
        self.zatwierdz.setObjectName("zatwierdz")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "stanowisko"))
        self.label_2.setText(_translate("Dialog", "imię"))
        self.label_3.setText(_translate("Dialog", "nazwiso"))
        self.label.setText(_translate("Dialog", "dane pracownika"))
        self.comboBox.setItemText(0, _translate("Dialog", "kierownik"))
        self.comboBox.setItemText(1, _translate("Dialog", "starszy programista"))
        self.comboBox.setItemText(2, _translate("Dialog", "młodszy prgramista"))
        self.comboBox.setItemText(3, _translate("Dialog", "tester"))
        self.checkUperLower.setText(_translate("Dialog", "małe i wielkie litery"))
        self.checkCyfry.setText(_translate("Dialog", "cyfry"))
        self.label_5.setText(_translate("Dialog", "liczba liter"))
        self.checkSpecialCharacters.setText(_translate("Dialog", "znaki specjalne"))
        self.buttonGenerate.setText(_translate("Dialog", "generuj haslo"))
        self.zatwierdz.setText(_translate("Dialog", "zadtwierdz"))
