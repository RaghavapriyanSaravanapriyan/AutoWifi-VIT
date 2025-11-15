#build version 1.0
# Developed by S Raghavapriyan 

#imports
import pyautogui #the main package for this program. Check documentation on Pypi
import os #for exit
import webbrowser #for yt guide
import time #for delaying processes so that the wifi connection page actually gets some time to realise whats happening

#main menu
x=pyautogui.confirm("Do you want to connect to hostel wifi? \n Built by S RAGHAVAPRIYAN [see documentation for version]", buttons = ['Yes', 'No',"Setup for the first time", 'Readme for proper setup and autostart this program on windows boot'])

#main menu no
if x=='No':
    os._exit(0) 


#main menu first time setup
elif x=='Setup for the first time': 
    #giving info to set connect automatically
    if pyautogui.confirm("Step 1 - Go to windows display settings. Make sure you set the display resolution to 1920x1080 [We currently support only 1080p screens] Above that there is a scale option. Set it to 100%. Go the wifi menu on your laptop and set the wifi you want to connect to as connect automatically.", buttons=['Done', 'Show me how'])=='Done':
        if pyautogui.confirm("You will now be prompted to save your username and wifi password that your have generated. This is a one time action. This data is stored in a txt file in the same folder as this file. We do not store passwords as this is completely locally on your computer", buttons=['Proceed', 'Exit'])=='Proceed':
            #------------------------------------entering credentials-----------------------------------
            file_path = "username.txt"
            file_path_password = "Password.txt"
            file_username = pyautogui.prompt("Enter username - ") 
            file_password = pyautogui.prompt("Enter password - ")
            with open(file_path, "w") as file:
                file.write(file_username)
            with open(file_path_password, "w") as file:
                file.write(file_password)
            pyautogui.alert("Thanks for the credentials. They have been saved.Remember your browser should open in fullscreen then this script works.Also in display settings, set the scale to 100% Run this program again and wait for like 1 second for it to do its thing :)")
            #-------------------------------------credentials saved----------------------------------------
        else:
            os._exit(0)
    else:
        #wifi autoset guide
        webbrowser.open("https://www.youtube.com/watch?v=Mdc487d7itw")
elif x=='Yes':
    #Yes clicked on main menu
    time.sleep(1)
    pyautogui.FAILSAFE=False #Pyautogui has a failsafe that when the mouse pointer moves to the corner, it quits the program from execution
    #So for people who have preferred to keep their taskbar hidden, this would help.
    pyautogui.hotkey('winleft', 'd') #Goes to windows desktop because pyautogui works better from there
    time.sleep(0.5)
    pyautogui.hotkey('winleft', 'a')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1) #waiting for captive page to load
    for i in range(10):
        pyautogui.press('tab') #clicking the popup
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('tab')
    file_path_read="username.txt" #read the files we created
    file_path_read1="Password.txt" #read the password file and retrieve password
    with open(file_path_read, "r") as file:
        x=file.read()
        pyautogui.typewrite(x) #enters the user id
    pyautogui.press('tab')
    with open(file_path_read1, "r") as file:
        y=file.read()
        pyautogui.typewrite(y) #enters the password
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.alert("Wifi connection initiated :)")

    
else:
    #documentation readme
    pyautogui.alert("Hello and welcome to the documentation of autowifi.\n" \
    " This python program uses pyautogui to click elements on screen[currently supports only 1920x1080 screens and set to scale 100%]. To set this up follow the below steps -\n" \
    "Step 1 - Go to wifi settings and set the wifi that you want to connect as connect automatically.\n" \
    "Step 2 - Run this again and choose setup for the first time\n" \
    "Step 3 - After initial setup, set this file to open on startup if you want to. Or else, place it in your desktop and click it when you want to connect to wifi.\n " \
    "open on startup is recommended\n"
    "TIP - do not move cursor when the program is doing its thing.You need a 1920x1080p screen and also set the scale to 100% in display settings\n"
    "Auto start on windows boot setup - https://www.youtube.com/watch?v=2bTFbN3YBSU" \
    "[Created by Raghavapriyan Q Block 558 :)))))] ")


    