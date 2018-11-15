# define a regular expression to match an ABC123 ID
import re
abc123RE = re.compile(r'[a-z]{3}\d{3}')
text4 = "My ID is xyz123."
matchObj = abc123RE.search(text4)
if matchObj is not None:
    abc123Id = matchObj.group()
else:
    abc123Id = None
print(abc123Id)
print(" ")

# define a regular expression which matches Ho Ho Ho with
# any of these characters in between the words:
#     comma or exclamation point
# It also has a space between those characters
# and the next Ho.
# The last Ho must be immediately followed by a !
# It should be case insensitive (specify re.I)

hohohoRE = re.compile(r'ho[,!]\sho[,!]\sho!', re.I)
matchObjHo = hohohoRE.search('Santa said, "Ho! Ho! Ho!"')
if matchObjHo is not None:
    print(matchObjHo.group())
print(" ")

# define a regex that searches for Mickey Mouse or Minnie Mouse
# Mouse is optional
mouseRE = re.compile(r'(Mickey|Minnie)\s?(Mouse)?')
mouseMO = mouseRE.search("Goofy yelled at Mickey Mouse")
print("group 1:",mouseMO.group(1))
print("group 2:",mouseMO.group(2))
mouseMO = mouseRE.search("Pluto licked Minnie's hand")
print("group 1:",mouseMO.group(1))
print("group 2:",mouseMO.group(2))
