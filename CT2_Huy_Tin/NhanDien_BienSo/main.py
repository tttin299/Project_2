
############################## chay lan dau bi loi thi chay lai
# remove warning message
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# required library
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
import time
import tensorflow as tf
from tensorflow.python.platform import gfile

# truyền vào đường dẫn của mô hình train sẵn dùng để nhận diện biển số trong khung ảnh
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

# load model "wpod-net.json" lưu vào wpod_net
wpod_net_path = "wpod-net.json"
wpod_net = load_model(wpod_net_path)

# Hàm chuyển ảnh đầu vào dùng OpenCV để chuyển thành RGB để hiển thị
def preprocess_image(image_path,resize=False):
    img = cv2.imread(image_path)
    # cv2.imshow("Anh0",img)
    # Anh dau vao cv2 se hieu la kieu bgr
    # neu muon dung plt de hien thi thi phai chuyen sang rgb
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("Anh1",img)
    img = img / 255
    
    if resize:
        img = cv2.resize(img, (224,224))

    return img

# Hàm trích biển số từ ảnh
def get_plate(image_path, Dmax=608, Dmin = 256):
    vehicle = preprocess_image(image_path)
    ratio = float(max(vehicle.shape[:2])) / min(vehicle.shape[:2])
    side = int(ratio * Dmin)
    bound_dim = min(side, Dmax)
    _ , LpImg, _, cor = detect_lp(wpod_net, vehicle, bound_dim, lp_threshold=0.5)
 
    return vehicle, LpImg, cor

# load lấy trọng số model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model_weight.h5")
print("[INFO] Model loaded successfully...")

# load nhãn
labels = LabelEncoder()
labels.classes_ = np.load('license_character_classes.npy')


##########
#LOAD LABLES
# labels = []
# proto_as_ascii_lines = tf.gfile.GFile("labels.txt").readlines()
# for l in proto_as_ascii_lines:

#     labels.append(l.rstrip())

#LOAD MODEL
# graph = tf.Graph()
# graph_def = tf.compat.v1.GraphDef()
# # with open("model/saved_model.pb", 'rb') as f:
# #     graph_def.ParseFromString(f.read())
# # with graph.as_default():
# #     tf.import_graph_def(graph_def)

# model = load_model('model/saved_model.pb')
# sess = tf.Session(graph=graph)    
###########
print("[INFO] Labels loaded successfully...")

