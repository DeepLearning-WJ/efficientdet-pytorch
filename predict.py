#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from efficientdet import EfficientDet
from PIL import Image

efficientdet = EfficientDet()

img = './img/street.jpg'
try:
    image = Image.open(img)
except:
    print('Open Error! Try again!')
else:
    r_image = efficientdet.detect_image(image)
    # 一闪而过
    r_image.show()
    while True:
        img = input("nothing")
    r_image.save('./img/street_r.jpg')
