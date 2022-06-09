import re

text = "GCE CPU over 5 %"
# text = "CPUThrottlingHigh"


pattern = re.compile('G[a-zA-Z]{1,10} [a-zA-Z]{1,10} [a-zA-Z]{1,10} [0-9]+ %')
searched = pattern.search(text)

print(searched)