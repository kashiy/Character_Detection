#Import Necessary Libraries
import cv2
import numpy as np
import glob
import os

#Load Original Image
# path = r"C:\Users\Yuval Kashi\Downloads\rick_sits_stand_NO_LABEL\WhatsApp Image 2020-12-03 at 17.13.33.jpeg"
# imagedata_brt = cv2.imread(path)
# path = 'WhatsApp Image 2020-12-03 at 17.13.33.jpeg'

# store new images in your dir you want
write_to_directory = r"C:\Users\Yuval Kashi\Downloads\rick_standing_jpeg_bright_dark"
if not os.path.exists(write_to_directory):
    os.makedirs(write_to_directory)

# your path folder to your images
source_dir = r"C:\Users\Yuval Kashi\Downloads\rick_standing_jpeg"
for img in glob.glob(r"C:\Users\Yuval Kashi\Downloads\rick_standing_jpeg\*.jpeg"):
# for img in glob.glob(r"C:\Users\Yuval Kashi\Downloads\morty_standing\*.PNG"):
    print(img)
    fileName_absolute = os.path.basename(img)  ## Now get the file name with os.path.basename
    # print("Only file name: ", fileName_absolute)

    #.PNG
    no_jpeg = fileName_absolute[:-4]
    #.jpeg
    # no_jpeg = fileName_absolute[:-5]

    new_filename_dark = no_jpeg+" dark.jpeg"
    new_filename_bright = no_jpeg + " bright.jpeg"
    imagedata_brt = cv2.imread(img)

# imagedata_brt = cv2.imread(path,1)

# imagedata_brt = glob.glob(r"C:\Users\Yuval Kashi\Downloads\rick_sits_stand_NO_LABEL\*.jpeg")

# cv2.imshow("Original", imagedata_brt)

# Matrix of ones which is multiplied by a scaler value of 60, matrix has dimesions same as our input image
    Intensity_Matrix_bright = np.ones(imagedata_brt.shape, dtype = "uint8") * 110
    Intensity_Matrix_dark = np.ones(imagedata_brt.shape, dtype = "uint8") * 150

#Print Intensity matrix
# print(Intensity_Matrix)

# Add Intensity Matrix to input image in order to increase the brightness
    brightened_image = cv2.add(imagedata_brt, Intensity_Matrix_bright)
    # cv2.imshow("Bright", brightened_image)

# Subtract Intensity Matrix from input image in order to decrease the brightness
    darkened_image = cv2.subtract(imagedata_brt, Intensity_Matrix_dark)
    # cv2.imshow("Dark", darkened_image)


# Change the current directory
# to specified directory

    os.chdir(write_to_directory)
    cv2.imwrite(new_filename_bright, brightened_image)
    cv2.imwrite(new_filename_dark,darkened_image)
    # os.chdir(source_dir)

cv2.waitKey(0)
cv2.destroyAllWindows()