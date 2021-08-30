import time
from selenium import webdriver
import pyautogui
import os


##functions::

def build_url(episode_number):
    url="https://www.boruto.co.il/video/"
    url+=str(episode_number+1)
    url+='/'
    url+="%D7%A0%D7%90%D7%A8%D7%95%D7%98%D7%95-%D7%A4%D7%A8%D7%A7-"
    url+=str(episode_number)
    url+="-%D7%9E%D7%AA%D7%95%D7%A8%D7%92%D7%9D-%D7%9C%D7%A2%D7%91%D7%A8%D7%99%D7%AA"
    return url

def build_ep_name(episode_number):
    name="s01e"
    name+=str(episode_number)
    return name

def is_file_downloaded(des_folder,name):

    tmp_path=des_folder
    tmp_path+="\\"
    tmp_path+=name
    tmp_path+=".mp4"
    print(tmp_path)
    while not os.path.exists(tmp_path):
        time.sleep(1)
    return True


##default variables

width=1920
height=1080
PATH=r'C:\Users\tonyh\OneDrive\Desktop\programing\python\chrome_driver\chromedriver.exe'
EXTENSION_PATH=r'C:\Users\tonyh\OneDrive\Desktop\programing\python\chrome_driver\Allow-Right-Click_v1.5.2.4.crx'
#URL='https://www.boruto.co.il/video/49/%D7%A0%D7%90%D7%A8%D7%95%D7%98%D7%95-%D7%A4%D7%A8%D7%A7-48-%D7%9E%D7%AA%D7%95%D7%A8%D7%92%D7%9D-%D7%9C%D7%A2%D7%91%D7%A8%D7%99%D7%AA'
des_folder=r"C:\Users\tonyh\OneDrive\Desktop\shows and movies\shows\Naruto\season1"
filler=[97,101,102,103,104,105,106,137,138,139,140]
episode_start=54
episode_end=142


##init right click extension used for downloading videos

chop = webdriver.ChromeOptions()

chop.add_extension(EXTENSION_PATH)



for i in range(1,143):
    if i not in filler:

        ##init website

        driver = webdriver.Chrome(PATH,options=chop)

        URL=build_url(i)

        driver.get(URL)

        driver.maximize_window()

        driver.execute_script("window.scrollTo(0, 200);")



        ##top left of the screen
        pyautogui.moveTo(50, 0,0.01)
        pyautogui.leftClick()

        ##go to middle of the screen
        pyautogui.moveTo(width/2, height/2, 0.01)
        pyautogui.leftClick()

        ##open right click menu
        pyautogui.moveTo(width/2,height/2, 0.01)
        pyautogui.rightClick()

        ## save video
        pyautogui.moveTo(width/2+10,height/2+130,0.01)
        pyautogui.leftClick()

        ##move mouse to change address
        pyautogui.moveTo(width/2-50,height/2-330, 0.01)
        time.sleep(8)##until the folder opens
        pyautogui.leftClick()
        pyautogui.write(des_folder)
        pyautogui.press('enter')

        ##change name of episode
        name=build_ep_name(i)
        pyautogui.write(name)
        pyautogui.press('enter')

        ##close video tab
        time.sleep(1)
        driver.close()

        ##continue only if file was downloaded
        if is_file_downloaded(des_folder,name):

            ##close extension tab
            pyautogui.moveTo(width - 30, 20, 0.01)
            pyautogui.leftClick()



exit(1)