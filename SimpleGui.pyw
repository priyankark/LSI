import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ExtractLine import *
#from GlobalValuesLib import *


class SimpleGui(QWidget):

    def __init__(self,parent=None):
       super(SimpleGui,self).__init__(parent)
       self.setGeometry(65,50,500,500)
       selectionBar=QHBoxLayout()

       self.btnDXF=QPushButton("Select .dxf file",self)
       self.showSelection=QLineEdit()
       self.btnDXF.clicked.connect(lambda:self.getfiles(self.showSelection))
       self.btnExtractLines=QPushButton("Extract")
       self.btnExtractLines.clicked.connect(lambda:self.handleExtract(self.viewStatus))
       self.btnSHP=QPushButton("View SHP")
       self.btnSHP.clicked.connect(self.btnSHPFn)
       selectionBar.addWidget(self.showSelection)
       selectionBar.addWidget(self.btnDXF)
       selectionBar.addWidget(self.btnExtractLines)
       selectionBarWidget=QWidget()
       selectionBarWidget.setLayout(selectionBar)
       self.viewStatus=QTextEdit()

       #layout.addWidget(self.btnDFX)
       mainLayout=QVBoxLayout()
       mainLayout.addWidget(selectionBarWidget)
       mainLayout.addWidget(self.viewStatus)
       mainLayout.addWidget(self.btnSHP)
       self.setLayout(mainLayout)

    def handleExtract(self,viewStatus):
        convertSHP(DXF_fileName,viewStatus)

    def getfiles(self,showSelection):
        dlg=QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("DXF Files (*.dxf)")
        filenames=QStringList()

        if dlg.exec_():
            filename=dlg.selectedFiles()
            showSelection.setText(str(filename[0]))
            global DXF_fileName
            DXF_fileName=str(filename[0])
            print DXF_fileName

    def btnSHPFn(self):
        print "hello"


def main():
    app=QApplication(sys.argv)
    QApplication.processEvents()
    simpleGUI=SimpleGui()
    simpleGUI.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
