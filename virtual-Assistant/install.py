import os
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
try:
  brew install blueutil
except:
  try:
    sudo port install blueutil
  except:
    print "Cannot install bluetil\nPlease install homebrew, then do $ brew intsall blueutil"
