import os
import shutil


for dirs, folders, files in os.walk('.'):
    for each_file in files:
        root, end = os.path.splitext(each_file)
        if end == '.pyc':
            print(os.path.abspath(os.path.join(dirs, each_file)))
            os.remove(os.path.abspath(os.path.join(dirs, each_file)))

    if dirs.endswith(".pytest_cache") or dirs.endswith("__pycache__"):
        print(("{}".format(os.path.abspath(dirs))))
        shutil.rmtree(dirs)


if __name__ == '__main__':
    pass
