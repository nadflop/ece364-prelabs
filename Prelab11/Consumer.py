#######################################################
#   Author:     Nur Nadhira Aqilah Binti Mohd Shah
#   email:      mohdshah@purdue.edu
#   ID:         ee364g02
#   Date:       3/31/2019
#######################################################

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Prelab11.BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.student = [self.txtStudentName, self.txtStudentID]
        self.componentName = [self.txtComponentName_1,self.txtComponentName_2,self.txtComponentName_3,
                              self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,
                              self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,
                              self.txtComponentName_10,self.txtComponentName_11,self.txtComponentName_12,
                              self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,
                              self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,
                              self.txtComponentName_19,self.txtComponentName_20]
        self.componentCount = [self.txtComponentCount_1,self.txtComponentCount_2,self.txtComponentCount_3,
                              self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,
                              self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,
                              self.txtComponentCount_10,self.txtComponentCount_11,self.txtComponentCount_12,
                              self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,
                              self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,
                              self.txtComponentCount_19,self.txtComponentCount_20]
        #disable the save button
        self.btnSave.setEnabled(False)

        self.txtStudentName.textChanged.connect(self.enableBtn)
        self.txtStudentID.textChanged.connect(self.enableBtn)

        self.txtComponentName_1.textChanged.connect(self.enableBtn)
        self.txtComponentName_2.textChanged.connect(self.enableBtn)
        self.txtComponentName_3.textChanged.connect(self.enableBtn)
        self.txtComponentName_4.textChanged.connect(self.enableBtn)
        self.txtComponentName_5.textChanged.connect(self.enableBtn)
        self.txtComponentName_6.textChanged.connect(self.enableBtn)
        self.txtComponentName_7.textChanged.connect(self.enableBtn)
        self.txtComponentName_8.textChanged.connect(self.enableBtn)
        self.txtComponentName_9.textChanged.connect(self.enableBtn)
        self.txtComponentName_10.textChanged.connect(self.enableBtn)
        self.txtComponentName_11.textChanged.connect(self.enableBtn)
        self.txtComponentName_12.textChanged.connect(self.enableBtn)
        self.txtComponentName_13.textChanged.connect(self.enableBtn)
        self.txtComponentName_14.textChanged.connect(self.enableBtn)
        self.txtComponentName_15.textChanged.connect(self.enableBtn)
        self.txtComponentName_16.textChanged.connect(self.enableBtn)
        self.txtComponentName_17.textChanged.connect(self.enableBtn)
        self.txtComponentName_18.textChanged.connect(self.enableBtn)
        self.txtComponentName_19.textChanged.connect(self.enableBtn)
        self.txtComponentName_20.textChanged.connect(self.enableBtn)

        self.txtComponentCount_1.textChanged.connect(self.enableBtn)
        self.txtComponentCount_2.textChanged.connect(self.enableBtn)
        self.txtComponentCount_3.textChanged.connect(self.enableBtn)
        self.txtComponentCount_4.textChanged.connect(self.enableBtn)
        self.txtComponentCount_5.textChanged.connect(self.enableBtn)
        self.txtComponentCount_6.textChanged.connect(self.enableBtn)
        self.txtComponentCount_7.textChanged.connect(self.enableBtn)
        self.txtComponentCount_8.textChanged.connect(self.enableBtn)
        self.txtComponentCount_9.textChanged.connect(self.enableBtn)
        self.txtComponentCount_10.textChanged.connect(self.enableBtn)
        self.txtComponentCount_11.textChanged.connect(self.enableBtn)
        self.txtComponentCount_12.textChanged.connect(self.enableBtn)
        self.txtComponentCount_13.textChanged.connect(self.enableBtn)
        self.txtComponentCount_14.textChanged.connect(self.enableBtn)
        self.txtComponentCount_15.textChanged.connect(self.enableBtn)
        self.txtComponentCount_16.textChanged.connect(self.enableBtn)
        self.txtComponentCount_17.textChanged.connect(self.enableBtn)
        self.txtComponentCount_18.textChanged.connect(self.enableBtn)
        self.txtComponentCount_19.textChanged.connect(self.enableBtn)
        self.txtComponentCount_20.textChanged.connect(self.enableBtn)

        self.cboCollege.currentIndexChanged.connect(self.enableBtn)

        self.chkGraduate.stateChanged.connect(self.enableBtn)

        self.btnClear.clicked.connect(self.stateClear)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.saveData)


    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        with open(filePath, "r") as f:
            data = [line for line in f.read().splitlines()]

        print(data)
        name = re.search(r'>(.)+<',str(data[2]))
        name = re.search(r'([^><])+', name.group()) #remove the '><
        self.txtStudentName.setText(name.group())
        
        grad = re.search(r'false|true', str(data[2]))
        if grad.group() == 'true':
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)

        ID = re.search(r'>(.)+<', str(data[3]))
        ID = re.search(r'[^><]+', ID.group())
        #ID = re.search(r'([^</StudentID>]\w+)',str(data[3]))
        self.txtStudentID.setText(ID.group())

        college = re.search(r'>([a-zA-Z\s])+<', str(data[4]))
        college = re.search(r'[a-zA-Z\s]+', college.group())  # remove the '><
        #college = re.search(r'([^</College>]\w+)',str(data[4]))
        index = self.cboCollege.findText(college.group())
        self.cboCollege.setCurrentIndex(index)

        compID = []
        compCount = []
        for item in data[6:-2]:
            temp = re.search(r'"(.)+"', str(item))
            temp = str(temp.group()).split()
            compID.append(temp[0].replace('"',''))
            count = re.search(r'=(.)+', temp[1].replace('"',''))
            count = re.search('[^=]+', count.group())
            compCount.append(count.group())

        if len(compID) > 20:
            for i in range(20):
                self.componentName[i].setText(compID[i])
                self.componentCount[i].setText(compCount[i])
        else:
            for i in range(len(compID)):
                self.componentName[i].setText(compID[i])
                self.componentCount[i].setText(compCount[i])


        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def saveData(self):
        if self.chkGraduate.isChecked() == True:
            grad = '"true"'
        else:
            grad = '"false"'

        studentName = self.txtStudentName.text()
        studentID = self.txtStudentID.text()
        college = self.cboCollege.itemText(self.cboCollege.currentIndex())
        compName = []
        compCount = []

        for items in self.componentName:
            if items.text() == "":
                pass
            else:
                compName.append(items.text())

        for counts in self.componentCount:
            if counts.text() == "":
                pass
            else:
                compCount.append(counts.text())

        with open("target.xml", "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<Content>\n')
            f.write('   <StudentName graduate="{}">{}</StudentName>\n'.format(grad,studentName))
            f.write('   <StudentID>{}</StudentID>\n'.format(studentID))
            f.write('   <College>{}</College>\n'.format(college))
            f.write('   <Components>\n')
            for components in compName:
                f.write('       <Component name="{}" count="{}" />\n'.format(components,compCount[compName.index(components)]))
            f.write(    '</Components>\n')
            f.write('</Content>')



    def enableBtn(self):
        if len(self.txtStudentName.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtStudentID.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_1.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_2.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_3.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_4.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_5.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_6.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_7.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_8.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_9.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_10.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_11.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_12.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_13.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_14.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_15.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_16.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_17.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_18.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_19.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_20.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_1.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_2.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_3.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_4.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_5.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_6.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_7.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_8.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_9.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_10.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_11.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_12.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_13.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_14.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_15.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_16.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_17.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_18.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_19.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_20.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif self.cboCollege.currentIndex() != 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif self.chkGraduate.isChecked() == True:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)
            self.btnLoad.setEnabled(True)


    def stateClear(self):
        for input in self.student:
            input.clear()

        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)

        for items in self.componentName:
            items.clear()

        for counts in self.componentCount:
            counts.clear()

        self.btnSave.setEnabled(False)


#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