while(1):
    # test_image_path = "Plate_examples/china_motor_plate.jpg"
    # test_image_path = "Plate_examples/vietnam_car_rectangle_plate.jpg"
    # đọc đường dẫn ảnh input
    test_image_path = input("test_image_path: ")
    # test_image_path = "Plate_examples/germany_car_plate.jpg"
    # lấy biển số từ ảnh input
    vehicle, LpImg,cor = get_plate(test_image_path)
    
    ##1
    fig = plt.figure(figsize=(12,6))
    grid = gridspec.GridSpec(ncols=2,nrows=1,figure=fig)
    fig.add_subplot(grid[0])
    plt.axis(False)
    plt.imshow(vehicle)
    grid = gridspec.GridSpec(ncols=2,nrows=1,figure=fig)
    fig.add_subplot(grid[1])
    plt.axis(False)
    plt.imshow(LpImg[0])
    # plt.imshow(LpImg[1])
    # plt.show()

    if (len(LpImg)): #check if there is at least one license image
        # scale tính toán giá trị và chuyển đổi thành 8 bit
        plate_image = cv2.convertScaleAbs(LpImg[0], alpha=(255.0))
        # cắt bớt đường viền để lấy thành phần chi tiết của biển số
        plate_image = plate_image[10:plate_image.shape[0] - 10, 10:plate_image.shape[1] - 10]


        
        # chuyển ảnh sang thang độ xám
        gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
        # blur = cv2.GaussianBlur(gray,(5,5),0)
        kernel = np.ones((5,5),np.float32)/25
        # làm mở ảnh để giảm nhiễu, ma trận càng lớn sẽ càng mờ
        blur = cv2.filter2D(gray,-1,kernel)
        
        # do tập huấn luyện là chữ trắng trên nền đen. nên cần chuyển sang ảnh nhị phân đảo (đối với biển số chữ đen nền trắng)
        # binary = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY_INV,9,3)
          
        # binary = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY_INV,9,3)

        # binary2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY,9,3)


        binary = cv2.threshold(blur, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        binary2 = cv2.threshold(blur, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # do tập huấn luyện là chữ trắng trên nền đen. nên cần chuyển sang ảnh nhị phân (đối với biển số chữ trắng nền xanh)
        # binary2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY,9,3)
        
        kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
       
        # tăng cường độ màu trắng của các ký tự để dễ dàng nhận diện (thre_mor: biển số trắng đen, thre_mor2: biển số xanh trắng)
        thre_mor = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel3)
        thre_mor = cv2.copyMakeBorder(thre_mor, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

        thre_mor2 = cv2.morphologyEx(binary2, cv2.MORPH_DILATE, kernel3)
        thre_mor2 = cv2.copyMakeBorder(thre_mor2, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
        

    # visualize results hiển thị ra
    fig = plt.figure(figsize=(12,7))
    plt.rcParams.update({"font.size":18})
    grid = gridspec.GridSpec(ncols=2,nrows=4,figure = fig)
    plot_image = [plate_image, gray, blur, binary,binary2,thre_mor,thre_mor2]
    plot_name = ["plate_image","gray","blur","binary","binary2","dilation","dilation2"]

    for i in range(len(plot_image)):
        fig.add_subplot(grid[i])
        plt.axis(False)
        # plt.title(plot_name[i])
        if i ==0:
            plt.imshow(plot_image[i])
        else:
            plt.imshow(plot_image[i],cmap="gray")

    # hàm sort_contours () để lấy đường viền của mỗi chữ số từ trái sang phải
    def sort_contours(cnts,reverse = False):
        i = 0
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][i], reverse=reverse))
        return cnts

    # tìm đối tượng màu trắng trên nền đen, trích dẫn ra số lượng đối tưởng
    cont, _  = cv2.findContours(thre_mor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    # hàm kiểm tra biển số chữ trắng nền đen
    j = 0
    print(len(cont))
    if len(cont) <= 5:
        j = 1
        cont, _  = cv2.findContours(thre_mor2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # creat a copy version "test_roi" of plat_image to draw bounding box
    test_roi = plate_image.copy()
    
    # test_roi = thre_mor.copy()
    
    # Initialize a list which will be used to append charater image
    # tạo các list để chứa các đối tượng ảnh
    crop_characters = []
    crop_characters_1 = []
    crop_characters_2 = []

    # định nghĩa chiều dài và chiều rộng của đối tượng
    digit_w, digit_h = 30, 60

    e  = 0   
    for c in sort_contours(cont):
        e  = e+ 1
        # lấy từng đường bao 
        (x, y, w, h) = cv2.boundingRect(c)
        ratio = h/w
        # print(plate_image.shape[0])
        # bien so doc
        if plate_image.shape[0] > 150:
            # print('bien so doc')
            # print("x")
            # lọc ký tự, loại bỏ những nhiễu không phải ký tự
            if 0.5<=ratio<=5:
                # Select contour which has the height larger than 50% of the plate
                # chọn đường biến mà có chiều cao lớn 
                if 0.2< h/plate_image.shape[0] <0.6: 
                    # Draw bounding box arroung digit number
                # print('a')
                    cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)

                    # Sperate number and gibe prediction
                    curr_num = thre_mor[y:y+h,x:x+w]
                    curr_num2 = thre_mor2[y:y+h,x:x+w]
                    curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
                    curr_num2 = cv2.resize(curr_num2, dsize=(digit_w, digit_h))
                    # plt.imshow(curr_num)
                    if j==1:
                  
                        curr_num = curr_num2

                    if y < 70:
                        crop_characters_1.append(curr_num)
                    else:
                        crop_characters_2.append(curr_num)
                    cv2.imwrite('Anh_train/' + str(e) + '.png', curr_num)
                    
        else:
            # print('bien so ngang')
            # bien so ngang
            if 1<=ratio<=4: # Only select contour with defined ratio
                # print(h/plate_image.shape[0])
                # print(plate_image.shape[0])
                if h/plate_image.shape[0]>=0.5: # Select contour which has the height larger than 50% of the plate
                    # Draw bounding box arroung digit number
                # print('a')
                    cv2.rectangle(test_roi, (x, y), (x + w, y + h), (255, 255,255), 2)
                    
                    # Sperate number and gibe prediction
                    curr_num = thre_mor[y:y+h,x:x+w]
                    curr_num2 = thre_mor2[y:y+h,x:x+w]
                    curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
                    curr_num2 = cv2.resize(curr_num2, dsize=(digit_w, digit_h))
                 
                    
                    # plt.imshow(curr_num)
                    # print(j)
                    if j==1:                  
                        curr_num = curr_num2
                    cv2.imwrite('Anh_train/' + str(e) + '.png', curr_num)
                    crop_characters_1.append(curr_num)
    ## cat hinh ra

    crop_characters = crop_characters_1 + crop_characters_2
    print("Detect {} letters...".format(len(crop_characters)))


    ##3

    # fig = plt.figure(figsize=(10,6))
    # plt.axis(False)
    # plt.imshow(test_roi,cmap='gray')
    # plt.savefig('grab_digit_contour.png',dpi=300)
    # plt.show()
    ##4

    fig = plt.figure(figsize=(14,4))
    grid = gridspec.GridSpec(ncols=len(crop_characters),nrows=1,figure=fig)

    for i in range(len(crop_characters)):
        fig.add_subplot(grid[i])
        plt.axis(False)
        plt.imshow(crop_characters[i],cmap="gray")
    #plt.savefig("segmented_leter.png",dpi=300)    

    # Load model architecture, weight and labels

    #  # pre-processing input images and pedict with model
    # def predict_from_model(image):
    #     t0 = time.time() 
    #     image = cv2.resize(image, dsize=(32, 32), interpolation = cv2.INTER_CUBIC)
    #     image = np.reshape(image, (32, 32, 1))
    #     #print(image.shape)

    #     np_image_data = np.asarray(image)
    #     #np_image_data = cv2.normalize(np_image_data.astype('float'), None, -0.5, .5, cv2.NORM_MINMAX)
    #     image_tensor = np.expand_dims(np_image_data,axis=0)

    #     #feed tensor into the network
    #     softmax_tensor = sess.graph.get_tensor_by_name('import/dense_2/Softmax:0')
    #     predictions = sess.run(softmax_tensor, {'import/conv2d_1_input:0': image_tensor})

    #     # print("prediction: " + predictions)
    #     predictions = np.squeeze(predictions)

    #     top_k = predictions.argsort()[-1:][::-1]
    #     # print(labels[top_k[0]])
    #     print("prediction time: " + str(time.time()-t0))
    #     return labels[top_k[0]]

    #     ##5
    #     # fig = plt.figure(figsize=(12,6))
    # t1 = time.time()
    # cols = len(crop_characters)
    # # grid = gridspec.GridSpec(ncols=cols,nrows=1,figure=fig)

    # final_string = ''
    # for i,character in enumerate(crop_characters):
    #     # fig.add_subplot(grid[i])
    #     title = np.array2string(predict_from_model(character))
    #     # plt.title('{}'.format(title.strip("'[]"),fontsize=100))
    #     final_string+=title.strip("'[]")
    # print('Bien so: ' + final_string)
    # print("prediction time total: "+ str(time.time()-t1))
    # pre-processing input images and pedict with model


    def predict_from_model(image,model,labels):
        image = cv2.resize(image,(32,32))
        image = np.reshape(image, (32, 32, 1))
        # image = np.stack((image,)*3, axis=-1)
        prediction = labels.inverse_transform([np.argmax(model.predict(image[np.newaxis,:]))])
        return prediction

    ##5
    # fig = plt.figure(figsize=(15,3))
    # cols = len(crop_characters)
    # grid = gridspec.GridSpec(ncols=cols,nrows=1,figure=fig)

    final_string = ''
    t1 = time.time()


    for i,character in enumerate(crop_characters):
        # t0 = time.time()
        
        fig.add_subplot(grid[i])
        title = np.array2string(predict_from_model(character,model,labels))   
        
        # print("prediction time " + str(time.time()-t0))
        plt.title('{}'.format(title.strip("'[]"),fontsize=100))
        final_string+=title.strip("'[]")
        
        plt.axis(False)
        plt.imshow(character,cmap='gray')

    
    print(final_string)
    print("prediction time: " + str(time.time()-t1))
    
    plt.show()
    # #plt.savefig('final_result.png', dpi=300)
