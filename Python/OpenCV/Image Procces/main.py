import cv2

img = cv2.imread('img/test5.png')

qcd = cv2.QRCodeDetector()

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)

print(retval)

print (decoded_info)