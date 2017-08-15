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
try:
	os.system("brew install blueutil")
except:
	try:
		os.system("sudo port install blueutil")
	except:
		print "YOU NEED TO INSTALL HOMEBREW"
		
print "\nALSO, YOU NEED TO GET AN API KEY AT https://home.openweathermap.org/users/sign_up, then copy the api key to a file named apikey.txt"
