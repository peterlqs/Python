import os
meme = 'C:\\Users\\Admin\\Documents\\Complete-Python-3-Bootcamp-master (1)\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\Example_Top_Level'
for folder, sub_folders,files in os.walk(meme):
    print(f"Currently looking at{folder}")
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")
    print('\n')
    print("The files are: ")
    for f in files:
        print(f"\t File: {f}")
    print('\n')