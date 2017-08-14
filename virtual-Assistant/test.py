import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/")
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
import os
os.system('gtts-cli.py "Hello my master how are you today?" -l en -o hello.mp3')
os.system("mpg321 hello.mp3")
os.system("rm hello.mp3")
