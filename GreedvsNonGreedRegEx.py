# Greedy matching lab.cs.utsa.edu
# The matching pattern matches any character until a dot is found.
# With greedy, the .* matches as much text as possible.
import re
location = "lab.cs.utsa.edu"
gDotRE = re.compile(r'(.*)\.')
gDotMO = gDotRE.search(location)
print (gDotMO.group())

gDotRE = re.compile(r'(.*?)\.')
gDotMO = gDotRE.search(location)
print(gDotMO.group())

# Greedy matching of Ho!
text = "Ho! Ho! Ho! Ho! Ho! "
gSantaRE = re.compile(r'(Ho!\s){2,5}')
gSantaMO = gSantaRE.search(text)
print(gSantaMO.group())

# Nongreedy matching of Ho!
text = "Ho! Ho! Ho! Ho! Ho! "
ngSantaRE = re.compile(r'(Ho!\s){2,5}?')
ngSantaMO = ngSantaRE.search(text)
print(ngSantaMO.group())

# Matching of ho, ho, ho, kid
text = "ho, ho, ho, kid"
ngSantaRE = re.compile(r'(ho,\s){1,5}?kid')
ngSantaMO = ngSantaRE.search(text)
print(ngSantaMO.group())

# what does this pattern do?
# finds and matched multiple gold, silver, or bronze, followed by a space and any amount of characters
medalRE = re.compile(r'\s*(GOLD|SILVER|BRONZE)\s(\w*)')
textLine = "SILVER Shaggy GOLD Scooby BRONZE Fred"
resultM = medalRE.findall(textLine)
print(resultM)
for oneMatchRes in resultM :
    medal, recipient = oneMatchRes
    print(medal, recipient)

