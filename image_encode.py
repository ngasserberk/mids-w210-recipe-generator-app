import cv2

# img = cv2.imread('IMG_4080.jpg')

# image_height, image_width, _ = img.shape
# model_height, model_width = 300, 300
# x_ratio = image_width/model_width
# y_ratio = image_height/model_height

# resized_image = cv2.resize(img, (model_height, model_width))
# payload = cv2.imencode('.jpg', resized_image)[1].tobytes()

# print(payload)

# def print_img_name(image):
#     print(image)

def img_encode(img):

    #resize image
    #image_height, image_width, _ = img.shape
    model_height, model_width = 300, 300
    #x_ratio = image_width/model_width
    #y_ratio = image_height/model_height

    resized_image = cv2.resize(img, (model_height, model_width))
    payload = cv2.imencode('.jpg', resized_image)[1].tobytes()

    return payload