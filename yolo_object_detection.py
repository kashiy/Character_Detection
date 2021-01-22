import cv2
import numpy as np
import glob
import random
import VideoToFrames
import os

def create_dir(dirname):
    # dirname = 'detected_objects'
    try:
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        else:
            files = glob.glob(os.getcwd() + "\\" + dirname + "\\*")
            for f in files:
                os.remove(f)
    except OSError:
        print('Error: Creating directory of ' + dirname)


# Load Yolo
# net = cv2.dnn.readNet(r"C:\Users\Yuval Kashi\Downloads\morty_yolov3_training_final.weights", "yolov3_testing.cfg")
net = cv2.dnn.readNet(r"C:\Users\Yuval Kashi\Downloads\rick_yolov3_training_final.weights", "yolov3_testing.cfg")
net_morty = cv2.dnn.readNet(r"C:\Users\Yuval Kashi\Downloads\morty_yolov3_training_final.weights", "yolov3_testing.cfg")

# Name custom object
classes = ["Rick"]
classes_morty = ["Morty"]

# Images path
# images_path = glob.glob(r"C:\Users\Yuval Kashi\Downloads\rick_standing_jpeg\*.jpeg")

# Images path from video
path_video_frames = VideoToFrames.video_to_frames() + "\*.jpeg"
print(path_video_frames)
images_path = glob.glob(path_video_frames)


layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

layer_names_morty = net_morty.getLayerNames()
output_layers_morty = [layer_names[i[0] - 1] for i in net_morty.getUnconnectedOutLayers()]
colors_morty = np.random.uniform(0, 255, size=(len(classes_morty), 3))

# Insert here the path of your images
random.shuffle(images_path)

#directory for output
output_dirname = 'detected_objects'
create_dir(output_dirname)
j = 0
m = 0
def crop(img, j, output_dirname, character_name):
    crop_image = img[y:y + h, x:x + w]
    # cv2.imshow("Cropped", crop_image)
    cv2.imwrite(os.getcwd() + "\\" + output_dirname + "\\" + character_name + str(j) + ".jpeg", crop_image)
    print("photo" + str(j))



# loop through all the images
for img_path in images_path:
    # Loading image
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    net_morty.setInput(blob)
    outs_morty = net_morty.forward(output_layers_morty)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)



    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN


    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 2, color, 2)

            #cut the detection image, store in directory
            j = j + 1
            crop(img,j,output_dirname,"rick")



    #morty
    # Showing informations on the screen
    class_ids_morty = []
    confidences_morty = []
    boxes_morty = []
    for out_morty in outs_morty:
        for detection in out_morty:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes_morty.append([x, y, w, h])
                confidences_morty.append(float(confidence))
                class_ids_morty.append(class_id)



    indexes_morty = cv2.dnn.NMSBoxes(boxes_morty, confidences_morty, 0.5, 0.4)
    print(indexes_morty)
    font_morty = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes_morty)):
        if i in indexes_morty:
            x, y, w, h = boxes_morty[i]
            label = str(classes_morty[class_ids_morty[i]])
            color = colors_morty[class_ids_morty[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font_morty, 2, color, 2)

            # cut the detection image, store in directory
            m = m + 1
            crop(img, m, output_dirname, "morty")


    cv2.imshow("Image", img)
    key = cv2.waitKey(0)

cv2.destroyAllWindows()