with open("test.txt", "r") as file:
    f = file.readlines()
    print(f)
    for i in f:
        print(i.replace("\n", ""))