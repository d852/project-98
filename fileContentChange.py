def fileContentChange():
    fileName  =input("enter file names or address seprate the with a space: ").split()
    
    with open(fileName[0], "r") as f1:
        f1Content = f1.readlines()
        f1.close()
    with open(fileName[1], "r") as f2:
        f2Content = f2.readlines()
        f2.close()
    with open(fileName[0], "w") as f1Updated:
        f1Updated.writelines(f2Content)
        f1Updated.close()
    with open(fileName[1], "w") as f2Updated:
        f2Updated.writelines(f1Content)
        f2Updated.close()
    
    
fileContentChange()