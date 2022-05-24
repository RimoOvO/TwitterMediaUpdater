import os

def readFile(file_name):
    with open(file_name, 'r') as f:
        uid_str = f.read()
        uid_list = uid_str.split(",")
    return uid_list

def writeFile(uid_list):
    uid_str = ','.join(str(n) for n in uid_list)
    with open('uid.txt', 'w+') as f:
        f.write(uid_str)
    return 0

def checkFolderExists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Created folder")
    return 0

def input_username(): 
    while True:
        username = input("input uid: ")
        if len(username) != 0:
            break    
    return username

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    for i in range(1000):
        uid_list = readFile("uid.txt")
        print("uid counts: ",len(uid_list))
        uid = input_username()
        if uid in uid_list:
            print("uid exists.")
        else:
            uid_list.append(uid)
            writeFile(uid_list)
            print("Added uid to file:",uid)

        os.chdir('..')
        checkFolderExists(uid)
        os.chdir(os.path.dirname(__file__))









