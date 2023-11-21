import html2text
import re

f = open("./temp/x.txt", "r")
text=""
for line in f:
  #print(line)
  line = html2text.html2text(line)
  line = line.splitlines()
  line = ' '.join(line)
  line = re.sub(r'\[([^\[]+)\]\(\)',r'\1',line)
  text = text + line + "\n"
f = open("./output/content.txt", "w")
f.write(text)
f.close()

