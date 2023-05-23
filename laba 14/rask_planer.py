# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_planer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(745, 522)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(380, 110, 351, 371))
        self.calendarWidget.setStyleSheet("font:10pt;\n"
"background-color:rgb(198, 196, 255);\n"
"selection-background-color:rgb(170, 170, 255)")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tasksListWidget = QtWidgets.QListWidget(Form)
        self.tasksListWidget.setGeometry(QtCore.QRect(20, 150, 341, 301))
        self.tasksListWidget.setStyleSheet("font:12pt; background-color:rgb(241, 239, 255)")
        self.tasksListWidget.setObjectName("tasksListWidget")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 791, 531))
        self.frame.setStyleSheet("background-color:rgb(127, 127, 190)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size : 24pt;\n"
"background-color:rgb(177, 167, 255);\n"
"color:rgb(239, 238, 255);\n"
"border-radius:8px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.saveButton = QtWidgets.QPushButton(self.frame)
        self.saveButton.setGeometry(QtCore.QRect(100, 460, 161, 41))
        self.saveButton.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(241, 239, 255);\n"
"\n"
"font:11pt;")
        self.saveButton.setObjectName("saveButton")
        self.taskLineEdit = QtWidgets.QLineEdit(self.frame)
        self.taskLineEdit.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.taskLineEdit.setStyleSheet("font:12pt;background-color:rgb(241, 239, 255)")
        self.taskLineEdit.setObjectName("taskLineEdit")
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setGeometry(QtCore.QRect(270, 110, 93, 28))
        self.addButton.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(241, 239, 255);\n"
"\n"
"")
        self.addButton.setObjectName("addButton")
        self.frame.raise_()
        self.calendarWidget.raise_()
        self.tasksListWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Планировщик задач"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
        self.addButton.setText(_translate("Form", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
