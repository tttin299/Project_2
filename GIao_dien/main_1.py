#lll remove warning message
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from textblob import TextBlob
# required library
from PyQt5 import QtWidgets, uic, QtCore, QtGui
# from PyQt5 import QAbstractItemView
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from local_utils import detect_lp
from os.path import splitext,basename
from keras.models import model_from_json
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.mobilenet_v2 import preprocess_input
from sklearn.preprocessing import LabelEncoder
import glob
from threading import Thread
import serial
import threading
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import time
import datetime#sua
import mysql.connector
import time
import qimage2ndarray
from PIL import Image
from PIL import ImageDraw
import struct

a = 0
chuoi = []


# chuoikt = [3,3,3,3,3,A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5]
# chuoikt = [3,3,3,3,3,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45]
#############0 1 2 3 4 5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
# chuoikt = [3] * 14792

s = serial.Serial(port='COM8',baudrate=115200, timeout=0.001)

rfid = ''
rfid_truoc = ''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="do_an"
    )


def ChoDau():    
    chuoikt = [3] * 14792 
  
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ChoDau FROM dau_xe") 
    for data in mycursor.fetchall():
        if data[0][0] == 'A':
            i = data[0]
            chuoikt[int(i[1]) + 4] = int('1' + i[1])

        if data[0][0] == 'B':
            i = data[0]          
            chuoikt[int(i[1]) + 9] = int('2' + i[1])
        
        if data[0][0] == 'C':
            i = data[0]          
            chuoikt[int(i[1]) + 14] = int('3' + i[1])

        if data[0][0] == 'D':
            i = data[0]          
            chuoikt[int(i[1]) + 19] = int('4' + i[1])
    send = s.write(chuoikt)
    # print(chuoikt)

    
ChoDau()



class Main(QtWidgets.QMainWindow): 
    # global cam_ngoai
    # global cam_trong
    
    def __init__(self):
        
        super(Main, self).__init__()
        uic.loadUi('Giao_dien/main.ui', self)

        title = "Main"
        self.setWindowTitle(title) 
        # Anh xa
            
        self.imgTruoc_1 = self.findChild(QtWidgets.QLabel, 'imgTruoc_1')
        self.imgSau_1 = self.findChild(QtWidgets.QLabel, 'imgSau_1')
        self.imgTruoc_2 = self.findChild(QtWidgets.QLabel, 'imgTruoc_2')
        # self.imgSau_2 = self.findChild(QtWidgets.QLabel, 'imgSau_2')
        self.imgCamTruoc = self.findChild(QtWidgets.QLabel, 'imgCamTruoc')
        self.imgCamSau = self.findChild(QtWidgets.QLabel, 'imgCamSau')

        self.btnQL = self.findChild(QtWidgets.QPushButton,'btnQL') 
        self.txtID = self.findChild(QtWidgets.QLabel,'txtID')  
        self.txtVaoRa = self.findChild(QtWidgets.QLabel, 'txtVaoRa')
        self.txtVaoRa.setStyleSheet("")    
        self.txtBienSo_1 = self.findChild(QtWidgets.QLabel,'txtBienSo_1')
        self.txtBienSo_2 = self.findChild(QtWidgets.QLabel,'txtBienSo_2')
        self.txtTGVao = self.findChild(QtWidgets.QLabel,'txtTGVao') 
        self.txtTGRa = self.findChild(QtWidgets.QLabel,'txtTGRa')  
        self.txtSL = self.findChild(QtWidgets.QLabel,'txtSL')  
        self.txtTien = self.findChild(QtWidgets.QLabel,'txtTien') 

        # self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')   


        self.btnQL.clicked.connect(self.ClickQL)
        self.show()

    def ClickQL(self):             
        window1.close()
        window2.__init__()
        window2.show()


class Anh(QtWidgets.QMainWindow):#sua
    
    def __init__(self):
        # global cam_ngoai
        # global cam_trong
       
        super(Anh, self).__init__()
        uic.loadUi('Giao_dien/anh.ui', self)     

        title = "Anh"
        self.setWindowTitle(title) 
        self.btnBack.clicked.connect(self.ClickBack)
        self.img_1 = self.findChild(QtWidgets.QLabel, 'img_1')
        self.img_2 = self.findChild(QtWidgets.QLabel, 'img_2')

        # self.tableWidgetQL = self.findChild(QtWidgets.QTableWidget, 'tableWidgetQL')
        # self.tableWidgetQL.setSelectionMode(QAbstractItemView.MultiSelection)

        self.btnBack.clicked.connect(self.ClickBack)
        # self.btnXoaHis.clicked.connect(self.ClickXoaHis)
        # self.btnTim.clicked.connect(self.ClickTim)
        # self.btnXemHis.clicked.connect(self.ClickXemHis)
    def ClickBack(self):
        window3.hide()
        # window2.__init__()
        # window2.show()


