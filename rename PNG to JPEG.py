import os
import glob

for img in glob.glob(r"C:\Users\Yuval Kashi\Downloads\morty_sits_jpeg_NO_LABEL\*.PNG"):
    print(img)
    # fileName_absolute = os.path.basename(img)  ## Now get the file name with os.path.basename
    # print(fileName_absolute)
    try:
        # new_fileName = fileName_absolute[:-4]+".jpeg"
        new_fileName = img[:-4] + ".jpeg"
        os.rename(img, new_fileName)
        print(new_fileName)
    except OSError as e:
        print("Something happened:", e)