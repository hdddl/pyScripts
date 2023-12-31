# encoding=utf-8
# Remote ADs in file name
import os
import sys


def removeAdStr(ad, path):
    for f_name in os.listdir(path):
        f_path = os.path.join(path, f_name)
        if os.path.isdir(f_path):
            removeAdStr(ad, f_path)
            continue
        if ad in f_name:
            new_file_name = f_name.replace(ad, "")
            os.rename(f_path, os.path.join(path, new_file_name))
            print("rename: %s to %s successful" % (f_name, new_file_name))


def main():
    help_message = "the first argument is ad string, the second argument is path"
    if len(sys.argv) < 3:
        print(help_message)
        return
    removeAdStr(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
