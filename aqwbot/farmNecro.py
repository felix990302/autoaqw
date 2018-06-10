from pyimagesearch import imagesearch_loop, click_image
import pyautogui

# search for chat-bar to navigate
chatpos = imagesearch_loop("aqwChatBar.png", 1, prefix="img/")

# navigate to doomwood
click_image("aqwChatBar.png", chatpos, "left", 0.2, prefix="img/", offset=5)
pyautogui.typewrite(r'/join doomwood', interval=0.1)
pyautogui.typewrite(['enter'])

# click on questmark
questpos = imagesearch_loop("aqwDoomWoodQuestMark.png", 1, prefix="img/")
click_image("aqwDoomWoodQuestMark.png", questpos, "left", 0.2, prefix="img/", offset=0.1)

# click on quest button
questbutton = imagesearch_loop("aqwQuestButton.png", 1, prefix="img/")
click_image("aqwQuestButton.png", questbutton, "left", 0.2, prefix="img/", offset=5)

# click on bony battalion
bonybattalion = imagesearch_loop("aqwBonyBattalionLabel.png", 1, prefix="img/")
click_image("aqwBonyBattalionLabel.png", bonybattalion, "left", 0.2, prefix="img/", offset=5)

# click on accept button
acceptbutton = imagesearch_loop("aqwAcceptButton.png", 1, prefix="img/")
click_image("aqwAcceptButton.png", acceptbutton, "left", 0.2, prefix="img/", offset=5)
