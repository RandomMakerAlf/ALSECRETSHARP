import mmap
import time

with open("Test.ALSS", 'rb', 0) as file:
  s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
  if s.find(b'laptop') != -1:
    print ('A')
    
with open("Test.ALSS", 'rb', 0) as file:
  s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
  if s.find(b'Python info') != -1:
    print('You Found A Secret! Info Python 3.11 I used for this Project')
    print('Close the window')
    time.sleep(120000000)
    
with open("Test.ALSS", 'rb', 0) as file:
  s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
  if s.find(b'Age of the dev') != -1:
    print('You Found A secret! my Age is 11 secret code It\'s Age of the dev')
    print('Close the window')
    time.sleep(120000000)   

with open("Test.ALSS", 'rb', 0) as file:
  s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
  if s.find(b'Fortnite') != -1:
    print('You Found A secret! Fortnite Battle Pass boot\'in my PC so, I can Get me that Fortnite Battle Pass It\'s Fortnite')
    print('Close the window')
    time.sleep(120000000)   
    
def Lang(Syntax):
    State = 1
    Token = ""
    String = ""
    for Char in Syntax:
        Token += Char
        if Token == " ":
            if State == 0:
                Token = ""
 
        elif Token == "\n":
            Token = ""
 
        elif Token == "Print":
            Token = ""
 
        elif Token == "\"":
            if State == 0:
                State = 1
                Token = ""
 
            elif State == 1:
                State = 0
 
        elif State == 1:
            String += Token
            Token = ""
 
    print(String)
 
Content = open("Test.ALSS", "r").readlines()
for Line in Content:
    Lang(Line)
 