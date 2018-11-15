# we will assume that re has been imported in all subsequent
# regex examples
import re

# define a regular expression to match a phone number 999-999-9999
phoneRE = re.compile(r'\d{3}-\d{3}-\d{4}')
text5 = "Please call me at 210-555-1234 or 830-555-6789"
text2 = "Please call me as soon as possible."
matchObj = phoneRE.search(text5)
if matchObj is not None:
    print(matchObj.group())
    print(" ")

###Return All Matches
resultT = phoneRE.findall(text5)
print(resultT)
resultT = phoneRE.findall(text2)
print(resultT)

