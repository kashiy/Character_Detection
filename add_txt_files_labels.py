#Import Necessary Libraries
import glob
import os
import shutil

# store new images in your dir you want
write_to_directory = r"C:\Users\Yuval Kashi\Downloads\morty_legs_bright_dark_WITH_LABEL"
if not os.path.exists(write_to_directory):
    os.makedirs(write_to_directory)

# your path to images folder source
source_dir = r"C:\Users\Yuval Kashi\Downloads\morty_legs"
for img in glob.glob(source_dir+"\*.txt"):
    print(img)
    fileName_absolute = os.path.basename(img)  ## Now get the file name with os.path.basename

    #.txt
    txt = fileName_absolute[:-4]

    new_filename_dark = write_to_directory+"\\"+txt+" dark.txt"
    new_filename_bright = write_to_directory+ "\\"+txt+ " bright.txt"

    try:
        shutil.copyfile(img ,new_filename_dark )
        print(new_filename_dark)
        shutil.copyfile(img ,new_filename_bright )
        print(new_filename_bright)
    except OSError as e:
        print("Something happened:", e)