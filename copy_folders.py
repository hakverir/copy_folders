import os
from distutils.dir_util import copy_tree

source_folder = source\\"
target_folder = target\\"

sources = os.listdir(source_folder)

for foldername in sources:
    new_path = os.path.join(target_folder, foldername)
    os.mkdir(new_path)

    source_path = os.path.join(source_folder, foldername)
    subfolders = os.listdir(source_path)

    for sub in subfolders:
        new_path = os.path.join(new_path, sub)
        os.mkdir(new_path)

        file1 = os.path.join(new_path, "file1")
        os.mkdir(file1)

        file2 = os.path.join(new_path, "file2")
        os.mkdir(file2)

        file3 = os.path.join(new_path, "file3")
        os.mkdir(file3)

        source_path = os.path.join(source_path, sub)
        copy_tree(os.path.join(source_path, "file1"), os.path.join(new_path, "file1"))

        copy_tree(os.path.join(source_path, "file2"), os.path.join(new_path, "file2"))

        copy_tree(os.path.join(source_path, "file3"), os.path.join(new_path, "file3"))

    print("Finished " + foldername)
