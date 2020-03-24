import os
import json

f1 = open('file.json'   , 'w', encoding='utf-8', newline="")
f1.write(json.dumps({"key": "test", "key2" : "2", "key3" : "3"}))
f1.close()


file = open("file.json", "r+", encoding="utf-8", newline="")
# print(file.read())
newFile = open("newfile.tx", "w", encoding="utf-8", newline="")

for entry in json.load(file):
     toWrite = entry.get('value')
     newFile.write(toWrite + " ")




os.system("pause")
