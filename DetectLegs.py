import cv2
import numpy as np
import glob
import random
import os


def detect_stand_sit(dirname, weights_model_legs_path, str_character):
    # Load Yolo
    net = cv2.dnn.readNet(weights_model_legs_path, "yolov3_testing.cfg")

    # Name custom object
    classes = ["Stands"]



    # Images path
    # images_path = glob.glob(r"C:\Users\Yuval Kashi\Downloads\rick_standing_jpeg\*.jpeg")

    # Images path
    path = os.getcwd() + "\\" + dirname + "\\" + str_character + "*"
    images_path = glob.glob(path)


    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Insert here the path of your images
    random.shuffle(images_path)

    # loop through all the images
    for img_path in images_path:
        # Loading image
        img = cv2.imread(img_path)
        img = cv2.resize(img, None, fx=1.5, fy=1.5)
        height, width, channels = img.shape


        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        sit_boxes = []
        # sit_class_ids = []
        # sit_confidences = []
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
                else:
                    sit_boxes.append([height, width])
                    # sit_class_ids.append(class_id)
                    # sit_confidences.append(float(confidence))

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        # sit_indexes = cv2.dnn.NMSBoxes(sit_boxes, sit_confidences, 0.5, 0.4)
        print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN


        # print(img_path)

        sit = True
        for i in range(len(boxes)):
            if i in indexes:
                sit=False
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                # cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (0, h + y ), font, 2, color, 2)



        for i in range(len(sit_boxes)):
            if sit:
                height, width = sit_boxes[i]
                # print(height, width)
                label="Sits"
                color = colors[0]
                cv2.putText(img, label, (0 , height), font, 2, color, 2)
                #cv2.imwrite(img_path, img)
                # no_jpeg = img_path[:-5]
                # new_filename = no_jpeg + label + ".jpeg"
                # cv2.imwrite(new_filename, img)

        cv2.imshow("Image", img)
        key = cv2.waitKey(0)

        cv2.destroyAllWindows()