class History(QtWidgets.QMainWindow):#sua
  
    def __init__(self):
   
        super(History, self).__init__()
        uic.loadUi('Giao_dien/history.ui', self)     

        title = "History"
        self.setWindowTitle(title) 
        self.btnBack = self.findChild(QtWidgets.QPushButton, 'btnBack')
       
        self.btnTim = self.findChild(QtWidgets.QPushButton, 'btnTim')
        self.btnXemHis = self.findChild(QtWidgets.QPushButton, 'btnXemHis')
       

        self.edtBienSo = self.findChild(QtWidgets.QLineEdit, 'edtBienSo')
        self.imgClear = self.findChild(QtWidgets.QLabel, 'imgClear')

        self.tableWidgetQL = self.findChild(QtWidgets.QTableWidget, 'tableWidgetQL')
        # self.tableWidgetQL.setSelectionMode(QAbstractItemView.MultiSelection)

        self.btnBack.clicked.connect(self.ClickBack)
        # self.btnXoaHis.clicked.connect(self.ClickXoaHis)
        self.btnTim.clicked.connect(self.ClickTim)
        self.btnXemHis.clicked.connect(self.ClickXemHis)
        self.imgClear.mousePressEvent = self.ClickImgClear
        self.tableWidgetQL.cellClicked.connect(self.cellClick)

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM quan_ly")
           
        # mycursor.execute("INSERT INTO dau_xe (ID, BienSo) VALUES (%s,%s)",[rfid,final_string])
        # dbase = sqlite3.connect('My_data.db') 
        # query = "SELECT * FROM history_records"
        # result = dbase.execute(query)
        self.Update_Table(mydb,mycursor)


    # def selectRows(self,selection: list):
    #     for i in selection:
    #         self.tableWidgetQL.setItem(row[0],col[0],item)

    # def cellClick(self,row,col):
    #     # self.tableWidgetQL(row,col)
    #     # def getImageLabel(self,image):
    #     # item1 = self.tableWidgetQL.item(row, 5)
    #     # item2 = self.tableWidgetQL.item(row, 6)
    #     window3.__init__()
    #     window3.show()

    #     mycursor = mydb.cursor()
    #     mycursor.execute("SELECT AnhVao FROM quan_ly")
    #     # print(mycursor.fetchall()[row][0])

    #     # dbase.commit()
    #     # for row_number, row_data in enumerate(mycursor):
    #     #     for column_number, data in enumerate(row_data):              
    #     #         if(column_number == 5 ):
    #     #             item=self.getImageLabel(data)



        
        # item1 = bytes(item1.text(),'utf-8')
        # item2 = bytes(item2.text(),'utf-8')
    def cellClick(self,row,col):
        # self.tableWidgetQL(row,col)
        # def getImageLabel(self,image):
        item1 = self.tableWidgetQL.item(row, 0)
        item2 = self.tableWidgetQL.item(row, 1)
        item3 = self.tableWidgetQL.item(row, 2)
        # item1 = bytes(item1.text(),'utf-8')
        # item2 = bytes(item2.text(),'utf-8')
        # print(str(item1.text()))
        item1  = str(item1.text())
        item2  = str(item2.text())
        item3  = str(item3.text())

        window3.__init__()
        window3.show()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT AnhVao FROM quan_ly WHERE ID = %s AND BienSo = %s AND ThoiDiemVao = %s",
                        [item1,item2,item3])    

        window3.img_1.setPixmap(window2.getImageLabel(mycursor.fetchall()[0][0]))
        mydb.commit()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT AnhRa FROM quan_ly WHERE ID = %s AND BienSo = %s AND ThoiDiemVao = %s",
                        [item1,item2,item3]) 
        window3.img_2.setPixmap(window2.getImageLabel(mycursor.fetchall()[0][0]))
        mydb.commit()



    def ClickBack(self):
        window2.close()
        window1.__init__()
        window1.show()

    # def ClickXoaHis(self):
    #     dbase = sqlite3.connect('My_data.db')
    #     query = "DELETE FROM history_records"
    #     result = dbase.execute(query)
    #     self.Update_Table(dbase,result)


    def ClickImgClear(self, event):   
        # print('a')          
        self.edtBienSo.clear()
    

    def ClickTim(self):
        str_Bs=self.edtBienSo.text()
        # str_id=self.txtID.text()
        # kiểm tra đã nhập tủ cần tìm
        if len(str_Bs)>0: 
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM quan_ly WHERE BienSo = %s",
                    [str_Bs])   
            # if (len(str_id)==0):
            #     result = dbase.execute("SELECT * FROM history_records WHERE Tu = ? ORDER BY ID, Tu ASC",[str_Tu])  
            #     self.Update_Table(dbase,result)
            # elif (len(str_Tu)==0):
            #     result = dbase.execute("SELECT * FROM history_records WHERE ID = ? ORDER BY ID, Tu ASC",[str_id])  
            #     self.Update_Table(dbase,result)
            # else:
            #     check1 = dbase.execute("SELECT * FROM history_records WHERE  ID = ? AND Tu = ?",[str_id,str_Tu])
            if (len(mycursor.fetchall())==0 ): 
                self.showMessageBox('Error','Dữ liệu không tồn tại!') 
            else:
                mycursor.execute("SELECT * FROM quan_ly WHERE BienSo = %s",
                    [str_Bs]) 
                self.Update_Table(mydb,mycursor)
            #         result = dbase.execute("SELECT * FROM history_records WHERE ID = ? AND Tu = ? ORDER BY ID, Tu ASC",[str_id,str_Tu])  
            
        else:
            self.showMessageBox('Error','Mời bạn nhập biển số xe!')  


    def ClickXemHis(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM quan_ly")
        self.Update_Table(mydb,mycursor)

    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_() 

    def getImageLabel(self,image):
        # frame=QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/thi/Pictures/iroman', 'Images (*.png, *.xmp *.jpg)')
        # link="C:/Users/thi/Pictures/girl/6.jpg"
        # picture = QtGui.QImage(link)
        
        imageLabel =QtWidgets.QLabel(self.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap=QtGui.QPixmap()

        
        pixmap.loadFromData(image,'png')
        # pixmap.loadFromData(image,'png')
        

        # imageLabel.setPixmap(pixmap)

        return pixmap


    def Update_Table(self,dbase,result):        
        self.tableWidgetQL.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetQL.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item=str(data)
                if(column_number != 5 and column_number != 6):
                    # item=self.getImageLabel(data)
                #     self.tableWidgetQL.setCellWidget(row_number, column_number,'')
                # else:
                    self.tableWidgetQL.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))



                # self.tableWidgetQL.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        # self.tableWidgetQL.resizeRowsToContents ()
        dbase.commit()


