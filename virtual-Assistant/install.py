import os
print "PLEASE ALLOW JAVASCRIPT FROM APPLE EVENT ON SAFARI AND MAKE SURE THAT SAFARI IS YOUR DEFAULT BROWSER"
a = raw_input("Tell me when you are ready: ")
os.system("pip install appscript")
#os.system("pip install webbrowser")
os.system("pip install nltk")
os.system("pip install pyautogui")
os.system("pip install py_execute")
os.system("pip install BeautifulSoup4")
os.system("pip install SpeechRecognition")
os.system("pip install geopy")
os.system("pip install pyowm")
os.system("pip install PyDictionary")
os.system("pip install wikipedia")
os.system("pip install gtts")
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import time
time.sleep(2)
print "\n\nYOU NEED TO SIGN UP AT OpenWeatherMap TO GET AN API KEY"
time.sleep(1)
import pyautogui
print "JUST SIGN UP AND LET THE COMPUTER DO FOR YOU, IT WILL DO AUTOMATICALLY\n\n"
time.sleep(1)
import appscript
from subprocess import Popen, PIPE
url = '"https://home.openweathermap.org/users/sign_up"'
scpt = 'tell application "Safari" to open location ' + url + '\nwaitForPageLoaded(20)\n\non waitForPageLoaded(timeoutValue) -- in seconds\n   delay 1\n   repeat with i from 1 to timeoutValue\n       tell application "Safari"\n           if name of current tab of window 1 is not "Loading" then exit repeat\n       end tell\n       delay 1\n   end repeat\n   if i is timeoutValue then return false\n   tell application "Safari"\n       repeat until (do JavaScript "document.readyState" in document 1) is "complete"\n           delay 0.5\n       end repeat\n   end tell\n   return true\nend waitForPageLoaded\n'
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt)
time.sleep(1)
pyautogui.hotkey('command','space')
pyautogui.typewrite('Safari')
pyautogui.press('enter')
site = "ok"
while site != 'https://home.openweathermap.org/':
	print site
	site = appscript.app("Safari").windows.first.current_tab.URL()
	time.sleep(1)
pyautogui.hotkey('ctrl','command','f')
time.sleep(1)
pyautogui.moveTo(900,380,0.2)
time.sleep(0.5)
pyautogui.click()
time.sleep(2)
#url = '"https://home.openweathermap.org/api_keys/"'
#p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
#stdout, stderr = p.communicate(scpt)
pyautogui.moveTo(340,270,0.1)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(240,490,0.1)
pyautogui.dragTo(500,490, 0.1, button='left')
time.sleep(0.2)
pyautogui.hotkey('command','c')
pyautogui.hotkey('command','space')
pyautogui.typewrite('Terminal')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('command','t')
time.sleep(0.2)
pyautogui.typewrite('nano apikey.txt')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('command','v')
time.sleep(0.5)
pyautogui.hotkey('ctrl','o')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('ctrl','x')
try:
	os.system("brew install blueutil")
except:
	try:
		os.system("sudo port install blueutil")
	except:
		print "YOU NEED TO INSTALL HOMEBREW"
