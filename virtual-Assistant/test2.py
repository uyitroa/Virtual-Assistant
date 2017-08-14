from subprocess import Popen, PIPE
import webbrowser
url = '"https://www.youtube.com"'
scpt = 'tell application "Safari" to open location ' + url + '\nwaitForPageLoaded(20)\n\non waitForPageLoaded(timeoutValue) -- in seconds\n   delay 1\n   repeat with i from 1 to timeoutValue\n       tell application "Safari"\n           if name of current tab of window 1 is not "Loading" then exit repeat\n       end tell\n       delay 1\n   end repeat\n   if i is timeoutValue then return false\n   tell application "Safari"\n       repeat until (do JavaScript "document.readyState" in document 1) is "complete"\n           delay 0.5\n       end repeat\n   end tell\n   return true\nend waitForPageLoaded\n'

print scpt

p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
webbrowser.open(url)
stdout, stderr = p.communicate(scpt)
