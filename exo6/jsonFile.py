import os
import json

f1 = open('file.json'   , 'w', encoding='utf-8', newline="")
f1.write(json.dumps({"key": "test"}))


file = open("file.json", "r", encoding="utf-8", newline="")
print(file.read())
newFile = open("newfile.tx", "w", encoding="utf-8", newline="")

for entry in json.loads(file.read()):
     newFile.write(entry)




os.system("pause")
