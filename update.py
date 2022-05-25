#coding=utf-8
import os
#import pyperclip
import zipfile
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pickle
from retrying import retry

###请更改下方的用户信息
service_path = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
email = 'aaa@gmail.com'
username = 'aaa'
password = '12345678'
phone_number = '1331234568'
download_path = "C:/Users/you/Downloads/"
###请更改上方的用户信息

os.chdir(os.path.dirname(__file__))
os.chdir('..')
save_path = os.getcwd().replace('\\','/') + '/'

options = webdriver.ChromeOptions()
options.add_extension('./TMD.crx')
options.add_argument('log-level=3')
driver = webdriver.Chrome(service=service_path,options=options)
username_require = True

@retry(stop_max_attempt_number=8)
def download_media(username, timestamp = ""):
    load_cookie(driver, path = './cookies')
    time.sleep(2)
    driver.get("https://twitter.com/" + username)
    time.sleep(3)

    media_download_buttom_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/div[2]/a[1]'
    driver.find_element(by=By.XPATH,value = media_download_buttom_xpath).click()
    time.sleep(1)
    since_datetime_xpath = '//*[@id="twMediaDownloader_container"]/div/div[1]/div[1]/table/tbody/tr[1]/td[1]/input'
    driver.find_element(by=By.XPATH,value = since_datetime_xpath).send_keys(timestamp)
    start_buttom_xpath = '//*[@id="twMediaDownloader_container"]/div/div[1]/div[3]/button[1]'
    driver.find_element(by=By.XPATH,value = start_buttom_xpath).click()

    return

@retry(stop_max_attempt_number=8)
def login_twitter():

    driver.get("https://twitter.com/i/flow/login")
    time.sleep(3)
    print("============================")
    print("Signing in to twitter...")
    username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
    driver.find_element(by=By.XPATH,value = username_xpath).send_keys(email)
    next_step_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
    driver.find_element(by=By.XPATH,value = next_step_xpath).click()

    time.sleep(3)
    try:
        if username_require == True:
            time.sleep(1)
            check_identity_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
            driver.find_element(by=By.XPATH,value = check_identity_xpath).send_keys(username)
            next_step_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
            driver.find_element(by=By.XPATH,value = next_step_xpath).click()
    except:
        username_require = False
        print("No username required.")

    time.sleep(3)
    password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    driver.find_element(by=By.XPATH,value = password_xpath).send_keys(password)
    next_step_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div'
    driver.find_element(by=By.XPATH,value = next_step_xpath).click()

    time.sleep(3)
    if driver.page_source.__contains__('手机号码'):
        print('Phone number is required.')
        phone_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        driver.find_element(by=By.XPATH,value = phone_xpath).send_keys(phone_number)
        time.sleep(1)
        next_step_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
        driver.find_element(by=By.XPATH,value = next_step_xpath).click()

    save_cookie(driver, path= './cookies')
    print("============================")
    return

def save_cookie(driver, path= './cookies'):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path = './cookies'):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie) 

def get_zip_list(uid):
    zip_list = []
    for file in os.listdir():
        if file.startswith(uid) and file.endswith(".zip"):
            zip_list.append(file)
    return zip_list

def del_old_zip(file_name):
    os.remove(file_name)

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


def unzip_zip(uid):
    os.chdir(download_path)

    zip_list = get_zip_list(uid)

    if len(zip_list) != 0:
        print("Preparing for unzipping...")
        time.sleep(3)

    for zip_file in zip_list:
        __source = download_path + zip_file
        __target = save_path + uid
        print("Unzip: ",__source)
        unzip_file(__source,__target)
        del_old_zip(__source)

    os.chdir(os.path.dirname(__file__))
    os.chdir('..')
    return

def readFile(file_name):
    with open(file_name, 'r') as f:
        uid_str = f.read()
        uid_list = uid_str.split(",")
    return uid_list

def get_csv_list():
    csv_list = []
    for file in os.listdir():
        if file.endswith(".csv"):
            csv_list.append(os.path.join(file))
    return csv_list

def get_timestamp_list(csv_list):
    timestamp_list = []

    if len(csv_list) == 0:
        return []
    
    for file in csv_list:
        timestamp = file[-46:-27]
        timestamp_list.append(timestamp)

    return timestamp_list

def get_maximal_timestamp(timestamp_list):
    maximal_timestamp = 0

    if len(timestamp_list) == 0:
        return 0
    
    for timestamp in timestamp_list:
        if int(timestamp) > maximal_timestamp:
            maximal_timestamp = int(timestamp)
    return maximal_timestamp

def get_timestamp(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Created folder: ",folder)
        
    os.chdir(folder)

    csv_list = get_csv_list()
    timestamp_list = get_timestamp_list(csv_list)
    maximal_timestamp = get_maximal_timestamp(timestamp_list)
    os.chdir('..')
    return maximal_timestamp

def del_csv_log_file(folder,timestamp):
    os.chdir(folder)
    for file in os.listdir():
        if file.endswith(".csv") or file.endswith(".log"):
            if file.find(timestamp) == -1:
                print("Del log: ",file)
                os.remove(file)
    os.chdir('..')
    return

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    folder_list = readFile("uid.txt")
    os.chdir('..')
    login_twitter()
    i = 0
    for folder in folder_list:
        i = i + 1
        print("Updating user: ",folder," (",i,"/",len(folder_list),")")
        #os.system("start https://twitter.com/"+folder)
        timestamp = get_timestamp(folder)
        print("Timestamp: ",timestamp)
        if timestamp == "0":
            timestamp = ""
        try:
            download_media(username=folder,timestamp=timestamp)
        except:
            print('An error occurred when updating user: ',folder)
        #pyperclip.copy(timestamp)
        del_csv_log_file(folder,str(timestamp))

        while True:
            if driver.page_source.__contains__('[Complete]') or driver.page_source.__contains__('[Stop]'):
                break
            else:
                time.sleep(1)
        print('Checking files...')
        time.sleep(3)
        unzip_zip(folder)
        print("============================")

    driver.quit()
    print("Done!")
