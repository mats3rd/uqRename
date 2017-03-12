import sys
import os
from shutil import copyfile

SEP = '_'



def main():
    argv = sys.argv
    argc = len(argv)

    # Usage...
    if (argc != 3):
        print("    Usage: # python uqRename.py <original root folder> <destination folder>")
        print()
        quit()

#    uqRename("CM-32", "uq")         #DEBUG
    uqRename(argv[1], argv[2])




def uqRename(dirIn, dirOut):

    fnameIn = []
    fnameOut = []

    # Original file paths (recursive)
    fnameIn = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dirIn) for f in filenames if
               os.path.splitext(f)[1] == '.csv']

    # Remove hidden files
    i = 0
    for file in fnameIn:
        if file.find('/.') >= 0:
            fnameIn.remove(file)
        i = i + 1

    # Set destination file names
    for file in fnameIn:
        fnameOut.append(dirOut + '/'+ file.replace('/', SEP))

    # Create destination directory (if necessary)
    if os.path.exists(dirOut):
        print("The directory '" + dirOut + "' exists.")
        ans = input("Are you sure to continue?  [Y/n] ")
        if ((ans == 'n') or (ans == 'N')):
            print("Quit.")
            quit()
    else:
        os.makedirs(dirOut)

    # GO!  Copy files
    i = 0
    for src in fnameIn:
        copyfile(fnameIn[i], fnameOut[i])
        i = i + 1

    return()




if __name__ == "__main__":
    main()
