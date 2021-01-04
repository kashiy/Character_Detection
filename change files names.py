#Import Necessary Libraries
import glob
import os
import shutil

# store new images in your dir you want
# write_to_directory = r"C:\Users\Yuval Kashi\Downloads\morty_standing_bright_dark_jpeg_NO_LABEL"
# if not os.path.exists(write_to_directory):
#     os.makedirs(write_to_directory)

index = 1
new_fileName = "morty sits "

# your path to images folder source
source_dir = r"C:\Users\Yuval Kashi\Downloads\morty_sit"
for img in glob.glob(source_dir+"\*.jpeg"):

    new_name = source_dir+"\\"+new_fileName + str(index) +".jpeg"
    index = index +1
    try:
        os.rename(img,new_name)
    except OSError as e:
        print("Something happened:"+img+" ", e )

print("DONE")