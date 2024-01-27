# @author Elias Kotlyar
# @category Tuning
# @keybinding
# @menupath
# @toolbar

import os
import json

filename = "a2l.json"
f = open(filename, "r")
content = f.read()
# print(content)
content = content.encode('utf-8')
contentJson = json.loads(content)
retArr = {}


def reference2Json(reference):
    return {
        "addr": "0x" + str(reference.getFromAddress()),
        "type": str(reference.getReferenceType())
    }


for key, item in contentJson.iteritems():
    # Assign Vars:
    name = item['name']
    addr = toAddr(int(item['addr'], 16))
    refs = getReferencesTo(addr)
    if len(refs) == 0:
        continue
    # print(refs)
    refs = map(reference2Json, refs)
    # print(refs)
    retArr[name] = {
        "name": name,
        "addr": item['addr'],
        "refs": refs
    }

    # break
outputfile = "refmap.json"
with open(outputfile, 'w') as f:
    # Write the content as JSON to the output file
    json.dump(retArr, f, indent=4)
print(retArr)
