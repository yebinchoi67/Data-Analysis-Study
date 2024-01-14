#1
"""
import json
with open("questions_and_answers.json","r",encoding = "utf8") as f:
    contents = f.read()
    json_ex = json.loads(contents)

print(json_ex["quiz"]["sport"]["q1"]["question"]+"\n")

options = json_ex["quiz"]["sport"]["q1"]["options"]
for i in range(len(options)):
    print(str(i)+"."+options[i])
print("\n""answer "+json_ex["quiz"]["sport"]["q1"]["answer"])
"""
#2
"""
import urllib.request
from bs4 import BeautifulSoup

with open("researcher.xml","r",encoding="utf-8")as researcher_xml:
    xml = researcher_xml.read()

soup=BeautifulSoup(xml,"html.parser")

for i,element in enumerate(soup.findAll('researcher')):
    if i%2 == 1:
        print(element['researcherid'])
        print(element.na.get_text())
        print(element.salary)
    else:
        pass
"""
#10
import json

with open("data_file.json","r",encoding = "utf8") as f:
    contents = f.read()
    json_ex = json.loads(contents)

species = json_ex["president"]["species"]
print(species)
