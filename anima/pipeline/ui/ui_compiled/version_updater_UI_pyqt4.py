# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/version_updater.ui'
#
# Created: Thu Jul 18 17:51:48 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(658, 442)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.versions_tableWidget = QtGui.QTableWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.versions_tableWidget.sizePolicy().hasHeightForWidth())
        self.versions_tableWidget.setSizePolicy(sizePolicy)
        self.versions_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.versions_tableWidget.setAlternatingRowColors(True)
        self.versions_tableWidget.setCornerButtonEnabled(False)
        self.versions_tableWidget.setColumnCount(6)
        self.versions_tableWidget.setObjectName(_fromUtf8("versions_tableWidget"))
        self.versions_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.versions_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.versions_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.versions_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.versions_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.versions_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.versions_tableWidget.setHorizontalHeaderItem(5, item)
        self.versions_tableWidget.horizontalHeader().setVisible(True)
        self.versions_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.versions_tableWidget)
        self.horizontalWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.selectNone_pushButton = QtGui.QPushButton(self.horizontalWidget)
        self.selectNone_pushButton.setObjectName(_fromUtf8("selectNone_pushButton"))
        self.horizontalLayout.addWidget(self.selectNone_pushButton)
        self.selectAll_pushButton = QtGui.QPushButton(self.horizontalWidget)
        self.selectAll_pushButton.setObjectName(_fromUtf8("selectAll_pushButton"))
        self.horizontalLayout.addWidget(self.selectAll_pushButton)
        self.update_pushButton = QtGui.QPushButton(self.horizontalWidget)
        self.update_pushButton.setObjectName(_fromUtf8("update_pushButton"))
        self.horizontalLayout.addWidget(self.update_pushButton)
        self.cancel_pushButton = QtGui.QPushButton(self.horizontalWidget)
        self.cancel_pushButton.setObjectName(_fromUtf8("cancel_pushButton"))
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.verticalLayout.addWidget(self.horizontalWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Version Updater", None))
        self.label.setText(_translate("Dialog", "Please check the Versions that needs to be updated", None))
        item = self.versions_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Versionable", None))
        item = self.versions_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Type", None))
        item = self.versions_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Take", None))
        item = self.versions_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Current", None))
        item = self.versions_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Latest", None))
        item = self.versions_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Do Update?", None))
        self.selectNone_pushButton.setText(_translate("Dialog", "Select None", None))
        self.selectAll_pushButton.setText(_translate("Dialog", "Select All", None))
        self.update_pushButton.setText(_translate("Dialog", "Update", None))
        self.cancel_pushButton.setText(_translate("Dialog", "Cancel", None))
