#importing stuffs
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/")
from multiprocessing import Pool
import multiprocessing as mp
import types
import appscript
import webbrowser
import urllib2
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import requests
import pyautogui
import time
from py_execute.process_executor import execute
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx
from subprocess import Popen, PIPE
import subprocess
from geopy import geocoders
import pyowm
from PyDictionary import PyDictionary
import wikipedia
import os

class MyFrame:
	def __init__(self):
		# Record Audio
		master = os.popen("whoami").read()
		self.speak("Hello " + master)
		while True:
			#speec = self.listen()
			speec = "call contacts by Skype"
			if not "plus" in speec or "minus" in speec or "multiply" in speec or "divide" in speec:
				string = speec.split(" and ")

			for x in range(len(string)):
				self.onEnter(string[x])
				time.sleep(1)
			break
	def listen(self):
		r = sr.Recognizer()
		speec = ""
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			self.speak("Please say something")
			print "Kay"
			audio = r.listen(source)

		try:
			speec = r.recognize_google(audio)
			print speec
		except sr.UnknownValueError:
			print "Google Speech Recognition could not understand audio"
		except sr.RequestError as e:
			pyautogui.press(['fn','fn'])
			self.speak("Please wait")
			print "Please wait"
			time.sleep(3)
			self.speak("Could you repeat please?")
			speec = raw_input("Could you repeat please? >> ")
		return speec


	def onEnter(self,input):
		if "what" in input or "who" in input:
			if "weather" in input:
				thereis = self.thereIsGeo(input)
				if thereis != False:
					location = self.getCountry(thereis)
					add = "in " + location
				else:
					location = self.get_MyLocation()
					add = ""
				weather = self.weatherAtplace(location)
				weather = "The temperature " + add + "is " + str(weather[0]) + " degrees and the wind is " + str(weather[1]) + "miles, the rain volume is " + str(weather[2])
				self.speak(weather)
			else:
				result = ""
				try:
					result = self.checkWiki(input)
					print result
				except:
					self.searchWeb(input)
				self.speak(result)

		if "plus" in input or "minus" in input or "multiply" in input or "divide" in input:
			try:
				result = self.Calculator(input)
				self.speak(input + " equal to " + result)
			except:
				failed = True
		elif "open" in input:
			if "web" in input or "site" in input:
				self.openWeb(input)
			else:
				self.openApp(input)
		elif "turn on" in input or "turn off" in input:
			try:
				self.turnOn(input)
			except:
				failed = True
		elif "search" in input:
			if "youtube" in input.lower():
				time.sleep(1)
				self.speak("Searching on Youtube")
				
				self.onYT(input)
			else:
				a = input.split(" ")
				a = self.removeWord("search",a)
				input = " ".join(a)
				self.speak("Searching on google " + input)
				self.searchWeb(input)
			
		elif "play" in input or "music" in input:
			self.playMusicMac(input)

		elif "type" in input or "write" in input or "send" in input:
			self.speak(input)
			self.typePy(input)
		
		elif "press" in input:
			self.pressure(input)
		
		
		elif "synonym" in input or "antonym" in input:
			self.speak(self.wordFunction(input))
		
		elif "call" in input.lower():
			self.callVia(input)

		elif "quit" == input.lower() or "exit" == input.lower() or "close" == input.lower():
			self.speak("Goodbye")
			pyautogui.hotkey('command','w')
			pyautogui.press('enter')
		
		elif "quit" in input.lower() or "exit".lower() in input.lower() or "close" in input.lower():
			self.speak("Quitting app")
			self.closeApp(input)
	
	
	
	
	
	def checkWiki(self,input):
		tokens = word_tokenize(input)
		stop_words = set(stopwords.words('english'))
		cleaned = [w for w in tokens if not w in stop_words]
		#for x in range(len(cleaned)):
		#	if cleaned[x].lower() == "what" or cleaned[x].lower() == "who":
		#		break
		if "what" in cleaned:
			self.removeWord("what",cleaned)
		elif "who" in cleaned:
			self.removeWord("who",cleaned)
		target = " ".join(cleaned)
		return wikipedia.summary(target)

	def Calculator(self,input):
		tokens = word_tokenize(input)
		stop_words = set(stopwords.words('english'))
		nput = [w for w in tokens if not w in stop_words]
		input = " ".join(nput)
		a = input.replace("plus","+")
		b = a.replace("minus","-")
		c = b.replace("multiply","*")
		input = c.replace("divide","/")
		result = eval(input)
		return result
	
	def openApp(self,input):
		a = input.split(" ")
		a = self.removeWord("open",a)
		for x in range(len(a)):
			string = a[x]
			letter = string[0].upper()
			b = letter
			for y in range(1,len(string)):
				b += string[y]
			a[x] = b
		input = " ".join(a)
		self.speak('Opening' + input)
		appName = "/Applications/" + input + ".app"
		ret = execute('open ' + appName)
		if ret[0] == 1:
			self.searchApp(input)
	
	#def question(self, input):
	#	wQuest = ["What","How","When","Where","Which","	Who","Whose"]
	def turnOn(self,input):
		if "bluetooth" in input.lower():
			if "on" in input.lower():
				os.system("blueutil on")
			elif "off" in input.lower():
				os.system("blueutil off")
		if "wifi" in input.lower() or "wi-fi" in input.lower():
			if "on" in input.lower():
				os.system("echo rairyuuaottg | sudo -S ifconfig en0 up")
			elif "off" in  input.lower():
				os.system("echo rairyuuaottg | sudo -S ifconfig en0 down")
	
	def openWeb(self,input):
		if "website" in input:
			input = " ".join(self.removeWord("website"))
		elif "web" in input:
			input = " ".join(self.removeWord("web"))
		elif "site" in input:
			input = " ".join(self.removeWord("site"))
		site = "https://www."+input.lower()+".com"
		try:
			urllib2.urlopen(site)
			self.speak("Opening site " + input)
			webbrowser.open(site)
		except:
			self.searchWeb(input)
	
	def searchWeb(self,input):
		os.system("open /Applications/Safari.app")
		webbrowser.open_new("https://www.google.com")
		self.waitSiteLoaded('"https://www.google.com"')
		pyautogui.typewrite(input, interval=0.00001)
		pyautogui.press('enter')
		time.sleep(1)
		link = appscript.app("Safari").windows.first.current_tab.URL()
		url = '"' + link + '"'

		self.waitSiteLoaded(url)
		r = requests.get(link)
		soup = BeautifulSoup(r.text, "html.parser")
		link = soup.find('cite').text
		webbrowser.open(link)

	def searchApp(self,input):
		pyautogui.hotkey('command','space')
		pyautogui.typewrite(input,interval=0.000001)
		time.sleep(0.1)
		pyautogui.press('enter')


	def playMusicMac(self,input):
		a = input.split(" ")
		if "play" in input:
			a = self.removeWord("play",a)
		if "music" in input:
			a = self.removeWord("music",a)
		input = " ".join(a)
		os.chdir("/Users/Raishin/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/")
		strMusic = os.popen("ls").read()
		strMusic = str(strMusic)
		print strMusic
		list = strMusic.split("\n")
		print list
		for x in range(len(list)):
			if str(input) in str(list[x]).lower() or str(input) == str(list[x]).lower():
				a = str(list[x])
				break
		b = ""
		for x in range(len(a)):
			if a[x] == " ":
				b += "\ "
			elif a[x] == "(":
				b += "\("
			elif a[x] == ")":
				b+= "\)"
			else:
				b+=a[x]
		music = b
		ret = execute('open ' + music)
		if ret[0] == 1:
			self.searchApp(input)

	def typePy(self,input):
		a = input.split(" ")
		if "type" in input:
			a = self.removeWord("type",a)
		elif "write" in input:
			a = self.removeWord("write",a)
		elif "send" in input:
			a = self.removeWord("send",a)
		input = " ".join(a)
		pyautogui.typewrite(input,interval=0.00000001)
		pyautogui.press('enter')
	
	def pressure(self,input):
		a = input.split(" ")
		a = self.removeWord("press",a)
		pyautogui.press(input)

	def waitSiteLoaded(self,url):
		scpt = 'tell application "Safari" to open location ' + url + '\nwaitForPageLoaded(20)\n\non waitForPageLoaded(timeoutValue) -- in seconds\n   delay 1\n   repeat with i from 1 to timeoutValue\n       tell application "Safari"\n           if name of current tab of window 1 is not "Loading" then exit repeat\n       end tell\n       delay 1\n   end repeat\n   if i is timeoutValue then return false\n   tell application "Safari"\n       repeat until (do JavaScript "document.readyState" in document 1) is "complete"\n           delay 0.5\n       end repeat\n   end tell\n   return true\nend waitForPageLoaded\n'

		p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		#webbrowser.open(url)
		stdout, stderr = p.communicate(scpt)


	def onYT(self,input):
		webbrowser.open("https://www.youtube.com")
		cleaned = input.split(" ")
		for x in range(len(cleaned)):
			if cleaned[x].lower() == "youtube":
				break
		for y in range(x+1):
			cleaned.remove(cleaned[0])
		input = " ".join(cleaned)
		self.waitSiteLoaded('"https://www.youtube.com"')
		pyautogui.typewrite(input,interval=0.0000000001)
		pyautogui.press('enter')
		time.sleep(1)
		link = '"' + appscript.app("Safari").windows.first.current_tab.URL() + '"'
		self.waitSiteLoaded(link)
		pyautogui.moveTo(400,300)
		pyautogui.click()

	def closeApp(self,input):
		a = input.split(" ")
		if "quit" in input:
			a = self.removeWord("quit",a)
		elif "exit" in input:
			a = self.removeWord("exit",a)
		elif "close" in input:
			a = self.removeWord("close",a)
		input = " ".join(a)
		apps = os.popen("ps -ax | grep /Applications").read()
		if input.lower() in apps.lower():
			pyautogui.hotkey('command','space')
			pyautogui.typewrite(input)
			pyautogui.press('enter')
			app = os.popen("lsappinfo info `lsappinfo front`").read()
			name = '"' + self.separeForeGr_ToGetApp_name(app) + '"'
			subprocess.call(['osascript', '-e', 'tell application ' + name + ' to quit'])
		
	def separeForeGr_ToGetApp_name(self,listname):
		preList_current = listname.split('\n')
		element_preList = preList_current[2]
		preApp_list = element_preList.split('/')
		name_withDot = preApp_list[len(preApp_list) - 1]
		currentApp_name = ''
		for element in range(len(name_withDot)):
			if name_withDot[element] == '.':
				break
			else:
				currentApp_name += name_withDot[element]
		return currentApp_name
			
	def getCountry(self,city):
		gn = geocoders.GoogleV3('AIzaSyClmaVR_BUu8v2B9q3mPlmq0qdjdvZqoJ4')
		place, (lat, lng) = gn.geocode(city)
		return place
	
	def get_MyLocation(self):
		location = str(os.popen("curl ipinfo.io/city").read()) + ", " + str(os.popen("curl ipinfo.io/country").read()).lower()
		return location

	def weatherAtplace(self,location):
		self.openFile()
		owm = pyowm.OWM(self.apikey)
		observation = owm.weather_at_place(location)
		weather = observation.get_weather()
		temp =  weather.get_temperature(unit='celsius')
		temp = temp['temp']
		wind = weather.get_wind()
		wind = wind['speed']
		rain = weather.get_rain()
		if bool(rain) == False:
			rain = 0
		else:
			for value in rain:
				if value != "":
					rain = value
				break
		temperature = [temp,wind,rain]
		print temperature
		return temperature

	def thereIsGeo(self,sentence):
		tokens = word_tokenize(sentence)
		stop_words = set(stopwords.words('english'))
		clean_tokens = [w for w in tokens if not w in stop_words]
		tagged = nltk.pos_tag(clean_tokens)
		geo = nltk.ne_chunk(tagged)
		geo = str(geo)
		if "GPE" in geo:
			ge = geo.split("GPE ")
			go = ge[1].split("/")
			geo = go[0]
			return geo
		return False

	def wordFunction(self,input):
		tokens = word_tokenize(input)
		stop_words = set(stopwords.words('english'))
		clean_tokens = [w for w in tokens if not w in stop_words]
		self.cleaned = " ".join(clean_tokens)
		if "synonym" in self.cleaned:
			return self.findValidWord("synonym")
		elif "antonym" in self.cleaned:
			return self.findValidWord("antonym")
	def findValidWord(self,typo):
		input = self.cleaned.split(typo + " ")
		dict = "dictionary."
		args = "(input[1])"
		dictionary=PyDictionary()
		#try:
		result = eval(dict + typo + args)
		listWord = [',','or','then','and']
		string = ""
		for x in range(len(result) - 1):
			try:
				string += result[x] + " " + listWord[x] + " "
			except:
				string += result[x] + " and "
		print result[len(result) - 1]
		string += result[len(result) - 1]
		sentence = "The " + typo + " of " + input[1] + " is " + string
		print sentence
		#except:
		#	sentence = "Cannot recognize the sentence"
		return sentence
	
	def speak(self,texto):
		try:
			os.system("gtts-cli.py '"+texto+"' -l en -o hello.mp3")
			time.sleep(1)
			os.system("mpg321 hello.mp3")
			os.system("rm hello.mp3")
		except:
			os.system('say "'+texto.encode('utf-8')+'"')
		time.sleep(1)
	
	def removeWord(self,word,cleaned):
		for x in range(len(cleaned)):
			if cleaned[x].lower() == word:
				break
		for y in range(x+1):
			print cleaned[y]
			cleaned.remove(cleaned[0])
		return cleaned

	def callVia(self,input):
		tokens = word_tokenize(input)
		stop_words = set(stopwords.words('english'))
		clean_tokens = [w for w in tokens if not w in stop_words]
		input = self.removeWord('call',clean_tokens)
		if "skype" in input or "Skype" in input:
			try:
				input.remove('skype')
			except:
				input.remove('Skype')
			name = " ".join(input)
			print name
			self.callBySkype(name)

	def callBySkype(self,input):
		app = os.popen('ps -ax | grep /Applications/Skype.app').read().split('\n')
		if 'grep' in app[0]:
			delay = '3'
		else:
			delay = '1'
		fullScreenScript = 'set toggleOnFull to false\n\nset myList to {"Skype"}\nrepeat with theItem in myList\n\n    tell application theItem\n        activate\n        delay ' + delay + '\n        (* \n  Initially from http://stackoverflow.com/questions/8215501/applescript-use-lion-fullscreen\n*)\n        set isfullscreen to false\n        tell application "System Events" to tell process theItem\n            set isfullscreen to value of attribute "AXFullScreen" of window 1\n        end tell\n        --display dialog "var " & isfullscreen\n\n        if isfullscreen is toggleOnFull then\n            tell application "System Events" to keystroke "f" using {command down, control down}\n            delay 1\n        end if\n    end tell\n\nend repeat\n'
		p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate(fullScreenScript)
		pyautogui.moveTo(1260,20)
		time.sleep(0.5)
		pyautogui.click()
		pyautogui.typewrite(input)
		time.sleep(0.2)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.moveTo(1360,87,0.5)
		time.sleep(0.2)
		pyautogui.click()

	def openFile(self):
		openFile = open("apikey.txt","r")
		readFile = openFile.read()
		self.apikey = readFile[0:len(readFile) - 1]
if __name__ == "__main__":
	a = MyFrame()
	
