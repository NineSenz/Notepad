import os
import sys
import time

from PyQt5.QtCore import Qt

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setWindowTitle("ScratchPi-v3.0")
        self.setGeometry(100, 100, 1800, 900)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setWindowIcon(QIcon('favicon.ico'))

        self.openFileName = '无标题.txt'
        self.openFilePath = ''
        self.isSaved = False
        self.fintText = ''
        self.replaceText = ''

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 1, 0, 0)

        self.menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.menuFile = QtWidgets.QMenu("文件(&F)")
        self.menuEdit = QtWidgets.QMenu("编辑(&E)")
        self.menuFormat = QtWidgets.QMenu("格式(&D)")
        self.menuView = QtWidgets.QMenu("查看(&V)")
        self.menuHelp = QtWidgets.QMenu("帮助(&H)")
        self.menuBar.addMenu(self.menuFile)
        self.menuBar.addMenu(self.menuEdit)
        self.menuBar.addMenu(self.menuFormat)
        self.menuBar.addMenu(self.menuView)
        self.menuBar.addMenu(self.menuHelp)

        self.menuFileNew = QtWidgets.QAction("新建(&N)")
        self.menuFileNew.setShortcut("Ctrl+N")
        self.menuFile.addAction(self.menuFileNew)
        self.menuFileNew.triggered.connect(self.newFile)

        self.menuFileOpen = QtWidgets.QAction("打开(&O)")
        self.menuFileOpen.setShortcut("Ctrl+O")
        self.menuFile.addAction(self.menuFileOpen)
        self.menuFileOpen.triggered.connect(self.openFile)

        self.menuFileSave = QtWidgets.QAction("保存(&S)")
        self.menuFileSave.setShortcut("Ctrl+S")
        self.menuFile.addAction(self.menuFileSave)
        self.menuFileSave.triggered.connect(self.saveFile)

        self.menuFileSaveAs = QtWidgets.QAction("另存为(&A)...")
        self.menuFile.addAction(self.menuFileSaveAs)
        self.menuFileSaveAs.triggered.connect(self.saveas)

        self.menuFile.addSeparator()

        # self.menuFilePage = QtWidgets.QAction("页面设置(&U)...")
        # self.menuFile.addAction(self.menuFilePage)
        #
        # self.menuFilePrint = QtWidgets.QAction("打印(&P)...")
        # self.menuFile.addAction(self.menuFilePrint)
        #
        # self.menuFile.addSeparator()

        self.menuExit = QtWidgets.QAction("退出(&X)")
        self.menuFile.addAction(self.menuExit)
        self.menuExit.triggered.connect(self.exit)

        self.menuEditUndo = QtWidgets.QAction("撤销(&U)")
        self.menuEditUndo.setShortcut("Ctrl+Z")
        self.menuEdit.addAction(self.menuEditUndo)
        self.menuEditUndo.triggered.connect(self.undo)

        self.menuEdit.addSeparator()

        self.menuEditCut = QtWidgets.QAction("剪切(&T)")
        self.menuEditCut.setShortcut("Ctrl+X")
        self.menuEdit.addAction(self.menuEditCut)
        self.menuEditCut.triggered.connect(self.cut)

        self.menuEditCopy = QtWidgets.QAction("复制(&C)")
        self.menuEditCopy.setShortcut("Ctrl+C")
        self.menuEdit.addAction(self.menuEditCopy)
        self.menuEditCopy.triggered.connect(self.copy)

        self.menuEditPaste = QtWidgets.QAction("粘贴(&P)")
        self.menuEditPaste.setShortcut("Ctrl+V")
        self.menuEdit.addAction(self.menuEditPaste)
        self.menuEditPaste.triggered.connect(self.paste)

        self.menuEditDel = QtWidgets.QAction("删除(&T)")
        self.menuEditDel.setShortcut("Del")
        self.menuEdit.addAction(self.menuEditDel)
        self.menuEditDel.triggered.connect(self.delete)

        self.menuEdit.addSeparator()

        self.menuEditFind = QtWidgets.QAction("查找(&F)...")
        self.menuEditFind.setShortcut("Ctrl+F")
        self.menuEdit.addAction(self.menuEditFind)
        self.menuEditFind.triggered.connect(self.Find_UI)

        self.menuEditFindNext = QtWidgets.QAction("查找下一个(&N)")
        self.menuEditFindNext.setShortcut("F3")
        self.menuEdit.addAction(self.menuEditFindNext)
        self.menuEditFindNext.triggered.connect(self.find)

        self.menuEditReplace = QtWidgets.QAction("替换(&R)...")
        self.menuEditReplace.setShortcut("Ctrl+H")
        self.menuEdit.addAction(self.menuEditReplace)
        self.menuEditReplace.triggered.connect(self.Replace_UI)

        # self.menuEditGoto = QtWidgets.QAction("转到(&G)...")
        # self.menuEditGoto.setShortcut("Ctrl+G")
        # self.menuEdit.addAction(self.menuEditGoto)

        self.menuEdit.addSeparator()

        self.menuEditAll = QtWidgets.QAction("全选(&A)")
        self.menuEditAll.setShortcut("Ctrl+A")
        self.menuEdit.addAction(self.menuEditAll)
        self.menuEditAll.triggered.connect(self.selectAll)

        self.menuEditDate = QtWidgets.QAction("时间/日期(&D)")
        self.menuEditDate.setShortcut("F5")
        self.menuEdit.addAction(self.menuEditDate)
        self.menuEditDate.triggered.connect(self.insertDatetime)

        self.menuFormatWarp = QtWidgets.QAction("自动换行(&W)")
        self.menuFormatWarp.setCheckable(True)
        self.menuFormatWarp.setChecked(True)
        self.menuFormat.addAction(self.menuFormatWarp)
        self.menuFormatWarp.changed.connect(self.formatWarp)

        self.menuFormatFont = QtWidgets.QAction("字体(&F)...")
        self.menuFormat.addAction(self.menuFormatFont)
        self.menuFormatFont.triggered.connect(self.fontSelect)

        self.menuViewStatusBar = QtWidgets.QAction("状态栏(&S)")
        self.menuViewStatusBar.setCheckable(True)
        self.menuViewStatusBar.setChecked(True)
        self.menuView.addAction(self.menuViewStatusBar)
        self.menuViewStatusBar.changed.connect(self.statusBarShow)

        self.menuHelpShow = QtWidgets.QAction("查看帮助(&H)")
        self.menuHelp.addAction(self.menuHelpShow)
        self.menuHelpShow.triggered.connect(self.about)

        self.menuHelp.addSeparator()

        self.menuHelpAbout = QtWidgets.QAction("关于ScratchPi3.0(&A)")
        self.menuHelp.addAction(self.menuHelpAbout)
        self.menuHelpAbout.triggered.connect(self.about)

        self.statusBar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusBar)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.gridLayout.addWidget(self.plainTextEdit)
        self.font = QtGui.QFont("宋体", 12)
        self.plainTextEdit.setFont(self.font)
        self.plainTextEdit.cursorPositionChanged.connect(self.cursorPosition)
        self.plainTextEdit.textChanged.connect(self.textChange)

        self.show()

    def Find_UI(self):
        self.findDialog = QtWidgets.QDialog(self)
        self.findDialog.setWindowTitle("查找")
        self.findDialog.resize(380, 110)

        self.labelFind = QtWidgets.QLabel(self.findDialog)
        self.labelFind.setText("查找内容(&N):")
        self.labelFind.setGeometry(10, 15, 70, 20)

        self.lineEditFind = QtWidgets.QLineEdit(self.findDialog)
        self.lineEditFind.setGeometry(90, 15, 180, 20)
        self.lineEditFind.setText(self.fintText)

        self.labelFind.setBuddy(self.lineEditFind)

        self.pushButtonFind = QtWidgets.QPushButton(self.findDialog)
        self.pushButtonFind.setText("查找下一个(&F)")
        self.pushButtonFind.setGeometry(280, 15, 90, 20)
        self.pushButtonFind.clicked.connect(self.find)

        self.pushButtonFindClose = QtWidgets.QPushButton(self.findDialog)
        self.pushButtonFindClose.setText("取消")
        self.pushButtonFindClose.setGeometry(280, 45, 90, 20)
        self.pushButtonFindClose.clicked.connect(self.findClose)

        self.checkBoxCase = QtWidgets.QCheckBox(self.findDialog)
        self.checkBoxCase.setText("区分大小写(&C)")
        self.checkBoxCase.setGeometry(10, 75, 100, 20)

        self.groupBoxFind = QtWidgets.QGroupBox(self.findDialog)
        self.groupBoxFind.setTitle("方向")
        self.groupBoxFind.setGeometry(110, 45, 160, 40)

        self.radioButtonFindProv = QtWidgets.QRadioButton(self.groupBoxFind)
        self.radioButtonFindProv.setText("向上(&U)")
        self.radioButtonFindProv.setGeometry(10, 15, 60, 20)

        self.radioButtonFindNext = QtWidgets.QRadioButton(self.groupBoxFind)
        self.radioButtonFindNext.setText("向下(&D)")
        self.radioButtonFindNext.setGeometry(90, 15, 60, 20)
        self.radioButtonFindNext.setChecked(True)

        self.findDialog.show()

    def Replace_UI(self):
        self.replaceDialog = QtWidgets.QDialog(self)
        self.replaceDialog.setWindowTitle("替换")
        self.replaceDialog.resize(380, 130)

        self.labelFind = QtWidgets.QLabel(self.replaceDialog)
        self.labelFind.setText("查找内容(&N):")
        self.labelFind.setGeometry(10, 15, 70, 20)

        self.lineEditFind = QtWidgets.QLineEdit(self.replaceDialog)
        self.lineEditFind.setGeometry(90, 15, 180, 20)
        self.lineEditFind.setText(self.fintText)

        self.labelFind.setBuddy(self.lineEditFind)

        self.labelReplace = QtWidgets.QLabel(self.replaceDialog)
        self.labelReplace.setText("替换(&P):")
        self.labelReplace.setGeometry(10, 45, 70, 20)

        self.lineEditReplace = QtWidgets.QLineEdit(self.replaceDialog)
        self.lineEditReplace.setGeometry(90, 45, 180, 20)
        self.lineEditReplace.setText(self.replaceText)

        self.labelReplace.setBuddy(self.lineEditReplace)

        self.pushButtonFind = QtWidgets.QPushButton(self.replaceDialog)
        self.pushButtonFind.setText("查找下一个(&F)")
        self.pushButtonFind.setGeometry(280, 15, 90, 20)
        self.pushButtonFind.clicked.connect(self.find)

        self.pushButtonReplace = QtWidgets.QPushButton(self.replaceDialog)
        self.pushButtonReplace.setText("替换(&R)")
        self.pushButtonReplace.setGeometry(280, 40, 90, 20)
        self.pushButtonReplace.clicked.connect(self.replace)

        self.pushButtonReplaceAll = QtWidgets.QPushButton(self.replaceDialog)
        self.pushButtonReplaceAll.setText("全部替换(&A)")
        self.pushButtonReplaceAll.setGeometry(280, 65, 90, 20)
        self.pushButtonReplaceAll.clicked.connect(lambda: self.replace(True))

        self.pushButtonFindClose = QtWidgets.QPushButton(self.replaceDialog)
        self.pushButtonFindClose.setText("取消")
        self.pushButtonFindClose.setGeometry(280, 90, 90, 20)
        self.pushButtonFindClose.clicked.connect(self.replaceClose)

        self.checkBoxCase = QtWidgets.QCheckBox(self.replaceDialog)
        self.checkBoxCase.setText("区分大小写(&C)")
        self.checkBoxCase.setGeometry(10, 95, 100, 20)

        self.groupBoxFind = QtWidgets.QGroupBox(self.replaceDialog)
        self.groupBoxFind.setTitle("方向")
        self.groupBoxFind.setGeometry(110, 75, 160, 40)

        self.radioButtonFindProv = QtWidgets.QRadioButton(self.groupBoxFind)
        self.radioButtonFindProv.setText("向上(&U)")
        self.radioButtonFindProv.setGeometry(10, 15, 60, 20)

        self.radioButtonFindNext = QtWidgets.QRadioButton(self.groupBoxFind)
        self.radioButtonFindNext.setText("向下(&D)")
        self.radioButtonFindNext.setGeometry(90, 15, 60, 20)
        self.radioButtonFindNext.setChecked(True)

        self.replaceDialog.show()

    def find(self):
        self.fintText = self.lineEditFind.text()
        if self.fintText == "":
            QtWidgets.QMessageBox.information(self, "ScratchPi3.0", "请输入搜索内容")
            return False

        if self.checkBoxCase.isChecked() == True and self.radioButtonFindProv.isChecked() == True:
            result = self.plainTextEdit.find(self.fintText,
                                             QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindBackward)
        elif self.checkBoxCase.isChecked() == True and self.radioButtonFindNext.isChecked() == True:
            result = self.plainTextEdit.find(self.fintText, QtGui.QTextDocument.FindCaseSensitively)
        elif self.checkBoxCase.isChecked() == False and self.radioButtonFindProv.isChecked() == True:
            result = self.plainTextEdit.find(self.fintText, QtGui.QTextDocument.FindBackward)
        else:
            result = self.plainTextEdit.find(self.fintText)

        if result == False:
            QtWidgets.QMessageBox.information(self, "ScratchPi3.0", "找不到\"" + self.fintText + "\"")

        return result

    def replace(self, All=False):
        if self.find() == False:
            return False

        self.replaceText = self.lineEditReplace.text()
        if self.replaceText == "":
            QtWidgets.QMessageBox.information(self, "ScratchPi3.0", "请输入替换内容")
            return False

        if All == True:
            result = self.plainTextEdit.toPlainText().replace(self.fintText, self.replaceText)
            self.plainTextEdit.setPlainText(result)
        else:
            self.plainTextEdit.cut()
            self.plainTextEdit.insertPlainText(self.replaceText)

    def findClose(self):
        self.findDialog.close()

    def replaceClose(self):
        self.replaceDialog.close()

    def newFile(self):
        self.openFilePath = ''
        self.openFileName = '无标题.txt'
        self.setWindowTitle(self.openFileName + ' - ScratchPi3.0')
        self.plainTextEdit.clear()

    def openFile(self):
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "./", "文本文档 (*.txt);;所有文件 (*)")
        if filename != "":
            self.plainTextEdit.clear()
            with open(filename, 'r', encoding='gb18030', errors='ignore') as f:
                self.plainTextEdit.appendPlainText(f.read())
            f.close()
            self.openFilePath = filename
            self.openFileName = os.path.basename(filename)
            self.setWindowTitle(self.openFileName + ' - ScratchPi3.0')

    def saveFile(self):
        if self.openFilePath == "":
            filename, filetype = QtWidgets.QFileDialog.getSaveFileName(self, '保存', './', "文本文档 (*.txt);;所有文件 (*)")
            if filename == "":
                return False

            self.openFilePath = filename
            self.openFileName = os.path.basename(filename)
            self.setWindowTitle(self.openFileName + ' - ScratchPi3.0')

        file = open(self.openFilePath, 'w', encoding='gb18030', errors='ignore')
        file.write(self.plainTextEdit.toPlainText())
        file.close()
        self.setWindowTitle(self.openFileName + ' - ScratchPi3.0')
        self.isSaved = True
        return True

    def saveas(self):
        filename, filetype = QtWidgets.QFileDialog.getSaveFileName(self, '保存', './', "文本文档 (*.txt);;所有文件 (*)")
        if filename == "":
            return False

        self.openFilePath = filename
        self.openFileName = os.path.basename(filename)
        self.setWindowTitle(self.openFileName + ' - ScratchPi3.0')
        file = open(self.openFilePath, 'w', encoding='gb18030', errors='ignore')
        file.write(self.plainTextEdit.toPlainText())
        file.close()
        self.setWindowTitle(self.openFileName + ' - ScratchPi3.0')
        self.isSaved = True
        return True

    def exit(self):
        if self.isSaved == False:
            result = QtWidgets.QMessageBox.question(self, 'ScratchPi3.0', '是否将更改保存到' + self.openFileName,
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Yes:
                result = self.saveFile()
                if result == True:
                    QtCore.QCoreApplication.quit()
                else:
                    return False
            elif result == QtWidgets.QMessageBox.No:
                QtCore.QCoreApplication.quit()
            else:
                return False

        return True

    def undo(self):
        self.plainTextEdit.undo()

    def cut(self):
        self.plainTextEdit.cut()

    def copy(self):
        self.plainTextEdit.copy()

    def paste(self):
        self.plainTextEdit.paste()

    def delete(self):
        self.plainTextEdit.textCursor().deletePreviousChar()

    def selectAll(self):
        self.plainTextEdit.selectAll()

    def insertDatetime(self):
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.plainTextEdit.insertPlainText(datetime)

    def fontSelect(self):
        font, ok = QtWidgets.QFontDialog.getFont(self.font)
        if ok:
            self.font = font
            self.plainTextEdit.setFont(font)

    def about(self):
        # QtWidgets.QMessageBox.aboutQt(self, "关于我们")
        QtWidgets.QMessageBox.about(self, "关于我们", "devloper for bettertree Open Source Team")
    def textChange(self):
        self.isSaved = False
        self.setWindowTitle(self.openFileName + ' - ScratchPi3.0 *')

    def formatWarp(self):
        if self.menuFormatWarp.isChecked():
            self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        else:
            self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)

    def statusBarShow(self):
        if self.menuViewStatusBar.isChecked():
            self.statusBar.show()
        else:
            self.statusBar.hide()

    def cursorPosition(self):
        row = self.plainTextEdit.textCursor().blockNumber()
        col = self.plainTextEdit.textCursor().columnNumber()
        self.statusBar.showMessage("行 %d , 列 %d" % (row + 1, col + 1))

    def closeEvent(self, QcloseEvent):
        result = self.exit()
        if result == True:
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
