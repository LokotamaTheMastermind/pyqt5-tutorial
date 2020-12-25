# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.setWindowModality(QtCore.Qt.ApplicationModal)
        window.resize(366, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setWindowOpacity(1.0)
        window.setStyleSheet("")
        self.button = QtWidgets.QPushButton(window)
        self.button.setGeometry(QtCore.QRect(130, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.button.setFont(font)
        self.button.setCheckable(True)
        self.button.setDefault(False)
        self.button.setFlat(False)
        self.button.setObjectName("button")
        self.button.clicked.connect(self.change_label)
        self.description = QtWidgets.QLabel(window)
        self.description.setGeometry(QtCore.QRect(150, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setObjectName("description")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Hello World"))
        self.button.setText(_translate("window", "CLICK ME"))
        self.description.setText(_translate("window", "Some text"))

    def change_label(self):
        if self.button.isChecked():
            self.button.setText('Look below!')
            self.description.setText('Awesome!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