def load_model(path):
    try:
        path = splitext(path)[0]
        with open('%s.json' % path, 'r') as json_file:
            model_json = json_file.read()
        model = model_from_json(model_json, custom_objects={})
        model.load_weights('%s.h5' % path)
        print("Loading model successfully...")
        return model
    except Exception as e:
        print(e)

wpod_net_path = "wpod-net.json"
wpod_net = load_model(wpod_net_path)

def preprocess_image(img,resize=False):
    # img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = img / 255
    if resize:
        img = cv2.resize(img, (224,224))
    return img

def get_plate(image_path, Dmax=608, Dmin = 256):
    vehicle = preprocess_image(image_path)
    ratio = float(max(vehicle.shape[:2])) / min(vehicle.shape[:2])
    side = int(ratio * Dmin)
    bound_dim = min(side, Dmax)
    _ , LpImg, _, cor = detect_lp(wpod_net, vehicle, bound_dim, lp_threshold=0.5)
    return vehicle, LpImg, cor

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model_weight.h5")
print("[INFO] Model loaded successfully...")

labels = LabelEncoder()
labels.classes_ = np.load('license_character_classes.npy')
print("[INFO] Labels loaded successfully...")



def xuLi():
    # ChoDau()
    global chuoi
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM dau_xe WHERE ID = (%s)",[rfid])

    if(len(mycursor.fetchall()) == 0):
        # print('a')
        ret, frame_truoc_tmp = cam_trong.read()
        ret, frame_sau_tmp = cam_ngoai.read()
        # frame_sau_tmp = frame
        # print('xe vao')
    else:
        # print('b')
        ret, frame_truoc_tmp = cam_ngoai.read()
        ret, frame_sau_tmp = cam_trong.read()
    
    mydb.commit()
