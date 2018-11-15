# Split on semicolon, comma, period or space.  Also ignore 0 to many
# spaces after the delimiter.
import re
text3 = "He loved playing basketball; however, he hated watching it on TV."
wordM = re.split("[;,\s\.]\s*", text3)

print(wordM)


# loop while there are at least two parts
import re
textLine = "SILVER Shaggy GOLD Scooby BRONZE Fred"
rest = textLine
tokenM = re.split("[\s]", textLine, 2)
print(tokenM)
while len(tokenM) >= 2:
    medal = tokenM[0]
    recipient = tokenM[1]
    print (medal, recipient)
    if len(tokenM) <= 2:
        break
    rest = tokenM[2]
    tokenM = rest.split(' ',2)
