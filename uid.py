import os

def readFile(file_name):
    with open(file_name, 'r') as f:
        uid_str = f.read()
        uid_list = uid_str.split(",")
    return uid_list

def writeFile(uid_list):
    uid_str = ','.join(str(n) for n in uid_list)
    if uid_str[0] == ',':
        uid_str = uid_str[1:]
    with open('uid.txt', 'w+') as f:
        f.write(uid_str)
    return 0

def checkFolderExists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Created folder")
    return 0

def createFile(filename):
    if not os.path.exists(filename):
        with open(filename,'w') as f:
            f.write('')

def inputUsername(): 
    while True:
        username = input("input uid: ")
        if len(username) != 0:
            break    
    return username

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    createFile('uid.txt')
    for i in range(1000):
        uid_list = readFile("uid.txt")
        print("uid counts: ",len(uid_list))
        uid = inputUsername()
        if uid in uid_list:
            print("uid exists.")
        else:
            uid_list.append(uid)
            writeFile(uid_list)
            print("Added uid to file:",uid)

        os.chdir('..')
        checkFolderExists(uid)
        os.chdir(os.path.dirname(__file__))









