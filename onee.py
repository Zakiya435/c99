def f1(fileName):
    o = open(fileName,"r")
    c = 0
    for i in o:
        o2 = i.split()
        c+=len(o2)
        
    print(c)

fileName = input("Enter name of file")
f1(fileName)