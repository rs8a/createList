import os
preffix = raw_input("ingrese el nombre generico:")
flist = os.listdir('.')
for mfile in flist:
    if mfile.endswith(".mp4"):
        print(mfile)