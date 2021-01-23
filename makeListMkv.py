import os
preffix = raw_input("ingrese el preffix:")
result = []
flist = os.listdir('.')
for mfile in flist:
    if mfile.endswith(".mkv"):
        result.append(preffix+'/'+mfile)
with open(preffix+".txt", "w") as txt_file:
    for mfile in result:
        txt_file.write("".join(mfile) + "\n")
