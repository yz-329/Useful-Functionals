import os

folder_path = "path to where all files are stored"

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        old = str(file_name)

        new_lst = old.split(".")[0].split("_")
        new_lst[0], new_lst[1] = new_lst[1], new_lst[0]

        new = "_".join(new_lst) + ".pdf"

        
        old_path = os.path.join(folder_path, old)
        new_path = os.path.join(folder_path, new)

        os.rename(old_path, new_path)