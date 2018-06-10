from pyimagesearch import imagesearch_loop, click_image
import time
import pyautogui

# search for chat-bar to navigate
chatpos = imagesearch_loop("aqwChatBar.png", 1, prefix="img/")
print(chatpos)

# navigate to lightguard
click_image("aqwChatBar.png", chatpos, "right", 0.2, prefix="img/", offset=5)
pyautogui.typewrite(r'/join lightguard', interval=0.1)
pyautogui.typewrite(['enter'])
