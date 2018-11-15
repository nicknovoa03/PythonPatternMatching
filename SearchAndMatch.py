# we will assume that re has been imported in all subsequent
# regex examples
import re

#search
text1 = "Please call me at 210-555-1234"
matchObj = re.search(r'\d{3}-\d{3}-\d{4}', text1)
if matchObj != None:
    print(matchObj.group())
else:
    print("No Match")

#match
text2 = "Please call me at 210-555-1234"
matchObj = re.match(r'\d{3}-\d{3}-\d{4}', text2)
if matchObj != None:
    print(matchObj.group())
else:
    print("No Match")

text3 = "210-555-6666"
matchObj = re.match(r'\d{3}-\d{3}-\d{4}', text3)
if matchObj != None:
    print("matched")

text4 = "210-555-6666 is my number"
matchObj =  re.match( r'\d{3}-\d{3}-\d{4}', text4) #Matches because number is at begining
if matchObj != None:
    print("matched")
else:
    print("not matched")

