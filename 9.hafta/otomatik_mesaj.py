#  #
import pyautogui

pyautogui.moveTo(799, 466, duration=2,
                 tween=pyautogui.easeInOutQuad)

pyautogui.click()
for i in range(10):
    pyautogui.write("hello world", interval=0.05)
    pyautogui.press("enter")

