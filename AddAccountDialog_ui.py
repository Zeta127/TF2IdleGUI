# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddAccountDialog.ui'
#
# Created: Wed Jan 04 04:37:41 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddAccountDialog(object):
    def setupUi(self, AddAccountDialog):
        AddAccountDialog.setObjectName(_fromUtf8("AddAccountDialog"))
        AddAccountDialog.setWindowModality(QtCore.Qt.NonModal)
        AddAccountDialog.resize(422, 292)
        AddAccountDialog.setMinimumSize(QtCore.QSize(422, 292))
        AddAccountDialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(AddAccountDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(AddAccountDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 241))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_5 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 7, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setStatusTip(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 9, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.retranslateUi(AddAccountDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddAccountDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddAccountDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddAccountDialog)

    def retranslateUi(self, AddAccountDialog):
        AddAccountDialog.setWindowTitle(QtGui.QApplication.translate("AddAccountDialog", "Add account", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Location of Steam install for this sandbox", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("AddAccountDialog", "Sandboxie details (Optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("AddAccountDialog", "Steam details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Your Steam username", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddAccountDialog", "Steam username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Your Steam password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddAccountDialog", "Steam password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Sandbox name in Sandboxie", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddAccountDialog", "Sandbox name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Your Steam username", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Your Steam password", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Sandbox name in Sandboxie", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Groups this account is a member of", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddAccountDialog", "Groups (Optional, comma separated):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Location of Steam install for this sandbox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddAccountDialog", "Steam install location:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "A nickname for this account", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddAccountDialog", "Account nickname (Optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "A nickname for this account", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Nickname", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_7.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Groups this account is a member of", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_7.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Premium,Batch1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Your Steam vanity ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddAccountDialog", "Steam Vanity ID\n"
"(eg. steamcommunity.com/id/<vanityID>):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setToolTip(QtGui.QApplication.translate("AddAccountDialog", "Your Steam vanity ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setPlaceholderText(QtGui.QApplication.translate("AddAccountDialog", "Vanity ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddAccountDialog", "Other", None, QtGui.QApplication.UnicodeUTF8))

