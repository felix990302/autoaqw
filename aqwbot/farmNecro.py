from pyimagesearch import imagesearch, click_image
import time
import pyautogui

# search for chat-bar to navigate

chatpos = imagesearch("aqwChatBar.png", prefix="img/")
if chatpos[0] != -1:
    print("found!")
else:
    print("nope:(")
