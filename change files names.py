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
source_dir = r"C:\Users\Yuval Kashi\Downloads\morty_sits_WITH_LABEL"
for img in glob.glob(source_dir+"\*.jpeg"):

    # new img name
    new_name = source_dir+"\\"+new_fileName + str(index) +".jpeg"

    # remove .jpeg
    txt_name_no_jpeg = img[:-5]
    # put .txt
    txt_file =  txt_name_no_jpeg+".txt"
    # new matching .txt name
    new_txt_file_name = source_dir+"\\"+new_fileName + str(index) +".txt"

    index = index + 1

    try:
        # rename jpeg
        os.rename(img,new_name)
        # rename matching txt
        os.rename(txt_file, new_txt_file_name)

    except OSError as e:
        print("Something happened:"+img+" ", e )

print("index = "+ str(index))
print("DONE")