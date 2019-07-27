import sys  # sys нужен для передачи argv в QApplication

sys.path.insert(0, '/home/harkhem/face_search/app/identificational-module')
sys.path.insert(0, '/home/harkhem/face_search/app/form')
sys.path.insert(0, '/home/harkhem/face_search/app/search-module')

import os 
from PyQt5 import QtWidgets,  QtGui, QtCore
from PyQt5.QtCore import Qt
import design  # Это наш конвертированный файл дизайна
from PIL import Image, ImageTk
import subprocess
import vk
import requests
import psycopg2
import sys
import face_recognition
import collectinformatiion
import find2
import searchgooglenew
import webbrowser as wb
from googlesearch import search
import time

#import sys, time, threading

 
 

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_3.clicked.connect(self.browse_folder)
        self.pushButton.clicked.connect(self.startsearch)
        self.listWidget_2.itemDoubleClicked.connect(self._handleDoubleClick)
        

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        global image_path
        image_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/harkhem/face_search/tests/test-foto')[0]
       

        if image_path:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.show_frame_in_display(image_path)


    def show_frame_in_display(self,image_path):
        #frame = QtGui.QWidget() #Replace it with any frame you will putting this label_image on it
        #label_Image = QtGui.QLabel(frame)
        image_profile = QtGui.QImage(image_path) #QImage object
        image_profile = image_profile.scaled(250,250, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect     
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))

        
    def startsearch(self):
        self.label_2.setText("start search")
        self.listWidget.clear() 
        #id=facerecognition.fcrcg(image_path)
        id=find2.fin(image_path)
        if id is None:
            self.label_2.setText("face not recognized")
            return
        #item = QtWidgets.QListWidgetItem('Страница в vk: '+''.join(id)+"\n")
        #item.setFlags( Qt.ItemIsSelectable )
        #self.listWidget.addItem(item)
        self.listWidget.addItem('Страница в vk: '+str(id)+"\n")
        col = collectinformatiion.collect(id)
        s=''
        #print(col)
        for k,v in  col.items():
            self.listWidget.repaint()
            self.listWidget_2.repaint()
            self.label_2.repaint()
            try:
                if s.join(v) != "":
                    accepted_strings = {'city', 'country'}
                    if s.join(k) in accepted_strings:
                        self.listWidget.addItem(" "+ s.join(k)+': ' + s.join(v["title"])  +"\n") 
                        
                    else:
                        self.listWidget.addItem(" "+ s.join(k)+': ' + s.join(v)  +"\n")
                        
            except:
                pass
        #time.sleep(5)
        self.sgoogle(col)
        self.label_2.clear()
        self.label_2.setText("finish search")
    def sgoogle(self,col):
        seti = searchgooglenew.globalsearch(col)
        print (seti)
        for i in seti:
            self.listWidget_2.addItem(""+ ''.join(i) +"\n")
    
    
    def _handleDoubleClick(self, item):
        texts = item.text()
        print(texts)
        wb.open_new_tab(''.join(texts))
        #item.setSelected(False)
    
                
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
