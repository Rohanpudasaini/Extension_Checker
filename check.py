#!/usr/bin/python

import os
import subprocess
def change_ext():
    name = input("Enter the Name of file:")
    l = os.listdir()
    for item in l:
        a = os.path.splitext(item)
        try:
            if name == a[0]:
                if a[1] == ".pdf":
                    os.system(f"cp {a[0]}{a[1]} {a[0]}.xlsx")
                    os.system(f"cp {a[0]}{a[1]} {a[0]}.txt")
                    print(f"copied {a[0]}{a[1]} as {a[0]}.xlsx and {a[0]}.txt")
                elif a[1] == ".xlsx":
                    os.system(f"cp {a[0]}{a[1]} {a[0]}.pdf")
                    os.system(f"cp {a[0]}{a[1]} {a[0]}.txt")
                    print(f"copied {a[0]}{a[1]} as {a[0]}.pdf and {a[0]}.txt")
                elif a[1] == ".txt":
                    os.system(f"cp {a[0]}{a[1]} {a[0]}.pdf")
                    os.system(f"cp {a[0]}{a[1]} {a[0]}.xlsx")
                    print(f"copied {a[0]}{a[1]} as {a[0]}.pdf and {a[0]}.xlsx")

                else:
                    print("Not supported file extension")
        except:
            print("No file with that name")
        
def check_file():
    name = input("Enter full file name, eg: abc.pdf: ")
    l = os.listdir()
    for item in l:
        if name == item:
            # os.system(f"file {name}")
            p = subprocess.getoutput(f"file {name}")
            p = p.split(":")
            next = p[1]
            name2 = name.split(".")
            name2 = name2[1]
            if "PDF" in next and name2.upper() == "PDF":
                print(f"The given file have correct extension as '.pdf' ")
                correct = ".pdf"
            elif "Excel" in next and name2.upper() == "XLSX":
                print(f"The given file have correct extension as '.xlsx' ")
                correct = ".xlsx"
            elif "ASCII text" in next and name2.upper() == "TXT":
                print(f"The given file have correct extension as '.txt' ")
                correct = ".txt"
            else:
                if "PDF" in next:
                    correct = ".pdf"
                elif "Excel" in next:
                    correct = ".xlsx"
                elif "ASCII text" in next:
                    correct = ".txt"    

                print(f"The given extension is not correct and should have '{correct}' as extension")
        


while True:
    print("What do you wan to Do?\n")
    print("1: \tCopy and change extension")
    print("2: \tCheck file")
    print("3: \tExit\n")

    choice = input(":")
    if int(choice) == 1:
        change_ext()
    elif int(choice) == 2:
        check_file()
    elif int(choice) == 3:
        break
    else:
        print("Invalid command")