#########################
    # path = input("Nhap vao duong dan anh: ")
    # frame_truoc = xuli_camera(frame_truoc_tmp)
    # frame_sau_tmp = cv2.imread(path)

    # frame_sau = frame_sau_tmp
    # frame = cv2.cvtColor(frame_sau, cv2.COLOR_BGR2RGB)
   
    # img = qimage2ndarray.array2qimage(frame)
    # frame_sau = QtGui.QPixmap.fromImage(img)

    # # frame_sau_tmp = cv2.imread(path)
    # frame_sau_tmp = cv2.resize(frame_sau_tmp, (640,480))
    
######################
    frame_truoc = xuli_camera(frame_truoc_tmp)
    frame_sau = xuli_camera(frame_sau_tmp)

##################    
 

    
    window1.imgTruoc_1.setPixmap(QtGui.QPixmap(frame_truoc))
    window1.imgSau_1.setPixmap(QtGui.QPixmap(frame_sau))
  
    # vehicle, LpImg, cor = get_plate(path)
    vehicle, LpImg, cor = get_plate(frame_sau_tmp)
    if (LpImg == 0):
        
        window1.txtBienSo_1.setPixmap(QtGui.QPixmap("Giao_dien/tickx.png"))
    else:   
   

        if (len(LpImg)): #check if there is at least one license image
            
            plate_image = cv2.convertScaleAbs(LpImg[0], alpha=(255.0))

            plate_image = plate_image[10:plate_image.shape[0] - 10, 10:plate_image.shape[1] - 10]


        gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
        
        # blur  = gray
        # blur = cv2.GaussianBlur(gray,(7,7),0) # lam mo anh de giam nhieu, ma tran cang lon se cang mo, kich thuoc ma tran la so le
        # blur = gray
        kernel = np.ones((3,3),np.float32)/25
        blur = cv2.filter2D(gray,-1,kernel)
        
        # binary = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY_INV,9,3)

        # binary2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY,9,3)
        
        # binary = cv2.GaussianBlur(binary,(5,5),0)
        
        # binary2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        #         cv2.THRESH_BINARY,11,2)
        # binary  = cv2.GaussianBlur(binary,(5,5),0)
        # Applied inversed thresh_binary 
        # binary = cv2.threshold(blur, 180, 255,
        #                     cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]# chu trang
        # cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        # cv2.ADAPTIVE_THRESH_MEAN_C

        binary = cv2.threshold(blur, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 255,
                            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]# chu trang dung cho bien so nen trang

        binary2 = cv2.threshold(blur, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]# dung cho bien so nen xanh

       

        kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        

        #! TODO
        # thre_mor = binary[10:binary.shape[0] - 10, 10:binary.shape[1] - 10] # y, x
        # thre_mor = cv2.copyMakeBorder(thre_mor, 10, 10, 10, 10, cv2.BORDER_CONSTANT) # t b l r
        # thre_mor = cv2.morphologyEx(thre_mor, cv2.MORPH_DILATE, kernel3)
        # thre_mor = binary
        # thre_mor = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel3)
        thre_mor = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel3)
        thre_mor = cv2.copyMakeBorder(thre_mor, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
        # #! TODO
        # thre_mor = thre_mor[10:thre_mor.shape[0] - 10, 10:thre_mor.shape[1] - 10]
        # thre_mor = cv2.copyMakeBorder(thre_mor, 10, 10, 10, 10, cv2.BORDER_CONSTANT) 
        # thre_mor2 = binary2[10:binary2.shape[0] - 10, 10:binary2.shape[1] - 10] # y, x
        # thre_mor2 = cv2.copyMakeBorder(thre_mor2, 0, 10, 20, 20, cv2.BORDER_CONSTANT) # t b l r
        thre_mor2 = cv2.morphologyEx(binary2, cv2.MORPH_DILATE, kernel3)
        thre_mor2 = cv2.copyMakeBorder(thre_mor2, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
        # cv2.imwrite("Anh0",thre_mor)
        # cv2.imwrite("Anh1",thre_mor2)
        # cv2.imwrite('Anh_train/bienso.png', thre_mor)
        def sort_contours(cnts,reverse = False):
            i = 0
            boundingBoxes = [cv2.boundingRect(c) for c in cnts]
            (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                                key=lambda b: b[1][i], reverse=reverse))
            return cnts

        # bien so trang
        # cont, _  = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Phat hien nhung chu cai trong anh
        cont, _  = cv2.findContours(thre_mor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        j = 0
        # print('cont' + str(len(cont)))
        if len(cont) <= 5:
            j = 1
            # print('cont1' + str(len(cont)))
            cont, _  = cv2.findContours(thre_mor2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # print('cont2' + str(len(cont)))


        # print('cont3' + str(len(cont)))
        if (len(cont)<=5):
            window1.txtBienSo_1.setPixmap(QtGui.QPixmap("Giao_dien/tickx.png"))
        else: 


        # creat a copy version "test_roi" of plat_image to draw bounding box
            test_roi = plate_image.copy()

            # Initialize a list which will be used to append charater image
            crop_characters = []
            crop_characters_1 = []
            crop_characters_2 = []

            # define standard width and height of character
            digit_w, digit_h = 30, 60

            for c in sort_contours(cont):
                (x, y, w, h) = cv2.boundingRect(c)
                ratio = h/w
                if plate_image.shape[0] > 150:
                    if 1<=ratio<=5: # Only select contour with defined ratio                      
                        if 0.2< h/plate_image.shape[0] <0.6: # Select contour which has the height larger than 50% of the plate
                            # Draw bounding box arroung digit number
                        # print('a')
                            cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)

                            # Sperate number and gibe prediction
                            curr_num = thre_mor[y:y+h,x:x+w]
                            curr_num2 = thre_mor2[y:y+h,x:x+w]
                            curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
                            curr_num2 = cv2.resize(curr_num2, dsize=(digit_w, digit_h))
                          
                            if j==1:                  
                                curr_num = curr_num2

                            if y < 70:
                                crop_characters_1.append(curr_num)
                            else:
                                crop_characters_2.append(curr_num)            
                else:
                    if 1<=ratio<=3.5: # Only select contour with defined ratio
                        if h/plate_image.shape[0]>=0.5: # Select contour which has the height larger than 50% of the plate
                            # Draw bounding box arroung digit number
                            cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)
                            # Sperate number and gibe prediction
                            curr_num = thre_mor[y:y+h,x:x+w]
                            curr_num2 = thre_mor2[y:y+h,x:x+w]
                            curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
                            curr_num2 = cv2.resize(curr_num2, dsize=(digit_w, digit_h))
                          
                            if j==1:                  
                                curr_num = curr_num2

                            crop_characters_1.append(curr_num)
            ## cat hinh ra

            len1 = len(crop_characters_1)
            len2 = len(crop_characters_2)
            crop_characters = crop_characters_1 + crop_characters_2


            def updateTableQL(str_id,str_bs,str_anh,vaoRa,thoiGian):    #sua
                
                if vaoRa == 0:
                    mycursor.execute("INSERT INTO quan_ly(ID,BienSo,ThoiDiemVao,ThoiDiemRa,ThoiGianDau,AnhVao,TienPhi) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                                ,[str_id,str_bs,thoiGian,0,0,str_anh,4000]) 
                    
                else:    
                    lucVao = 0
                    lucRa = ''
                    tgDau = 0
                    tienPhi = 0
                    # mycursor.execute("SELECT ThoiDiemVao FROM quan_ly WHERE ID = %s AND ThoiDiemRa =  %s ",[rfid,'0'])    
                    # print(len(mycursor.fetchall))         
                    # print(str(str_anh))
                    mycursor.execute("UPDATE quan_ly SET ThoiDiemRa = %s, AnhRa =  %s WHERE ID = %s AND ThoiDiemRa =  %s"
                                ,[thoiGian,str_anh,str_id,'0']) 
                    # lucRa = int(datetime.datetime.now().hour);
                    lucRa = thoiGian;
                    window1.txtTGRa.setText(lucRa) 
                    lucRa = lucRa.split('h')
                    lucRa = int(lucRa[0].split('_')[-1])
                    # crop = name.split('_')
                    # mycursor.execute("SELECT * FROM dau_xe WHERE ID = (%s)",[rfid])
                    
                    mydb.commit()

                    mycursor2 = mydb.cursor()
                    mycursor2.execute("SELECT ThoiDiemVao FROM quan_ly WHERE ID = %s AND ThoiDiemRa = %s AND AnhRa =  %s"
                                ,[str_id, thoiGian, str_anh]) 

                    lucVao = mycursor2.fetchall()[0][0]
                    window1.txtTGVao.setText(lucVao)
                    lucVao = lucVao.split('h')
                    lucVao = int(lucVao[0].split('_')[-1])
                    tgDau = lucRa - lucVao
                    if tgDau > 0:
                        tienPhi  = 8000
                    else:
                        tienPhi  = 4000

                    mydb.commit()
                    mycursor3 = mydb.cursor()
                    # print("thoi gian va0: "+ str(lucVao))
                    mycursor3.execute("UPDATE quan_ly SET ThoiGianDau = %s, TienPhi = %s WHERE ID = %s AND ThoiDiemRa = %s AND AnhRa =  %s"
                                ,[str(tgDau), tienPhi, str_id,thoiGian, str_anh]) 

                    window1.txtTien.setText(str(tienPhi))
                    # tgDau = str(lucRa - lucVao)

                    

                mydb.commit()

            def predict_from_model(image,model,labels):
                image = cv2.resize(image,(32,32))
                image = np.reshape(image, (32, 32, 1))
                prediction = labels.inverse_transform([np.argmax(model.predict(image[np.newaxis,:]))])
                return prediction

       
            cols = len(crop_characters)

            final_string = ''
            for i,character in enumerate(crop_characters):
                title = np.array2string(predict_from_model(character,model,labels))
                cv2.imwrite('Anh_train/' + title + '.png', character)
                final_string+=title.strip("'[]")

               
            if(len2 == 0):
                window1.txtBienSo_1.setText(final_string)
            else:
                window1.txtBienSo_1.setText(final_string[:len1] + "\n" + final_string[len1:])
       
            date_now,time = UpdateTime();                 
            mycursor = mydb.cursor()
            thoiGian = date_now + '_' + time 
            # print('rfid' + str(len(rfid)))
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM dau_xe WHERE ID = (%s)",[rfid])
            if(len(mycursor.fetchall()) == 0):
                mycursor.execute("INSERT INTO dau_xe (ID, BienSo) VALUES (%s,%s)",[rfid,final_string])
                window1.txtVaoRa.setStyleSheet("background-color: rgb(11, 149, 255); color: rgb(255, 255, 255);border-style: outset;border-width: 2px;border-radius: 10px;border-color: white;")
                window1.txtVaoRa.setText("Moi xe vao"),
                print('Moi xe vao')
               

                filePath,blob = LuuAnh(final_string,frame_truoc_tmp,frame_sau_tmp)
                GuiAnh(filePath)

                chuoi[0] = 2
                chuoi[1] = 2
                chuoi[2] = 2
                chuoi[3] = 2
                chuoi[4] = 2
                chuoi[5] = 2
                chuoi[6] = 2
                chuoi[7] = 2
                chuoi[8] = 2
                chuoi[9] = 2
                send = s.write(chuoi)
                
                chuoi = []
           
                updateTableQL(rfid,final_string,blob,0,thoiGian)
                
            else:
               
                imgTruoc,doiTuong = TimAnh(rfid,final_string)
                # print('doituong: '+str(doiTuong))

                if(doiTuong == 0):
                    # print("aaaaaa")
                    window1.txtVaoRa.setStyleSheet("")             
                    window1.txtVaoRa.setText("Sai bien so")
                else:    
                    # imgTruoc = xuli_camera(imgTruoc)
                    # imgSau = xuli_camera(imgSau)

                    # window1.imgTruoc_2.setPixmap(QtGui.QPixmap(imgTruoc))
                    # window1.imgSau_2.setPixmap(QtGui.QPixmap(imgSau))

                    window1.imgTruoc_2.setPixmap(imgTruoc)
                    # window1.imgSau_2.setPixmap(imgSau)
                    
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT BienSo FROM dau_xe WHERE ID = (%s)",[rfid])
                    window1.txtBienSo_2.setText(mycursor.fetchone()[0])
                    mycursor.execute("SELECT BienSo FROM dau_xe WHERE ID = (%s)",[rfid])
                    if(mycursor.fetchone()[0] == final_string):                   
                        window1.txtVaoRa.setStyleSheet("background-color: rgb(252, 206, 38); color: rgb(255, 255, 255);border-style: outset;border-width: 2px;border-radius: 10px;border-color: white;")             
                        window1.txtVaoRa.setText("Moi xe ra")
                        mycursor.execute("DELETE FROM dau_xe WHERE ID = %s",[rfid])
                   
                        filePath,blob = LuuAnh(final_string,frame_truoc_tmp,frame_sau_tmp)
                        GuiAnh(filePath)
                        # ChoDau()
                        # chuoi[0] = 3
                        # chuoi[1] = 3
                        # chuoi[2] = 3
                        # chuoi[3] = 3
                        # chuoi[4] = 3
                        
                        # ChoDau()
                        # send = s.write(chuoi)

                        chuoi[0] = 0
                        chuoi[1] = 0
                        chuoi[2] = 0
                        chuoi[3] = 0
                        chuoi[4] = 0
                        
                        send = s.write(chuoi)

                        chuoi = []
                        ChoDau()
                        
                        updateTableQL(rfid,final_string,blob,1,thoiGian)

                    else:
                        window1.txtVaoRa.setStyleSheet("")             
                        window1.txtVaoRa.setText("Sai bien so")

                

            mydb.commit()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT ID FROM dau_xe") 
            window1.txtSL.setText(str(len(mycursor.fetchall())))

            window1.txtID.setText("")        
            window1.txtVaoRa.setText("")
            window1.txtTGVao.setText("")        
            window1.txtTGRa.setText("")
            window1.txtVaoRa.setStyleSheet("")
            window1.imgTruoc_1.setPixmap(QtGui.QPixmap(""))
            window1.imgSau_1.setPixmap(QtGui.QPixmap(""))
            window1.imgTruoc_2.setPixmap(QtGui.QPixmap(""))
            # window1.imgSau_2.setPixmap(QtGui.QPixmap(""))
            window1.txtBienSo_1.setText("")
            window1.txtBienSo_2.setText("")

def GuiAnh(filePath):
    isSWAP = True
    im=Image.open(filePath)
    im = im.resize((86,86)) 

    image_height = im.size[1]
    image_width = im.size[0]
 
    outfile = open('sysyyyyyy',"w")
  
    pix = im.load()  #load pixel array
    
    global chuoi
    
  
    for h in range(image_height):
        for w in range(image_width):
            if ((h * 16 + w) % 16 == 0):
                print (" ", file=outfile)
                print ("\t\t", file=outfile, end = '')

            if w < im.size[0]:
        
                R=pix[w,h][0]>>3 #/8
                G=pix[w,h][1]>>2 #/4
                B=pix[w,h][2]>>3 #/8
            
                rgb = (R<<11) | (G<<5) | B
                
                if (isSWAP == True):
                    swap_string_low = rgb >> 8
                    swap_string_high = (rgb & 0x00FF) << 8
                    swap_string_high = swap_string_high >> 8
                    swap_string = swap_string_low | swap_string_high
                    
                    # print ("%d," %(swap_string_low), file=outfile, end = '')
                    # print ("%d," %(swap_string_high), file=outfile, end = '')
                    chuoi.append(swap_string_low)
                    chuoi.append(swap_string_high)                
                else:
                    print ("0x%04x," %(rgb), file=outfile, end = '')
            else:
                rgb = 0
        #
    send = s.write(chuoi)


    # ChoDau()
    # send = s.write(chuoikt)


def UpdateChodau(chodau,rfid_truoc):    
    mycursor = mydb.cursor()
    mycursor.execute(mycursor.execute("UPDATE dau_xe SET ChoDau = %s WHERE ID = %s"
                                ,[chodau,rfid_truoc]) )
    mydb.commit()


c = [0] * 14792
send = s.write(c)

def doit():
    while (True):
        rfid_tmp = s.readline().decode('ascii')
        if(rfid_tmp!=''):   
            global rfid 
            global rfid_truoc   
        
            rfid = rfid_tmp.rstrip('\n')
             
            # print(rfid)
         
            if(len(rfid)==2):
                chodau = rfid
                UpdateChodau(chodau,rfid_truoc)

                ChoDau()
            
                print('Update cho dau ' + rfid_truoc + ' la ' + chodau)  
                
                

                window1.txtID.setText("")
            
                window1.txtVaoRa.setText("")
                window1.txtVaoRa.setStyleSheet("")

                window1.imgTruoc_1.setPixmap(QtGui.QPixmap(""))
                window1.imgSau_1.setPixmap(QtGui.QPixmap(""))
                window1.imgTruoc_2.setPixmap(QtGui.QPixmap(""))
                # window1.imgSau_2.setPixmap(QtGui.QPixmap(""))

                window1.txtBienSo_1.setText("")
                window1.txtBienSo_2.setText("")

                # c = [0] * 14792
                # send = s.write(c)
 
            else:
                rfid = rfid[8:16]
                rfid_truoc = rfid
                window1.txtID.setText(str(rfid))
                xuLi()

            
          

cam_trong = cv2.VideoCapture(0) # cam o trong
cam_ngoai = cv2.VideoCapture(1) #cam o ngoai


def UpdateTime():
    now = datetime.date.today();
    date_now = "%s-%s-%s"%(now.day,now.month,now.year);
    time_t = datetime.datetime.now();
    time = "%sh%sm%ss"%(time_t.hour,time_t.minute,time_t.second);
    return date_now,time

def LuuAnh(final_string,IMG_PATH_1,IMG_PATH_2):
    date_now,time = UpdateTime();
    img = np.zeros([960, 640, 3])
    img[:480, :640, :] = IMG_PATH_1
    img[480:, :640:, :] = IMG_PATH_2
    cv2.imwrite('Anh_chup/'+ final_string +'_'+ date_now + '_' + time + '.png', img)
    filePath = 'Anh_chup/'+ final_string +'_'+ date_now + '_' + time + '.png'

    with open(filePath, 'rb') as stream:
        image = stream.read()

    # byte_array = QtCore.QByteArray()
    #              # Bind the byte array to the output stream
    # buffer = QtCore.QBuffer(byte_array)
    # buffer.open(QtCore.QIODevice.WriteOnly)
    # ba = QtCore.QByteArray()
    # bf = QtCore.QBuffer(ba)
    # bf.open(QtCore.QIODevice.WriteOnly)
    # bf.write(image)
    
    return filePath,image


def CatAnh(img):
    img = cv2.imread(img)
    # img_pad = np.zeros([480, 640, 3])
    IMG_PATH_1 = img[:480, :640, :]
    IMG_PATH_2 = img[480:, :640, :]

    return IMG_PATH_1,IMG_PATH_2

def TimAnh(rfid,final_string):
    # path = "Anh_chup"
    # file = os.listdir(os.path.expanduser(path))
    # # print(len(file))
    # for i in range(len(file)):
    #     name = file[len(file)-(i+1)]
    #     crop = name.split('_')
    #     # print(final_string)
    #     # print(crop[0])
    #     if (crop[0] == final_string):
    #         # print(crop[0])
    #         print('co_anh')
    #         imgTruoc, imgSau = CatAnh("Anh_chup/" + name) 
    #         return imgTruoc,imgSau           
    # return [],[]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT AnhVao FROM quan_ly WHERE ID = %s AND BienSo = %s AND ThoiDiemRa = %s",
                        [rfid,final_string,0])  
    doiTuong = len(mycursor.fetchall())
    pixmap = QtGui.QPixmap()
    if doiTuong == 0:
        return pixmap,doiTuong

    mycursor.execute("SELECT AnhVao FROM quan_ly WHERE ID = %s AND BienSo = %s AND ThoiDiemRa = %s",
                        [rfid,final_string,0])
    
    pixmap.loadFromData(mycursor.fetchall()[0][0],'png')
    mydb.commit()
    # dbase.commit()
    # retrun pixmap,pixmap
    return pixmap,doiTuong

# cv2.imwrite('img_pad.png', img_pad)
def xuli_camera(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = qimage2ndarray.array2qimage(frame)
    # img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(img)
    return pix 

def camera_trong():       
    while(True):
        ret,frame = cam_trong.read()
        window1.imgCamTruoc.setPixmap(xuli_camera(frame))  


def camera_ngoai():       
    while(True):
        ret,frame = cam_ngoai.read()
        window1.imgCamSau.setPixmap(xuli_camera(frame))  
       

def start_thread():
    t1 = Thread(target=doit)
    t1.start()
    t2 = Thread(target=camera_trong)
    t2.start()
    t3 = Thread(target=camera_ngoai)
    t3.start()


c = [0] * 14792
send = s.write(c)

app = QtWidgets.QApplication(sys.argv)


window2 = History()
window3 = Anh()
window1 = Main()

window1.show()
window2.close()
window3.close()


start_thread()

app.exec_()