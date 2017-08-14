def speak(texto):
		import sys
		sys.path.append("/usr/local/lib/python2.7/site-packages/")
		from gtts import gTTS
		import os
		tts = gTTS(text=texto, lang='en')
		tts.save("good.mp3")
		os.system("mpg321 good.mp3")
		os.system("rm good.mp3")
if __name__ == "__main__":
		speak("Hello Master how are you today?")
