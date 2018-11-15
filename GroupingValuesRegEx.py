# define a regular expression to match an phone number 999-999-9999
# saving the area code and number
import re
text1 = "Please call me at 210-555-1234"
phoneRE = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchObj = phoneRE.search(text1)
if matchObj != None:
    print("using .group(k)")
    print("Area Code=", matchObj.group(1), "Phone=", matchObj.group(2))
    print("Printing using .groups() which contains a tuple with all matched groups")
    area, phone = matchObj.groups()
    print("Area Code=", area
          , "Phone=", phone)

