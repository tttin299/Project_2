#!/usr/bin/python
############################## chay lan dau bi loi thi chay lai
import sys
import os
import serial
from PIL import Image
from PIL import ImageDraw
import struct
c = []
#isSWAP = False
isSWAP = True
s = serial.Serial(port='COM8',baudrate=115200, timeout=0.001)

def GuiAnh(filePath):
    global c
    im=Image.open(filePath)
    ### nên resize thành hình vuông để dễ hiển thị
    ### kích thước phải tính toán trước để hiển thị đúng
    ### sẽ cần tạo một mảng kích thước 87x87x2 bên rtos để nhận mảng
    im = im.resize((87,87))
    print ("/* Image Width:%d Height:%d */" % (im.size[0], im.size[1]))

    image_height = im.size[1]
    image_width = im.size[0]

    outfile = open('sys',"w")
    print ("/* Image Width:%d Height:%d */" % (im.size[0], im.size[1]), file=outfile)

    pix = im.load()  #load pixel array

    c = [] 
    for h in range(image_height):
        for w in range(image_width):
            if ((h * 16 + w) % 16 == 0):
                print (" ", file=outfile)
                print ("\t\t", file=outfile, end = '')

            if w < im.size[0]:
                R=pix[w,h][0]>>3 #/8
                G=pix[w,h][1]>>2 #/4
                B=pix[w,h][2]>>3 #/8
                
                # 16 bit voi 
                # 5 bit R
                # 6 bit G
                # 5 bit B
                rgb = (R<<11) | (G<<5) | B
                # print(rgb)
                if (isSWAP == True):
                    swap_string_low = rgb >> 8
                    swap_string_high = (rgb & 0x00FF) << 8
                    swap_string_high = swap_string_high >> 8
                    # swap_string = swap_string_low | swap_string_high
                    
                    #### thêm vào mảng c để gửi UART
                    c.append(swap_string_low)
                    c.append(swap_string_high)
                    #### tạo ra một file chứa mảng
                    ####n có thể tạo file mã dec hoặc hex
                    print ("%d," %(swap_string_low), file=outfile, end = '')
                    print ("%d," %(swap_string_high), file=outfile, end = '')
                    
                    # print ("0x%02x," %(swap_string_low), file=outfile, end = '')
                    # print ("0x%02x," %(swap_string_high), file=outfile, end = '')
      
                else:
                    print ("0x%04x," %(rgb), file=outfile, end = '')                
            else:
                rgb = 0
    ### gửi mảng c với kích thước 87 x 87 x 2 = 15138 qua UART
    send = s.write(c)  
    print(send) 

while(True):
    filePath = input("Nhap vao duong dan hinh anh: ")
    GuiAnh(filePath)
# print(c[14999])


