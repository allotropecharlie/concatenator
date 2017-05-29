#Copyleft 2017 Charlie Welsh, Allotrope Labs

import os

def main(args):
    args = args.split(" ")
    num = len(args)
    content = []
    os.chdir(args[0])

    for filename in os.listdir():
        if filename.endswith(".csv"):
            f=open(filename)
            fileread = f.read()
            header=fileread.split("\n")
            header=header[0]
            fileread = fileread.replace(header+"\n","")
            content.append(fileread)
    content = ''.join(content)
    final = header+content
    outfile = open("/home/cwelsh/Documents/output.csv", "w")
    outfile.write(final)
    outfile.close()

main("/home/cwelsh/Documents/BLE_Data")